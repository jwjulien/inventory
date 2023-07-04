# ======================================================================================================================
#      File:  /inventory/gui/tabs/suppliers.py
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
"""Tab listing suppliers and their associated parts."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from typing import List

from PySide6 import QtCore, QtWidgets

from inventory.gui.base.tab_suppliers import Ui_TabSuppliers
from inventory.gui.dialogs.supplier import SupplierDialog
from inventory.model.suppliers import Supplier, SupplierPart




# ======================================================================================================================
# Tab Supplier
# ----------------------------------------------------------------------------------------------------------------------
class TabSuppliers(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_TabSuppliers()
        self.ui.setupUi(self)

        # Add suppliers to the list widget.
        suppliers: List[Supplier] = Supplier.select()
        for supplier in suppliers:
            self._add_item(supplier)

        self.ui.suppliers.sortItems(QtCore.Qt.AscendingOrder)

        # Connect events.
        self.ui.suppliers.doubleClicked.connect(self._edit)
        self.ui.suppliers.itemSelectionChanged.connect(self._selected)
        self.ui.add.clicked.connect(self._add)
        self.ui.remove.clicked.connect(self._remove)


# ----------------------------------------------------------------------------------------------------------------------
    def _add_item(self, supplier: Supplier) -> QtWidgets.QListWidgetItem:
        item = QtWidgets.QListWidgetItem(supplier.name)
        item.setData(QtCore.Qt.UserRole, supplier)
        self.ui.suppliers.addItem(item)
        return item

# ----------------------------------------------------------------------------------------------------------------------
    def _selected(self) -> None:
        selected = self.ui.suppliers.selectedItems()
        suppliers = [item.data(QtCore.Qt.UserRole) for item in selected]
        parts = [part for supplier in suppliers for part in supplier.parts]
        self.ui.parts.setParts(parts)


# ----------------------------------------------------------------------------------------------------------------------
    def _edit(self) -> None:
        selected = self.ui.suppliers.selectedItems()
        if len(selected) != 1:
            return
        item = selected[0]
        supplier = item.data(QtCore.Qt.UserRole)
        if SupplierDialog(self, supplier).exec():
            item.setText(supplier.name)
            self.ui.suppliers.sortItems(QtCore.Qt.AscendingOrder)


# ----------------------------------------------------------------------------------------------------------------------
    def _add(self) -> None:
        supplier = Supplier()
        if SupplierDialog(self, supplier).exec():
            self._add_item(supplier)
            self.ui.suppliers.sortItems(QtCore.Qt.AscendingOrder)


# ----------------------------------------------------------------------------------------------------------------------
    def _remove(self) -> None:
        selected = self.ui.suppliers.selectedItems()
        if not selected:
            return
        for item in selected:
            supplier = item.data(QtCore.Qt.UserRole)
            if supplier.parts:
                msg = QtWidgets.QMessageBox(self)
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle('Error')
                msg.setText('Cannot remove a supplier that\nhas parts associated with it.')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                return
            self.ui.suppliers.takeItem(self.ui.suppliers.row(item))
            supplier.delete_instance()




# End of File
