# ======================================================================================================================
#      File:  /inventory/gui/pages/parts.py
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
"""Main window stacked widget part view page."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtGui, QtWidgets
from sqlalchemy.orm import Session

from inventory.gui.base.page_parts import Ui_PageParts
from inventory.gui.dialogs.part import PartDialog
from inventory.model import Part




# ======================================================================================================================
# Page Parts Widget
# ----------------------------------------------------------------------------------------------------------------------
class PageParts(QtWidgets.QWidget):
    def __init__(self, parent, engine):
        super().__init__(parent)
        self.ui = Ui_PageParts()
        self.ui.setupUi(self)
        self.engine = engine

        self.ui.parts.doubleClicked.connect(self.selected)


    def refresh(self):
        self.ui.parts.clearContents()
        with Session(self.engine) as session:
            for part in Part.GetAll(session):
                idx = self.ui.parts.rowCount()
                self.ui.parts.insertRow(idx)
                category = QtWidgets.QTableWidgetItem(part.category.full_title)
                category.setData(QtCore.Qt.UserRole, part.id)
                self.ui.parts.setItem(idx, 0, category)
                self.ui.parts.setItem(idx, 1, QtWidgets.QTableWidgetItem(part.value))
                self.ui.parts.setItem(idx, 2, QtWidgets.QTableWidgetItem(part.package))
                self.ui.parts.setItem(idx, 3, QtWidgets.QTableWidgetItem(str(part.quantity)))
                self.ui.parts.setItem(idx, 4, QtWidgets.QTableWidgetItem(f'${part.price:.2f}'))
        self.ui.parts.resizeColumnsToContents()


    def selected(self) -> None:
        selected = self.ui.parts.selectedIndexes()
        row = selected[0].row()
        category = self.ui.parts.item(row, 0)
        id = category.data(QtCore.Qt.UserRole)
        with Session(self.engine) as session:
            part = Part.GetById(session, id)
            dialog = PartDialog(self, self.engine, part)
            result = dialog.exec()
            print(result)




# End of File
