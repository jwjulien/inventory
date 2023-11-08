# ======================================================================================================================
#      File:  /inventory/gui/main_window.py
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
"""Main window for the Inventory application."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import ctypes
import os
from importlib import metadata

from PySide6 import QtCore, QtGui, QtWidgets

from inventory.gui.base.main_window import Ui_MainWindow
from inventory.gui.tabs.categories import TabCategories
from inventory.gui.tabs.lost import TabLost
from inventory.gui.tabs.parts import TabParts
from inventory.gui.tabs.projects import TabProjects
from inventory.gui.tabs.storage import TabStorage
from inventory.gui.tabs.suppliers import TabSuppliers
from inventory.model.base import db
from inventory.model.categories import Category
from inventory.model.documents import Document, Reference as DocumentReference
from inventory.model.parts import Part
from inventory.model.projects import Project, Revision, Material
from inventory.model.storage import Area, Unit, Slot, Location
from inventory.model.suppliers import Supplier, Product
from inventory.libraries.scanner import ScannerWorker
from inventory.libraries.references import Reference




# ======================================================================================================================
# Main Window Class
# ----------------------------------------------------------------------------------------------------------------------
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Setup window title with name and version info from package metadata.
        name = 'inventory'
        version = metadata.version(name)
        self.setWindowTitle(f'{name.title()} - Version {version}')

        # Setup icon and indicate to Windows that it should be shown in the taskbar.
        icon = os.path.join('inventory', 'assets', 'icons', 'boxes.png')
        self.setWindowIcon(QtGui.QIcon(icon))
        if os.name == 'nt':
            myappid = f'exsystems.{name}.{version}'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        # Connect to database.
        db.connect()
        db.create_tables([
            Category,
            Document, DocumentReference,
            Part,
            Project, Revision, Material,
            Area, Unit, Slot, Location,
            Supplier, Product,
        ])

        # Setup tabs.
        self.ui.tab_parts = TabParts(self)
        self.ui.tabs.addTab(self.ui.tab_parts, 'All Parts')
        self.ui.tab_categories = TabCategories(self)
        self.ui.tabs.addTab(self.ui.tab_categories, 'By Category')
        self.ui.tab_projects = TabProjects(self)
        self.ui.tabs.addTab(self.ui.tab_projects, 'By Project')
        self.ui.tab_storage = TabStorage(self)
        self.ui.tabs.addTab(self.ui.tab_storage, 'By Location')
        self.ui.tab_suppliers = TabSuppliers(self)
        self.ui.tabs.addTab(self.ui.tab_suppliers, 'By Supplier')
        self.ui.tab_lost = TabLost(self)
        self.ui.tabs.addTab(self.ui.tab_lost, 'Lost Parts')
        tooltip = 'Shows parts that have not been assigned to any location(s) yet.'
        self.ui.tabs.setTabToolTip(self.ui.tabs.indexOf(self.ui.tab_lost), tooltip)

        # Setup a thread pool for background tasks.
        self.threadpool = QtCore.QThreadPool(self)

        # Setup the barcode scanner.
        self._setup_scanner()


    def _setup_scanner(self):
        # TODO: This VID/PID should be configurable.
        # VENDOR_ID = 0x0581
        # PRODUCT_ID = 0x0103
        VENDOR_ID = 0x0581
        PRODUCT_ID = 0x011C

        self.scanner_worker = ScannerWorker(VENDOR_ID, PRODUCT_ID)
        # TODO: The received event needs to be connected to a handler that will actually show the user what they scanned.
        self.scanner_worker.received.connect(self._tag_scanned)
        self.threadpool.start(self.scanner_worker)


    def _tag_scanned(self, code: str) -> None:
        print('Received code:', code)
        try:
            reference = Reference.from_str(code, label='scanner')
        except ValueError:
            print('Error parsing:', code)
            raise
        thing = reference.lookup()
        print(thing.id, type(thing))


    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.scanner_worker.stop()
        return super().closeEvent(event)




# End of File
