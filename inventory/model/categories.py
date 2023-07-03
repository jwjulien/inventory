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
import collections
from datetime import datetime
from typing import List, Optional

# from sqlalchemy import ForeignKey, select
# from sqlalchemy.orm import relationship, backref, Mapped, mapped_column
# from sqlalchemy.ext.hybrid import hybrid_property
# from sqlalchemy import Column, Integer, String, DateTime
from peewee import CharField, DateTimeField, ForeignKeyField, PrimaryKeyField

from inventory.model.base import BaseModel



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


    def child_number(self) -> int:
        """Return the index of this category relative to it's sibling assigned to the same parent."""
        if self.parent is None:
            return None
        siblings = sorted(self.parent.children, key=lambda child: child.title)
        return siblings.index(self)




# ======================================================================================================================
# Part Categories Table
# ----------------------------------------------------------------------------------------------------------------------
# class PartCategory(BaseModel):
#     __tablename__ = 'part_categories'

#     # Columns
#     id: Mapped[int] = mapped_column(init=False, primary_key=True)
#     parent_id: Mapped[int] = mapped_column(ForeignKey('part_categories.id'))
#     default_designator: Mapped[Optional[str]] = mapped_column(String(10))
#     title: Mapped[str] = mapped_column(String(50))
#     created_on: Mapped[datetime]
#     # modified_on: Mapped[Optional[datetime]]

#     # Relationships
#     children = relationship('PartCategory',
#         cascade="all",
#         backref=backref("parent", remote_side='PartCategory.id'),
#         order_by='PartCategory.title',
#     )
#     parts = relationship('Part', backref='category', order_by='Part.value')


# # ----------------------------------------------------------------------------------------------------------------------
#     # Properties
#     @hybrid_property
#     def invalid(self) -> bool:
#         return not self.title


#     @hybrid_property
#     def inherited(self) -> bool:
#         return self.default_designator is None


#     @hybrid_property
#     def all_parts(self) -> List:
#         """Get a list of all of the parts under this category including the parts assigned to the children."""
#         def recurse(category):
#             parts = []
#             parts.extend(category.parts)
#             for child in category.children:
#                 parts.extend(recurse(child))
#             return parts
#         return recurse(self)


#     @hybrid_property
#     def is_leaf(self) -> bool:
#         return len(self.children) == 0


#     @hybrid_property
#     def depth(self) -> int:
#         if not self.parent:
#             return 0
#         else:
#             return self.parent.depth + 1


#     @hybrid_property
#     def full_title(self) -> str:
#         if self.parent:
#             return self.parent.full_title + '.' + self.title
#         return self.title


#     @hybrid_property
#     def designator(self) -> str:
#         if self.default_designator:
#             return self.default_designator
#         elif self.parent:
#             return self.parent.designator
#         return None

#     @designator.setter
#     def designator(self, value):
#         self.default_designator = value


# # ----------------------------------------------------------------------------------------------------------------------
#     # Static Methods
#     @staticmethod
#     def GetById(session, id):
#         return session.query(PartCategory).filter_by(id=id).first()


#     @staticmethod
#     def GetAll(session):
#         return session.query(PartCategory).all()


#     @staticmethod
#     def GetRoots(session):
#         return list(session.execute(select(PartCategory).filter_by(parent_id='').order_by(PartCategory.title)).scalars())


#     @staticmethod
#     def GetDict(session):
#         categories = collections.OrderedDict()
#         def addItems(nodes):
#             for node in nodes:
#                 categories[node.id] = node.full_title
#                 addItems(node.children)
#         roots = PartCategory.GetRoots(session)
#         addItems(roots)
#         return categories


#     @staticmethod
#     def GetChildren(session, parent_id):
#         return session.query(PartCategory).filter_by(parent_id=parent_id).all()




# End of File
