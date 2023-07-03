# ======================================================================================================================
#      File:  /inventory/model/categories.py
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
"""Part category support."""

# ======================================================================================================================
# Import Statements
# ----------------------------------------------------------------------------------------------------------------------
from peewee import CharField, ForeignKeyField

from inventory.model.base import BaseModel




# ======================================================================================================================
# Category Model
# ----------------------------------------------------------------------------------------------------------------------
class Category(BaseModel):
    class Meta:
        table_name = 'categories'

    # Columns
    parent = ForeignKeyField('self', backref='children', null=True)
    title = CharField(50)
    designator = CharField(10, null=True)


    # Properties
    @property
    def inherited_designator(self) -> str:
        """Fetch the designator for this category, which might be inherited from a parent."""
        # If assigned to this category, then that designator wins.
        if self.designator is not None:
            return self.designator
        # Otherwise, fall back on the part (which is possibly recursive).
        if self.parent is not None:
            return self.parent.inherited_designator
        # And if all else fails, None indicates that no designator was assigned.
        return None




# End of File
