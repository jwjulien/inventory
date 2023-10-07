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
from typing import List

from PySide6 import QtCore, QtWidgets
import qtawesome

from inventory.gui.base.tab_projects import Ui_TabProjects
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

        # Connect events.
        self.ui.projects.selected.connect(self._project_selected)
        self.ui.projects.imported.connect(self._bom_imported)
        self.ui.revisions.selected.connect(self._revision_selected)
        self.ui.back.clicked.connect(self._show_projects)
        self.ui.add_material.clicked.connect(self._add_material)
        self.ui.remove_material.clicked.connect(self._remove_material)
        self.ui.materials.itemChanged.connect(self._material_changed)
        self.ui.materials.itemSelectionChanged.connect(self._material_selected)


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
        self.ui.materials.clearContents()
        for material in revision.materials:
            self._append_material(material)
        self.ui.title.setText(f'{revision.project.title} Hardware Version {revision.version} Bill of Materials')
        self.ui.stack.setCurrentWidget(self.ui.page_parts)


# ----------------------------------------------------------------------------------------------------------------------
    def _append_material(self, material: Material) -> int:
        def non_edit_item(text: str) -> QtWidgets.QTableWidgetItem:
            item = QtWidgets.QTableWidgetItem(text)
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            return item
        row = self.ui.materials.rowCount()
        self.ui.materials.blockSignals(True)
        self.ui.materials.insertRow(row)
        designator = QtWidgets.QTableWidgetItem(material.designator)
        designator.setFlags(designator.flags() | QtCore.Qt.ItemIsEditable)
        designator.setData(QtCore.Qt.UserRole, material)
        self.ui.materials.setItem(row, 0, designator)
        self.ui.materials.setItem(row, 1, non_edit_item(material.part.summary))
        self.ui.materials.setItem(row, 2, non_edit_item(material.part.number))
        self.ui.materials.setItem(row, 3, non_edit_item(material.part.price))
        self.ui.materials.blockSignals(False)
        return row


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




# End of File
