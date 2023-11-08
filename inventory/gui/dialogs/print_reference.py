# ======================================================================================================================
#      File:  /inventory/gui/dialogs/print_reference.py
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
"""A dialog to help preview and print References."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtGui, QtWidgets
from PIL.ImageQt import ImageQt

from inventory.gui.base.dialog_print_reference import Ui_PrintReferenceDialog
from inventory.libraries.references import Reference
from inventory.libraries.printer.printers import LabelWriter450




# ======================================================================================================================
# Print Reference Dialog
# ----------------------------------------------------------------------------------------------------------------------
class PrintReferenceDialog(QtWidgets.QDialog):
    def __init__(self, parent, reference: Reference):
        super().__init__(parent)
        self.ui = Ui_PrintReferenceDialog()
        self.ui.setupUi(self)

        self.setWindowTitle(f'Print {reference.target.name} {reference.label} Label')
        self.ui.buttons.button(self.ui.buttons.StandardButton.Ok).setText('Print')

        self.label = reference.barcode_label()

        qt_image = ImageQt(self.label.image())
        self.ui.preview.setPixmap(QtGui.QPixmap.fromImage(qt_image))


    def accept(self) -> None:
        """Print the Reference label if the user accepts the dialog."""
        printer = LabelWriter450()
        self.label.print(printer)
        super().accept()




# End of File
