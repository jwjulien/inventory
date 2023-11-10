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
"""Main window category browser/editor tab."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtWidgets
import qtawesome

from inventory.gui.base.tab_categories import Ui_TabCategories
from inventory.gui.dialogs.category import CategoryDialog
from inventory.gui.prompts import Alert, YesNoPrompt
from inventory.gui.tabs.base import TabWidget
from inventory.gui.utilities import context_action
from inventory.model.categories import Category




# ======================================================================================================================
# Tab Categories Widget
# ----------------------------------------------------------------------------------------------------------------------
class TabCategories(TabWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_TabCategories()
        self.ui.setupUi(self)

        # Update the layout a bit for better readability.
        self.ui.categories.setColumnWidth(0, 325)
        self.ui.categories.setColumnWidth(1, 70)
        self.ui.categories.setColumnWidth(2, 30)

        # Add icons to the toolbar buttons.
        self.ui.insert_child.setIcon(qtawesome.icon('mdi.file-tree'))
        self.ui.insert_sibling.setIcon(qtawesome.icon('fa.list'))
        self.ui.make_child.setIcon(qtawesome.icon('fa5s.indent'))
        self.ui.make_sibling.setIcon(qtawesome.icon('fa5s.outdent'))
        self.ui.delete_category.setIcon(qtawesome.icon('fa.trash-o'))
        self.ui.collapse_all.setIcon(qtawesome.icon('mdi.collapse-all'))
        self.ui.expand_all.setIcon(qtawesome.icon('mdi.expand-all'))

        # Setup custom context menu for category tree.
        self.context_menu = QtWidgets.QMenu(self)
        self.context_delete = context_action(
            self.context_menu, 'Delete', self._delete, 'fa.trash-o', 'Del', self.ui.categories)
        self.context_sibling = context_action(
            self.context_menu, 'Insert Sibling', self._insert_sibling, 'fa.list', 'Ins', self.ui.categories)
        self.context_child = context_action(
            self.context_menu, 'Insert Child', self._insert_child, 'mdi.file-tree', 'Ctrl+Ins', self.ui.categories)
        self.context_menu.addSeparator()
        self.context_indent = context_action(
            self.context_menu, 'Make Child', self._make_child, 'fa5s.indent', 'Ctrl+]', self.ui.categories)
        self.context_outdent = context_action(
            self.context_menu, 'Make Sibling', self._make_sibling, 'fa5s.outdent', 'Ctrl+[', self.ui.categories)
        self.context_menu.addSeparator()
        self.context_collapse = context_action(
            self.context_menu, 'Collapse All', self.ui.categories.collapseAll, 'mdi.collapse-all')
        self.context_collapse = context_action(
            self.context_menu, 'Expand All', self.ui.categories.expandAll, 'mdi.expand-all')
        self.ui.categories.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.categories.customContextMenuRequested.connect(self._context_menu)

        # Connect events.
        self.ui.insert_child.clicked.connect(self._insert_child)
        self.ui.insert_sibling.clicked.connect(self._insert_sibling)
        self.ui.make_child.clicked.connect(self._make_child)
        self.ui.make_sibling.clicked.connect(self._make_sibling)
        self.ui.delete_category.clicked.connect(self._delete)
        self.ui.collapse_all.clicked.connect(self.ui.categories.collapseAll)
        self.ui.expand_all.clicked.connect(self.ui.categories.expandAll)
        self.ui.categories.doubleClicked.connect(self.edit)
        self.ui.categories.itemSelectionChanged.connect(self._selected)
        self._selected()


# ----------------------------------------------------------------------------------------------------------------------
    def refresh(self) -> None:
        """Called by the main window to (re) load categories when the tab is activated."""
        # Remove any existing items from the tree.
        while self.ui.categories.topLevelItemCount():
            self.ui.categories.takeTopLevelItem(0)

        # Clear out displayed parts.
        self.ui.parts.setParts(None)

        # Load categories into TreeWidget.
        roots = Category.select().where(Category.parent == None)
        for root in roots:
            self.ui.categories.addTopLevelItem(self._load_tree(root, None))

        # Sort the categories that were just loaded.
        self._sort()


# ----------------------------------------------------------------------------------------------------------------------
    def _load_tree(self, category: Category, parent: QtWidgets.QTreeWidgetItem) -> QtWidgets.QTreeWidgetItem:
        item = self._make_item(parent, category)
        for child in category.children:
            item.addChild(self._load_tree(child, item))
        return item


# ----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _make_item(parent: QtWidgets.QTreeWidgetItem, category: Category) -> QtWidgets.QTreeWidgetItem:
        item = QtWidgets.QTreeWidgetItem(parent, [
            category.title,
            category.inherited_designator,
            str(len(category.parts)) if category.parts else ''
        ])
        item.setData(0, QtCore.Qt.UserRole, category)
        return item


# ----------------------------------------------------------------------------------------------------------------------
    def _context_menu(self, point: QtCore.QPoint) -> None:
        self.context_menu.exec(self.ui.categories.mapToGlobal(point))


# ----------------------------------------------------------------------------------------------------------------------
    def _sort(self) -> None:
        """Sort the list of categories in the tree widget alphabetically by title."""
        self.ui.categories.sortItems(0, QtCore.Qt.AscendingOrder)


# ----------------------------------------------------------------------------------------------------------------------
    def _selected(self) -> None:
        selected = self.ui.categories.selectedItems()
        parts = []
        for item in selected:
            category: Category = item.data(0, QtCore.Qt.UserRole)
            parts.extend(category.parts)
        self.ui.parts.setParts(parts)

        self.ui.delete_category.setEnabled(bool(selected))
        self.ui.insert_child.setEnabled(bool(selected))
        self.ui.make_child.setEnabled(len(selected) >= 2)
        self.ui.make_sibling.setEnabled(any([bool(item.parent()) for item in selected]))

        self.context_delete.setEnabled(bool(selected))
        self.context_child.setEnabled(bool(selected))
        self.context_indent.setEnabled(len(selected) >= 2)
        self.context_outdent.setEnabled(any([bool(item.parent()) for item in selected]))


# ----------------------------------------------------------------------------------------------------------------------
    def edit(self) -> None:
        """Edit the selected category.

        Present the user with the CategoryDialog for editing the values for an existing category.
        """
        # Get the currently selected category from the tree - make sure there's only 1, otherwise ignore the request.
        selected = self.ui.categories.selectedItems()
        if len(selected) != 1:
            return
        selected = selected[0]

        category: Category = selected.data(0, QtCore.Qt.UserRole)

        # Show a dialog to let the user make changes.  Dialog will save to database if user accepts.
        if CategoryDialog(self, category).exec():

            # User accepted the changes - update the tree with the changed values.
            selected.setText(0, category.title)
            selected.setText(1, category.inherited_designator)

            selected.takeChildren()
            for child in category.children:
                self._load_tree(child, selected)

            self.ui.categories.expandAll()
            self._sort()


# ----------------------------------------------------------------------------------------------------------------------
    def _delete(self) -> None:
        """Remove the currently selected items."""
        selection = self.ui.categories.selectedItems()
        message = 'Are you sure you want to delete '
        if not selection:
            return
        category: Category = selection[0].data(0, QtCore.Qt.UserRole)
        if list(category.all_parts()):
            return Alert(self, 'Error', 'Cannot delete categories with parts.  Please move parts first.')
        if len(selection) == 1:
            message += category.title
        else:
            message += f'{len(selection)} items'
        if category.children:
            message += '?\n\nWarning: All children will be deleted recursively too.'
        if YesNoPrompt(self, 'Please confirm', message):
            def recurse(category: Category) -> None:
                for child in category.children:
                    recurse(child)
                category.delete_instance()

            for item in selection:
                # Remove the selected item from the database.
                recurse(item.data(0, QtCore.Qt.UserRole))

                # Remove the selected item from the tree.
                if item.parent():
                    item.parent().removeChild(item)
                else:
                    self.ui.categories.takeTopLevelItem(self.ui.categories.indexOfTopLevelItem(item))


# ----------------------------------------------------------------------------------------------------------------------
    def _insert_sibling(self) -> None:
        selected = self.ui.categories.selectedItems()
        if selected:
            selected = selected[-1]
            selected_category = selected.data(0, QtCore.Qt.UserRole)

            # To be a sibling, we want parent to be the same parent as selected.
            parent = selected_category.parent
        else:
            parent = None

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
    def _insert_child(self) -> None:
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
    def _make_child(self) -> None:
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
    def _make_sibling(self) -> None:
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
