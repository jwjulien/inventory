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
from inventory.model.projects import Project




# ======================================================================================================================
# Projects Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class ProjectsWidget(QtWidgets.QWidget):
    selected = QtCore.Signal(Project)

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_WidgetProjects()
        self.ui.setupUi(self)

        self.ui.add.setIcon(qtawesome.icon('fa5s.plus'))
        self.ui.remove.setIcon(qtawesome.icon('fa5s.times'))
        self.ui.remove.setEnabled(False)

        # Connect events.
        self.ui.add.clicked.connect(self.add)
        self.ui.remove.clicked.connect(self.remove)
        self.ui.projects.itemSelectionChanged.connect(self._selected)
        self.ui.projects.itemChanged.connect(self._changed)


# ----------------------------------------------------------------------------------------------------------------------
    def setProjects(self, projects: List[Project]) -> None:
        # Remove any existing rows.
        self.ui.projects.clear()

        # Insert the new projects into the list.
        for project in sorted(projects, key=lambda project: project.title):
            self._add_item(project)


# ----------------------------------------------------------------------------------------------------------------------
    def add(self) -> None:
        project = Project()
        item = self._add_item(project)
        self.ui.projects.editItem(item)


# ----------------------------------------------------------------------------------------------------------------------
    def _add_item(self, project: Project) -> QtWidgets.QListWidgetItem:
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
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle('Error')
            msg.setText('Cannot delete an Project with Revisions.\n\nRemove associated Revisions and try again.')
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        project.delete_instance()
        self.ui.projects.takeTopLevelItem(self.ui.projects.indexOfTopLevelItem(item))


# ----------------------------------------------------------------------------------------------------------------------
    def _selected(self) -> None:
        item = self.ui.projects.selectedItems()[0]
        project = item.data(0, QtCore.Qt.UserRole)
        self.selected.emit(project)
        self.ui.remove.setEnabled(bool(item))


# ----------------------------------------------------------------------------------------------------------------------
    def _changed(self, item: QtWidgets.QTreeWidgetItem) -> None:
        project: Project = item.data(0, QtCore.Qt.UserRole)
        project.title = item.text(0)
        project.description = item.text(1)
        project.save()
        self.ui.projects.sortItems(0, QtCore.Qt.AscendingOrder)





# End of File
