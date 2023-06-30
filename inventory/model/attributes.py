# ======================================================================================================================
#      File:  /inventory/model/attributes.py
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
"""Key/value attribute extensions for parts.

Allows arbitrary additional properties to be associated with individual parts.
"""

# ======================================================================================================================
# Import Statements
# ----------------------------------------------------------------------------------------------------------------------
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Text

from inventory.model.base import Base




# ======================================================================================================================
# Part Attribute Model
# ----------------------------------------------------------------------------------------------------------------------
class PartAttribute(Base):
    __tablename__ = 'part_attributes'
    part_id = Column(Integer, ForeignKey('parts.id'), primary_key=True)
    key = Column(String(25), primary_key=True)
    value = Column(Text)

    @staticmethod
    def GetUniqueKeys(session):
        attributes = session.query(PartAttribute).all()
        keys = [attribute.key for attribute in attributes]
        return list(set(keys))




# End of File
