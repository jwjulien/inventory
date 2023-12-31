# ======================================================================================================================
#      File:  /inventory/main.py
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
"""Main application launcher for Inventory."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import sys

import click
from PySide6 import QtWidgets
import qdarktheme
import qtawesome

from inventory.gui.main_window import MainWindow




# ======================================================================================================================
# Main Function
# ----------------------------------------------------------------------------------------------------------------------
@click.command()
@click.option('-p', '--prod', 'production', is_flag=True, help='switch to production mode')
def main(production: bool) -> int:
    # Set colors for QtAwesome icons before the main window is instantiated.
    qtawesome.set_defaults(
        color='#E0E1E3',
        color_active='#C9CDD0',
        color_selected='#ACB1B6',
        color_disabled='#9DA9B5'
    )

    sys.argv += ['-platform', 'windows:darkmode=2']
    app = QtWidgets.QApplication(sys.argv)
    qdarktheme.setup_theme('auto', additional_qss="QToolTip { border: 0px; }")
    window = MainWindow(production)
    window.show()
    return app.exec()




# End of File
