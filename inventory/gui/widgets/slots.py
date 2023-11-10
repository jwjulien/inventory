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
import pickle
from typing import List

from PySide6 import QtCore, QtWidgets

from inventory.gui.base.widget_slots import Ui_WidgetSlots
from inventory.gui.dialogs.part import PartDialog
from inventory.gui.dialogs.parts import PartsDialog
from inventory.gui.dialogs.print_reference import PrintReferenceDialog
from inventory.gui.utilities import context_action
from inventory.model.parts import Part
from inventory.model.storage import Unit, Slot
from inventory.libraries.references import Reference, ReferenceTarget
from inventory.gui.prompts import Alert
from inventory.gui.constants import Colors




# ======================================================================================================================
# Slots Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class SlotsWidget(QtWidgets.QWidget):
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
        self.context_edit = context_action(self.context_menu, 'Edit', self._edit, 'fa.pencil', 'F2', self.ui.slots)
        self.context_menu.addSeparator()
        self.context_cut = context_action(self.context_menu, 'Cut', self._cut, 'fa.cut', 'Ctrl+X', self.ui.slots)
        self.context_copy = context_action(self.context_menu, 'Copy', self._copy, 'fa.copy', 'Ctrl+C', self.ui.slots)
        self.context_paste = context_action(
            self.context_menu, 'Paste', self._paste, 'fa.paste', 'Ctrl+V', self.ui.slots)
        self.context_menu.addSeparator()
        self.context_merge = context_action(self.context_menu, 'Merge', self._merge, 'mdi.table-merge-cells')
        self.context_split = context_action(self.context_menu, 'Split', self._split, 'mdi.table-split-cell')
        self.context_menu.addSeparator()
        self.context_remove = context_action(
            self.context_menu, 'Remove Slot', self._remove, 'fa.trash-o', 'Delete', self.ui.slots)
        self.context_menu.addSeparator()
        self.context_print = context_action(self.context_menu, 'Print Label', self._print, 'fa.barcode')
        self.ui.slots.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.slots.customContextMenuRequested.connect(
            lambda point: self.context_menu.exec(self.ui.slots.mapToGlobal(point)))

        # Connect events.
        self.ui.slots.horizontalHeader().sectionResized.connect(self.ui.slots.resizeRowsToContents)
        self.ui.slots.itemSelectionChanged.connect(self._selected)
        self.ui.slots.itemChanged.connect(self._changed)
        self.ui.slots.doubleClicked.connect(self._show_parts)


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
                item = QtWidgets.QTableWidgetItem('')
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                self.ui.slots.setItem(row, column, item)

        # Fill in the assigned slot names.
        for slot in unit.slots:
            self._update_cell(slot)

        # Resize cell contents to fit - attempting make columns fit within window.
        columns = self.ui.slots.columnCount()
        if columns:
            width = self.ui.slots.width() / columns
            for column in range(columns):
                self.ui.slots.setColumnWidth(column, width)
        self.ui.slots.resizeRowsToContents()

        self.ui.slots.blockSignals(False)


# ----------------------------------------------------------------------------------------------------------------------
    def select(self, slot: Slot) -> None:
        item = self.ui.slots.item(slot.row, slot.column)
        item.setSelected(True)


# ----------------------------------------------------------------------------------------------------------------------
    def _update_cell(self, slot: Slot) -> None:
        item = self.ui.slots.item(slot.row, slot.column)
        item.setText(slot.name)
        item.setToolTip(slot.name)
        item.setData(QtCore.Qt.UserRole, slot)
        self._highlight_item(item)
        if slot.row_span > 1 or slot.column_span > 1:
            self.ui.slots.setSpan(slot.row, slot.column, slot.row_span, slot.column_span)


# ----------------------------------------------------------------------------------------------------------------------
    def _selected_slots(self) -> List[Slot]:
        """Returns a list of currently selected slots."""
        selected = self.ui.slots.selectedItems()
        slots = [item.data(QtCore.Qt.UserRole) for item in selected]
        return [slot for slot in slots if slot is not None]


# ----------------------------------------------------------------------------------------------------------------------
    def _selected_parts(self) -> List[Part]:
        """Get a list of unique parts from the currently selected slot(s)."""
        slots = self._selected_slots()
        return list(set([part for slot in slots for part in slot.parts]))


# ----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _slots_to_mime(slots: List[Slot]) -> QtCore.QMimeData:
        mime = QtCore.QMimeData()
        mime.setData('application/slots', pickle.dumps(slots))
        mime.setText(', '.join(slot.name for slot in slots))
        return mime


# ----------------------------------------------------------------------------------------------------------------------
    def _cut(self) -> None:
        slots = self._selected_slots()
        QtWidgets.QApplication.clipboard().setMimeData(self._slots_to_mime(slots))
        self._remove()



# ----------------------------------------------------------------------------------------------------------------------
    def _copy(self) -> None:
        slots = self._selected_slots()
        copies = [slot.copy() for slot in slots]
        QtWidgets.QApplication.clipboard().setMimeData(self._slots_to_mime(copies))


