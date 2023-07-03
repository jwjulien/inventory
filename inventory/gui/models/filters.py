# ======================================================================================================================
#      File:  /inventory/gui/models/filters.py
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
"""Subclassing the QSortFilterProxyModel to support wildcards on multiple columns."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore



# ======================================================================================================================
# Or Sort Filter Proxy Model Class
# ----------------------------------------------------------------------------------------------------------------------
class OrSortFilterProxyModel(QtCore.QSortFilterProxyModel):
    """Extend the default behavior of the QSortFilterProxyModel to support multiple columns for filtering."""
    def setFilterKeyColumns(self, *args):
        self.filter_columns = args

    def filterAcceptsRow(self, source_row: int, source_parent: QtCore.QModelIndex) -> bool:
        for column in self.filter_columns:
            index = self.sourceModel().createIndex(source_row, column)
            value = self.sourceModel().data(index, QtCore.Qt.DisplayRole)
            match = self.filterRegularExpression().match(value)
            if match.hasMatch():
                return True
        return False



# End of File
