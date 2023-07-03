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
from PySide6 import QtCore, QtGui, QtWidgets

from inventory.gui.base.dialog_part import Ui_DialogPart
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

        self.part = part

        # Populate the categories dropdown with a sorted set of categories from the database.
        categories = list(Category.select())
        categories.sort(key=lambda category: category.full_title)
        for category in categories:
            self.ui.category.addItem(category.full_title, category)

        if part.category_id:
            self.ui.category.setCurrentText(part.category.full_title)
        self.ui.value.setText(part.value)
        self.ui.part_number.setText(part.number)
        self.ui.footprint.setText(part.package)
        if part.price:
            self.ui.price.setValue(float(part.price))
        if part.weight:
            self.ui.weight.setValue(float(part.weight) if part.weight else 0)
        if part.threshold:
            self.ui.threshold.setValue(int(part.threshold) if part.threshold else 0)
        self.ui.notes.setPlainText(part.notes)


    def accept(self) -> None:
        """When the user accepts the changes, update the provided part."""
        self.part.category_id = self.ui.category.currentData()
        self.part.value = self.ui.value.text()
        self.part.number = self.ui.part_number.text()
        self.part.package = self.ui.footprint.text()
        self.part.price = self.ui.price.value()
        self.part.weight = self.ui.weight.value()
        self.part.threshold = self.ui.threshold.value()
        self.part.notes = self.ui.notes.toPlainText()
        self.part.save()
        return super().accept()


    def reject(self) -> None:
        # TODO: Hook close event and warn if there are changes before closing.
        return super().reject()




# End of File