# ----------------------------------------------------------------------------------------------------------------------
    def _paste(self) -> None:
        clipboard = QtWidgets.QApplication.clipboard()
        mime = clipboard.mimeData()
        data = mime.data('application/slots')
        if data:
            slots: List[Slot] = pickle.loads(data)
            offset_top = min([slot.row for slot in slots])
            offset_left = min([slot.column for slot in slots])

            current = self.ui.slots.selectedItems()
            top = min([item.row() for item in current])
            left = min([item.column() for item in current])

            # First pass: update the slot location and ensure it's not occupied.
            for slot in slots:
                slot.unit = self.unit
                slot.row = slot.row - offset_top + top
                slot.column = slot.column - offset_left + left

                # Be sure to check for overlap on spanned cells too.
                for row in range(slot.row_span):
                    for column in range(slot.column_span):
                        data = self.ui.slots.item(slot.row + row, slot.column + column).data(QtCore.Qt.UserRole)
                        if data:
                            return Alert(self, 'Paste Error', 'Unable to paste over existing slots')

            # Second pass: paste the items in and save them.
            self.ui.slots.blockSignals(True)
            for slot in slots:
                self._update_cell(slot)
                slot.save(force_insert=bool(slot.id))  # Force it to be inserted if the Slot was cut (i.e. deleted).
            self.ui.slots.blockSignals(False)

            # Update the context menu availability once the paste is complete.
            self._selected()


# ----------------------------------------------------------------------------------------------------------------------
    def _edit(self) -> None:
        """Edit the currently selected cell."""
        selected = self.ui.slots.selectedIndexes()
        if selected:
            self.ui.slots.edit(selected[-1])


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
                msg = f'Cannot delete Slot with Parts still located within it.\n\Remove parts first.'
                Alert(self, f"Can't delete {slot.name}", msg)
                continue

            # Remove the slot from the GUI.
            self.ui.slots.blockSignals(True)
            if slot.row_span > 1 or slot.column_span > 1:
                self.ui.slots.setSpan(item.row(), item.column(), 1, 1)
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
        if len(selected) != 1:
            return
        slot: Slot = selected[0].data(QtCore.Qt.UserRole)
        reference = Reference(id=slot.id, target=ReferenceTarget.Slot, label=slot.name)
        dialog = PrintReferenceDialog(self, reference)
        dialog.exec()


# ----------------------------------------------------------------------------------------------------------------------
    def _show_parts(self) -> None:
        parts = self._selected_parts()
        if parts:
            if len(parts) == 1:
                dialog = PartDialog(self, parts[0])
            else:
                dialog = PartsDialog(self, parts)
            dialog.exec()


# ----------------------------------------------------------------------------------------------------------------------
    def _selected(self) -> None:
        items = self.ui.slots.selectedItems()
        slots = self._selected_slots()
        parts = self._selected_parts()
        self.context_parts.setEnabled(bool(parts))
        self.context_print.setEnabled(len(slots) == 1)
        self.context_merge.setEnabled(len(slots) <= 1 and len(items) > 1)
        def is_spanned(item: QtWidgets.QTableWidgetItem) -> bool:
            if self.ui.slots.rowSpan(item.row(), item.column()) > 1:
                return True
            if self.ui.slots.columnSpan(item.row(), item.column()) > 1:
                return True
            return False
        self.context_split.setEnabled(len(items) == 1 and is_spanned(items[0]))
        self.context_remove.setEnabled(bool(slots))


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
            item.setBackground(Colors.Danger)

        # If this item has Slot data but not parts, highlight it in yellow.
        elif slot and not slot.parts:
            item.setBackground(Colors.Warning)

        # Otherwise, restore the background to the QTableWidgetItem default background.
        else:
            item.setBackground(QtWidgets.QTableWidgetItem('').background())


# ----------------------------------------------------------------------------------------------------------------------
    def _merge(self) -> None:
        """Merge the currently selected cell with the open cell to the right.

        When merging slots we need a selection that currently contains zero or one Slot.  If a Slot already exists, it
        will be updated to include the new cell(s).
        """
        slots = self._selected_slots()
        if len(slots) > 1:
            return

        # Get or make the Slot for this merge.
        slot = slots[0] if slots else Slot(unit=self.unit, name='')

        # Update the location and span info for this Slot.
        items = self.ui.slots.selectedItems()
        rows = [item.row() for item in items]
        columns = [item.column() for item in items]
        slot.row = min(rows)
        slot.column = min(columns)
        slot.column_span = max(columns) - slot.column + 1
        slot.row_span = max(rows) - slot.row + 1
        slot.save()

        # Update the QTableWidgetItem to match the item changes.
        self.ui.slots.setSpan(slot.row, slot.column, slot.row_span, slot.column_span)
        item = self.ui.slots.item(slot.row, slot.column)
        item.setText(slot.name)
        item.setData(QtCore.Qt.UserRole, slot)
        self._highlight_item(item)

        # If this was a new slot then trigger an edit.
        if not slot.name:
            self.ui.slots.editItem(item)


# ----------------------------------------------------------------------------------------------------------------------
    def _split(self) -> None:
        """Merge the currently selected cell with the open cell below."""
        # We can only split one cell at a time.
        items = self.ui.slots.selectedItems()
        if len(items) != 1:
            return

        # Ensure this slot actually spans something.
        slot: Slot = items[0].data(QtCore.Qt.UserRole)
        if slot.row_span <= 1 and slot.column_span <= 1:
            return

        # Update the slot back to a single cell.  To change the size the user must first split the merged cell and then
        # re-merge.
        slot.row_span = 1
        slot.column_span = 1
        slot.save()

        # Update the table to revert back to individual cells.
        self.ui.slots.setSpan(slot.row, slot.column, 1, 1)

        # Update the context menu to match the new selection.
        self._selected()




# End of File
