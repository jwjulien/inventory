# ======================================================================================================================
#      File:  /inventory/model/parts/__init__.py
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
"""The coup de grace of the model - the parts class itself."""

# ======================================================================================================================
# Import Statements
# ----------------------------------------------------------------------------------------------------------------------
from typing import Dict

from peewee import BlobField, CharField, FloatField, ForeignKeyField, IntegerField, TextField
from playhouse.fields import PickleField
from playhouse.hybrid import hybrid_property

from inventory.model.base import BaseModel
from inventory.model.categories import Category




# ======================================================================================================================
# Part Class
# ----------------------------------------------------------------------------------------------------------------------
class Part(BaseModel):
    class Meta:
        table_name = 'parts'

    # Columns
    category = ForeignKeyField(Category, backref='parts')
    value = CharField(50)
    number = CharField(50)
    package = CharField(20, null=True)
    price = FloatField(null=True)
    weight = FloatField(null=True)
    threshold = IntegerField(default=0)
    notes = TextField(default='')
    attributes: Dict[str, str] = PickleField(default=dict)
    image = BlobField(null=True)


    # Properties
    @hybrid_property
    def quantity(self) -> int:
        return sum([location.quantity for location in self.locations])


    @hybrid_property
    def valuation(self) -> float:
        if self.price is not None:
            return self.quantity * self.price
        return 0


    @hybrid_property
    def is_stocked(self) -> bool:
        return self.threshold is not None


    @hybrid_property
    def low_stock(self) -> bool:
        return self.is_stocked and self.quantity < (self.threshold * 1.25)


    @hybrid_property
    def needs_reorder(self) -> bool:
        return self.is_stocked and self.quantity < self.threshold


    @hybrid_property
    def summary(self) -> str:
        text = self.category.full_title(', ')
        text += f', {self.value}'
        for value in self.attributes.values():
            text += f', {value}'
        if self.package is not None:
            text += f', {self.package}'
        return text




# End of File
