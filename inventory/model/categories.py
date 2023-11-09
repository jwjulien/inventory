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
from typing import Iterator, List, TYPE_CHECKING

from peewee import CharField, ForeignKeyField
from playhouse.hybrid import hybrid_property

from inventory.model.base import BaseModel

if TYPE_CHECKING:
    from inventory.model.parts import Part




# ======================================================================================================================
# Category Model
# ----------------------------------------------------------------------------------------------------------------------
class Category(BaseModel):
    class Meta:
        table_name = 'categories'

    # Columns
    parent: 'Category' = ForeignKeyField('self', backref='children', null=True)
    title: str = CharField(50)
    designator: str = CharField(10, null=True)

    children: List['Category']
    parts: List['Part']


    # Properties
    @hybrid_property
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


    @hybrid_property
    def chain(self) -> List['Category']:
        """Return the complete, recursive chain of categories running up the tree from this category."""
        def recurse(category: Category) -> List[Category]:
            if category.parent:
                chain = recurse(category.parent)
            else:
                chain = []
            chain.append(category)
            return chain
        return recurse(self)


    def all_parts(self) -> Iterator['Part']:
        for part in self.parts:
            yield part
        for child in self.children:
            yield from child.all_parts()


    def full_title(self, separator: str = ' > ') -> str:
        """Fetch the full title, including titles of this category and each of it's parents moving up the tree."""
        return separator.join(category.title for category in self.chain if category.title)




# End of File
