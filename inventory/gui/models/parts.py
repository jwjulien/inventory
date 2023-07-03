# ======================================================================================================================
#      File:  /inventory/gui/models/parts.py
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
"""QAbstractTableModel extension specifically for a table of parts."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtGui, QtWidgets

from inventory.model import Part
from inventory.gui.constants import Brushes




# ======================================================================================================================
# Parts Table Model
# ----------------------------------------------------------------------------------------------------------------------
class PartsTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, session):
        super().__init__(parent)
        self.header = [
            'Category',
            'Value',
            'Package',
            'Quantity',
            'Price'
        ]

        self.parts = Part.GetAll(session)


    def rowCount(self, parent):
        return len(self.parts)


    def columnCount(self, parent):
        return len(self.header)


    def data(self, index, role):
        if not index.isValid():
            return None

        part = self.parts[index.row()]

        if role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                return part.category.full_title
            elif index.column() == 1:
                return part.value
            elif index.column() == 2:
                return part.package
            elif index.column() == 3:
                return str(part.quantity)
            elif index.column() == 4:
                return f'${part.price:.2f}'

        elif role == QtCore.Qt.UserRole:
            return part

        elif role == QtCore.Qt.ForegroundRole:
            if index.column() == 3 and part.threshold:
                if part.quantity < part.threshold:
                    return Brushes.Danger
                elif part.quantity < (part.threshold + 5):
                    return Brushes.Warning


        return None


    def headerData(self, column: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[column]

        return None




# End of File
