# ======================================================================================================================
#      File:  /inventory/gui/tabs/parts.py
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
"""Main window part list tab."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from typing import List

from PySide6 import QtCore, QtWidgets

from inventory.gui.base.tab_parts import Ui_TabParts
from inventory.gui.dialogs.part import PartDialog
from inventory.gui.constants import Brushes
from inventory.model.parts import Part




# ======================================================================================================================
# Tab Parts Widget
# ----------------------------------------------------------------------------------------------------------------------
class TabParts(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_TabParts()
        self.ui.setupUi(self)

        # Setup model with all of the parts.
        parts: List[Part] = Part.select()
        for row, part in enumerate(parts):
            self._insert_row(row)
            self._update_row(row, part)
        self.ui.parts.resizeColumnsToContents()

        # Connect events.
        self.ui.add.clicked.connect(self.add)
        self.ui.parts.doubleClicked.connect(self.edit)
        self.ui.filter.textChanged.connect(self.filter)


# ----------------------------------------------------------------------------------------------------------------------
    def _insert_row(self, row: int) -> None:
        self.ui.parts.insertRow(row)
        for column in range(self.ui.parts.columnCount()):
            self.ui.parts.setItem(row, column, QtWidgets.QTableWidgetItem(''))


# ----------------------------------------------------------------------------------------------------------------------
    def _update_row(self, row: int, part: Part) -> None:
        category = self.ui.parts.item(row, 0)
        category.setText(part.category.full_title)
        category.setData(QtCore.Qt.UserRole, part)

        self.ui.parts.item(row, 1).setText(part.value)
        self.ui.parts.item(row, 2).setText(part.number)
        self.ui.parts.item(row, 3).setText(part.package)

        quantity = self.ui.parts.item(row, 4)
        quantity.setText(str(part.quantity))
        if part.needs_reorder:
            quantity.setForeground(Brushes.Danger)
        elif part.low_stock:
            quantity.setForeground(Brushes.Warning)
        else:
            item = QtWidgets.QTreeWidgetItem()
            brush = item.foreground(0)
            quantity.setForeground(brush)

        self.ui.parts.item(row, 5).setText(f'${part.price:.3f}')
        self.ui.parts.item(row, 6).setText(f'${part.liability:.2f}')


# ----------------------------------------------------------------------------------------------------------------------
    def add(self) -> None:
        part = Part()
        if PartDialog(self, part).exec():
            row = self.ui.parts.rowCount()
            self._insert_row(row)
            self._update_row(row, part)


# ----------------------------------------------------------------------------------------------------------------------
    def edit(self) -> None:
        selected = self.ui.parts.selectedItems()[0]
        part = selected.data(QtCore.Qt.UserRole)
        if PartDialog(self, part).exec():
            self._update_row(selected.row(), part)


# ----------------------------------------------------------------------------------------------------------------------
    def filter(self) -> None:
        """Filter the contents of the parts table based upon the filter input text.

        The text in the filter input is split on spaces and compared against the `category`, `value`, `package` and
        `number` attributes of the Part.  For each word in the filter input, the text must be a wildcard match against
        at least one of those columns for the row to be shown.  In other words, there is an implicit "AND" between each
        word in the filter input.

        Note: There is room for significant improvement here, such as using AND/OR/XOR operators within the filter text.
        """
        filter_text = [f'*{word}*' for word in self.ui.filter.text().split(' ')]
        filter_res = [QtCore.QRegularExpression().fromWildcard(text, QtCore.Qt.CaseInsensitive) for text in filter_text]
        for row in range(self.ui.parts.rowCount()):
            # Gather the text from each of the columns that we want to filter on.
            columns = [self.ui.parts.item(row, column).text() for column in [0, 1, 2, 3]]

            # To show a row, we need at least one match from any of the columns for each filter word.
            matches = []
            for filter_re in filter_res:
                match = False
                for text in columns:
                    # If we get a match for this keyword on any column, set match to True and push it into matches.
                    if filter_re.match(text).hasMatch():
                        match = True
                        break
                matches.append(match)

            # Matches contains a bool for each word in the filter box, we need all of them to have a match to show the
            # row.
            show = all(matches)
            self.ui.parts.setRowHidden(row, not show)




# End of File
