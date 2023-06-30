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
import collections

from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, Integer, String, Text, DateTime

from inventory.model.base import Base




# ======================================================================================================================
# Project Class
# ----------------------------------------------------------------------------------------------------------------------
class Project(Base):
    """A project is quite simply that, a physical widget that has been designed in-house.  Projects untimately contain
    a list of parts that make of the bill of materials.  The BOM is a complete listing of what is required to construct
    the physical widget.  The project contains revisions to track the various design iterations and their associated
    BOMs."""
    __tablename__ = 'projects'

    # -----[ Columns ]--------------------------------------------------------------------------------------------------
    id = Column(Integer, primary_key=True)
    title = Column(String(40))
    description = Column(Text)
    created_on = Column(DateTime)
    modified_on = Column(DateTime)

    # -----[ Relationships ]--------------------------------------------------------------------------------------------
    revisions = relationship('Revision', backref='project', order_by='Revision.version')

    # -----[ Static Methods ]-------------------------------------------------------------------------------------------
    @staticmethod
    def GetAll(session):
        """Return all of the projects in the database."""
        return session.query(Project).order_by(Project.title).all()

    @staticmethod
    def GetById(session, id):
        """Return a single project with the corresponding ID."""
        return session.query(Project).filter_by(id=id).first()




# ======================================================================================================================
# Project Revision Class
# ----------------------------------------------------------------------------------------------------------------------
class Revision(Base):
    """A revision is a version of a project.  Various project iterations, or versions, may have slightly different
    bill of materials lists so versions must be tracked independently."""
    __tablename__ = 'revisions'

    # -----[ Columns ]--------------------------------------------------------------------------------------------------
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    version = Column(String(32))
    created_on = Column(DateTime)
    modified_on = Column(DateTime)

    # -----[ Relationships ]--------------------------------------------------------------------------------------------
    boms = relationship('BOM', backref='revision', order_by='BOM.designator')

    # -----[ Properties ]-----------------------------------------------------------------------------------------------
    @hybrid_property
    def total_cost(self):
        """Hybrid property that returns the total cost of the project by summing the price of each individual
        component."""
        return sum([bom.part.price or 0 for bom in self.boms])

    @hybrid_property
    def parts(self):
        """Hybrid property that groups bom entries into a dictionary where the keys are unique parts and the values
        are a list of bom entries.  Useful when view BOMs as parts are generally grouped showing a list of designators
        rather than individual parts."""
        grouped = collections.OrderedDict()
        # Ordered dict will remember the order that the entries are placed into it.  We would prefer for the parts
        # without designators to be located at the end of the list so resort the parts accordingly.
        for bom in sorted(self.boms, key=lambda bom: (bom.designator is None, bom.designator)):
            if bom.part not in grouped:
                grouped[bom.part] = []
            grouped[bom.part].append(bom)
        return grouped

    # -----[ Static Methods ]-------------------------------------------------------------------------------------------
    @staticmethod
    def GetById(session, id):
        """Return a single project revision with the corresponding ID."""
        return session.query(Revision).filter_by(id=id).first()




# ======================================================================================================================
# Project Revision BOM Entry Class
# ----------------------------------------------------------------------------------------------------------------------
class BOM(Base):
    """A BOM (in this sense) is a single entry that maps a part to a project revision.  The mapping contains an
    additional attribute to designate the corresponding part in the schematic."""
    __tablename__ = 'boms'

    # -----[ Columns ]--------------------------------------------------------------------------------------------------
    id = Column(Integer, primary_key=True)
    revision_id = Column(Integer, ForeignKey("revisions.id"))
    part_id = Column(Integer, ForeignKey("parts.id"))
    designator = Column(String(10))
    created_on = Column(DateTime)
    modified_on = Column(DateTime)

    # -----[ Static Methods ]-------------------------------------------------------------------------------------------
    @staticmethod
    def GetById(session, id):
        """Return a single BOM entry with the corresponding ID."""
        return session.query(BOM).filter_by(id=id).first()




# End of File
