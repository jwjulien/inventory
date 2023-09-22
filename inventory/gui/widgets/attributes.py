# ======================================================================================================================
#      File:  /inventory/gui/widgets/attributes.py
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
"""Widget for editing additional part attributes (key value pairs)."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import re
from typing import Dict, List

from PySide6 import QtCore, QtGui, QtWidgets

from inventory.gui.base.widget_attributes import Ui_AttributesWidget



# ======================================================================================================================
# Attribute Key Validator Class
# ----------------------------------------------------------------------------------------------------------------------
class AttributeKeyValidator(QtGui.QValidator):
    """A validator specific to part attribute keys.

    They must only contain lowercase letters and numbers and must be unique.
    """

    def __init__(self, parent, invalid: List[str]):
        super().__init__(parent)
        self.invalid = invalid


# ----------------------------------------------------------------------------------------------------------------------
    def validate(self, text: str, _position: int):
        if not text:
            return QtGui.QValidator.State.Intermediate
        if text in self.invalid:
            return QtGui.QValidator.State.Invalid
        matches = re.match('^[a-zA-Z_][a-zA-Z0-9_]{0,20}$', text)
        if matches is None:
            return QtGui.QValidator.State.Invalid
        return QtGui.QValidator.State.Acceptable


# ----------------------------------------------------------------------------------------------------------------------
    def fixup(self, text: str) -> str:
        return re.sub('[^a-zA-Z0-9_]{1,20}$', '', text)




# ======================================================================================================================
# Attribute Key Editor Class
# ----------------------------------------------------------------------------------------------------------------------
class AttributeKeyEditor(QtWidgets.QStyledItemDelegate):
    """A delegate for editing the key column that applies the above validator class."""
    def __init__(self, parent):
        super().__init__(parent)
        self._options = []


# ----------------------------------------------------------------------------------------------------------------------
    def createEditor(self,
                     parent: QtWidgets.QWidget,
                     option: QtWidgets.QStyleOptionViewItem,
                     index: QtCore.QModelIndex
                     ) -> QtWidgets.QWidget:
        combo = QtWidgets.QComboBox(parent)
        combo.addItems(self._options)
        combo.setEditable(True)

        # Gather a list of existing keys that do not belong to this row.
        existing = [self.parent().item(row, 0).text() for row in range(self.parent().rowCount()) if row != index.row()]

        # Setup a validator to keep an eye on the text that the user enters.
        validator = AttributeKeyValidator(combo, existing)
        combo.setValidator(validator)

        return combo


# ----------------------------------------------------------------------------------------------------------------------
    def setOptions(self, options: List[str]) -> None:
        """Set a list of options to be used in the combo box delegate for this editor."""
        self._options = options




# ======================================================================================================================
# Attributes Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class AttributesWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_AttributesWidget()
        self.ui.setupUi(self)

        # Setup a delegate for editing key column.
        self._delegate = AttributeKeyEditor(self.ui.attributes)
        self.ui.attributes.setItemDelegateForColumn(0, self._delegate)

        # Connect events.
        self.ui.add.clicked.connect(self.add)
        self.ui.remove.clicked.connect(self.remove)
        self.ui.attributes.itemSelectionChanged.connect(self.selected)
        self.ui.attributes.itemChanged.connect(self.changed)


# ----------------------------------------------------------------------------------------------------------------------
    def setAttributes(self, attributes: Dict[str, str]):
        self.ui.attributes.blockSignals(True)

        # Empty any existing items from the table.
        while self.ui.attributes.rowCount():
            self.ui.attributes.removeRow(0)

        # Put items into table.
        for attribute, value in attributes.items():
            row = self.ui.attributes.rowCount()
            self.ui.attributes.insertRow(row)
            key = QtWidgets.QTableWidgetItem(attribute)
            key.setData(QtCore.Qt.UserRole, attribute)
            self.ui.attributes.setItem(row, 0, key)
            self.ui.attributes.setItem(row, 1, QtWidgets.QTableWidgetItem(value))

        self.ui.attributes.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.ui.attributes.blockSignals(False)


# ----------------------------------------------------------------------------------------------------------------------
    def attributes(self) -> Dict[str, str]:
        attributes = {}
        for row in range(self.ui.attributes.rowCount()):
            # Skip any attributes that don't have a key/value pair set (they raise AttributeError on call to `text`).
            try:
                key = self.ui.attributes.item(row, 0).text()
                value = self.ui.attributes.item(row, 1).text()
            except AttributeError:
                continue
            attributes[key] = value
        return attributes


# ----------------------------------------------------------------------------------------------------------------------
    def setSuggestions(self, suggestions: List[str]) -> None:
        """Set a list of suggestions for possible attributes when adding new ones to the widget."""
        # Remove existing values from the list of suggestions.
        current = [self.ui.attributes.item(row, 0).text() for row in range(self.ui.attributes.rowCount())]
        for text in current:
            if text in suggestions:
                suggestions.remove(text)

        # Pass the remaining suggestion(s) to the delegate.
        self._delegate.setOptions(suggestions)


# ----------------------------------------------------------------------------------------------------------------------
    def selected(self) -> None:
        selection = self.ui.attributes.selectedItems()
        rows = set([item.row() for item in selection])
        self.ui.remove.setEnabled(bool(rows))
        self.ui.remove.setText('Remove Attribute' + ('s' if len(rows) > 1 else ''))


# ----------------------------------------------------------------------------------------------------------------------
    def changed(self, item: QtWidgets.QTableWidgetItem) -> None:
        self.ui.attributes.sortByColumn(0, QtCore.Qt.AscendingOrder)


# ----------------------------------------------------------------------------------------------------------------------
    def add(self) -> None:
        row = self.ui.attributes.rowCount()
        self.ui.attributes.insertRow(row)
        key = QtWidgets.QTableWidgetItem('')
        self.ui.attributes.setItem(row, 0, key)
        self.ui.attributes.setItem(row, 1, QtWidgets.QTableWidgetItem(''))
        self.ui.attributes.editItem(key)


# ----------------------------------------------------------------------------------------------------------------------
    def remove(self) -> None:
        selection = self.ui.attributes.selectedItems()
        rows = set([selected.row() for selected in selection])
        for row in sorted(rows, reverse=True):
            self.ui.attributes.removeRow(row)




# End of File
