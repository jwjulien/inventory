# ======================================================================================================================
#      File:  /inventory/gui/widgets/document_list.py
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
"""A widget for listing documents for a Part."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from tempfile import NamedTemporaryFile
import os

from PySide6 import QtCore, QtWidgets
import qtawesome

from inventory.gui.base.widget_document_list import Ui_DocumentListWidget
from inventory.gui.dialogs.document import DocumentDialog
from inventory.gui.utilities import context_action
from inventory.model.parts import Part
from inventory.model.documents import Document




# ======================================================================================================================
# Document List Widget
# ----------------------------------------------------------------------------------------------------------------------
class DocumentListWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_DocumentListWidget()
        self.ui.setupUi(self)

        self.part: Part = None

        self.ui.add.setIcon(qtawesome.icon('fa5s.file-upload'))

        # Setup custom context menu
        self.context_menu = QtWidgets.QMenu(self)
        self.context_open = context_action(self.context_menu, 'Open Document', self._open, 'fa.external-link')
        self.context_add = context_action(self.context_menu, 'Add document', self._add, 'fa5s.file-upload')
        self.context_remove = context_action(self.context_menu, 'Remove document', self._remove, 'mdi.file-remove')
        self.context_edit = context_action(self.context_menu, 'Edit label', self._edit, 'ri.file-edit-line')
        self.ui.documents.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.documents.customContextMenuRequested.connect(self._context_menu)

        # Connect events
        self.ui.documents.itemChanged.connect(self._item_changed)
        self.ui.documents.doubleClicked.connect(self._open)
        self.ui.add.clicked.connect(self._add)


# ----------------------------------------------------------------------------------------------------------------------
    def setPart(self, part: Part) -> None:
        self.part = part

        self.ui.documents.clear()
        for document in self.part.documents:
            self._list_item(document)


# ----------------------------------------------------------------------------------------------------------------------
    def _list_item(self, document: Document) -> QtWidgets.QListWidgetItem:
        item = QtWidgets.QListWidgetItem(f'{document.label} ({document.filename})')
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        item.setData(QtCore.Qt.UserRole, document)
        self.ui.documents.addItem(item)
        return item


# ----------------------------------------------------------------------------------------------------------------------
    def _context_menu(self, point: QtCore.QPoint) -> None:
        try:
            self._selected_document()
        except AssertionError:
            selected = False
        else:
            selected = True
        self.context_open.setEnabled(selected)
        self.context_remove.setEnabled(selected)
        self.context_edit.setEnabled(selected)
        self.context_menu.exec(self.ui.documents.mapToGlobal(point))


# ----------------------------------------------------------------------------------------------------------------------
    def _item_changed(self, item) -> None:
        """When the user edits a label for a document, update the label in the database."""
        document: Document = item.data(QtCore.Qt.UserRole)
        document.label = item.text()
        document.save()


# ----------------------------------------------------------------------------------------------------------------------
    def _add(self) -> None:
        """Select a new document to add to the list."""
        dialog = DocumentDialog(self)
        if dialog.exec():
            document = dialog.document(self.part)
            document.save()
            self._list_item(document)


# ----------------------------------------------------------------------------------------------------------------------
    def _edit(self) -> None:
        """Trigger an edit for the label of the currently selected item."""
        self.ui.documents.editItem(self._selected_item())


# ----------------------------------------------------------------------------------------------------------------------
    def _selected_item(self) -> QtWidgets.QListWidgetItem:
        """Return the currently selected QListWidget item."""
        selection = self.ui.documents.selectedItems()
        assert len(selection) == 1
        return selection[0]


# ----------------------------------------------------------------------------------------------------------------------
    def _selected_row(self) -> int:
        """Return the currently selected row index."""
        return self.ui.documents.row(self._selected_item())


# ----------------------------------------------------------------------------------------------------------------------
    def _selected_document(self) -> Document:
        """Return the currently selected Document."""
        row = self._selected_row()
        document: Document = self.ui.documents.item(row).data(QtCore.Qt.UserRole)
        return document


# ----------------------------------------------------------------------------------------------------------------------
    def _remove(self) -> None:
        """Remove the currently selected Document from this Part."""
        document = self._selected_document()
        document.delete_instance()
        self.ui.documents.takeItem(self._selected_row())


# ----------------------------------------------------------------------------------------------------------------------
    def _open(self) -> None:
        """Ask the OS to open this document for us to view."""
        document = self._selected_document()
        with NamedTemporaryFile(suffix=f'_Doc{document.id}_{document.filename}', delete=False) as temp_file:
            temp_file.write(document.content)
        os.system(temp_file.name)




# End of File
