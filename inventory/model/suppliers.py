# ======================================================================================================================
#      File:  /inventory/model/suppliers.py
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
"""Model support for parts suppliers."""

# ======================================================================================================================
# Import Statements
# ----------------------------------------------------------------------------------------------------------------------
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, Integer, String, DateTime

from inventory.model.base import Base




# ======================================================================================================================
# Supplier
# ----------------------------------------------------------------------------------------------------------------------
class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    website = Column(String(100))
    search = Column(String(200))
    created_on = Column(DateTime)
    modified_on = Column(DateTime)

    references = relationship('PartSupplier', backref='supplier')

    @hybrid_property
    def parts(self):
        """Return a list of unique parts associated with this supplier."""
        return list(set([reference.part for reference in self.references]))

    @staticmethod
    def GetAll(session):
        return session.query(Supplier).order_by(Supplier.name).all()

    @staticmethod
    def GetById(session, id):
        return session.query(Supplier).filter_by(id=id).first()


# ----------------------------------------------------------------------------------------------------------------------
class PartSupplier(Base):
    __tablename__ = 'part_suppliers'

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    part_id = Column(Integer, ForeignKey('parts.id'))
    number = Column(String(80))
    created_on = Column(DateTime)
    modified_on = Column(DateTime)

    @staticmethod
    def GetById(session, id):
        return session.query(PartSupplier).filter_by(id=id).first()



# End of File
