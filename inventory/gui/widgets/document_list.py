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
"""A widget for listing document references for a Part."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from tempfile import NamedTemporaryFile
import os

from PySide6 import QtCore, QtGui, QtWidgets

from inventory.gui.base.widget_document_list import Ui_DocumentListWidget
from inventory.gui.dialogs.document_browser import DocumentBrowserDialog
from inventory.gui.dialogs.document import DocumentDialog
from inventory.model.parts import Part
from inventory.model.documents import Reference




# ======================================================================================================================
# Document List Widget
# ----------------------------------------------------------------------------------------------------------------------
class DocumentListWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_DocumentListWidget()
        self.ui.setupUi(self)

        self.part: Part = None

        self.pop_menu = QtWidgets.QMenu(self)
        self.pop_open = QtGui.QAction('Open document', self)
        self.pop_open.triggered.connect(self._open)
        self.pop_menu.addAction(self.pop_open)
        self.pop_add = QtGui.QAction('Add document', self)
        self.pop_add.triggered.connect(self._add)
        self.pop_menu.addAction(self.pop_add)
        self.pop_remove = QtGui.QAction('Remove document', self)
        self.pop_remove.triggered.connect(self._remove)
        self.pop_menu.addAction(self.pop_remove)
        self.pop_label = QtGui.QAction('Edit label', self)
        self.pop_label.triggered.connect(self._edit)
        self.pop_menu.addAction(self.pop_label)
        self.pop_edit = QtGui.QAction('Edit document', self)
        self.pop_edit.triggered.connect(self._edit_document)
        self.pop_menu.addAction(self.pop_edit)

        self.ui.references.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.references.customContextMenuRequested.connect(self._context_menu)
        self.ui.references.itemChanged.connect(self._item_changed)
        self.ui.references.doubleClicked.connect(self._open)


# ----------------------------------------------------------------------------------------------------------------------
    def setPart(self, part: Part) -> None:
        self.part = part

        self.ui.references.clear()
        for reference in self.part.references:
            self._list_item(reference)


# ----------------------------------------------------------------------------------------------------------------------
    def _list_item(self, reference: Reference) -> QtWidgets.QListWidgetItem:
        item = QtWidgets.QListWidgetItem(reference.label)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        item.setData(QtCore.Qt.UserRole, reference)
        item.setToolTip(reference.document.title + reference.document.extension)
        self.ui.references.addItem(item)
        return item


# ----------------------------------------------------------------------------------------------------------------------
    def _context_menu(self, point: QtCore.QPoint) -> None:
        try:
            self._selected_reference()
        except AssertionError:
            selected = False
        else:
            selected = True
        self.pop_open.setEnabled(selected)
        self.pop_remove.setEnabled(selected)
        self.pop_label.setEnabled(selected)
        self.pop_edit.setEnabled(selected)
        self.pop_menu.exec(self.ui.references.mapToGlobal(point))


# ----------------------------------------------------------------------------------------------------------------------
    def _item_changed(self, item) -> None:
        """When the user edits a title for a document, update the label in the database."""
        reference: Reference = item.data(QtCore.Qt.UserRole)
        reference.label = item.text()
        reference.save()


# ----------------------------------------------------------------------------------------------------------------------
    def _add(self) -> None:
        """Select a new document to add to the list."""
        dialog = DocumentBrowserDialog(self)
        if dialog.exec():
            document = dialog.document()
            reference = Reference(label=document.title)
            reference.document = document
            reference.part = self.part
            reference.save()

            item = self._list_item(reference)
            self.ui.references.editItem(item)


# ----------------------------------------------------------------------------------------------------------------------
    def _edit(self) -> None:
        """Trigger an edit for the label of the currently selected item."""
        self.ui.references.editItem(self._selected_item())


# ----------------------------------------------------------------------------------------------------------------------
    def _selected_item(self) -> QtWidgets.QListWidgetItem:
        """Return the currently selected QListWidget item."""
        selection = self.ui.references.selectedItems()
        assert len(selection) == 1
        return selection[0]


# ----------------------------------------------------------------------------------------------------------------------
    def _selected_row(self) -> int:
        """Return the currently selected row index."""
        return self.ui.references.row(self._selected_item())


# ----------------------------------------------------------------------------------------------------------------------
    def _selected_reference(self) -> Reference:
        """Return the currently selected Reference."""
        row = self._selected_row()
        reference: Reference = self.ui.references.item(row).data(QtCore.Qt.UserRole)
        return reference


# ----------------------------------------------------------------------------------------------------------------------
    def _remove(self) -> None:
        """Remove the currently selected Reference from this Part."""
        reference = self._selected_reference()
        reference.delete_instance()
        self.ui.references.takeItem(self._selected_row())


# ----------------------------------------------------------------------------------------------------------------------
    def _edit_document(self) -> None:
        """Edit the document - possibly replacing the contents with a new upload."""
        reference = self._selected_reference()
        dialog = DocumentDialog(self, reference.document)
        dialog.exec()


# ----------------------------------------------------------------------------------------------------------------------
    def _open(self) -> None:
        """Ask the OS to open this document for us to view."""
        reference = self._selected_reference()
        with NamedTemporaryFile(prefix=reference.document.title + '_',
                                suffix=reference.document.extension,
                                delete=False) as handle:
            handle.write(reference.document.content)

        os.system(handle.name)




# End of File
