# ======================================================================================================================
#      File:  /inventory/gui/dialogs/document_browser.py
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
"""Document browser dialog to allow associating Documents with Parts."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtCore, QtWidgets

from inventory.gui.base.dialog_document_browser import Ui_DocumentBrowserDialog
from inventory.gui.dialogs.document import DocumentDialog
from inventory.model.documents import Document
from inventory.gui.prompts import Confirmation




# ======================================================================================================================
# Document Browser Dialog
# ----------------------------------------------------------------------------------------------------------------------
class DocumentBrowserDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_DocumentBrowserDialog()
        self.ui.setupUi(self)

        self.ui.documents.clear()
        for document in Document.select():
            item = QtWidgets.QListWidgetItem(document.title)
            item.setData(QtCore.Qt.UserRole, document)
            self.ui.documents.addItem(item)

        self.ui.filter.textChanged.connect(self._filter_changed)
        self.ui.documents.itemSelectionChanged.connect(self._selection_changed)
        self.ui.documents.doubleClicked.connect(self.accept)
        self.ui.add.clicked.connect(self._add)
        self.ui.remove.clicked.connect(self._remove)


# ----------------------------------------------------------------------------------------------------------------------
    def document(self) -> Document:
        return self.ui.documents.currentItem().data(QtCore.Qt.UserRole)


# ----------------------------------------------------------------------------------------------------------------------
    def _filter_changed(self) -> None:
        filter_text = [f'*{word}*' for word in self.ui.filter.text().split(' ')]
        filter_res = [QtCore.QRegularExpression().fromWildcard(text, QtCore.Qt.CaseInsensitive) for text in filter_text]
        for row in range(self.ui.documents.count()):
            text = self.ui.documents.item(row).text()
            show = all([filter_re.match(text).hasMatch() for filter_re in filter_res])
            self.ui.documents.setRowHidden(row, not show)


# ----------------------------------------------------------------------------------------------------------------------
    def _selection_changed(self) -> None:
        selected = self.ui.documents.selectedItems()
        self.ui.buttons.button(self.ui.buttons.StandardButton.Ok).setEnabled(len(selected) == 1)
        self.ui.remove.setEnabled(len(selected) == 1)


# ----------------------------------------------------------------------------------------------------------------------
    def _add(self) -> None:
        document = Document()
        dialog = DocumentDialog(self, document)
        if dialog.exec():
            item = QtWidgets.QListWidgetItem(document.title)
            item.setData(QtCore.Qt.UserRole, document)
            self.ui.documents.addItem(item)
            self.ui.documents.setCurrentItem(item)


# ----------------------------------------------------------------------------------------------------------------------
    def _remove(self) -> None:
        document: Document = self.ui.documents.currentItem().data(QtCore.Qt.UserRole)
        if document.references:
            Confirmation(self, 'Cannot delete document', 'Document has references to parts - please remove them first')
        else:
            document.delete_instance()
            self.ui.documents.takeItem(self.ui.documents.currentRow())





# End of File
