# ======================================================================================================================
#      File:  /inventory/gui/models/categories.py
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
"""QAbstractTableModel extension specifically for a tree of categories."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from typing import List
from PySide6 import QtCore

from inventory.model.categories import Category
from inventory.gui.models.converter import Converter, Column




# ======================================================================================================================
# Category Tree Item
# ----------------------------------------------------------------------------------------------------------------------
# class TreeItem:
#     def __init__(self, category: PartCategory, parent=None):
#         self.parent_item: 'TreeItem' = parent
#         self.child_items: List['TreeItem'] = []
#         self.data: PartCategory = category


#     def child(self, row: int) -> 'TreeItem':
#         return self.child_items[row]


#     def child_count(self) -> int:
#         return len(self.child_items)


#     def child_number(self) -> int:
#         if self.parent_item is not None:
#             self.parent_item.child_items.index(self)
#         return 0

#     def column_count(self) -> int:
#         return 2


#     def data(self, column) -> str:
#         if column == 0:
#             return self.data.title
#         if column == 1:
#             return self.data.designator
#         return ''


#     def insert_children(self, position: int, count: int, columns: int) -> bool:
#         if position < 0 or position > self.child_count:
#             return False

#         for row in range(count):




# ======================================================================================================================
# Category Tree Model
# ----------------------------------------------------------------------------------------------------------------------
class CategoryTreeModel(QtCore.QAbstractItemModel):
    def __init__(self, parent):
        super().__init__(parent)
        self.columns = [
            Column('Title', Converter('title')),
            Column('Designator', Converter('designator', null='N/A'))
        ]

        # roots = Category.select().where(Category.parent == None)

        # Wrap the roots into a single root (because that's how Qt thinks) and deliberately don't call save on this new
        # instance.  This is not intended to be stored in the database.
        # self.root_item = Category(title='root', children=roots)


# ----------------------------------------------------------------------------------------------------------------------
    def columnCount(self, parent: QtCore.QModelIndex = None) -> int:
        return len(self.columns)


# ----------------------------------------------------------------------------------------------------------------------
    def rowCount(self, parent: QtCore.QModelIndex = None) -> int:
        parent_item = self._get_item(parent)
        return len(parent_item.children)


# ----------------------------------------------------------------------------------------------------------------------
    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole) -> str:
        if not index.isValid():
            return None

        category = self._get_item(index)

        if role in [QtCore.Qt.DisplayRole, QtCore.Qt.EditRole]:
            converter = self.columns[index.column()].converter
            return converter.get(category)

        elif role == QtCore.Qt.UserRole:
            return category

        return None


# ----------------------------------------------------------------------------------------------------------------------
    def headerData(self, column: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole) -> str:
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.columns[column].title

        return None


# ----------------------------------------------------------------------------------------------------------------------
    def index(self, row: int, column: int, parent: QtCore.QModelIndex) -> QtCore.QModelIndex:
        if parent.isValid() and parent.column() != 0:
            return QtCore.QModelIndex()

        parent_item = self._get_item(parent)
        child_item = parent_item.children[row]
        if child_item:
            return self.createIndex(row, column, child_item)

        return QtCore.QModelIndex()


# ----------------------------------------------------------------------------------------------------------------------
    def _get_item(self, index: QtCore.QModelIndex) -> Category:
        if index.isValid():
            item = index.internalPointer()
            if item:
                return Category.get_by_id(item)

        # Invalid index indicates a request for the root item.  We don't have a single root in the database, we have
        # many, so we need to build a fake root Category instead.
        roots = Category.select().where(Category.parent == None)
        return Category(title='root', children=roots)


# ----------------------------------------------------------------------------------------------------------------------
    def parent(self, index: QtCore.QModelIndex) -> QtCore.QModelIndex:
        if not index.isValid():
            return QtCore.QModelIndex()

        child_item = self._get_item(index)
        parent_item = child_item.parent

        if parent_item is None:
            return QtCore.QModelIndex()

        return self.createIndex(parent_item.child_number, 0, parent_item)


# # ----------------------------------------------------------------------------------------------------------------------
#     def flags(self, index: QtCore.QModelIndex) -> QtCore.Qt.ItemFlag:
#         return super().flags(index) | QtCore.Qt.ItemIsEditable


# # ----------------------------------------------------------------------------------------------------------------------
#     def setData(self, index: QtCore.QModelIndex, value: str, role: QtCore.Qt.ItemDataRole) -> None:
#         if not index.isValid():
#             return

#         category = self.categories[index.row()]

#         if role == QtCore.Qt.EditRole:
#             converter = self.columns.values()[index.column()].converter
#             converter.set(category, value)


# # ----------------------------------------------------------------------------------------------------------------------
#     def setHeaderData(self, section: int, orientation: QtCore.Qt.Orientation, value: any, role: int = ...) -> bool:
#         return super().setHeaderData(section, orientation, value, role)


# # ----------------------------------------------------------------------------------------------------------------------
#     def insertColumn(self, position: int, count: int, parent: QtCore.QModelIndex) -> None:
#         raise ValueError('This model does not support adding new columns')


# # ----------------------------------------------------------------------------------------------------------------------
#     def removeColumns(self, position: int, count: int, parent: QtCore.QModelIndex) -> None:
#         raise ValueError('This model does not support removing columns')


# # ----------------------------------------------------------------------------------------------------------------------
#     def insertRows(self, position: int, count: int, parent: QtCore.QModelIndex) -> None:
#         for _ in range(count):
#             self.categories.insert(position, PartCategory())
#             # TODO: Need to set some reasonable defaults for PartCategory


# # ----------------------------------------------------------------------------------------------------------------------
#     def removeRows(self, position: int, count: int, parent: QtCore.QModelIndex) -> None:
#         for _ in range(count):
#             self.categories.pop(position)




# End of File
