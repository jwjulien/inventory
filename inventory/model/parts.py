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
from datetime import datetime
from typing import List, Optional

from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import relationship, Mapped, mapped_column, Session
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from sqlalchemy.sql import func

from inventory.model.base import Base
from inventory.model.mixins import ProxiedDictMixin
from inventory.model.attributes import PartAttribute
from inventory.model.categories import PartCategory




# ======================================================================================================================
# Part Class
# ----------------------------------------------------------------------------------------------------------------------
class Part(ProxiedDictMixin, Base):
    __tablename__ = 'parts'

    # Columns
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('part_categories.id'))
    value: Mapped[str] = mapped_column(String(50))
    number: Mapped[str] = mapped_column(String(50))
    package: Mapped[str] = mapped_column(String(20))
    price: Mapped[float]
    weight: Mapped[float]
    threshold: Mapped[int]
    notes: Mapped[str]
    created_on: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    # TODO: Modified date is not populated until first update.  Need to either populate in a migration or find a way to
    # gracefully handle empty dates.  This seems like it could be an issue with the sqlite implementation, specifically?
    # modified_on: Mapped[Optional[datetime]] = mapped_column(DateTime)


    # Relationships
    # references = relationship('PartSupplier', backref='part')
    locations = relationship('SlotPart', backref='part')
    # boms = relationship('BOM', backref='part')
    attributes = relationship(PartAttribute, collection_class=attribute_mapped_collection('key'), cascade="all, delete-orphan")
    _proxied = association_proxy("attributes", "value", creator=lambda key, value: PartAttribute(key=key, value=value))


    # Properties
    @hybrid_property
    def quantity(self) -> int:
        return sum([location.quantity for location in self.locations])


    @hybrid_property
    def liability(self) -> float:
        if self.price is not None:
            return self.quantity * self.price
        return 0


    @hybrid_property
    def is_stocked(self) -> bool:
        return self.threshold is not None


    @hybrid_property
    def needs_reorder(self) -> bool:
        return self.is_stocked and self.quantity < self.threshold


    @hybrid_property
    def categories(self) -> List[PartCategory]:
        def recurse(category):
            categories = []
            if category.parent:
                categories.extend(recurse(category.parent))
            categories.append(category)
            return categories
        return recurse(self.category) if self.category else []

    @hybrid_property
    def description(self) -> str:
        parts = [category.title for category in self.categories]
        parts.append(self.value)
        for key in self:
            parts.append(self[key])
        if self.package is not None:
            parts.append(self.package)
        return ', '.join(parts)


# ----------------------------------------------------------------------------------------------------------------------
    # Static methods
    @staticmethod
    def GetByNumber(session: Session, number: str) -> 'Part':
        return session.query(Part).filter_by(number=number).scalar()


    @staticmethod
    def GetById(session: Session, id: int) -> 'Part':
        return session.execute(select(Part).filter_by(id=str(id))).scalar()


    @staticmethod
    def GetAll(session: Session) -> List['Part']:
        return session.execute(select(Part).order_by(Part.value)).scalars()


    @staticmethod
    def GetRecentlyModified(session: Session, limit: int = 15) -> List['Part']:
        return session.query(Part).order_by(Part.modified_on.desc()).limit(limit).scalars()


    @staticmethod
    def GetUnstored(session: Session) -> List['Part']:
        parts = Part.GetAll(session)
        return [part for part in parts if not part.locations]


    @staticmethod
    def GetByCategoryId(session: Session, category_id: int) -> List['Part']:
        return session.query(Part).filter_by(category_id=category_id).order_by(Part.value).scalars()




# End of File
