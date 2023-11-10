# ======================================================================================================================
#      File:  /inventory/gui/widgets/location.py
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
"""Location viewing widget within the parts dialog."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from datetime import datetime

from PySide6 import QtCore, QtWidgets
import timeago

from inventory.gui.base.widget_location import Ui_LocationWidget
from inventory.gui.dialogs.location_mapping import LocationMappingDialog
from inventory.gui.dialogs.relocate import RelocateDialog
from inventory.gui.prompts import Alert, YesNoPrompt
from inventory.gui.utilities import context_action
from inventory.model.storage import Location
from inventory.model.parts import Part




# ======================================================================================================================
# Location Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class LocationWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_LocationWidget()
        self.ui.setupUi(self)

        self.part: Part = None

        # Setup header to best show column contents.
        header = self.ui.locations.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        # Setup context menu.
        self.context = QtWidgets.QMenu(self)
        self.context_edit = context_action(
            self.context, 'Edit Location', self._edit, 'fa.pencil', 'F2', self.ui.locations)
        self.context_remove = context_action(
            self.context, 'Remove Location', self._remove, 'fa.times', 'Delete', self.ui.locations)
        self.context.addSeparator()
        self.context_add = context_action(
            self.context, 'Add Location', self._add, 'fa.plus', 'Insert', self.ui.locations)
        self.context_relocate = context_action(
            self.context, 'Relocate...', self._relocate, 'fa.arrows-alt', 'Ctrl+R', self.ui.locations)
        self.ui.locations.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.locations.customContextMenuRequested.connect(
            lambda point: self.context.exec(self.ui.locations.mapToGlobal(point)))

        # Connect events.
        self.ui.locations.itemSelectionChanged.connect(self._selected)
        self.ui.locations.doubleClicked.connect(self._edit)


# ----------------------------------------------------------------------------------------------------------------------
    def setPart(self, part: Part) -> None:
        self.part = part

        for location in self.part.locations:
            row = self._insert_row()
            self._update_row(row, location)


# ----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _format_date(date: datetime) -> str:
        if date is None:
            return 'Unknown'
        return timeago.format(date)


# ----------------------------------------------------------------------------------------------------------------------
    def _insert_row(self) -> int:
        row = self.ui.locations.rowCount()
        self.ui.locations.insertRow(row)
        self.ui.locations.setItem(row, 0, QtWidgets.QTableWidgetItem(''))
        self.ui.locations.setItem(row, 1, QtWidgets.QTableWidgetItem(''))
        self.ui.locations.setItem(row, 2, QtWidgets.QTableWidgetItem(''))
        self.ui.locations.item(row, 0).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        return row


# ----------------------------------------------------------------------------------------------------------------------
    def _update_row(self, row: int, location: Location) -> None:
        self.ui.locations.item(row, 0).setText(str(location.quantity))
        self.ui.locations.item(row, 1).setText(self._format_date(location.last_counted))
        self.ui.locations.item(row, 2).setText(location.name)
        self.ui.locations.item(row, 0).setData(QtCore.Qt.UserRole, location)


# ----------------------------------------------------------------------------------------------------------------------
    def _find_location_row(self, location: Location) -> int:
        for row in range(self.ui.locations.rowCount()):
            if self.ui.locations.item(row, 0).data(QtCore.Qt.UserRole) == location:
                return row
        return None


# ----------------------------------------------------------------------------------------------------------------------
    def _selected(self) -> None:
        selected = self.ui.locations.selectedItems()
        self.context_edit.setEnabled(bool(selected))
        self.context_remove.setEnabled(bool(selected))

        quantity = sum([self.ui.locations.item(item.row(), 0).data(QtCore.Qt.UserRole).quantity for item in selected])
        self.context_relocate.setEnabled(quantity > 0)


# ----------------------------------------------------------------------------------------------------------------------
    def _edit(self) -> None:
        selected = self.ui.locations.selectedItems()
        if not selected:
            return
        item = selected[0]
        location = self.ui.locations.item(item.row(), 0).data(QtCore.Qt.UserRole)
        if not location:
            return
        if LocationMappingDialog(self, location).exec():
            self._update_row(item.row(), location)


# ----------------------------------------------------------------------------------------------------------------------
    def _add(self) -> None:
        location = Location(part=self.part)
        if LocationMappingDialog(self, location).exec():
            row = self._insert_row()
            self._update_row(row, location)


# ----------------------------------------------------------------------------------------------------------------------
    def _remove(self) -> None:
        selected = self.ui.locations.selectedItems()
        rows = set([item.row() for item in selected])
        for row in sorted(rows, reverse=True):
            location: Location = self.ui.locations.item(row, 0).data(QtCore.Qt.UserRole)
            if location.quantity > 0:
                Alert(self, 'Unable to delete location', 'Cannot delete a location with non-zero part quantity.')
            else:
                location.delete_instance()
                self.ui.locations.removeRow(row)


# ----------------------------------------------------------------------------------------------------------------------
    def _relocate(self) -> None:
        """Prompt the user to select a new location for the parts located in the selected location.

        If accepted, then move the quantity from selected location to new location.
        """
        selected = self.ui.locations.selectedItems()
        rows = list(set([item.row() for item in selected]))
        if len(rows) != 1:
            return
        row = rows[0]
        old_location: Location = self.ui.locations.item(row, 0).data(QtCore.Qt.UserRole)
        if old_location.quantity == 0:
            return

        dialog = RelocateDialog(self, old_location)
        if dialog.exec():
            # User has accepted their settings.  Take action.
            destination = dialog.destination()
            quantity = dialog.quantity()

            # Get a Location for the part in the destination slot, if it exists.
            new_location: Location = (Location.select()
                .where(Location.slot == destination, Location.part == old_location.part)
                .get_or_none())
            if new_location is None:
                # No Location info exists at this location yet.
                msg = QtWidgets.QMessageBox(self)
                msg.setIcon(QtWidgets.QMessageBox.Question)
                msg.setWindowTitle('Create new location info?')
                text = 'No location information exists for this\npart at the selected location.\n\n'
                text += 'Should a new Location be created?'
                msg.setText(text)
                msg.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Yes |
                    QtWidgets.QMessageBox.StandardButton.No
                )
                if msg.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                    # The user has confirmed they would like to move the parts here.
                    new_location = Location.create(part=old_location.part, slot=destination, quantity=quantity)
                    old_location.quantity -= quantity

                    # Insert the new location into the table.
                    self._update_row(self._insert_row(), new_location)

            else:
                # Location already exists, so merge the specified quantities instead.
                old_location.quantity -= quantity
                new_location.quantity += quantity
                new_location.save()

                # Update the existing row quantity information for the new location.
                self._update_row(self._find_location_row(new_location), new_location)

            # Parts (might) remain at the old location - update the quantity.
            # Doing this here may be redundant, if the row gets removed, but at least covers the path where the user
            # says no, tey want to keep the location reference with a zero quantity.
            self._update_row(row, old_location)

            # If there are no parts left at the old location then lets ask the user if they want to get rid of it.
            if old_location.quantity == 0:
                text = f'There are no items left at:\n  {old_location.name}\nWould you like to remove the old location?'
                if YesNoPrompt(self, 'Remove old location information?', text):
                    old_location.delete_instance()
                    self.ui.locations.removeRow(row)




# End of File
