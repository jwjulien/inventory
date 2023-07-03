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
            item = QtWidgets.QTreeWidgetItem(parent, [category.title, category.inherited_designator])
            item.setData(0, QtCore.Qt.UserRole, category)
            for child in category.children:
                item.addChild(recurse(child, item))
            return item
        for root in roots:
            self.ui.categories.addTopLevelItem(recurse(root, None))

        self.ui.categories.setColumnWidth(0, 350)
        self.ui.categories.expandAll()

        # Connect events.
        self.ui.categories.doubleClicked.connect(self.selected)
        QtGui.QShortcut(QtGui.QKeySequence("Insert"), self.ui.categories, self.insert)


    def selected(self) -> None:
        # Get the currently selected category from the tree.
        selected = self.ui.categories.selectedIndexes()[0]
        category = selected.data(QtCore.Qt.UserRole)

        # Show a dialog to let the user make changes.  Dialog will save to database if user accepts.
        if CategoryDialog(self, category).exec():
            # User accepted the changes - update the tree with the changed values.
            item = self.ui.categories.itemFromIndex(selected)
            item.setText(0, category.title)
            item.setText(1, category.inherited_designator)


    def insert(self) -> None:
        print('Insert!')


# End of File
