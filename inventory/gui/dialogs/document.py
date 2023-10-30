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

from inventory.gui.base.dialog_document import Ui_DocumentDialog
from inventory.model.documents import Document




# ======================================================================================================================
# Document Dialog
# ----------------------------------------------------------------------------------------------------------------------
class DocumentDialog(QtWidgets.QDialog):
    def __init__(self, parent, document: Document):
        super().__init__(parent)
        self.ui = Ui_DocumentDialog()
        self.ui.setupUi(self)

        self.document = document

        self.ui.file.setLabel('Document')
        self.ui.file.setFilters({'Documents': '*.pdf *.md'})
        if document.id:
            self.ui.file.setPlaceholderText('Selecting a new file will replace the existing file')
        else:
            self.ui.file.setPlaceholderText('Select a file...')
        self.ui.title.setText(document.title)
        self.ui.mime.setCurrentText(document.mime)

        self.ui.file.changed.connect(self._file_changed)


# ----------------------------------------------------------------------------------------------------------------------
    def _file_changed(self) -> None:
        self.ui.buttons.button(self.ui.buttons.StandardButton.Ok).setEnabled(self.ui.file.isValid())
        if self.ui.file.isValid():
            filename, extension = os.path.splitext(self.ui.file.filename())
            if not self.ui.title.text():
                self.ui.title.setText(os.path.basename(filename))
            if extension == '.pdf':
                self.ui.mime.setCurrentText('application/pdf')
            elif extension == '.md':
                self.ui.mime.setCurrentText('application/markdown')


# ----------------------------------------------------------------------------------------------------------------------
    def accept(self) -> None:
        self.document.title = self.ui.title.text()
        self.document.mime = self.ui.mime.currentText()
        if self.ui.file.isValid():
            with open(self.ui.file.filename(), 'rb') as handle:
                self.document.content = handle.read()

        if self.document.title and self.document.mime and self.document.content:
            self.document.save()
            return super().accept()




# End of File
