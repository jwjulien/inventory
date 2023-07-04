# ======================================================================================================================
#      File:  /inventory/gui/dialogs/relocate.py
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
"""A dialog for easily moving parts from one slot to another."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtWidgets

from inventory.gui.base.dialog_relocate import Ui_DialogRelocate
from inventory.model.storage import Slot, Location



# ======================================================================================================================
# Relocate Dialog Class
# ----------------------------------------------------------------------------------------------------------------------
class RelocateDialog(QtWidgets.QDialog):
    """A dialog to assist with moving parts from one storage slot to another.

    Presents the user with information about a Location where the part is currently stored and gives them a list of
    Slots to move the part into.

    Two methods are provided for retrieving the user's results:
        quantity: Provides the quantity (up to a maximum of the existing quantity) they wish to move.  This defaults to
            all of the parts from the existing location for convenience.
        destination: The Slot into which the user has elected to transfer the Parts.
    """
    def __init__(self, parent, existing: Location):
        super().__init__(parent)
        self.ui = Ui_DialogRelocate()
        self.ui.setupUi(self)

        self.ui.quantity.setValue(existing.quantity)
        self.ui.quantity.setMaximum(existing.quantity)
        self.ui.part.setText(existing.part.summary)
        self.ui.existing.setText(existing.name)

        for slot in sorted(Slot.select(), key=lambda slot: slot.full_title()):
            text = slot.full_title()
            self.ui.destination.addItem(text, slot)
            if slot == existing.slot:
                self.ui.destination.setCurrentText(text)


# ----------------------------------------------------------------------------------------------------------------------
    def quantity(self) -> int:
        return self.ui.quantity.value()


# ----------------------------------------------------------------------------------------------------------------------
    def destination(self) -> Slot:
        return self.ui.destination.currentData(QtCore.Qt.UserRole)




# End of File
