# ======================================================================================================================
#      File:  /inventory/gui/widgets/slots.py
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
"""A widget for listing slots."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from typing import List

from PySide6 import QtCore, QtWidgets

from inventory.gui.base.widget_slots import Ui_WidgetSlots
from inventory.model.storage import Slot




# ======================================================================================================================
# Slots Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class SlotsWidget(QtWidgets.QWidget):
    selected = QtCore.Signal(Slot)

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_WidgetSlots()
        self.ui.setupUi(self)

        self.ui.slots.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        # Connect events.
        self.ui.add.clicked.connect(self.add)
        self.ui.slots.itemSelectionChanged.connect(self._selected)


# ----------------------------------------------------------------------------------------------------------------------
    def setSlots(self, slots: List[Slot]) -> None:

        # Remove any existing rows.
        while self.ui.slots.rowCount():
            self.ui.slots.removeRow(0)

        # Remove columns too.
        while self.ui.slots.columnCount():
            self.ui.slots.removeColumn(0)

        if not slots:
            return

        # Add columns, row,s and cells back in now.
        unit = slots[0].unit  # Unit is the same for all the slots.
        for row in range(unit.rows):
            self.ui.slots.insertRow(self.ui.slots.rowCount())
            for column in range(unit.columns):
                if row == 0:
                    self.ui.slots.insertColumn(self.ui.slots.columnCount())
                self.ui.slots.setItem(row, column, QtWidgets.QTableWidgetItem(''))

        # Fill in the assigned slot names.
        for slot in slots:
            item = self.ui.slots.item(slot.row, slot.column)
            item.setText(slot.name)
            item.setData(QtCore.Qt.UserRole, slot)


# ----------------------------------------------------------------------------------------------------------------------
    def add(self) -> None:
        slot = Slot()


# ----------------------------------------------------------------------------------------------------------------------
    def _selected(self) -> None:
        selected = self.ui.slots.selectedItems()
        if not selected:
            return self.selected.emit(None)
        item = selected[0]
        slot = item.data(QtCore.Qt.UserRole)
        self.selected.emit(slot)





# End of File
