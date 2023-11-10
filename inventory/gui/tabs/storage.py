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
import qtawesome

from inventory.gui.base.tab_storage import Ui_TabStorage
from inventory.gui.tabs.base import TabWidget
from inventory.model.storage import Area, Unit, Slot




# ======================================================================================================================
# Tab Storage Class
# ----------------------------------------------------------------------------------------------------------------------
class TabStorage(TabWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_TabStorage()
        self.ui.setupUi(self)

        self.ui.back.setIcon(qtawesome.icon('fa.arrow-left'))

        self.ui.areas.selected.connect(self._area_selected)
        self.ui.units.selected.connect(self._unit_selected)
        self.ui.back.clicked.connect(self._show_areas)

        self.ui.units.hide()
        self._show_areas()


# ----------------------------------------------------------------------------------------------------------------------
    def refresh(self) -> None:
        areas = Area.select()
        self.ui.areas.setAreas(areas)


# ----------------------------------------------------------------------------------------------------------------------
    def _show_areas(self) -> None:
        self.ui.stack.setCurrentWidget(self.ui.page_areas)


# ----------------------------------------------------------------------------------------------------------------------
    def _area_selected(self, area: Area) -> None:
        self.ui.units.show()
        self.ui.units.setUnits(area, area.units)


# ----------------------------------------------------------------------------------------------------------------------
    def _unit_selected(self, unit: Unit) -> None:
        if unit is not None:
            self.ui.title.setText(f'{unit.area.name} > {unit.name}')
            self.ui.stack.setCurrentWidget(self.ui.page_slots)
            self.ui.slots.setUnit(unit)
        else:
            self.show_areas()


# ----------------------------------------------------------------------------------------------------------------------
    def set_area(self, area: Area) -> None:
        self.ui.areas.select(area)


# ----------------------------------------------------------------------------------------------------------------------
    def set_unit(self, unit: Unit) -> None:
        self.set_area(unit.area)
        self.ui.units.select(unit)
        self._unit_selected(unit)


# ----------------------------------------------------------------------------------------------------------------------
    def set_slot(self, slot: Slot) -> None:
        self.set_unit(slot.unit)
        self.ui.slots.select(slot)




# End of File
