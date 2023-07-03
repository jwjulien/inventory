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

from inventory.gui.base.tab_categories import Ui_TabCategories
from inventory.gui.dialogs.category import CategoryDialog
from inventory.model.categories import Category




# ======================================================================================================================
# Tab Categories Widget
# ----------------------------------------------------------------------------------------------------------------------
class TabCategories(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_TabCategories()
        self.ui.setupUi(self)

        # Load categories into TreeWidget.
        roots = Category.select().where(Category.parent == None)
        def recurse(category: Category, parent: QtWidgets.QTreeWidgetItem) -> QtWidgets.QTreeWidgetItem:
            item = self._make_item(parent, category)
            for child in category.children:
                item.addChild(recurse(child, item))
            return item
        for root in roots:
            self.ui.categories.addTopLevelItem(recurse(root, None))

        self._sort()

        # Update the layout a bit for better readability.
        self.ui.categories.setColumnWidth(0, 350)
        self.ui.categories.expandAll()

        # Connect events.
        self.ui.categories.doubleClicked.connect(self.edit)
        QtGui.QShortcut(QtGui.QKeySequence("Insert"), self.ui.categories, self.insert_sibling)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Insert"), self.ui.categories, self.insert_child)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+]"), self.ui.categories, self.make_child)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+["), self.ui.categories, self.make_sibling)


# ----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _make_item(parent: QtWidgets.QTreeWidgetItem, category: Category) -> QtWidgets.QTreeWidgetItem:
        item = QtWidgets.QTreeWidgetItem(parent, [category.title, category.inherited_designator])
        item.setData(0, QtCore.Qt.UserRole, category)
        return item


# ----------------------------------------------------------------------------------------------------------------------
    def _sort(self) -> None:
        """Sort the list of categories alphabetically by title."""
        self.ui.categories.sortItems(0, QtCore.Qt.AscendingOrder)


# ----------------------------------------------------------------------------------------------------------------------
    def edit(self) -> None:
        """Edit the selected category.

        Present the user with the CategoryDialog for editing the values for an existing category.
        """
        # Get the currently selected category from the tree.
        selected = self.ui.categories.selectedIndexes()[0]
        category: Category = selected.data(QtCore.Qt.UserRole)

        # Show a dialog to let the user make changes.  Dialog will save to database if user accepts.
        if CategoryDialog(self, category).exec():

            # User accepted the changes - update the tree with the changed values.
            item = self.ui.categories.itemFromIndex(selected)
            item.setText(0, category.title)
            item.setText(1, category.inherited_designator)

            self._sort()


# ----------------------------------------------------------------------------------------------------------------------
    def insert_sibling(self) -> None:
        selected = self.ui.categories.selectedItems()
        if not selected:
            return
        selected = selected[-1]
        selected_category = selected.data(0, QtCore.Qt.UserRole)

        # To be a sibling, we want parent to be the same parent as selected.
        parent = selected_category.parent
        category = Category(parent=parent)

        if CategoryDialog(self, category).exec():
            # If not parent then insert this item as a new top level item.
            if parent is None:
                item = self._make_item(None, category)
                self.ui.categories.addTopLevelItem(item)

            # Otherwise, append this item to the selected item's parent item.
            else:
                item = self._make_item(selected.parent(), category)
                selected.parent().addChild(item)

            # Resort the tree to shuffle this new item into the proper location.
            self._sort()


# ----------------------------------------------------------------------------------------------------------------------
    def insert_child(self) -> None:
        selected = self.ui.categories.selectedItems()
        if not selected:
            return
        selected = selected[-1]
        parent = selected.data(0, QtCore.Qt.UserRole)

        category = Category(parent=parent)

        if CategoryDialog(self, category).exec():
            # Insert this new item as a child of the original selection.
            item = self._make_item(selected, category)
            selected.addChild(item)

            # Resort the tree to shuffle this new item into the proper location.
            self._sort()


# ----------------------------------------------------------------------------------------------------------------------
    def make_child(self) -> None:
        selected = self.ui.categories.selectedItems()
        if len(selected) <= 1:
            return
        destination_item = selected.pop()
        destination_category = destination_item.data(0, QtCore.Qt.UserRole)
        for source_item in selected:
            # Move the item in the TreeWidget.
            if source_item.parent():
                source_item.parent().removeChild(source_item)
            else:
                self.ui.categories.takeTopLevelItem(self.ui.categories.indexOfTopLevelItem(source_item))
            destination_item.addChild(source_item)

            # Move the item in the model.
            source_category = source_item.data(0, QtCore.Qt.UserRole)
            source_category.parent = destination_category
            source_category.save()

        # Resort the tree now that the items have been moved.
        self._sort()


# ----------------------------------------------------------------------------------------------------------------------
    def make_sibling(self) -> None:
        selected = self.ui.categories.selectedItems()
        if not selected:
            return
        for selected_item in selected:
            # Move the item in the tree first.
            parent = selected_item.parent()
            if not parent:
                # Item is already in the root of the tree - skip it.
                continue
            parent.removeChild(selected_item)
            if parent.parent():
                parent.parent().addChild(selected_item)
            else:
                self.ui.categories.addTopLevelItem(selected_item)

            # Move the item in the model.
            selected_category = selected_item.data(0, QtCore.Qt.UserRole)
            selected_category.parent = selected_category.parent.parent
            selected_category.save()

        self._sort()




# End of File
