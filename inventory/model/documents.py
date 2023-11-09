# ======================================================================================================================
#      File:  /inventory/model/documents.py
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
"""Model support for documents and associating them with Parts."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from peewee import CharField, ForeignKeyField
from playhouse.fields import CompressedField

from inventory.model.base import BaseModel
from inventory.model.parts import Part




# ======================================================================================================================
# Document Table
# ----------------------------------------------------------------------------------------------------------------------
class Document(BaseModel):
    class Meta:
        table_name = 'documents'

    # Columns
    label = CharField(40)
    filename = CharField(30)
    content = CompressedField()
    part = ForeignKeyField(Part, backref='documents')




# End of File
