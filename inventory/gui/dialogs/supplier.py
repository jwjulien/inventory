# ======================================================================================================================
#      File:  /inventory/gui/dialogs/supplier.py
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
"""Dialog for editing supplier information."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtWidgets

from inventory.gui.base.dialog_supplier import Ui_SupplierDialog
from inventory.model.suppliers import Supplier




# ======================================================================================================================
# Supplier Dialog
# ----------------------------------------------------------------------------------------------------------------------
class SupplierDialog(QtWidgets.QDialog):
    def __init__(self, parent, supplier: Supplier):
        super().__init__(parent)
        self.ui = Ui_SupplierDialog()
        self.ui.setupUi(self)

        self.supplier = supplier

        self.ui.name.setText(supplier.name)
        self.ui.website.setText(supplier.website)
        self.ui.search.setText(supplier.search)


# ----------------------------------------------------------------------------------------------------------------------
    def accept(self) -> None:
        self.supplier.name = self.ui.name.text()
        self.supplier.website = self.ui.website.text()
        self.supplier.search = self.ui.search.text()
        self.supplier.save()
        return super().accept()




# End of File
