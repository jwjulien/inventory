# ======================================================================================================================
#      File:  /inventory/gui/widgets/projects.py
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
"""A widget for listing projects."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from typing import List

from PySide6 import QtCore, QtWidgets
import qtawesome

from inventory.gui.base.widget_projects import Ui_WidgetProjects
from inventory.gui.prompts import Alert
from inventory.gui.wizards.bom_import import BomImportWizard
from inventory.model.projects import Project, Revision




# ======================================================================================================================
# Projects Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class ProjectsWidget(QtWidgets.QWidget):
    selected = QtCore.Signal(Project)
    imported = QtCore.Signal(Revision)

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_WidgetProjects()
        self.ui.setupUi(self)

        self.ui.add.setIcon(qtawesome.icon('fa5s.plus'))
        self.ui.remove.setIcon(qtawesome.icon('fa5s.times'))
        self.ui.remove.setEnabled(False)

        # Connect events.
        self.ui.add.clicked.connect(self._add_new)
        self.ui.import_bom.clicked.connect(self._import)
        self.ui.remove.clicked.connect(self.remove)
        self.ui.projects.itemSelectionChanged.connect(self._selected)
        self.ui.projects.itemChanged.connect(self._changed)


# ----------------------------------------------------------------------------------------------------------------------
    def setProjects(self, projects: List[Project]) -> None:
        # Remove any existing rows.
        self.ui.projects.clear()

        # Insert the new projects into the list.
        for project in sorted(projects, key=lambda project: project.title):
            self.add(project)


# ----------------------------------------------------------------------------------------------------------------------
    def _add_new(self) -> None:
        project = Project()
        item = self.add(project)
        self.ui.projects.editItem(item)


# ----------------------------------------------------------------------------------------------------------------------
    def select(self, project: Project) -> None:
        """"Programmatically select the specified project."""
        for row in range(self.ui.projects.topLevelItemCount()):
            item = self.ui.projects.topLevelItem(row)
            if project == item.data(0, QtCore.Qt.UserRole):
                item.setSelected(True)
                break


# ----------------------------------------------------------------------------------------------------------------------
    def add(self, project: Project) -> QtWidgets.QListWidgetItem:
        item = QtWidgets.QTreeWidgetItem()
        item.setText(0, project.title)
        item.setText(1, project.description)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        item.setData(0, QtCore.Qt.UserRole, project)
        self.ui.projects.addTopLevelItem(item)
        return item


# ----------------------------------------------------------------------------------------------------------------------
    def remove(self) -> None:
        selected = self.ui.projects.selectedItems()
        if not selected:
            return
        item = selected[0]
        project: Project = item.data(0, QtCore.Qt.UserRole)

        # Do not let the user remove an project with revisions mapped to it.  As a safety measure, and to prevent
        # orphans, we instead force them to remove the revisions manually first.  Here, provide them with an error message
        # and abort.
        if project.revisions:
            msg = 'Cannot delete an Project with Revisions.\n\nRemove associated Revisions and try again.'
            return Alert(self, 'Error', msg)

        project.delete_instance()
        self.ui.projects.takeTopLevelItem(self.ui.projects.indexOfTopLevelItem(item))


# ----------------------------------------------------------------------------------------------------------------------
    def _import(self) -> None:
        dialog = BomImportWizard(self)
        if dialog.exec():
            self.imported.emit(dialog.committed_revision)


# ----------------------------------------------------------------------------------------------------------------------
    def _selected(self) -> None:
        selected = self.ui.projects.selectedItems()
        self.ui.remove.setEnabled(bool(selected))
        if selected:
            item = selected[0]
            project = item.data(0, QtCore.Qt.UserRole)
            self.selected.emit(project)


# ----------------------------------------------------------------------------------------------------------------------
    def _changed(self, item: QtWidgets.QTreeWidgetItem) -> None:
        project: Project = item.data(0, QtCore.Qt.UserRole)
        project.title = item.text(0)
        project.description = item.text(1)
        project.save()
        self.ui.projects.sortItems(0, QtCore.Qt.AscendingOrder)





# End of File
