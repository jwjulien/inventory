# ======================================================================================================================
#      File:  /inventory/gui/dialogs/supplier_mapping.py
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
"""Dialog to allow the user to set a Product, mapping a Supplier to a Part."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtWidgets

from inventory.gui.base.dialog_supplier_mapping import Ui_DialogSupplierMapping
from inventory.model.suppliers import Supplier, Product




# ======================================================================================================================
# Supplier Mapping Dialog
# ----------------------------------------------------------------------------------------------------------------------
class SupplierMappingDialog(QtWidgets.QDialog):
    def __init__(self, parent, product: Product):
        super().__init__(parent)
        self.ui = Ui_DialogSupplierMapping()
        self.ui.setupUi(self)

        self.product = product

        # Load GUI
        self.ui.supplier.clear()
        for supplier in Supplier.select().order_by(Supplier.name):
            self.ui.supplier.addItem(supplier.name, supplier)
            if product.supplier_id and supplier == product.supplier:
                self.ui.supplier.setCurrentText(supplier.name)

        self.ui.number.setText(product.number)


# ----------------------------------------------------------------------------------------------------------------------
    def accept(self) -> None:
        self.product.supplier = self.ui.supplier.currentData(QtCore.Qt.UserRole)
        self.product.number = self.ui.number.text()
        self.product.save()
        return super().accept()




# End of File
