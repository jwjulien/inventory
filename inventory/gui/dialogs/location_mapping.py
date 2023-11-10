# ======================================================================================================================
#      File:  /inventory/gui/dialogs/location_mapping.py
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
"""Location mapping dialog for connecting parts with locations."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from datetime import datetime

from partsscale.scale import DeviceError, Scale
from PySide6 import QtCore, QtWidgets
import timeago

from inventory.gui.base.dialog_location_mapping import Ui_DialogLocationMapping
from inventory.gui.dialogs.parts_counter import PartsCounterDialog
from inventory.model.storage import Area, Slot, Location




# ======================================================================================================================
# Location Mapper Dialog Class
# ----------------------------------------------------------------------------------------------------------------------
class LocationMappingDialog(QtWidgets.QDialog):
    def __init__(self, parent, location: Location):
        super().__init__(parent)
        self.ui = Ui_DialogLocationMapping()
        self.ui.setupUi(self)

        self.location = location

        # Load GUI
        self.ui.slot.clear()
        area: Area
        for area in sorted(Area.select(), key=lambda area: area.name):
            area_item = QtWidgets.QTreeWidgetItem(self.ui.slot, [area.name])
            self.ui.slot.addTopLevelItem(area_item)
            for unit in sorted(area.units, key=lambda unit: unit.name):
                unit_item = QtWidgets.QTreeWidgetItem(area_item, [unit.name])
                area_item.addChild(unit_item)
                for slot in sorted(unit.slots, key=lambda slot: slot.name):
                    slot_item = QtWidgets.QTreeWidgetItem(unit_item, [slot.name])
                    slot_item.setData(0, QtCore.Qt.UserRole, slot)
                    unit_item.addChild(slot_item)
                    if self.location.slot_id and slot == self.location.slot:
                        slot_item.setSelected(True)
                        self.ui.slot.scrollTo(self.ui.slot.indexFromItem(slot_item, 0))
                        unit_item.setExpanded(True)
                        area_item.setExpanded(True)

        # Only enable the count button if there is a scale present and the part has a weight.
        # TODO: Add a calibrate button for the part here to set a weight and then count?
        try:
            Scale()
        except DeviceError:
            self.ui.count.setEnabled(False)
            self.ui.count.setToolTip('Scale not found')
        else:
            self.ui.count.setEnabled(self.location.part and bool(self.location.part.weight))
            self.ui.count.setToolTip('No part weight defined')

        self.ui.quantity.setValue(location.quantity or 0)
        self.ui.last_counted.setText(timeago.format(location.last_counted) if location.last_counted else 'Unknown')
        self.last_counted: datetime = location.last_counted

        # Events
        self.ui.reset.clicked.connect(self._reset)
        self.ui.count.clicked.connect(self._count)
        self.ui.slot.itemSelectionChanged.connect(self._slot_selected)
        self._slot_selected()


# ----------------------------------------------------------------------------------------------------------------------
    def _reset(self) -> None:
        # Cache the updated date for now and copy it into `self.location` only when the user accepts the dialog.
        self.last_counted = datetime.now()
        self.ui.last_counted.setText('just now')


# ----------------------------------------------------------------------------------------------------------------------
    def _count(self) -> None:
        dialog = PartsCounterDialog(self, self.location.part)
        if dialog.exec():
            self.ui.quantity.setValue(dialog.count())
            self._reset()


# ----------------------------------------------------------------------------------------------------------------------
    def _slot_selected(self) -> None:
        valid = False
        selected = self.ui.slot.selectedItems()
        if selected:
            item = selected[0]
            slot = item.data(0, QtCore.Qt.UserRole)
            valid = bool(slot)
        self.ui.buttonBox.button(self.ui.buttonBox.StandardButton.Ok).setEnabled(valid)


# ----------------------------------------------------------------------------------------------------------------------
    def accept(self) -> None:
        self.location.slot = self.ui.slot.selectedItems()[0].data(0, QtCore.Qt.UserRole)
        self.location.quantity = self.ui.quantity.value()
        self.location.last_counted = self.last_counted
        self.location.save()
        return super().accept()




# End of File
