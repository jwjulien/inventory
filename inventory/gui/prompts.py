# ======================================================================================================================
#      File:  /inventory/gui/prompts.py
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
"""Prompt dialog helpers."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtWidgets




# ======================================================================================================================
# Yes/No Confirmation Dialog
# ----------------------------------------------------------------------------------------------------------------------
def YesNoPrompt(parent: QtWidgets.QWidget, title: str, message: str) -> bool:
    """Prompt the user with a yes/no question and return their response as a bool.

    Arguments:
        title: Title for the top of the window.
        message: The actual prompt for the user.

    Returns:
        True if the user said Yes or False if the user said No or closed the dialog.
    """
    result = QtWidgets.QMessageBox.question(
        parent,
        title,
        message,
        QtWidgets.QMessageBox.StandardButton.Yes,
        QtWidgets.QMessageBox.StandardButton.No
    )
    return result == QtWidgets.QMessageBox.StandardButton.Yes




# ======================================================================================================================
# Alert Dialog
# ----------------------------------------------------------------------------------------------------------------------
def Alert(parent: QtWidgets.QWidget, title: str, message: str):
    """Show the user a message in a dialog.

    Arguments:
        title: Title for the top of the window.
        message: The actual prompt for the user.
    """
    QtWidgets.QMessageBox.warning(
        parent,
        title,
        message,
        QtWidgets.QMessageBox.StandardButton.Ok
    )




# End of File
