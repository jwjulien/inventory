# ======================================================================================================================
#      File:  /inventory/gui/widgets/areas.py
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
"""A widget for listing areas."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from typing import List

from PySide6 import QtCore, QtWidgets

from inventory.gui.base.widget_areas import Ui_WidgetAreas
from inventory.model.storage import Area




# ======================================================================================================================
# Areas Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class AreasWidget(QtWidgets.QWidget):
    selected = QtCore.Signal(Area)

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_WidgetAreas()
        self.ui.setupUi(self)

        # Connect events.
        self.ui.add.clicked.connect(self.add)
        self.ui.remove.clicked.connect(self.remove)
        self.ui.areas.itemSelectionChanged.connect(self._selected)
        self.ui.areas.itemChanged.connect(self._changed)


# ----------------------------------------------------------------------------------------------------------------------
    def setAreas(self, areas: List[Area]) -> None:
        # Remove any existing rows.
        self.ui.areas.clear()

        # Insert the new areas into the list.
        for area in sorted(areas, key=lambda area: area.name):
            self._add_item(area)


# ----------------------------------------------------------------------------------------------------------------------
    def add(self) -> None:
        area = Area()
        item = self._add_item(area)
        self.ui.areas.editItem(item)


# ----------------------------------------------------------------------------------------------------------------------
    def _add_item(self, area: Area) -> QtWidgets.QListWidgetItem:
        item = QtWidgets.QListWidgetItem(area.name)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        item.setData(QtCore.Qt.UserRole, area)
        self.ui.areas.addItem(item)
        return item


# ----------------------------------------------------------------------------------------------------------------------
    def remove(self) -> None:
        selected = self.ui.areas.selectedItems()
        if not selected:
            return
        item = selected[0]
        area: Area = item.data(QtCore.Qt.UserRole)
        if area.units:
            message = 'Cannot delete an Area with Units.\n\nRemove associated Units and try again.'
            QtWidgets.QMessageBox(icon=QtWidgets.QMessageBox.warning, title='Error', text=message).exec()
            return
        area.delete_instance()
        self.ui.areas.takeItem(self.ui.areas.row(item))


# ----------------------------------------------------------------------------------------------------------------------
    def _selected(self) -> None:
        item = self.ui.areas.selectedItems()[0]
        area = item.data(QtCore.Qt.UserRole)
        self.selected.emit(area)


# ----------------------------------------------------------------------------------------------------------------------
    def _changed(self, item: QtWidgets.QTreeWidgetItem) -> None:
        area: Area = item.data(QtCore.Qt.UserRole)
        area.name = item.text()
        area.save()
        self.ui.areas.sortItems(QtCore.Qt.AscendingOrder)





# End of File
