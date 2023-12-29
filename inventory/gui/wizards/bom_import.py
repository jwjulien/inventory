# ======================================================================================================================
#      File:  /inventory/gui/wizards/bom_import.py
#   Project:  Inventory
#    Author:  Jared Julien <jaredjulien@exsystems.net>
# Copyright:  (c) 2023 Jared Julien, eX Systems
# ---------------------------------------------------------------------------------------------------------------------
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ----------------------------------------------------------------------------------------------------------------------
"""Support for locating a BOM and importing including project/revision creation and material entry."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from dataclasses import dataclass
import os
import re
from typing import Iterator, List

from PySide6 import QtCore, QtGui, QtWidgets
import qtawesome
from thefuzz import fuzz, process

from inventory.gui.base.wizard_bom_import import Ui_BomImportWizard
from inventory.model.parts import Part
from inventory.model.projects import Project, Revision, Material
from inventory.model.suppliers import Supplier
from inventory.gui.dialogs.part_select import PartSelectDialog




# ======================================================================================================================
# BOM Line Item Class
# ----------------------------------------------------------------------------------------------------------------------
@dataclass
class LineItem:
    designator: str = None
    description: str = None
    supplier: str = None
    number: str = None
    quantity: int = 1
    part: Part = None


    def copy(self, **overrides) -> 'LineItem':
        return LineItem(
            designator = overrides.get('designator', self.designator),
            description = overrides.get('description', self.description),
            supplier = overrides.get('supplier', self.supplier),
            number = overrides.get('number', self.number),
            quantity = overrides.get('quantity', self.quantity),
            part = overrides.get('part', self.part),
        )


    def parse(text: str, mapping: List[str]) -> 'LineItem':
        text = text.strip(' |')
        parts = re.split(' +\| +', text)
        if len(parts) != len(mapping):
            return None
        line = LineItem()
        for idx, part in enumerate(parts):
            column = mapping[idx]
            if 'desig' in column:
                line.designator = part
            elif 'desc' in column:
                line.description = part
            elif 'supp' in column:
                line.supplier = part
            elif 'num' in column:
                line.number = part
            elif 'qty' in column or 'quan' in column:
                try:
                    line.quantity = int(part)
                except ValueError:
                    pass
        return line




# ======================================================================================================================
# BOM Class
# ----------------------------------------------------------------------------------------------------------------------
@dataclass
class BOM:
    project: str
    revision: str
    items: List[LineItem]

    @staticmethod
    def parse(text: str) -> 'BOM':
        title, body = re.split('\n[-=]+\n', text, 1, re.MULTILINE)

        # Attempt to extract project and revision info from the title, if it exists.
        matches = re.match('^(.+?)[ -]+hardware (?:revi|ver)sion[ -]+(\S+)', title, re.IGNORECASE)
        if matches:
            project = matches.group(1)
            revision = matches.group(2)
        else:
            project = ''
            revision = ''

        # Parse the table header to get column heading names.
        lines = body.strip().split('\n')
        header = lines.pop(0)
        headings = re.split(' +\| +', header.strip(' |'))
        mapping = [heading.lower() for heading in headings]
        if len(mapping) < 3:
            raise ValueError

        # Pop the separator row out and toss it - we don't need it where we're going.
        lines.pop(0)

        def get_number(designator: str) -> int:
            """Intelligently get the designator number from the provided string.

            Returns:
                The integer portion of a designator.  For example, for part "D3", return 3.

            Raises:
                ValueError: If the provided designator doesn't contain any integer.
            """
            try:
                return int(re.findall('\d+', designator)[0])
            except IndexError as error:
                raise ValueError from error


        def get_text(designator: str) -> int:
            """Intelligently get the designator text from the provided string.

            Returns:
                The textual portion of a designator.  For example, for part "D3", return D.

            Raises:
                ValueError: If the provided designator doesn't contain any text.
            """
            try:
                return re.findall('\D+', designator)[0]
            except IndexError as error:
                raise ValueError from error


        def item_generator(item: LineItem) -> Iterator[LineItem]:
            """Generate new items from this item using it's designator to break it apart into individual line items.

            This step is performed to convert a condensed BOM with line items having quantities greater than 1 into an
            expanded list of individual items that will be needed to enter the BOM into the project.

            Yields:
                One or more items that are represented by the provided line item.
            """
            # If the item is bogus, just bail out now.
            if not item:
                return

            # If this part has no designator, fall back on iterating using quantity instead.
            if not item.designator:
                for _ in range(item.quantity):
                    yield item.copy(quantity=1)

            else:
                for chunk in item.designator.split(','):
                    chunk = chunk.strip()
                    if '-' in chunk:
                        start, end = chunk.split('-')
                        start = start.strip()
                        end = end.strip()
                        designator = get_text(start)
                        start = get_number(start)
                        end = get_number(end)
                        for idx in range(start, end + 1):
                            yield item.copy(designator=f'{designator}{idx}', quantity=1)
                    else:
                        yield item.copy(designator=chunk, quantity=1)


        # Parse the remaining lines into BOM line items.
        lines = [LineItem.parse(line, mapping) for line in lines]

        # Expand designators that have ranges (e.g. "C1-C3") and groups ("C1,C5") into a flat list.
        items: List[LineItem] = [item for line in lines for item in item_generator(line)]

        # Build a lookup table for the parts searching that's about to follow.
        # Merge in a cross reference for supplier part numbers.
        all_parts = Part.select()
        suppliers = Supplier.select()
        by_number = dict([(part, part.number.lower()) for part in all_parts])
        by_number.update(dict([(prdct.part, prdct.number) for splr in suppliers for prdct in splr.products]))

        # Generate a secondary table of parts using their summaries.
        by_summary = dict([(part, part.summary.lower()) for part in all_parts])

        # Attempt to match parts to the line items.
        for item in items:
            # Attempt to match off the part number, if it's specified.
            if item.number:
                _, score, part = process.extractOne(item.number.lower(), by_number, scorer=fuzz.partial_ratio)
                if score >= 75: # Empirically derived.
                    item.part = part

            # Fallback on trying to match LineItem.description against Part.summary if there is no part number.
            else:
                _, score, part = process.extractOne(item.description.lower(), by_summary, scorer=fuzz.partial_ratio)
                if score >= 75: # Empirically derived.
                    item.part = part

        return BOM(
            project=project,
            revision=revision,
            items=items
        )





# ======================================================================================================================
# Bom Import Wizard
# ----------------------------------------------------------------------------------------------------------------------
class BomImportWizard(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_BomImportWizard()
        self.ui.setupUi(self)

        self.bom: BOM = None
        self.committed_revision: Revision = None

        self.ui.next.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ui.back.setIcon(qtawesome.icon('fa5s.chevron-left'))

        self.ui.file_select.setLabel('Select BOM')
        self.ui.file_select.addFilter('Markdown Files', '*.md')

        self.ui.stack.setCurrentIndex(0)

        self.ui.next.clicked.connect(self._next)
        self.ui.back.clicked.connect(self._back)
        self.ui.stack.currentChanged.connect(self._update_controls)
        self.ui.file_select.changed.connect(self._update_controls)
        self.ui.file_select.selected.connect(self._bom_selected)
        self.ui.radio_project_existing.clicked.connect(self._use_existing_project)
        self.ui.radio_project_new.clicked.connect(self._create_new_project)
        self.ui.radio_revision_existing.clicked.connect(self._use_existing_revision)
        self.ui.radio_revision_new.clicked.connect(self._create_new_revision)
        self.ui.materials.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.materials.customContextMenuRequested.connect(self._on_material_menu)
        self.ui.materials.doubleClicked.connect(self._map_part)

        self.pop_menu = QtWidgets.QMenu(self)
        self.pop_add = QtGui.QAction('Map Part', self)
        self.pop_add.triggered.connect(self._map_part)
        self.pop_menu.addAction(self.pop_add)
        self.pop_remove = QtGui.QAction('Remove Mapping', self)
        self.pop_menu.addAction(self.pop_remove)
        self.pop_remove.triggered.connect(self._remove_mapping)

        self._update_controls()


# ----------------------------------------------------------------------------------------------------------------------
    def _next(self) -> None:
        """Advance to the next page when the user presses the next button."""
        index = self.ui.stack.currentIndex()

        # Take action for the current step before proceeding.
        if index == 0: # File Select -> Project Selection
            # When switching from the BOM file select to the project selection, update th list of available projects.
            self.ui.project_combo.clear()
            found = False
            project: Project
            for project in Project.select():
                self.ui.project_combo.addItem(project.title, project)
                if self.bom and project.title.lower() == self.bom.project.lower():
                    found = True
                    self.ui.radio_project_existing.setChecked(True)
                    self._use_existing_project()
                    self.ui.project_combo.setCurrentText(project.title)
                    self.ui.project_combo.setFocus()

            # If no matching project was found then assume we will want to create one.
            if not found:
                self.ui.radio_project_new.setChecked(True)
                self._create_new_project()
                self.ui.project_editor.setText(self.bom.project)
                self.ui.project_editor.setFocus()

        elif index == 1: # Project Selection -> Revision Selection
            found = False
            self.ui.radio_revision_existing.setEnabled(bool(self.project.revisions))
            self.ui.revision_combo.clear()
            revision: Revision
            for revision in self.project.revisions:
                self.ui.revision_combo.addItem(revision.version, revision)
                if self.bom and revision.version.lower() == self.bom.revision.lower():
                    found = True
                    self.ui.radio_revision_existing.setChecked(True)
                    self._use_existing_revision()
                    self.ui.revision_combo.setCurrentText(revision.version)
                    self.ui.revision_combo.setFocus()

            if not found:
                self.ui.radio_revision_new.setChecked(True)
                self._create_new_revision()
                self.ui.revision_editor.setText(self.bom.revision)
                timestamp = os.path.getmtime(self.ui.file_select.filename())
                date = QtCore.QDateTime.fromSecsSinceEpoch(int(timestamp))
                self.ui.revision_date.setDate(date.date())
                self.ui.revision_editor.setFocus()

        elif index == 2: # Revision Selection -> Material Mapping
            self.ui.materials.clear()
            for line in self.bom.items:
                item = QtWidgets.QTreeWidgetItem(self.ui.materials)
                item.setText(0, line.designator)
                item.setText(1, line.description)
                item.setText(2, line.number)
                item.setText(3, line.part.summary if line.part else '')
                item.setText(4, line.part.number if line.part else '')
                item.setData(0, QtCore.Qt.UserRole, line)
                self.ui.materials.addTopLevelItem(item)
            for idx in range(self.ui.materials.columnCount()):
                self.ui.materials.resizeColumnToContents(idx)

        elif index == 3: # Commit Changes
            self.committed_revision = self.revision

            # Attempt to gather any Materials already associated with this revision.
            materials = list(Material.select().where(Material.revision_id == self.committed_revision.id))

            # Save the revision and project.
            self.committed_revision.project.save()
            self.committed_revision.save()

            # Walk through materials and update the database.
            for row in range(self.ui.materials.topLevelItemCount()):
                item = self.ui.materials.topLevelItem(row)
                line: LineItem = item.data(0, QtCore.Qt.UserRole)
                if not line.part:
                    continue

                # Search for an existing material with this designator already in the BOM..
                for material in materials:
                    # Match existing materials by their designator.
                    if material.designator == line.designator:
                        material.part = line.part
                        material.save()
                        break
                else:
                    # No Material exists yet, so we need to create a new one.
                    material = Material.create(revision=self.committed_revision, part=line.part, designator=line.designator)

            # We're done.  Accept (and close) this dialog.
            self.accept()


        # Advance to the next step if not at the end.
        index += 1
        if index < self.ui.stack.count():
            self.ui.stack.setCurrentIndex(index)


# ----------------------------------------------------------------------------------------------------------------------
    def _back(self) -> None:
        """Revert to the previous page when the user presses the back button."""
        index = self.ui.stack.currentIndex() - 1
        if index >= 0:
            self.ui.stack.setCurrentIndex(index)


# ----------------------------------------------------------------------------------------------------------------------
    def _update_controls(self) -> None:
        """Passively update control availability based upon the current statuses of the stack pages."""
        next_enabled = True
        widget = self.ui.stack.currentWidget()

        if widget == self.ui.page_browse:
            next_enabled &= self.ui.file_select.isValid()

        elif widget == self.ui.page_project:
            pass

        elif widget == self.ui.page_revision:
            self.ui.project_name.setText(self.project.title)

        elif widget == self.ui.page_materials:
            title = f'{self.project.title} Hardware Version {self.revision.version} Bill of Materials'
            self.ui.bom_title.setText(title)

        final = self.ui.stack.currentIndex() == self.ui.stack.count() - 1
        self.ui.next.setEnabled(next_enabled)
        self.ui.next.setText('Commit' if final else 'Next')
        self.ui.next.setIcon(qtawesome.icon('fa5s.check' if final else 'fa5s.chevron-right'))
        self.ui.back.setVisible(self.ui.stack.currentIndex() > 0)


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def project(self) -> Project:
        if self.ui.radio_project_existing.isChecked():
            return self.ui.project_combo.currentData(QtCore.Qt.UserRole)
        return Project(title=self.ui.project_editor.text(), description=self.ui.project_description.toPlainText())


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def revision(self) -> Revision:
        if self.ui.radio_revision_existing.isChecked():
            return self.ui.revision_combo.currentData(QtCore.Qt.UserRole)
        return Revision(project=self.project,
                        version=self.ui.revision_editor.text(),
                        date=self.ui.revision_date.date().toPython())


# ----------------------------------------------------------------------------------------------------------------------
    def _bom_selected(self, filename: str) -> None:
        """Fires when the user selects a valid filename in the BOM file select widget."""
        # Verify that the currently selected BOM can be parsed.  Just because the filename is valid in the widget
        # doesn't mean that it's a properly formatted Markdown table containing BOM entries.
        with open(filename, 'r') as handle:
            text = handle.read()
        try:
            self.bom = BOM.parse(text)
        except ValueError:
            self.ui.file_select.setError('Unable to parse a BOM from the provided file')
            self.ui.next.setEnabled(False)
        else:
            # If the BOM is valid, automatically advance to the next tab.
            self._next()



# ----------------------------------------------------------------------------------------------------------------------
    def _use_existing_project(self) -> None:
        self.ui.project_combo.setEnabled(True)
        self.ui.project_editor.setEnabled(False)
        self.ui.project_description.setEnabled(False)


# ----------------------------------------------------------------------------------------------------------------------
    def _create_new_project(self) -> None:
        self.ui.project_combo.setEnabled(False)
        self.ui.project_editor.setEnabled(True)
        self.ui.project_description.setEnabled(True)


# ----------------------------------------------------------------------------------------------------------------------
    def _use_existing_revision(self) -> None:
        self.ui.revision_combo.setEnabled(True)
        self.ui.revision_editor.setEnabled(False)
        self.ui.revision_date.setEnabled(False)


# ----------------------------------------------------------------------------------------------------------------------
    def _create_new_revision(self) -> None:
        self.ui.revision_combo.setEnabled(False)
        self.ui.revision_editor.setEnabled(True)
        self.ui.revision_date.setEnabled(True)


# ----------------------------------------------------------------------------------------------------------------------
    def _on_material_menu(self, point: QtCore.QPoint) -> None:
        item = self.ui.materials.selectedItems()[0]
        line = item.data(0, QtCore.Qt.UserRole)
        self.pop_add.setEnabled(not bool(line.part))
        self.pop_remove.setEnabled(bool(line.part))
        self.pop_menu.exec(self.ui.materials.mapToGlobal(point))


# ----------------------------------------------------------------------------------------------------------------------
    def _map_part(self) -> None:
        selected = self.ui.materials.selectedItems()
        if selected:
            item = selected[0]
            line = item.data(0, QtCore.Qt.UserRole)
            dialog = PartSelectDialog(self, Part.select())
            dialog.setFilter(line.part.number if line.part else line.number)
            dialog.setWindowTitle(f'Select part for {line.description} {line.number}')
            if dialog.exec():
                line.part = dialog.part()
                item.setText(3, line.part.summary)
                item.setText(4, line.part.number)


# ----------------------------------------------------------------------------------------------------------------------
    def _remove_mapping(self) -> None:
        selected = self.ui.materials.selectedItems()
        if selected:
            item = selected[0]
            line = item.data(0, QtCore.Qt.UserRole)
            line.part = None
            item.setText(3, '')
            item.setText(4, '')




# End of File
