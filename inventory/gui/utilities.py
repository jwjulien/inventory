# ======================================================================================================================
#      File:  /inventory/gui/utilities.py
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
"""GUI helpers."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from typing import Callable

from PySide6 import QtCore, QtGui, QtWidgets
import qtawesome




# ======================================================================================================================
# Context Menu Action Helper
# ----------------------------------------------------------------------------------------------------------------------
def context_action(menu: QtWidgets.QMenu,
                   title: str,
                   slot: Callable,
                   icon: str = None,
                   shortcut: str = None,
                   shortcut_widget: QtWidgets.QWidget = None
                   ) -> QtGui.QAction:
    """Add a QAction to a QMenu with a particular focus on custom context menus.

    Arguments:
        menu: A reference to the QMenu to which this QAction is to be added.
        title: Textual name for the item in the context menu.
        slot: A callback method to be connected to the `triggered` slot of the QAction.
        icon: Optional qtawesome icon name.  If not provided, no icon will be displayed.
        shortcut: Optional QKeySequence to be used as a shortcut to this action.
        shortcut_widget: An optional widget to add the shortcut to, if provided, to enable the use of keyboard shortcuts
            within the widget.  Really, if `shortcut` is provided, you likely want to include `shortcut_widget` too.

    Returns:
        The QAction instance that was created.  The action will already be added to the passed `menu`, however, if a
        reference is needed to do things like enable.disable the specific action, then this reference should be saved
        by the caller of this function.
    """
    action = QtGui.QAction(title, menu)
    if icon is not None:
        action.setIcon(qtawesome.icon(icon))
    if shortcut is not None:
        action.setShortcut(QtGui.QKeySequence(shortcut))
        if shortcut_widget is not None:
            action.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
            shortcut_widget.addAction(action)
    menu.addAction(action)
    action.triggered.connect(slot)
    return action




# End of File
