# ======================================================================================================================
#      File:  /inventory/model/__init__.py
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
"""Top level imports for the model.

This is mostly needed to ensure that Base get associated with all of the ORM classes such that they all know about each
other.
"""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
# from inventory.model.attributes import PartAttribute
from inventory.model.base import Base
from inventory.model.categories import PartCategory
from inventory.model.parts import Part
# from inventory.model.projects import Project, Revision, BOM
from inventory.model.storage import Area, Unit, Slot, SlotPart
# from inventory.model.suppliers import Supplier, PartSupplier




__all__ = [
    'Base',
    'PartAttribute',
    'PartCategory',
    'Part',
    'Project',
    'Revision',
    'BOM',
    'Area',
    'Unit',
    'Slot',
    'SlotPart',
    'Supplier',
    'PartSupplier'
]




# End of File
