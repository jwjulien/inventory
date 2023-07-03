# ======================================================================================================================
#      File:  /inventory/model/base.py
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
"""Declarative base singleton for use by all ORM classes in this model."""

# ======================================================================================================================
# Import Statements
# ----------------------------------------------------------------------------------------------------------------------
from datetime import datetime

from peewee import Model, SqliteDatabase, PrimaryKeyField, DateTimeField



# ======================================================================================================================
# Global Variables
# ----------------------------------------------------------------------------------------------------------------------
# TODO: Should this be moved to a better location within the app?  Feels wrong that it's a global defined here.  If
# done in MainWindow then how does it get associated with BaseModel?
db = SqliteDatabase('parts.sqlite')




# ======================================================================================================================
# SQLalchemy Declarative Base
# ----------------------------------------------------------------------------------------------------------------------
class BaseModel(Model):
    """Base class for all ORM classes in this model."""
    class Meta:
        database = db


    # Common columns for all classes
    id = PrimaryKeyField()
    created_on = DateTimeField(default=datetime.now)
    modified_on = DateTimeField(null=True)


    def save(self, *args, **kwargs):
        """Override the default save method to add a write of the current date/time to the "modified_on" field."""
        # Only set the modified_on field when not creating brand new rows.
        if self.id is not None:
            self.modified_on = datetime.now()
        super().save(*args, **kwargs)




# End of File
