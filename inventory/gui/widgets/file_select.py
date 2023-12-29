# ======================================================================================================================
#      File:  /inventory/gui/widgets/file_select.py
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
"""A generic, reusable widget for selecting files on the local filesystem."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import fnmatch
import os
from typing import Dict

from PySide6 import QtCore, QtWidgets

from inventory.gui.base.widget_file_select import Ui_FileSelectWidget




# ======================================================================================================================
# File Select Widget Class
# ----------------------------------------------------------------------------------------------------------------------
class FileSelectWidget(QtWidgets.QWidget):
    changed = QtCore.Signal()     # Every time the user makes a change to the filename - valid or not.
    selected = QtCore.Signal(str) # Only when the user makes a change to the filename that is "valid".

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_FileSelectWidget()
        self.ui.setupUi(self)

        self.ui.error.setStyleSheet('QLabel { color: "#dc3545"; }')
        self.ui.error.hide()

        self._filters: Dict[str, str] = {
            'All Files': '*.*'
        }

        self.setAcceptDrops(True)

        # Connect events.
        self.ui.browse.clicked.connect(self._browse)
        self.ui.editor.textChanged.connect(self._changed)


# ----------------------------------------------------------------------------------------------------------------------
    def setLabel(self, text: str) -> None:
        self.ui.label.setText(text)


# ----------------------------------------------------------------------------------------------------------------------
    def setPlaceholderText(self, text: str) -> None:
        self.ui.editor.setPlaceholderText(text)


# ----------------------------------------------------------------------------------------------------------------------
    def filename(self) -> str:
        """Return the filename of the file currently selected.

        Raises:
            ValueError if the current selection is invalid.
        """
        return self.ui.editor.text()


# ----------------------------------------------------------------------------------------------------------------------
    def setFilename(self, filename: str) -> None:
        """Set the current filename selection to that which is provided.

        Arguments:
            The filename of the file being selected.
        """
        self.ui.editor.setText(os.path.abspath(filename))


# ----------------------------------------------------------------------------------------------------------------------
    def filters(self) -> str:
        """Get the previously configured filter value."""
        return self._filters


# ----------------------------------------------------------------------------------------------------------------------
    def setFilters(self, filters: Dict[str, str]) -> None:
        """Explicitly set the filters for the the QFileDialog.

        Arguments:
            filters: A dict where the keys are the human readable names of each filter and the values are the
                corresponding glob patterns for the associated filename(s).
        """
        self._filters = filters


# ----------------------------------------------------------------------------------------------------------------------
    def addFilter(self, name: str, pattern: str) -> None:
        """Append a new filter to the existing set of filters.

        The default filters is for "All Files (*.*)".  If you wish to exclude that option, use the `setFilters` method
        to explicitly set the filters instead.

        Note: Setting a filter with the same name as an existing filter will override the pattern value for the existing
        filter.

        Arguments:
            name: A human readable name that describes the file type.
            pattern: The glob pattern that matches the file(s), for example "*.md" to match markdown files.  Pattern
                can also include multiple, comma separated values, such as "*.md, *.markdown".
        """
        self._filters[name] = pattern


# ----------------------------------------------------------------------------------------------------------------------
    def isValid(self) -> bool:
        """Returns true if the current value is valid according to any supplied rules."""
        return self.error() is None


# ----------------------------------------------------------------------------------------------------------------------
    def error(self) -> str:
        """Get the current error message, or None if no error exists."""
        filename = self.filename()

        # Verify that the provided path exists.
        if not os.path.exists(filename):
            return 'Above path does not exist'

        # Verify the path is a file.
        if not os.path.isfile(filename):
            return 'Above path is not a file'

        # Verify that the path matches at least one of the file filters.
        filters = [filter for pattern in self._filters.values() for filter in pattern.split(' ')]
        if not any([fnmatch.filter([filename], filter) for filter in filters]):
            return f'Above file is not a supported type {", ".join(filters)}'

        # If all of the above checks passed then this file is valid.
        return None


# ----------------------------------------------------------------------------------------------------------------------
    def setError(self, error: str) -> None:
        """Override the currently displayed error message with the provided value.

        This error message is not retained.  As soon as the user makes a change to the filename the provided text will
        be replaced.

        This method is intended to be used to show errors that have occurred after the `selected` Signal has been
        invoked, such as file parsing errors for invalid file formatting that is outside the scope of the validation
        performed by this widget.

        Arguments:
            error: The error string to be displayed.
        """
        self.ui.error.setText(error)
        self.ui.error.show()


# ----------------------------------------------------------------------------------------------------------------------
    def _browse(self) -> None:
        """When the user clicks the browse button, launch a file search dialog."""
        # Build a Qt filter string from the dict of filter(s).
        filters = dict(self._filters)
        all_files = filters.pop('All Files', None)
        filters = ';;'.join(f'{name} ({pattern})' for name, pattern in filters.items())
        # Move "All Files" to the end, if provided.
        if all_files is not None:
            filters += f';;All Files ({all_files})'

        # Start in the directory of the currently selected file.
        dir = os.path.dirname(self.filename())

        # Give the user an open-file dialog to browse for a file.
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file...', dir, filter=filters)
        if filename:
            # Update the editor.  This will trigger the "changed" event and, by connection, the `changed` method below.
            self.ui.editor.setText(filename)


# ----------------------------------------------------------------------------------------------------------------------
    def _changed(self) -> None:
        """When the editor text is changed re-run validation."""
        # Update the error message, as appropriate.
        valid = self.isValid()
        self.ui.error.setVisible(not valid)
        self.ui.error.setText(self.error() or 'N/A')

        # Emit the changed Signal each time the filename text is changed.
        self.changed.emit()

        # Only emit the selected Signal when the selected file is valid.
        if valid:
            self.selected.emit(self.filename())


# ----------------------------------------------------------------------------------------------------------------------
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()


# ----------------------------------------------------------------------------------------------------------------------
    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()


# ----------------------------------------------------------------------------------------------------------------------
    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            urls = event.mimeData().urls()
            if len(urls) == 1:
                url = urls[0]
                if url.isLocalFile():
                    event.accept()
                    filename = url.toLocalFile()
                    self.setFilename(filename)
                    return
        event.ignore()




# End of File
