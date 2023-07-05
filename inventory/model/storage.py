# ======================================================================================================================
#      File:  /inventory/model/storage.py
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
"""Model support for part storage locations."""

# ======================================================================================================================
# Import Statements
# ----------------------------------------------------------------------------------------------------------------------
from typing import List, Tuple

from peewee import CharField, DateTimeField, ForeignKeyField, IntegerField
from playhouse.hybrid import hybrid_property

from inventory.model.base import BaseModel
from inventory.model.parts import Part




# ======================================================================================================================
# Area Class
# ----------------------------------------------------------------------------------------------------------------------
class Area(BaseModel):
    class Meta:
        table_name = 'areas'

    # Columns
    name = CharField(40)


    # Properties
    @hybrid_property
    def parts(self):
        """Get a list of all of the parts located within this Area."""
        return list(set([part for unit in self.units for part in unit.parts]))




# ======================================================================================================================
# Unit Class
# ----------------------------------------------------------------------------------------------------------------------
class Unit(BaseModel):
    class Meta:
        table_name = 'units'

    # Columns
    area = ForeignKeyField(Area, backref='units')
    name = CharField(40)
    rows = IntegerField(default=1)
    columns = IntegerField(default=1)


    # Properties
    @hybrid_property
    def parts(self):
        """Get a list of all of the parts located within this Unit."""
        return list(set([part for slot in self.slots for part in slot.parts]))


# # ----------------------------------------------------------------------------------------------------------------------
#     # Methods
#     def __getitem__(self, index) -> 'Row':
#         return Row(self, index)



# # ======================================================================================================================
# # Row Class
# # ----------------------------------------------------------------------------------------------------------------------
# @dataclass
# class Row:
#     unit: Unit
#     row: int

#     def __getitem__(self, col_num: int) -> 'Slot':
#         for slot in self.unit.slots:
#             if slot.row == self.row_num and slot.column == col_num:
#                 return slot
#         return None




# ======================================================================================================================
# Slot Class
# ----------------------------------------------------------------------------------------------------------------------
class Slot(BaseModel):
    class Meta:
        table_name = 'slots'

    # Columns
    unit = ForeignKeyField(Unit, backref='slots')
    name = CharField(40)
    row = IntegerField()
    column = IntegerField()
    row_span = IntegerField(default=1)
    column_span = IntegerField(default=1)
    proportion_vertical = IntegerField(default=1)
    proportion_horizontal = IntegerField(default=1)


    # Properties
    @property
    def parts(self) -> List[Part]:
        """Get a list of all of the parts located within this Slot."""
        return list(set([location.part for location in self.locations]))


    @property
    def locations(self) -> List['Location']:
        return Location.select().where(Location.slot_id == self.id)


    @property
    def chain(self) -> Tuple[Area, Unit, 'Slot']:
        return (self.unit.area, self.unit, self)


    def full_title(self, separator: str = ' > ') -> str:
        return separator.join(item.name for item in self.chain)





# ======================================================================================================================
# Location Class
# ----------------------------------------------------------------------------------------------------------------------
class Location(BaseModel):
    """Poorly named class that maps the n:n relationship between a part and a storage slot (aka: location)."""
    class Meta:
        table_name = 'locations'

    # Columns
    slot = ForeignKeyField(Slot, backref='locations')
    part = ForeignKeyField(Part, backref='locations')
    quantity = IntegerField()
    last_counted = DateTimeField(null=True)


    @property
    def name(self) -> str:
        return f'{self.slot.unit.area.name} > {self.slot.unit.name} > {self.slot.name}'




# End of File
