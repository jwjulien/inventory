# ======================================================================================================================
#      File:  /inventory/gui/dialogs/part_weight.py
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
"""Dialog to allow the user to accurately determine a parts weight using a USB scale."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtWidgets
from partsscale.scale import Scale

from inventory.gui.base.dialog_part_weight import Ui_PartWeightDialog




# ======================================================================================================================
# Part Weight Dialog
# ----------------------------------------------------------------------------------------------------------------------
class PartWeightDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_PartWeightDialog()
        self.ui.setupUi(self)

        self.scale = Scale()

        self.ui.tare.clicked.connect(self.scale.tare)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.periodic)
        self.timer.start(125)


# ----------------------------------------------------------------------------------------------------------------------
    def periodic(self) -> None:
        weight = self.scale.weight()
        self.ui.weight.display(f'{weight:.3f}'[:5])
        weight /= self.ui.count.value()
        self.ui.part_weight.setValue(weight)


# ----------------------------------------------------------------------------------------------------------------------
    def weight(self) -> float:
        """Return the calculated weight of an individual part in grams."""
        return self.ui.part_weight.value()





# End of File
