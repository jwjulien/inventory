# ======================================================================================================================
#      File:  /inventory/gui/tabs/projects.py
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
"""Tab implementation for project BOM parts."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import re
from typing import List

from PySide6 import QtCore, QtGui, QtWidgets
import qtawesome

from inventory.gui.base.tab_projects import Ui_TabProjects
from inventory.gui.dialogs.part import PartDialog
from inventory.gui.dialogs.part_select import PartSelectDialog
from inventory.model.projects import Project, Revision, Material
from inventory.model.parts import Part




# ======================================================================================================================
# Project Tab Class
# ----------------------------------------------------------------------------------------------------------------------
class TabProjects(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_TabProjects()
        self.ui.setupUi(self)

        projects: List[Project] = Project.select()
        self.ui.projects.setProjects(projects)

        self.ui.revisions.setEnabled(False)
        self.ui.back.setIcon(qtawesome.icon('fa5s.chevron-left'))
        self.ui.add_material.setIcon(qtawesome.icon('fa5s.plus'))
        self.ui.remove_material.setIcon(qtawesome.icon('fa5s.times'))

        self._selected_revision: Revision = None

        # Setup column spacing.
        header = self.ui.materials.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # Connect events.
        self.ui.projects.selected.connect(self._project_selected)
        self.ui.projects.imported.connect(self._bom_imported)
        self.ui.revisions.selected.connect(self._revision_selected)
        self.ui.back.clicked.connect(self._show_projects)
        self.ui.add_material.clicked.connect(self._add_material)
        self.ui.remove_material.clicked.connect(self._remove_material)
        self.ui.materials.itemChanged.connect(self._material_changed)
        self.ui.materials.itemSelectionChanged.connect(self._material_selected)

        # Setup custom context menu for editing parts in the Materials table.
        self.pop_menu = QtWidgets.QMenu(self)
        self.pop_view = QtGui.QAction('View Part', self)
        self.pop_view.triggered.connect(self._view_part)
        self.pop_menu.addAction(self.pop_view)
        self.pop_change = QtGui.QAction('Select Alternative', self)
        self.pop_change.triggered.connect(self._select_part)
        self.pop_menu.addAction(self.pop_change)
        self.pop_add = QtGui.QAction('Add Part', self)
        self.pop_add.triggered.connect(self._add_material)
        self.pop_menu.addAction(self.pop_add)
        self.pop_remove = QtGui.QAction('Remove Part', self)
        self.pop_remove.triggered.connect(self._remove_part)
        self.pop_menu.addAction(self.pop_remove)
        self.ui.materials.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.materials.customContextMenuRequested.connect(
            lambda point: self.pop_menu.exec(self.ui.materials.mapToGlobal(point)))


# ----------------------------------------------------------------------------------------------------------------------
    def _project_selected(self, project: Project) -> None:
        self.ui.revisions.setEnabled(bool(project))
        self.ui.revisions.setProject(project)


# ----------------------------------------------------------------------------------------------------------------------
    def _bom_imported(self, revision: Revision) -> None:
        # Refresh projects to possibly include a new addition.
        self.ui.projects.setProjects(Project.select())
        self.ui.projects.select(revision.project)
        self.ui.revisions.select(revision)
        self._revision_selected(revision)


# ----------------------------------------------------------------------------------------------------------------------
    def _revision_selected(self, revision: Revision) -> None:
        self._selected_revision = revision
        self._clear_materials()
        def designator(material: Material) -> str:
            # Attempt to pad numeric portion of designators to get expected sort order.
            matches = re.match(r'^(\D+)(\d+)$', material.designator)
            if matches:
                return f'{matches.group(1)}{int(matches.group(2)):04d}'
            return material.designator
        for material in sorted(revision.materials, key=designator):
            self._append_material(material)
        self.ui.title.setText(f'{revision.project.title} Hardware Version {revision.version} Bill of Materials')
        self.ui.stack.setCurrentWidget(self.ui.page_parts)


# ----------------------------------------------------------------------------------------------------------------------
    def _clear_materials(self) -> None:
        """Remove all of the materials currently displayed in the BOM table."""
        while self.ui.materials.rowCount():
            self.ui.materials.removeRow(0)


# ----------------------------------------------------------------------------------------------------------------------
    def _append_material(self, material: Material) -> int:
        def non_edit_item() -> QtWidgets.QTableWidgetItem:
            item = QtWidgets.QTableWidgetItem('')
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            return item
        row = self.ui.materials.rowCount()
        self.ui.materials.blockSignals(True)
        self.ui.materials.insertRow(row)
        designator = QtWidgets.QTableWidgetItem('')
        designator.setFlags(designator.flags() | QtCore.Qt.ItemIsEditable)
        self.ui.materials.setItem(row, 0, designator)
        self.ui.materials.setItem(row, 1, non_edit_item())
        self.ui.materials.setItem(row, 2, non_edit_item())
        self.ui.materials.setItem(row, 3, non_edit_item())
        self.ui.materials.blockSignals(False)
        self._update_material(row, material)
        return row


# ----------------------------------------------------------------------------------------------------------------------
    def _update_material(self, row: int, material: Material) -> None:
        self.ui.materials.blockSignals(True)
        self.ui.materials.item(row, 0).setData(QtCore.Qt.UserRole, material)
        self.ui.materials.item(row, 0).setText(material.designator)
        self.ui.materials.item(row, 1).setText(material.part.summary)
        self.ui.materials.item(row, 2).setText(material.part.number)
        self.ui.materials.item(row, 3).setText(f'${material.part.price:.2f}')
        self.ui.materials.blockSignals(False)


# ----------------------------------------------------------------------------------------------------------------------
    def _show_projects(self) -> None:
        self.ui.stack.setCurrentWidget(self.ui.page_projects)


# ----------------------------------------------------------------------------------------------------------------------
    def _add_material(self) -> None:
        dialog = PartSelectDialog(self, Part.select())
        if dialog.exec():
            # Calculate the next available designator.
            part = dialog.part()
            prefix = part.category.inherited_designator
            if prefix:
                idx = 1
                while True:
                    designator = f'{prefix}{idx}'
                    try:
                        self._selected_revision.lookup_material(designator)
                    except KeyError:
                        break
                    idx += 1
            else:
                designator = ''

            # Add a new Material to the database.
            material = Material(revision=self._selected_revision, part=part, designator=designator)
            material.save()

            # Display it for the user and select the calculated Designator for editing.
            row = self._append_material(material)
            self.ui.materials.scrollToItem(self.ui.materials.item(row, 0))
            self.ui.materials.editItem(self.ui.materials.item(row, 0))


# ----------------------------------------------------------------------------------------------------------------------
    def _remove_material(self) -> None:
        rows = list(set([index.row() for index in self.ui.materials.selectedIndexes()]))
        if len(rows) == 1:
            material: Material = self.ui.materials.item(rows[0], 0).data(QtCore.Qt.UserRole)
            material.delete_instance()
            self.ui.materials.removeRow(rows[0])


# ----------------------------------------------------------------------------------------------------------------------
    def _material_changed(self, item: QtWidgets.QTableWidgetItem) -> None:
        material: Material = self.ui.materials.item(item.row(), 0).data(QtCore.Qt.UserRole)
        material.designator = self.ui.materials.item(item.row(), 0).text()
        material.save()


# ----------------------------------------------------------------------------------------------------------------------
    def _material_selected(self) -> None:
        rows = list(set([index.row() for index in self.ui.materials.selectedIndexes()]))
        self.ui.remove_material.setEnabled(bool(rows))


# ----------------------------------------------------------------------------------------------------------------------
    def _selected_row(self) -> int:
        """Get the currently selected row index from the materials table.

        Returns:
            The single index that is selected in the materials table.

        Raises:
            AssertionError: If no Material is selected or if more than one Material is selected.
        """
        selected = self.ui.materials.selectedItems()
        rows = list(set([item.row() for item in selected]))
        assert len(rows) == 1
        return rows[0]


# ----------------------------------------------------------------------------------------------------------------------
    def _selected_material(self) -> Material:
        """Get the currently selected material from the materials table.

        Returns:
            The single material that is selected in the materials table.

        Raises:
            AssertionError: If no Material is selected or if more than one Material is selected.
        """
        row = self._selected_row()
        item = self.ui.materials.item(row, 0)
        return item.data(QtCore.Qt.UserRole)


# ----------------------------------------------------------------------------------------------------------------------
    def _view_part(self) -> None:
        material = self._selected_material()
        dialog = PartDialog(self, material.part)
        dialog.exec()


# ----------------------------------------------------------------------------------------------------------------------
    def _select_part(self) -> None:
        material = self._selected_material()
        dialog = PartSelectDialog(self, Part.select())
        dialog.setPart(material.part)
        if dialog.exec():
            material.part = dialog.part()
            material.save()
            self._update_material(self._selected_row(), material)


# ----------------------------------------------------------------------------------------------------------------------
    def _remove_part(self) -> None:
        material = self._selected_material()
        material.delete_instance()
        row = self._selected_row()
        self.ui.materials.removeRow(row)




# End of File
