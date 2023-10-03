# ======================================================================================================================
#      File:  /inventory/model/projects.py
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
"""Model support for projects that user parts."""

# ======================================================================================================================
# Import Statements
# ----------------------------------------------------------------------------------------------------------------------
from typing import Dict, List

from peewee import CharField, DateField, ForeignKeyField, TextField
from playhouse.hybrid import hybrid_property

from inventory.model.base import BaseModel
from inventory.model.parts import Part




# ======================================================================================================================
# Project Model
# ----------------------------------------------------------------------------------------------------------------------
class Project(BaseModel):
    """A project is quite simply that, a physical widget that has been designed in-house.  Projects ultimately contain
    a list of parts that make of the bill of materials.  The BOM is a complete listing of what is required to construct
    the physical widget.  The project contains revisions to track the various design iterations and their associated
    BOMs."""
    class Meta:
        table_name = 'projects'

    title = CharField(40)
    description = TextField()




# ======================================================================================================================
# Project Revision Model
# ----------------------------------------------------------------------------------------------------------------------
class Revision(BaseModel):
    """A revision is a version of a project.  Various project iterations, or versions, may have slightly different
    bill of materials lists so versions must be tracked independently."""
    class Meta:
        table_name = 'revisions'

    project = ForeignKeyField(Project, backref='revisions')
    version = CharField(32)
    date = DateField()


    @hybrid_property
    def total_cost(self):
        """The sum of all parts associated with a Revision of a Project."""
        return sum([bom.part.price or 0 for bom in self.lines])


    @hybrid_property
    def parts(self) -> Dict[Part, List['Material']]:
        """Hybrid property that groups bom entries into a dictionary where the keys are unique parts and the values
        are a list of bom entries.  Useful when view BOMs as parts are generally grouped showing a list of designators
        rather than individual parts."""
        grouped = {}
        for material in sorted(self.materials, key=lambda material: (material.designator is None, material.designator)):
            if material.part not in grouped:
                grouped[material.part] = []
            grouped[material.part].append(material)
        return grouped


    def lookup_material(self, designator: str) -> 'Material':
        for material in self.materials:
            if material.designator == designator:
                return material
        raise KeyError(f'Designator "{designator}" does not exist on {self.project.title} version {self.version}')




# ======================================================================================================================
# Project Revision Material Model
# ----------------------------------------------------------------------------------------------------------------------
class Material(BaseModel):
    """A single entry from a bill of materials for a Project Revision."""
    class Meta:
        table_name = 'materials'

    revision = ForeignKeyField(Revision, backref='materials')
    part = ForeignKeyField(Part, backref='materials')
    designator = CharField(10)




# End of File
