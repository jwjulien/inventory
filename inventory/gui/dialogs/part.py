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
from typing import List

import io
from partsscale.scale import Scale, DeviceError
from PySide6 import QtCore, QtGui, QtWidgets
from PIL import Image
from PIL.ImageQt import ImageQt
import requests

from inventory.gui.base.dialog_part import Ui_DialogPart
from inventory.gui.dialogs.category import CategoryDialog
from inventory.gui.dialogs.part_weight import PartWeightDialog
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

        # Don't allow setting tabbed attributes until this part has an ID.
        self.ui.tabs.setEnabled(bool(part.id))

        # Disable weighing parts when no scale is present.
        try:
            Scale()
        except DeviceError:
            self.ui.calibrate.setEnabled(False)
            self.ui.calibrate.setToolTip('Scale not found')

        # Connect events.
        self.ui.category.currentIndexChanged.connect(self._category_changed)
        self.ui.new_category.clicked.connect(self._add_category)
        self.ui.calibrate.clicked.connect(self._weigh_parts)
        self.ui.image.urlDropped.connect(self._dropped_image)
        self.ui.set_image.clicked.connect(self._select_image)
        self.ui.remove_image.clicked.connect(self._remove_image)
        self.ui.buttons.button(QtWidgets.QDialogButtonBox.StandardButton.Apply).clicked.connect(self._save)
        self.ui.buttons.button(QtWidgets.QDialogButtonBox.StandardButton.Discard).clicked.connect(self.reject)

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

        if part.image:
            byte_array = QtCore.QByteArray(part.image)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(byte_array, "PNG")
            self.ui.image.setPixmap(pixmap)
            self.ui.remove_image.setEnabled(True)

        self.ui.locations.setPart(part)
        self.ui.materials.setPart(part)
        self.ui.suppliers.setPart(part)
        self.ui.documents.setPart(part)

        projects = set([material.revision.project.title for material in part.materials])
        self.ui.tabs.setTabText(0, f'Locations ({len(part.locations)})')
        self.ui.tabs.setTabText(1, f'Projects ({len(projects)})')
        self.ui.tabs.setTabText(2, f'Suppliers ({len(part.products)})')


# ----------------------------------------------------------------------------------------------------------------------
    def _save(self) -> None:
        """Save this part."""
        # TODO: Only allow save if part is valid - i.e. has a value and part number.
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

        pixmap = self.ui.image.pixmap()
        if pixmap:
            byte_array = QtCore.QByteArray()
            buffer = QtCore.QBuffer(byte_array)
            buffer.open(QtCore.QIODevice.WriteOnly)
            pixmap.save(buffer, "PNG")
            self.part.image = byte_array.data()
        else:
            self.part.image = None

        self.part.save()
        self.ui.tabs.setEnabled(True)


# ----------------------------------------------------------------------------------------------------------------------
    def accept(self) -> None:
        """When the user accepts the changes, update the provided part."""
        self._save()
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


# ----------------------------------------------------------------------------------------------------------------------
    def _weigh_parts(self) -> None:
        """Open a dialog to handle weighing parts and determine the per-part weight."""
        dialog = PartWeightDialog(self)
        if dialog.exec():
            self.ui.weight.setValue(dialog.weight())


# ----------------------------------------------------------------------------------------------------------------------
    def _dropped_image(self, url: QtCore.QUrl) -> None:
        if url.isLocalFile():
            image = Image.open(url.toLocalFile())
        else:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Linux i641 x86_64) Gecko/20130401 Firefox/67.1'
            }
            response = requests.get(url.url(), headers=headers, timeout=5)
            response.raise_for_status()
            data = io.BytesIO(response.content)
            image = Image.open(data)
        image.thumbnail((250, 250))
        qt_image = ImageQt(image)
        pixmap = QtGui.QPixmap(qt_image)
        self.ui.image.setPixmap(pixmap)
        self.ui.remove_image.setEnabled(True)


# ----------------------------------------------------------------------------------------------------------------------
    def _select_image(self) -> None:
        """Browse and set an image for this Part."""
        filter = 'Image FIles (*.png *.jpg *.jpeg *.bmp *.gif *.webp);;All Files (*.*)'
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select image...', filter=filter)
        if filename:
            image = ImageQt(filename)
            pixmap = QtGui.QPixmap.fromImage(image)
            self.ui.image.setPixmap(pixmap)
            self.ui.remove_image.setEnabled(True)


# ----------------------------------------------------------------------------------------------------------------------
    def _remove_image(self) -> None:
        """Remove the currently set image for this part."""
        self.ui.image.clear()
        self.ui.remove_image.setEnabled(False)




# End of File
