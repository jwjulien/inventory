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

from PySide6 import QtCore, QtWidgets
import timeago

from inventory.gui.base.dialog_location_mapping import Ui_DialogLocationMapping
from inventory.model.storage import Slot, Location




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
        for slot in sorted(Slot.select(), key=lambda slot: slot.full_title()):
            title = slot.full_title()
            self.ui.slot.addItem(title, slot)
            if location.slot_id and slot == location.slot:
                self.ui.slot.setCurrentText(title)

        self.ui.quantity.setValue(location.quantity or 0)
        self.ui.last_counted.setText(timeago.format(location.last_counted) if location.last_counted else 'Unknown')
        self.last_counted: datetime = location.last_counted

        # Events
        self.ui.reset.clicked.connect(self._reset)


# ----------------------------------------------------------------------------------------------------------------------
    def _reset(self) -> None:
        # Cache the updated date for now and copy it into `self.location` only when the user accepts the dialog.
        self.last_counted = datetime.now()
        self.ui.last_counted.setText('just now')


# ----------------------------------------------------------------------------------------------------------------------
    def accept(self) -> None:
        self.location.slot = self.ui.slot.currentData(QtCore.Qt.UserRole)
        self.location.quantity = self.ui.quantity.value()
        self.location.last_counted = self.last_counted
        self.location.save()
        return super().accept()




# End of File
