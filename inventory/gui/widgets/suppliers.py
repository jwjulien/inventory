# ======================================================================================================================
#      File:  /inventory/gui/widgets/suppliers.py
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
"""Widget for mapping suppliers into parts."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtWidgets

from inventory.gui.base.widget_suppliers import Ui_SuppliersWidget
from inventory.gui.dialogs.supplier_mapping import SupplierMappingDialog
from inventory.model.suppliers import Supplier, Product
from inventory.model.parts import Part




# ======================================================================================================================
# Supplier Widget
# ----------------------------------------------------------------------------------------------------------------------
class SuppliersWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_SuppliersWidget()
        self.ui.setupUi(self)

        self.part: Part = None

        # Setup header to best show column contents.
        header = self.ui.suppliers.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        # Connect events.
        self.ui.map.clicked.connect(self._map)
        self.ui.edit.clicked.connect(self._edit)
        self.ui.remove.clicked.connect(self._remove)
        self.ui.suppliers.doubleClicked.connect(self._edit)
        self.ui.suppliers.itemSelectionChanged.connect(self._selected)

        # TODO: What about a context menu or button to open a search for an item using the supplier.search url, when
        # available.


# ----------------------------------------------------------------------------------------------------------------------
    def setPart(self, part: Part):
        self.part = part

        for supplier in self.part.products:
            row = self._insert_row()
            self._update_row(row, supplier)


# ----------------------------------------------------------------------------------------------------------------------
    def _insert_row(self) -> int:
        row = self.ui.suppliers.rowCount()
        self.ui.suppliers.insertRow(row)
        self.ui.suppliers.setItem(row, 0, QtWidgets.QTableWidgetItem(''))
        self.ui.suppliers.setItem(row, 1, QtWidgets.QTableWidgetItem(''))
        self.ui.suppliers.item(row, 0).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        return row


# ----------------------------------------------------------------------------------------------------------------------
    def _update_row(self, row: int, product: Product) -> None:
        self.ui.suppliers.item(row, 0).setText(product.supplier.name)
        self.ui.suppliers.item(row, 1).setText(product.number)
        self.ui.suppliers.item(row, 0).setData(QtCore.Qt.UserRole, product)


# ----------------------------------------------------------------------------------------------------------------------
    def _selected(self) -> None:
        selected = self.ui.suppliers.selectedItems()
        rows = list(set([item.row() for item in selected]))
        self.ui.remove.setEnabled(bool(rows))
        self.ui.edit.setEnabled(bool(rows))


# ----------------------------------------------------------------------------------------------------------------------
    def _map(self) -> None:
        product = Product(part=self.part)
        if SupplierMappingDialog(self, product).exec():
            row = self._insert_row()
            self._update_row(row, product)


# ----------------------------------------------------------------------------------------------------------------------
    def _edit(self) -> None:
        selected = self.ui.suppliers.selectedItems()
        if not selected:
            return
        item = selected[0]
        supplier = self.ui.suppliers.item(item.row(), 0).data(QtCore.Qt.UserRole)
        if not supplier:
            return
        if SupplierMappingDialog(self, supplier).exec():
            self._update_row(item.row(), supplier)


# ----------------------------------------------------------------------------------------------------------------------
    def _remove(self) -> None:
        selected = self.ui.suppliers.selectedItems()
        rows = set([item.row() for item in selected])
        for row in sorted(rows, reverse=True):
            supplier: Supplier = self.ui.suppliers.item(row, 0).data(QtCore.Qt.UserRole)
            supplier.delete_instance()
            self.ui.suppliers.removeRow(row)




# End of File
