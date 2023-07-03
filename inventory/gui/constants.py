# ======================================================================================================================
#      File:  /inventory/gui/constants.py
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
"""Constants for use across the various GUI windows."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtGui



# ======================================================================================================================
# Common Colors
# ----------------------------------------------------------------------------------------------------------------------
class Colors:
    """Borrowed from Bootstrap."""
    Primary = QtGui.QColor(13, 110, 253)
    Success = QtGui.QColor(25, 135, 84)
    Danger = QtGui.QColor(220, 53, 69)
    Warning = QtGui.QColor(255, 193, 7)
    Info = QtGui.QColor(13, 202, 240)



# ======================================================================================================================
# Common Brushes
# ----------------------------------------------------------------------------------------------------------------------
class Brushes:
    Primary = QtGui.QBrush(Colors.Primary)
    Success = QtGui.QBrush(Colors.Success)
    Danger = QtGui.QBrush(Colors.Danger)
    Warning = QtGui.QBrush(Colors.Warning)
    Info = QtGui.QBrush(Colors.Info)




# End of File
