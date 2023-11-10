# ======================================================================================================================
#      File:  /inventory/gui/tabs/lost.py
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
"""A tab with a list of parts that have not been assigned to a location."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from inventory.gui.base.tab_parts import Ui_TabParts
from inventory.gui.tabs.base import TabWidget
from inventory.model.parts import Part




# ======================================================================================================================
# Tab Lost Widget
# ----------------------------------------------------------------------------------------------------------------------
class TabLost(TabWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_TabParts()
        self.ui.setupUi(self)


# ----------------------------------------------------------------------------------------------------------------------
    def refresh(self):
        # Setup model with all of the parts.
        parts = Part.select()
        lost_parts = [part for part in parts if not part.locations]
        self.ui.parts.setParts(lost_parts)




# End of File
