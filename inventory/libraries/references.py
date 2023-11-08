# ======================================================================================================================
#      File:  /inventory/libraries/references.py
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
"""Inventory-specific barcode generation."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from enum import IntEnum
from dataclasses import dataclass

from aztec_code_generator import AztecCode
from PIL import Image
from pylibdmtx import pylibdmtx

from inventory.model.base import BaseModel
from inventory.model.categories import Category
from inventory.model.documents import Document, Reference as DocumentReference
from inventory.model.parts import Part
from inventory.model.projects import Project, Revision, Material
from inventory.model.storage import Area, Unit, Slot, Location
from inventory.model.suppliers import Supplier, Product




# ======================================================================================================================
# Reference Target Enumeration
# ----------------------------------------------------------------------------------------------------------------------
class ReferenceTarget(IntEnum):
    """Indicates the target of a reference."""
    Part = 0x10      # Link directly to a specific part.
    Category = 0x20  # Reference to a part Category.
    Area = 0x30      # Reference to a storage Area.
    Unit = 0x31      # Reference to a storage Unit within an Area.
    Slot = 0x32      # Reference to a storage Slot within a Unit.
    Location = 0x33  # Reference to a storage Location within a specific Slot.
    Project = 0x40   # Reference to a Project that uses a part.
    Revision = 0x41  # Reference to a specific Revision of a Project.
    Material = 0x42  # Reference to a specific Project BOM line item.
    Supplier = 0x50  # Reference to a single Supplier for a Part.
    Product = 0x51   # Reference to a Supplier-specific Product.
    Document = 0x60  # Reference to a Document that may be associated with a Part.
    Reference = 0x61 # Getting a bit meta, but this is a Document Reference specific to a Part and Document.




# ======================================================================================================================
# Reference Class
# ----------------------------------------------------------------------------------------------------------------------
@dataclass
class Reference:
    """A generic reference to a Part, Location, Project, Category, etc."""
    target: ReferenceTarget  # The target of this reference
    id: int                  # The unique database ID for this Reference target
    version: int = 1         # Reference version (this attribute shouldn't be set manually - let this default rule)


# ----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def generate(item: BaseModel) -> 'Reference':
        """Generate a new Reference to the Part, Supplier, Location, etc. provided.

        This constructor is most useful when generating new References for database items, such as when printing
        barcodes.
        """
        map = {
            Part: ReferenceTarget.Part,
            Category: ReferenceTarget.Category,
            Area: ReferenceTarget.Area,
            Unit: ReferenceTarget.Unit,
            Slot: ReferenceTarget.Slot,
            Location: ReferenceTarget.Location,
            Project: ReferenceTarget.Project,
            Revision: ReferenceTarget.Revision,
            Material: ReferenceTarget.Material,
            Supplier: ReferenceTarget.Supplier,
            Product: ReferenceTarget.Product,
            Document: ReferenceTarget.Document,
            DocumentReference: ReferenceTarget.Reference
        }
        return Reference(target=map[type(item)], id=item.id)


# ----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def from_str(text: str) -> 'Reference':
        """Generate a Reference to a Part, Supplier, Location, etc. from a provided string.

        This constructor is likely most useful when decoding previously `encode`ed References.
        """
        if not text.startswith('#'):
            raise ValueError('Expected string to start with "#"')
        elif not text.endswith('$'):
            raise ValueError('Expected string to end with "$"')
        else:
            text = text.strip('#$')
        parts = text.split(':')
        if len(parts) != 3:
            raise ValueError('Expected three values separated by colons (\':\')')
        parts = [int(value, 16) for value in parts]
        version = parts[0]
        if version == 1:
            return Reference(
                version=1,
                target=ReferenceTarget(parts[1]),
                id=parts[2]
            )
        else:
            raise ValueError(f'Unsupported barcode reference version {version}')


# ----------------------------------------------------------------------------------------------------------------------
    def encode(self) -> str:
        """Encode this barcode information into a bytes string."""
        return f'#{self.version:X}:{self.target.value:02X}:{self.id:08X}$'


# ----------------------------------------------------------------------------------------------------------------------
    def lookup(self) -> BaseModel:
        """Attempt to fetch the target of this reference from the database.

        Returns:
            A specific implementation of BaseModel, such as a Part, Location, Category, etc. that is the target of this
            reference.
        """
        map = {
            ReferenceTarget.Part: Part,
            ReferenceTarget.Category: Category,
            ReferenceTarget.Area: Area,
            ReferenceTarget.Unit: Unit,
            ReferenceTarget.Slot: Slot,
            ReferenceTarget.Location: Location,
            ReferenceTarget.Project: Project,
            ReferenceTarget.Revision: Revision,
            ReferenceTarget.Material: Material,
            ReferenceTarget.Supplier: Supplier,
            ReferenceTarget.Product: Product,
            ReferenceTarget.Document: Document,
            ReferenceTarget.Reference: DocumentReference,
        }
        model = map[self.target]
        return model.get_by_id(self.id)


# ----------------------------------------------------------------------------------------------------------------------
    def aztec(self) -> Image:
        return AztecCode(self.encode()).image()


# ----------------------------------------------------------------------------------------------------------------------
    def datamatrix(self) -> Image:
        """Generate a datamatrix image with the encoded flavor of this Reference.

        Side note: 119 characters of data seems to be the upper limit for what will fit on and scan from a 1/2" label.
        That translates to a 220x220 pixel matrix that scales down *okay*.
        """
        data = self.encode()
        matrix = pylibdmtx.encode(data.encode('utf8'))
        image = Image.frombytes('RGB', (matrix.width, matrix.height), matrix.pixels).convert('1')
        return image




# End of File
