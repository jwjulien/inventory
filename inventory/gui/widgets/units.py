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
from inventory.gui.dialogs.parts import PartsDialog
from inventory.gui.dialogs.print_reference import PrintReferenceDialog
from inventory.gui.prompts import Alert
from inventory.gui.utilities import context_action
from inventory.model.storage import Area, Unit
from inventory.libraries.references import Reference, ReferenceTarget




# ======================================================================================================================
# Units Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class UnitsWidget(QtWidgets.QWidget):
    selected = QtCore.Signal(Unit)

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_WidgetUnits()
        self.ui.setupUi(self)

        self.area: Area = None

        # Set parameters for column sizes on the header (which doesn't change).
        header = self.ui.units.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        # Setup custom context menu.
        self.context = QtWidgets.QMenu(self)
        self.context_view = context_action(
            self.context, 'View Slots', self._show_slots, 'fa.arrow-right', 'Enter', self.ui.units)
        self.context_edit = context_action(self.context, 'Edit', self._edit, 'fa.pencil', 'F2', self.ui.units)
        self.context_parts = context_action(self.context, 'View All Parts', self._show_parts, 'fa.list')
        self.context.addSeparator()
        self.context_add = context_action(self.context, 'Add Unit', self._add, 'fa.plus')
        self.context_remove = context_action(self.context, 'Remove Unit', self._remove, 'fa.trash-o')
        self.context.addSeparator()
        self.context_print = context_action(self.context, 'Print Label', self._print, 'fa.barcode')
        self.ui.units.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.units.customContextMenuRequested.connect(
            lambda point: self.context.exec(self.ui.units.mapToGlobal(point)))

        # Connect events.
        self.ui.units.itemChanged.connect(self._changed)
        self.ui.units.itemSelectionChanged.connect(self._selected)
        self.ui.units.doubleClicked.connect(self._show_slots)


# ----------------------------------------------------------------------------------------------------------------------
    def setUnits(self, area: Area, units: List[Unit]) -> None:
        self.area = area

        self.ui.units.blockSignals(True)

        # Remove any existing rows.
        while self.ui.units.rowCount():
            self.ui.units.removeRow(0)

        # Insert the new units into the list.
        for unit in sorted(units, key=lambda unit: unit.name):
            self._append_unit(unit)

        self.ui.units.blockSignals(False)


# ----------------------------------------------------------------------------------------------------------------------
    def select(self, unit: Unit) -> None:
        for row in range(self.ui.units.rowCount()):
            item = self.ui.units.item(row, 0)
            if unit == item.data(QtCore.Qt.UserRole):
                item.setSelected(True)
                break


# ----------------------------------------------------------------------------------------------------------------------
    def _selected(self) -> None:
        selected = bool(self.ui.units.selectedItems())
        self.context_remove.setEnabled(selected)
        self.context_view.setEnabled(selected)
        self.context_print.setEnabled(selected)



# ----------------------------------------------------------------------------------------------------------------------
    def _add(self) -> None:
        if self.area is None:
            return
        self.ui.units.blockSignals(True)
        unit = Unit(area=self.area)
        row = self._append_unit(unit)
        self.ui.units.blockSignals(False)
        self.ui.units.edit(self.ui.units.indexFromItem(self.ui.units.item(row, 0)))


# ----------------------------------------------------------------------------------------------------------------------
    def _edit(self) -> None:
        """Edit the currently selected cell."""
        selected = self.ui.units.selectedIndexes()
        if selected:
            self.ui.units.edit(selected[-1])


# ----------------------------------------------------------------------------------------------------------------------
    def _remove(self) -> None:
        """Remove the currently selected Units."""
        selected = self.ui.units.selectedItems()
        if not selected:
            return
        item = selected[0]
        unit: Unit = item.data(QtCore.Qt.UserRole)

        # Do not let the user remove an area with units mapped to it.  As a safety measure, and to prevent orphans, we
        # instead force them to remove the units manually first.  Here, provide them with an error message and abort.
        if unit.slots:
            return Alert(self, 'Error', 'Cannot delete an Unit with Slots.\n\nRemove associated Slots and try again.')

        unit.delete_instance()
        self.ui.units.removeRow(self.ui.units.row(item))


# ----------------------------------------------------------------------------------------------------------------------
    def _print(self) -> None:
        selected = self.ui.units.selectedIndexes()
        unit = self.ui.units.item(selected[0].row(), 0).data(QtCore.Qt.UserRole)
        reference = Reference(id=unit.id, target=ReferenceTarget.Unit, label=unit.name)
        dialog = PrintReferenceDialog(self, reference)
        dialog.exec()


# ----------------------------------------------------------------------------------------------------------------------
    def _append_unit(self, unit: Unit) -> int:
        row = self.ui.units.rowCount()
        self.ui.units.insertRow(row)
        self.ui.units.setItem(row, 0, QtWidgets.QTableWidgetItem(unit.name))
        self.ui.units.setItem(row, 1, QtWidgets.QTableWidgetItem(str(unit.rows)))
        self.ui.units.setItem(row, 2, QtWidgets.QTableWidgetItem(str(unit.columns)))
        self.ui.units.item(row, 0).setData(QtCore.Qt.UserRole, unit)
        return row


# ----------------------------------------------------------------------------------------------------------------------
    def _show_slots(self) -> None:
        selected = self.ui.units.selectedItems()
        if len(selected) != 1:
            self.selected.emit(None)
            return
        item = selected[0]
        unit = self.ui.units.item(item.row(), 0).data(QtCore.Qt.UserRole)
        self.selected.emit(unit)


# ----------------------------------------------------------------------------------------------------------------------
    def _show_parts(self) -> None:
        selected = self.ui.units.selectedItems()
        if not selected:
            return
        item = selected[0]
        unit: Unit = self.ui.units.item(item.row(), 0).data(QtCore.Qt.UserRole)
        dialog = PartsDialog(self, unit.parts)
        dialog.exec()


# ----------------------------------------------------------------------------------------------------------------------
    def _changed(self, item: QtWidgets.QTableWidgetItem) -> None:
        unit = self.ui.units.item(item.row(), 0).data(QtCore.Qt.UserRole)
        unit.name = self.ui.units.item(item.row(), 0).text()
        unit.rows = int(self.ui.units.item(item.row(), 1).text() or 0)
        unit.columns = int(self.ui.units.item(item.row(), 2).text() or 0)
        unit.save()





# End of File
