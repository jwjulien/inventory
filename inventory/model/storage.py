# ======================================================================================================================
#      File:  /inventory/model/stored.py
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
from datetime import datetime
from typing import List, Optional
from dataclasses import dataclass

from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import relationship, Mapped, mapped_column, Session
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import String, DateTime
from sqlalchemy.sql import func

from inventory.model.base import Base




# ======================================================================================================================
# Area Class
# ----------------------------------------------------------------------------------------------------------------------
class Area(Base, kw_only=True):
    __tablename__ = 'storage_areas'

    # Columns
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    created_on: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    # modified_on: Mapped[Optional[datetime]]


    # Relationships
    units = relationship('Unit', backref='area')


# ----------------------------------------------------------------------------------------------------------------------
    # Properties
    @hybrid_property
    def parts(self):
        """Hybrid property that returns a list of unique parts that are associated with this unit."""
        parts = []
        for unit in self.units:
            parts.extend(unit.parts)
        return list(set(parts))


# ----------------------------------------------------------------------------------------------------------------------
    # Static Methods
    @staticmethod
    def GetAll(session: Session) -> List['Area']:
        return session.execute(select(Area).order_by(Area.name)).scalars()


    @staticmethod
    def GetById(session: Session, id: int) -> 'Area':
        return session.execute(select(Area).filter_by(id=str(id))).scalar()





# ======================================================================================================================
# Unit Class
# ----------------------------------------------------------------------------------------------------------------------
class Unit(Base, kw_only=True):
    __tablename__ = 'storage_units'

    # Columns
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    area_id: Mapped[int] = mapped_column(ForeignKey('storage_areas.id'))
    name: Mapped[str] = mapped_column(String(40))
    rows: Mapped[int]
    columns: Mapped[int]
    created_on: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    # modified_on: Mapped[Optional[datetime]]

    # Relationships
    slots = relationship('Slot', backref='unit')


# ----------------------------------------------------------------------------------------------------------------------
    # Properties
    @hybrid_property
    def parts(self) -> List:
        """Hybrid property that returns a list of unique parts that are associated with this unit."""
        parts = []
        for slot in self.slots:
            parts.extend(slot.parts)
        return list(set(parts))


# ----------------------------------------------------------------------------------------------------------------------
    # Methods
    def __getitem__(self, index) -> 'Row':
        return Row(self, index)


# ----------------------------------------------------------------------------------------------------------------------
    # Static Methods
    @staticmethod
    def GetById(session: Session, id: int) -> 'Unit':
        return session.execute(select(Unit).filter_by(id=str(id))).scalar()



# ======================================================================================================================
# Row Class
# ----------------------------------------------------------------------------------------------------------------------
@dataclass
class Row:
    unit: Unit
    row: int

    def __getitem__(self, col_num: int) -> 'Slot':
        for slot in self.unit.slots:
            if slot.row == self.row_num and slot.column == col_num:
                return slot
        return None




# ======================================================================================================================
# Slot Class
# ----------------------------------------------------------------------------------------------------------------------
class Slot(Base, kw_only=True):
    __tablename__ = 'storage_slots'

    # Columns
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    unit_id: Mapped[int] = mapped_column(ForeignKey('storage_units.id'))
    name: Mapped[str] = mapped_column(String(40))
    row: Mapped[int]
    span: Mapped[int]
    column: Mapped[int]
    proportion_vertical: Mapped[int] = mapped_column(default=1)
    proportion_horizontal: Mapped[int] = mapped_column(default=1)
    created_on: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    # modified_on: Mapped[Optional[datetime]]


    # Relationships
    locations = relationship('SlotPart', backref='slot')


# ----------------------------------------------------------------------------------------------------------------------
    # Properties
    @hybrid_property
    def parts(self) -> List:
        """Hybrid property that returns a list of unique parts that are associated with this slot."""
        return list(set([location.part for location in self.locations]))


# ----------------------------------------------------------------------------------------------------------------------
    # Static Methods
    @staticmethod
    def GetAll(session: Session) -> List['Slot']:
        return session.execute(select(Slot)).scalars()


    @staticmethod
    def GetById(session: Session, id: int) -> 'Slot':
        return session.execute(select(Slot).filter_by(id=str(id))).scalar()


    @staticmethod
    def GetByName(session: Session, name: str) -> 'Slot':
        return session.execute(select(Slot).filter_by(name=name)).scalar()



# ======================================================================================================================
# Slot Part Class
# ----------------------------------------------------------------------------------------------------------------------
class SlotPart(Base, kw_only=True):
    """Poorly named class that maps the n:n relationship between a part and a storage slot (aka: location)."""
    __tablename__ = 'part_slots'

    # Columns
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    slot_id: Mapped[int] = mapped_column(ForeignKey('storage_slots.id'))
    part_id: Mapped[int] = mapped_column(ForeignKey('parts.id'))
    quantity: Mapped[int] = mapped_column(default=0)
    last_counted: Mapped[Optional[datetime]]
    created_on: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    # modified_on: Mapped[Optional[datetime]]


# ----------------------------------------------------------------------------------------------------------------------
    # Static Methods
    @staticmethod
    def GetById(session: Session, id: int) -> 'SlotPart':
        return session.execute(select(SlotPart).filter_by(id=str(id))).scalar()


    @staticmethod
    def GetByIds(session: Session, slot_id: int, part_id: int) -> 'SlotPart':
        return session.execute(select(SlotPart).filter_by(slot_id=str(slot_id), part_id=str(part_id))).scalar()




# End of File
