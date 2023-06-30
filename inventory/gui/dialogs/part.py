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

from sqlalchemy.orm import Session

from inventory.gui.base.dialog_part import Ui_DialogPart
from inventory.model import Part, PartCategory




# ======================================================================================================================
# Part Dialog
# ----------------------------------------------------------------------------------------------------------------------
class PartDialog(QtWidgets.QDialog):
    def __init__(self, parent, engine, part: Part):
        super().__init__(parent)
        self.ui = Ui_DialogPart()
        self.ui.setupUi(self)

        self.ui.category.clear()
        with Session(engine) as session:
            for category in PartCategory.GetAll(session):
                self.ui.category.addItem(category.full_title, category.id)

        self.ui.category.setCurrentText(part.category.full_title)
        self.ui.value.setText(part.value)
        self.ui.part_number.setText(part.number)
        self.ui.footprint.setText(part.package)
        self.ui.price.setValue(float(part.price))
        self.ui.weight.setValue(float(part.weight) if part.weight else 0)
        self.ui.threshold.setValue(int(part.threshold) if part.threshold else 0)


# TODO: Hook close event and warn if there are changes before closing.




# End of File
