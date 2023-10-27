# ======================================================================================================================
#      File:  /inventory/gui/dialog/part_view.py
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
"""Dialog showing information about a single part."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtWidgets

from inventory.gui.base.dialog_part import Ui_DialogPart
from inventory.gui.dialogs.category import CategoryDialog
from inventory.model.parts import Part
from inventory.model.categories import Category




# ======================================================================================================================
# Part Dialog
# ----------------------------------------------------------------------------------------------------------------------
class PartDialog(QtWidgets.QDialog):
    def __init__(self, parent, part: Part):
        super().__init__(parent)
        self.ui = Ui_DialogPart()
        self.ui.setupUi(self)

        # Populate the categories dropdown with a sorted set of categories from the database.
        categories = list(Category.select())
        categories.sort(key=lambda category: category.full_title())
        for category in categories:
            self.ui.category.addItem(category.full_title(), category)

        # Connect events.
        self.ui.category.currentIndexChanged.connect(self._category_changed)
        self.ui.new_category.clicked.connect(self._add_category)

        # Load part information into dialog.
        self.load(part)

        self._category_changed()



# ----------------------------------------------------------------------------------------------------------------------
    def load(self, part: Part):
        self.part = part

        self.setWindowTitle(f'Edit {part.summary}' if part.value else 'Add new part')

        self.ui.attributes.setAttributes(part.attributes)

        if part.category_id:
            self.ui.category.setCurrentText(part.category.full_title())
        self.ui.value.setText(part.value)
        self.ui.part_number.setText(part.number)
        if self.part.package is not None:
            self.ui.footprint.setText(part.package)
        if part.price:
            self.ui.price.setValue(float(part.price))
        if part.weight:
            self.ui.weight.setValue(float(part.weight) if part.weight else 0)
        if part.threshold:
            self.ui.threshold.setValue(int(part.threshold) if part.threshold else 0)
        self.ui.notes.setPlainText(part.notes)

        self.ui.locations.setPart(part)
        self.ui.materials.setPart(part)
        self.ui.suppliers.setPart(part)


# ----------------------------------------------------------------------------------------------------------------------
    def accept(self) -> None:
        """When the user accepts the changes, update the provided part."""
        self.part.category_id = self.ui.category.currentData()
        self.part.value = self.ui.value.text()
        self.part.number = self.ui.part_number.text()
        self.part.package = self.ui.footprint.text()
        if not self.part.package:
            self.part.package = None
        self.part.price = self.ui.price.value()
        self.part.weight = self.ui.weight.value()
        self.part.threshold = self.ui.threshold.value()
        self.part.notes = self.ui.notes.toPlainText()
        self.part.attributes = self.ui.attributes.attributes()
        self.part.save()
        return super().accept()


# ----------------------------------------------------------------------------------------------------------------------
    def reject(self) -> None:
        # TODO: Hook close event and warn if there are changes before closing.
        return super().reject()


# ----------------------------------------------------------------------------------------------------------------------
    def _category_changed(self) -> None:
        """Fires when the category selection was changed by the user."""
        # Get a list of attributes that are attributes to other parts in this category to offer as suggestions.
        category: Category = self.ui.category.currentData(QtCore.Qt.UserRole)
        self.ui.category.setToolTip(category.full_title())
        attributes = sorted(set([attribute for part in category.parts for attribute in part.attributes]))
        self.ui.attributes.setSuggestions(attributes)


# ----------------------------------------------------------------------------------------------------------------------
    def _add_category(self) -> None:
        """Prompt the user to add a new category to the database and then select it in the dropdown."""
        parent = self.ui.category.currentData(QtCore.Qt.UserRole)
        category = Category(parent=parent, title='')
        dialog = CategoryDialog(self, category)
        if dialog.exec():
            category.save()
            title = category.full_title()
            self.ui.category.addItem(title, category)
            self.ui.category.model().sort(0, QtCore.Qt.AscendingOrder)
            self.ui.category.setCurrentText(title)





# End of File
