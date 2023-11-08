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
from PySide6 import QtCore, QtGui, QtWidgets

from inventory.gui.base.widget_slots import Ui_WidgetSlots
from inventory.gui.dialogs.parts import PartsDialog
from inventory.gui.dialogs.print_reference import PrintReferenceDialog
from inventory.gui.utilities import context_action
from inventory.model.storage import Unit, Slot
from inventory.libraries.references import Reference, ReferenceTarget




# ======================================================================================================================
# Constants
# ----------------------------------------------------------------------------------------------------------------------
Danger = '#d9534f'
Warning = '#f0ad4e'




# ======================================================================================================================
# Slots Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class SlotsWidget(QtWidgets.QWidget):
    selected = QtCore.Signal(Slot)

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_WidgetSlots()
        self.ui.setupUi(self)

        self.unit: Unit = None

        # Setup column spacing in table.
        self.ui.slots.setWordWrap(True)

        # Setup custom context menu.
        self.context_menu = QtWidgets.QMenu(self)
        self.context_parts = context_action(self.context_menu, 'View Parts', self._show_parts, 'fa.list')
        self.context_remove = context_action(self.context_menu, 'Remove Slot', self._remove, 'fa.trash-o')
        self.context_print = context_action(self.context_menu, 'Print Label', self._print, 'fa.barcode')
        # TODO: Add stuffs for adding and removing column/row spans.
        self.ui.slots.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.slots.customContextMenuRequested.connect(self._context_menu)

        # Connect events.
        self.ui.slots.horizontalHeader().sectionResized.connect(self.ui.slots.resizeRowsToContents)
        self.ui.slots.itemSelectionChanged.connect(self._selected)
        self.ui.slots.itemChanged.connect(self._changed)


# ----------------------------------------------------------------------------------------------------------------------
    def setUnit(self, unit: Unit) -> None:
        self.unit = unit

        self.ui.slots.blockSignals(True)

        # Remove any existing rows.
        while self.ui.slots.rowCount():
            self.ui.slots.removeRow(0)

        # Remove columns too.
        while self.ui.slots.columnCount():
            self.ui.slots.removeColumn(0)

        # Add columns, rows and cells back in now.
        for row in range(unit.rows):
            self.ui.slots.insertRow(self.ui.slots.rowCount())
            for column in range(unit.columns):
                if row == 0:
                    self.ui.slots.insertColumn(self.ui.slots.columnCount())
                self.ui.slots.setItem(row, column, QtWidgets.QTableWidgetItem(''))

        # Fill in the assigned slot names.
        for slot in unit.slots:
            item = self.ui.slots.item(slot.row, slot.column)
            item.setText(slot.name)
            item.setToolTip(slot.name)
            item.setData(QtCore.Qt.UserRole, slot)
            self._highlight_item(item)
            if slot.row_span > 1 or slot.column_span > 1:
                self.ui.slots.setSpan(slot.row, slot.column, slot.row_span, slot.column_span)

        # Resize cell contents to fit - attempting make columns fit within window.
        columns = self.ui.slots.columnCount()
        if columns:
            width = self.ui.slots.width() / columns
            for column in range(columns):
                self.ui.slots.setColumnWidth(column, width)
        self.ui.slots.resizeRowsToContents()

        self.ui.slots.blockSignals(False)


# ----------------------------------------------------------------------------------------------------------------------
    def _context_menu(self, point: QtCore.QPoint) -> None:
        selected = self.ui.slots.selectedItems()
        if len(selected) != 1:
            return
        slot: Slot = selected[0].data(QtCore.Qt.UserRole)
        if not slot:
            return
        self.context_menu.exec(self.ui.slots.mapToGlobal(point))


# ----------------------------------------------------------------------------------------------------------------------
    def _remove(self) -> None:
        selection = self.ui.slots.selectedItems()
        for item in selection:
            slot: Slot = item.data(QtCore.Qt.UserRole)

            # Don't try to delete slots that are empty - can happen on multiple selections.
            if slot is None:
                continue

            # Don't allow slots to be deleted that have parts mapped to them.
            if len(slot.locations) > 0:
                msg = QtWidgets.QMessageBox(self)
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle(f'Can\'t delete {slot.name}')
                msg.setText(f'Cannot delete {slot.name} with parts located in it.\n\nPlease remove parts first.')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()
                continue

            # Remove the slot from the GUI.
            self.ui.slots.blockSignals(True)
            item.setText('')
            item.setBackground(QtWidgets.QTableWidgetItem('').background())
            item.setData(QtCore.Qt.UserRole, None)
            self._highlight_item(item)
            self.ui.slots.blockSignals(False)

            # Remove the slot from the database.
            slot.delete_instance()


# ----------------------------------------------------------------------------------------------------------------------
    def _print(self) -> None:
        selected = self.ui.slots.selectedItems()
        if not selected:
            return
        slot: Slot = selected[0].data(QtCore.Qt.UserRole)
        reference = Reference(id=slot.id, target=ReferenceTarget.Slot, label=slot.name)
        dialog = PrintReferenceDialog(self, reference)
        dialog.exec()


# ----------------------------------------------------------------------------------------------------------------------
    def _show_parts(self) -> None:
        selected = self.ui.slots.selectedItems()
        if not selected:
            return
        slot: Slot = selected[0].data(QtCore.Qt.UserRole)
        dialog = PartsDialog(self, slot.parts)
        dialog.exec()


# ----------------------------------------------------------------------------------------------------------------------
    def _selected(self) -> None:
        selected = self.ui.slots.selectedItems()
        if not selected:
            return self.selected.emit(None)
        item = selected[0]
        slot = item.data(QtCore.Qt.UserRole)
        self.selected.emit(slot)


# ----------------------------------------------------------------------------------------------------------------------
    def _changed(self, item: QtWidgets.QTreeWidgetItem) -> None:
        slot = item.data(QtCore.Qt.UserRole)
        if slot is None:
            # This is a new slot in an open hole - create a new slot with the provided info.
            slot = Slot(unit=self.unit)
            item.setData(QtCore.Qt.UserRole, slot)
        slot.name = item.text()
        slot.row = item.row()
        slot.column = item.column()
        slot.row_span = self.ui.slots.rowSpan(item.row(), item.column())
        self.column_span = self.ui.slots.columnSpan(item.row(), item.column())
        self._highlight_item(item)
        slot.save()


# ----------------------------------------------------------------------------------------------------------------------
    def _highlight_item(self, item: QtWidgets.QTableWidgetItem) -> None:
        slot: Slot = item.data(QtCore.Qt.UserRole)

        # If this item has Slot data but and empty name, highlight it in red.
        if slot and not slot.name.strip():
            item.setBackground(QtGui.QColor(Danger))

        # If this item has Slot data but not parts, highlight it in yellow.
        elif slot and not slot.parts:
            item.setBackground(QtGui.QColor(Warning))

        # Otherwise, restore the background to the QTableWidgetItem default background.
        else:
            item.setBackground(QtWidgets.QTableWidgetItem('').background())




# End of File
