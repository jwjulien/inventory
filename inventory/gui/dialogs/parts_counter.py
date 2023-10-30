# ======================================================================================================================
#      File:  /inventory/gui/dialogs/parts_counter.py
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
"""Parts counter dialog uses a USB connected scale to count parts by weight."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from collections import deque

from PySide6 import QtCore, QtWidgets
from partsscale.scale import Scale

from inventory.gui.base.dialog_parts_counter import Ui_PartsCounterDialog
from inventory.model.parts import Part




# ======================================================================================================================
# Parts Counter Dialog
# ----------------------------------------------------------------------------------------------------------------------
class PartsCounterDialog(QtWidgets.QDialog):
    def __init__(self, parent, part: Part):
        super().__init__(parent)
        self.ui = Ui_PartsCounterDialog()
        self.ui.setupUi(self)

        self.scale = Scale()
        self.part = part
        self._count: int = 0
        self._weights = deque(maxlen=10)

        self.ui.part_weight.setValue(self.part.weight)
        self.ui.drawer_weight.setValue(19.35820770263672)

        self.ui.tare.clicked.connect(self.scale.tare)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.periodic)
        self.timer.start(125)


# ----------------------------------------------------------------------------------------------------------------------
    def periodic(self) -> None:
        self._weights.append(self.scale.weight())
        weight = sum(self._weights) / len(self._weights)
        if self.ui.sub_drawer.isChecked():
            weight -= self.ui.drawer_weight.value()
        self.ui.weight.display(f'{weight:.3f}'[:5])
        self._count = int((weight / self.ui.part_weight.value()) + 0.5)
        self.ui.count.display(self._count if self._count else '---')


# ----------------------------------------------------------------------------------------------------------------------
    def count(self) -> int:
        """Return the current part count value."""
        return self._count




# End of File
