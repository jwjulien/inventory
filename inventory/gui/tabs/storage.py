# ======================================================================================================================
#      File:  /inventory/gui/tabs/storage.py
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
"""Tab implementation for storage aras, units, slots, and (ultimately) parts."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtWidgets

from inventory.gui.base.tab_storage import Ui_TabStorage
from inventory.model.storage import Area, Unit, Slot




# ======================================================================================================================
# Tab Storage Class
# ----------------------------------------------------------------------------------------------------------------------
class TabStorage(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_TabStorage()
        self.ui.setupUi(self)

        areas = Area.select()
        self.ui.areas.setAreas(areas)

        self.ui.areas.selected.connect(self.area_selected)
        self.ui.units.selected.connect(self.unit_selected)
        self.ui.slots.selected.connect(self.slot_selected)

        self.ui.units.hide()
        self.ui.slots.hide()
        self.ui.parts.hide()


    def area_selected(self, area: Area) -> None:
        self.ui.units.show()
        self.ui.slots.hide()
        self.ui.parts.show()
        self.ui.units.setUnits(area.units)
        self.ui.parts.setParts(area.parts)


    def unit_selected(self, unit: Unit) -> None:
        self.ui.slots.show()
        self.ui.slots.setSlots(unit.slots)
        self.ui.parts.setParts(unit.parts)


    def slot_selected(self, slot: Slot) -> None:
        if slot is not None:
            self.ui.parts.setParts(slot.parts)
        else:
            self.ui.parts.clear()



# End of File
