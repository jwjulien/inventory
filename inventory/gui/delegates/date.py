# ======================================================================================================================
#      File:  /inventory/gui/delegates/date.py
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
"""Date entry delegate specifically for editing in QTreeWidget (might also work in QTableWidget...)."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from typing import Union
from PySide6 import QtCore, QtGui, QtWidgets
import PySide6.QtCore
import PySide6.QtWidgets




# ======================================================================================================================
# Date Delegate Class
# ----------------------------------------------------------------------------------------------------------------------
class DateDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent, tree: QtWidgets.QTreeWidget):
        super().__init__(parent)
        self.tree = tree


    def createEditor(self,
                     parent: QtWidgets.QListWidget,
                     option: QtWidgets.QStyleOptionViewItem,
                     index: QtCore.QModelIndex
                     )-> QtWidgets.QDateEdit:
        """Create the DateEdit editor view."""
        editor = QtWidgets.QDateEdit(parent)
        item = self.tree.itemAt(0, index.row())
        editor.setDisplayFormat('MM/dd/yy')
        revision = item.data(0, QtCore.Qt.UserRole)
        editor.setDate(revision.date)
        return editor


# # ----------------------------------------------------------------------------------------------------------------------
#     def setEditorData(self, editor: QtWidgets.QDateEdit, index: QtCore.QModelIndex) -> None:
#         """Set the ComboBox's current index."""
#         item = self.parent().itemAt(0, index.row())
#         revision = item.data(0, QtCore.Qt.UserRole)
#         editor.setDate(revision.date)


# ----------------------------------------------------------------------------------------------------------------------
    def setModelData(self,
                     editor: QtWidgets.QDateEdit,
                     model: QtCore.QAbstractItemModel,
                     index: QtCore.QModelIndex
                     ) -> None:
        """Set the table's model's data when finished editing."""
        value = editor.date().toPython().strftime('%m/%d/%y')
        model.setData(index, value)



# End of File
