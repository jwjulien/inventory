# ======================================================================================================================
#      File:  /inventory/gui/dialogs/slot_select.py
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
"""A dialog for selecting a Slot, either for associating with a Location of for relocating Slots."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PySide6 import QtWidgets

from inventory.gui.base.dialog_slot_select import Ui_SlotSelectDialog
from inventory.model.storage import Area, Unit, Slot




# ======================================================================================================================
# Slot Select Dialog
# ----------------------------------------------------------------------------------------------------------------------
class SlotSelectDialog(QtWidgets.QDialog):
    """A dialog for selecting a Slot from the storage tree.

    Attributes:
        selected: Optional Slot to select as the starting point.
        unoccupied: A bool indicating if the selected Slot is valid when not occupied.  Default: True - Slot should not
            already be associated with a Location.
    """
    def __init__(self, parent: QtWidgets.QWidget, selected: Slot = None, unoccupied: bool = True):
        super().__init__(parent)
        self.ui = Ui_SlotSelectDialog()
        self.ui.setupUi(self)

        self._slot = selected
        self._unoccupied = unoccupied

        # Load areas to start.
        self.ui.areas.setAreas(Area.select())

        # Connect events.
        self.ui.areas.selected.connect(self._area_selected)
        self.ui.units.selected.connect(self._unit_selected)
        self.ui.slots.selectionChanged.connect(self._selected)

        # Make selection, if provided.
        if selected:
            self.ui.areas.select(selected.unit.area)
            self.ui.units.select(selected.unit)
            self.ui.slots.select(selected)
        else:
            # If not provided, then update the Ok button.
            self._selected()


# ----------------------------------------------------------------------------------------------------------------------
    def _area_selected(self, area: Area) -> None:
        self.ui.toolbox.setItemText(0, f'Area: {area.name}')
        self.ui.toolbox.setCurrentWidget(self.ui.page_unit)
        self.ui.units.setArea(area)


# ----------------------------------------------------------------------------------------------------------------------
    def _unit_selected(self, unit: Unit) -> None:
        self.ui.toolbox.setItemText(1, f'Unit: {unit.name}')
        self.ui.toolbox.setCurrentWidget(self.ui.page_slot)
        self.ui.slots.setUnit(unit)


# ----------------------------------------------------------------------------------------------------------------------
    def slot(self) -> Slot:
        index = self.ui.slots.selectedIndex()
        if index:
            return Slot(
                unit=self.ui.units.unit(),
                name=self._slot.name if self._slot else '',
                row=index.row(),
                column=index.column(),
                row_span=self._slot.row_span if self._slot else 1,
                column_span=self._slot.column_span if self._slot else 1
            )
        return None


# ----------------------------------------------------------------------------------------------------------------------
    def _selected(self) -> None:
        index = self.ui.slots.selectedIndex()
        valid = True
        if self._slot:
            for row in range(self._slot.row_span):
                for column in range(self._slot.column_span):
                    slot = self.ui.slots.slotAt(index.row() + row, index.column() + column)
                    valid &= not slot if self._unoccupied else bool(slot)
        self.ui.buttons.button(self.ui.buttons.StandardButton.Ok).setEnabled(valid)




# End of File
