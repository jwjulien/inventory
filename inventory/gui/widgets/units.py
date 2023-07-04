# ======================================================================================================================
#      File:  /inventory/gui/widgets/units.py
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
"""A widget for listing units."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from typing import List

from PySide6 import QtCore, QtWidgets

from inventory.gui.base.widget_units import Ui_WidgetUnits
from inventory.model.storage import Unit




# ======================================================================================================================
# Units Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class UnitsWidget(QtWidgets.QWidget):
    selected = QtCore.Signal(Unit)

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_WidgetUnits()
        self.ui.setupUi(self)

        header = self.ui.units.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        # Connect events.
        self.ui.add.clicked.connect(self.add)
        self.ui.units.itemSelectionChanged.connect(self._selected)


# ----------------------------------------------------------------------------------------------------------------------
    def setUnits(self, units: List[Unit]) -> None:
        # Remove any existing rows.
        while self.ui.units.rowCount():
            self.ui.units.removeRow(0)

        # Insert the new units into the list.
        for unit in sorted(units, key=lambda unit: unit.name):
            row = self.ui.units.rowCount()
            self.ui.units.insertRow(row)
            self.ui.units.setItem(row, 0, QtWidgets.QTableWidgetItem(unit.name))
            self.ui.units.setItem(row, 1, QtWidgets.QTableWidgetItem(str(unit.rows)))
            self.ui.units.setItem(row, 2, QtWidgets.QTableWidgetItem(str(unit.columns)))
            self.ui.units.item(row, 0).setData(QtCore.Qt.UserRole, unit)


# ----------------------------------------------------------------------------------------------------------------------
    def add(self) -> None:
        unit = Unit()


# ----------------------------------------------------------------------------------------------------------------------
    def _selected(self) -> None:
        item = self.ui.units.selectedItems()[0]
        unit = item.data(QtCore.Qt.UserRole)
        self.selected.emit(unit)





# End of File
