# ======================================================================================================================
#      File:  /inventory/gui/widgets/revisions.py
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
"""A widget for listing revisions."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from datetime import date, datetime

from PySide6 import QtCore, QtWidgets
import qtawesome

from inventory.gui.base.widget_revisions import Ui_WidgetRevisions
from inventory.gui.delegates.date import DateDelegate
from inventory.gui.prompts import Alert
from inventory.model.projects import Project, Revision




# ======================================================================================================================
# Revisions Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class RevisionsWidget(QtWidgets.QWidget):
    selected = QtCore.Signal(Revision)

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_WidgetRevisions()
        self.ui.setupUi(self)

        self.project: Project = None

        delegate = DateDelegate(self, self.ui.revisions)
        self.ui.revisions.setItemDelegateForColumn(1, delegate)

        self.ui.add.setIcon(qtawesome.icon('fa5s.plus'))
        self.ui.remove.setIcon(qtawesome.icon('fa5s.times'))
        self.ui.view_bom.setIcon(qtawesome.icon('fa5s.arrow-right'))
        self.ui.view_bom.setLayoutDirection(QtCore.Qt.RightToLeft)

        # Connect events.
        self.ui.add.clicked.connect(self.add)
        self.ui.remove.clicked.connect(self.remove)
        self.ui.view_bom.clicked.connect(self._view_bom)
        self.ui.revisions.itemSelectionChanged.connect(self._selected)
        self.ui.revisions.itemChanged.connect(self._changed)


# ----------------------------------------------------------------------------------------------------------------------
    def setProject(self, project: Project) -> None:
        self.project = project

        # Remove any existing rows.
        self.ui.revisions.clear()

        # Insert the new revisions into the list.
        for revision in sorted(project.revisions, key=lambda revision: revision.version):
            self._add_item(revision)


# ----------------------------------------------------------------------------------------------------------------------
    def select(self, revision: Revision) -> None:
        for row in range(self.ui.revisions.topLevelItemCount()):
            item = self.ui.revisions.topLevelItem(row)
            if revision == item.data(0, QtCore.Qt.UserRole):
                item.setSelected(True)
                break


# ----------------------------------------------------------------------------------------------------------------------
    def setEnabled(self, enabled: bool) -> None:
        self.ui.add.setEnabled(enabled)
        self.ui.remove.setEnabled(enabled and bool(self.ui.revisions.selectedIndexes()))
        self.ui.view_bom.setEnabled(enabled and bool(self.ui.revisions.selectedIndexes()))
        self.ui.revisions.setEnabled(enabled)


# ----------------------------------------------------------------------------------------------------------------------
    def add(self) -> None:
        revision = Revision()
        revision.project = self.project
        revision.date = date.today()
        item = self._add_item(revision)
        self.ui.revisions.editItem(item)


# ----------------------------------------------------------------------------------------------------------------------
    def _add_item(self, revision: Revision) -> QtWidgets.QListWidgetItem:
        item = QtWidgets.QTreeWidgetItem()
        item.setText(0, revision.version)
        item.setText(1, revision.date.strftime('%m/%d/%y'))
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        item.setData(0, QtCore.Qt.UserRole, revision)
        self.ui.revisions.addTopLevelItem(item)
        return item


# ----------------------------------------------------------------------------------------------------------------------
    def _view_bom(self) -> None:
        """User has clicked the View BOM button.  Switch views and show the BOM."""
        items = self.ui.revisions.selectedItems()
        if len(items) == 1:
            revision = items[0].data(0, QtCore.Qt.UserRole)
            self.selected.emit(revision)


# ----------------------------------------------------------------------------------------------------------------------
    def remove(self) -> None:
        selected = self.ui.revisions.selectedItems()
        if not selected:
            return
        item = selected[0]
        revision: Revision = item.data(0, QtCore.Qt.UserRole)

        # Do not let the user remove an revision with parts mapped to it.  As a safety measure, and to prevent
        # orphans, we instead force them to remove the parts manually first.  Here, provide them with an error message
        # and abort.
        if revision.parts:
            msg = 'Cannot delete an Revision with Materials.\n\nRemove associated Materials and try again.'
            return Alert(self, 'Error', msg)

        revision.delete_instance()
        self.ui.revisions.takeTopLevelItem(self.ui.revisions.indexOfTopLevelItem(item))


# ----------------------------------------------------------------------------------------------------------------------
    def _selected(self) -> None:
        items = self.ui.revisions.selectedItems()
        if len(items) == 1:
            self.ui.remove.setEnabled(bool(items[0]))
            self.ui.view_bom.setEnabled(bool(items[0]))


# ----------------------------------------------------------------------------------------------------------------------
    def _changed(self, item: QtWidgets.QTreeWidgetItem) -> None:
        revision: Revision = item.data(0, QtCore.Qt.UserRole)
        revision.version = item.text(0)
        revision.date = datetime.strptime(item.text(1), '%m/%d/%y')
        revision.save()
        self.ui.revisions.sortItems(0, QtCore.Qt.AscendingOrder)





# End of File
