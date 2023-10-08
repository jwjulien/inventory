# ======================================================================================================================
#      File:  /inventory/gui/widgets/materials.py
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
"""Project info viewing widget within the parts dialog."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtWidgets

from inventory.gui.base.widget_materials import Ui_MaterialWidget
from inventory.model.projects import Material
from inventory.model.parts import Part




# ======================================================================================================================
# Materials Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class MaterialsWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_MaterialWidget()
        self.ui.setupUi(self)

        self.part: Part = None

        # Setup header to best show column contents.
        header = self.ui.materials.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)


# ----------------------------------------------------------------------------------------------------------------------
    def setPart(self, part: Part) -> None:
        self.part = part

        for material in self.part.materials:
            row = self._insert_row()
            self._update_row(row, material)


# ----------------------------------------------------------------------------------------------------------------------
    def _insert_row(self) -> int:
        row = self.ui.materials.rowCount()
        self.ui.materials.insertRow(row)
        self.ui.materials.setItem(row, 0, QtWidgets.QTableWidgetItem(''))
        self.ui.materials.setItem(row, 1, QtWidgets.QTableWidgetItem(''))
        self.ui.materials.setItem(row, 2, QtWidgets.QTableWidgetItem(''))
        self.ui.materials.item(row, 0).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        return row


# ----------------------------------------------------------------------------------------------------------------------
    def _update_row(self, row: int, material: Material) -> None:
        self.ui.materials.item(row, 0).setData(QtCore.Qt.UserRole, material)
        self.ui.materials.item(row, 0).setText(material.revision.project.title)
        self.ui.materials.item(row, 0).setToolTip(material.revision.project.description)
        self.ui.materials.item(row, 1).setText(
            f"{material.revision.version} ({material.revision.date.strftime('%Y-%m-%d')})")
        self.ui.materials.item(row, 2).setText(material.designator)




# End of File
