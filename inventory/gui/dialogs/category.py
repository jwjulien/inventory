# ======================================================================================================================
#      File:  /inventory/gui/dialogs/category.py
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
"""Dialog for editing category information."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtWidgets

from inventory.gui.base.dialog_category import Ui_DialogCategory
from inventory.model.categories import Category




# ======================================================================================================================
# Category Dialog Class
# ----------------------------------------------------------------------------------------------------------------------
class CategoryDialog(QtWidgets.QDialog):
    def __init__(self, parent, category: Category):
        super().__init__(parent)
        self.ui = Ui_DialogCategory()
        self.ui.setupUi(self)

        self.category = category

        self.ui.title.setText(self.category.title)
        self.ui.designator.setText(self.category.designator)
        self.ui.designator.setPlaceholderText(self.category.inherited_designator)


    def accept(self) -> None:
        self.category.title = self.ui.title.text()
        self.category.designator = self.ui.designator.text()

        # Convert empty string for designator into null value.
        if not self.category.designator:
            self.category.designator = None

        self.category.save()
        super().accept()




# End of File
