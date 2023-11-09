# ======================================================================================================================
#      File:  /inventory/gui/dialogs/dialog_document.py
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
"""Dialog for adding and editing Documents."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import os

from PySide6 import QtWidgets
import requests

from inventory.gui.base.dialog_document import Ui_DocumentDialog
from inventory.model.documents import Document
from inventory.model.parts import Part




# ======================================================================================================================
# Document Dialog
# ----------------------------------------------------------------------------------------------------------------------
class DocumentDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_DocumentDialog()
        self.ui.setupUi(self)

        self.ui.file.setLabel('Document')
        self.ui.file.setFilters({'Common Documents': '*.pdf *.md *.txt', 'All Files': '*.*'})
        self.ui.file.setPlaceholderText('Select a file...')

        # Connect Events
        self.ui.file.changed.connect(self._file_changed)
        self.ui.url.textChanged.connect(self._url_changed)
        self.ui.select_file.clicked.connect(self._source_changed)
        self.ui.select_url.clicked.connect(self._source_changed)


# ----------------------------------------------------------------------------------------------------------------------
    def _file_changed(self) -> None:
        self.ui.buttons.button(self.ui.buttons.StandardButton.Ok).setEnabled(self.ui.file.isValid())
        if self.ui.file.isValid() and not self.ui.filename.text():
            filename = self.ui.file.filename()
            self.ui.filename.setText(os.path.basename(filename))
            self._set_default_label(filename)


# ----------------------------------------------------------------------------------------------------------------------
    def _url_changed(self) -> None:
        """The user has selected a URL."""
        if not self.ui.filename.text():
            try:
                filename = self.ui.url.text().rsplit('/', 1)[1]
                self.ui.filename.setText(filename)
                self._set_default_label(filename)
            except IndexError:
                pass


# ----------------------------------------------------------------------------------------------------------------------
    def _set_default_label(self, filename: str) -> None:
        """Attempt to set a default label for the document based upon the filename."""
        # Don't both if there is already a label for this document.
        if self.ui.label.currentText():
            return
        extension = os.path.splitext(filename)[1]
        if extension == '.pdf':
            self.ui.label.setCurrentText('Datasheet')


# ----------------------------------------------------------------------------------------------------------------------
    def _source_changed(self) -> None:
        if self.ui.select_file.isChecked():
            self.ui.file.setEnabled(True)
            self.ui.url.setEnabled(False)
        else:
            self.ui.file.setEnabled(False)
            self.ui.url.setEnabled(True)


# ----------------------------------------------------------------------------------------------------------------------
    def document(self, part: Part) -> Document:
        return Document(
            label=self.ui.label.currentText(),
            filename=self.ui.filename.text(),
            content=self.content(),
            part=part
        )


# ----------------------------------------------------------------------------------------------------------------------
    def content(self) -> None:
        if self.ui.select_file.isChecked():
            with open(self.ui.file.filename(), 'rb') as handle:
                return handle.read()
        else:
            url = self.ui.url.text()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
            }
            response = requests.get(url, allow_redirects=True, headers=headers, timeout=5)
            return response.content


# ----------------------------------------------------------------------------------------------------------------------
    def accept(self) -> None:
        try:
            if self.content() and self.ui.filename.text() and self.ui.label.currentText():
                super().accept()
        except (FileNotFoundError, requests.exceptions.MissingSchema):
            pass




# End of File
