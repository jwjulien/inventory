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
from PySide6 import QtCore, QtGui, QtWidgets
from sqlalchemy.orm import Session

from inventory.gui.base.tab_parts import Ui_TabParts
from inventory.gui.dialogs.part import PartDialog
from inventory.gui.constants import Brushes
from inventory.gui.models.parts import PartsTableModel
from inventory.gui.models.filters import OrSortFilterProxyModel
from inventory.model import Part




# ======================================================================================================================
# Tab Parts Widget
# ----------------------------------------------------------------------------------------------------------------------
class TabParts(QtWidgets.QWidget):
    def __init__(self, parent, session):
        super().__init__(parent)
        self.ui = Ui_TabParts()
        self.ui.setupUi(self)

        # Setup model with all of the parts.
        self.session = session
        self.model = PartsTableModel(self, self.session)

        # Setup a proxy to handle filtering of parts.
        self.proxy = OrSortFilterProxyModel(self.ui.parts)
        self.proxy.setSourceModel(self.model)
        self.proxy.setFilterKeyColumns(0, 1, 2)
        self.proxy.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.filter.textChanged.connect(lambda: self.proxy.setFilterWildcard(self.ui.filter.text()))
        self.ui.parts.setModel(self.proxy)

        # Connect events.
        self.ui.parts.doubleClicked.connect(self.selected)


    def selected(self) -> None:
        selected = self.ui.parts.selectedIndexes()[0]
        part = self.proxy.data(selected, QtCore.Qt.UserRole)
        PartDialog(self, self.session, part).exec()
        left = self.model.createIndex(selected.row(), 0)
        right = self.model.createIndex(selected.row(), self.model.columnCount(None) - 1)
        self.ui.parts.dataChanged(left, right, [QtCore.Qt.DisplayRole, QtCore.Qt.ForegroundRole])




# End of File
