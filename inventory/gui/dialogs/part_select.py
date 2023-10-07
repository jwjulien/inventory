# ======================================================================================================================
#      File:  /inventory/gui/dialogs/part_select.py
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
"""A dialog for selecting a part from a list."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from typing import List

from PySide6 import QtCore, QtWidgets

from inventory.gui.base.dialog_part_select import Ui_PartSelectDialog
from inventory.model.parts import Part




# ======================================================================================================================
# Part Select Dialog Class
# ----------------------------------------------------------------------------------------------------------------------
class PartSelectDialog(QtWidgets.QDialog):
    """A dialog to assist with selecting a single part from a provided list."""
    def __init__(self, parent, parts: List[Part]):
        super().__init__(parent)
        self.ui = Ui_PartSelectDialog()
        self.ui.setupUi(self)
        self.ui.parts.setParts(parts)
        self.ui.parts.selected.connect(self._selection_changed)
        self._selection_changed(None)


# ----------------------------------------------------------------------------------------------------------------------
    def _selection_changed(self, part: Part) -> None:
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(bool(part))


# ----------------------------------------------------------------------------------------------------------------------
    def setFilter(self, text: str) -> None:
        """Set the current filter text for this selection."""
        self.ui.parts.setFilter(text)


# ----------------------------------------------------------------------------------------------------------------------
    def part(self) -> Part:
        """Return the currently selected Part."""
        return self.ui.parts.selectedPart()




# End of File
