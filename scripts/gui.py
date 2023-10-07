# ======================================================================================================================
#      File:  /scripts/gui.py
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
"""Intelligently regenerate the UI files into the base .py files for the project.

This means that, by default, the .py files will only be regenerated if the timestamp on the .ui file is newer than the
timestamp on the .py file.
"""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from glob import glob
import logging
import os

import click




# ======================================================================================================================
# Constants
# ----------------------------------------------------------------------------------------------------------------------
UiPath = 'ui'
OutputPath = os.path.join('inventory', 'gui', 'base')




# ======================================================================================================================
# Aliased Group
# ----------------------------------------------------------------------------------------------------------------------
class AliasedGroup(click.Group):
    """Allows any number of prefix characters to be used to invoke a command, so long as they are unique to the command.

    This operates similarly to how Mercurial commands work.  For example, "c" or "cl" could be used for `clean` or "u"
    or "up" could be used instead of typing out "update".  This is largely for convenience.
    """
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx)
                   if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail(f"Too many matches: {', '.join(sorted(matches))}")


    def resolve_command(self, ctx, args):
        # always return the full command name
        _, cmd, args = super().resolve_command(ctx, args)
        return cmd.name, cmd, args




# ======================================================================================================================
# Click Application
# ----------------------------------------------------------------------------------------------------------------------
@click.group(cls=AliasedGroup)
@click.option('-v', '--verbose', count=True, help='increase verbosity of output')
def generate(verbose: int):
    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(2, verbose)]
    logging.basicConfig(level=level)




# ======================================================================================================================
# Clean Command
# ----------------------------------------------------------------------------------------------------------------------
@generate.command()
def clean():
    """Remove all of the generated .py files from the OutputPath in preparation for a complete regeneration."""
    _clean()


def _clean():
    # Extracted from the `clean` command to facilitate reuse by update command.
    for path in glob(os.path.join(OutputPath, '*.py')):
        filename = os.path.basename(path)
        try:
            logging.info('Removing %s', filename)
            logging.debug('Full path: %s', path)
            os.unlink(path)
        except:
            logging.critical('Failed to remove %s', filename)




# ======================================================================================================================
# Generate Command
# ----------------------------------------------------------------------------------------------------------------------
@generate.command()
@click.option('-c', '--clean', is_flag=True, help='perform a `clean` before generating')
def update(clean: bool):
    """Update the .py files for all .ui elements."""
    if clean:
        _clean()

    generated = False
    for source in glob(os.path.join(UiPath, '*.ui')):
        # Determine proper paths to the input and output files.
        source_filename = os.path.basename(source)
        destination_filename = os.path.splitext(source_filename)[0] + '.py'
        destination = os.path.join(OutputPath, destination_filename)
        logging.debug('Input file: %s', source)
        logging.debug('Output file: %s', destination)

        # Test if .ui file has been changed since last generated.
        if not os.path.exists(destination) or os.path.getmtime(source) > os.path.getmtime(destination):
            generated = True
            print(f'Regenerating {destination_filename} because {source_filename} has changed')

            command = f'poetry run pyside6-uic -o {destination} {source}'
            logging.debug('Generation shell command: %s', command)
            if os.system(command):
                logging.error('Failed to regenerate file')
        else:
            logging.info('%s is unchanged', source_filename)

    if not generated:
        print('All files are up to date')



# End of File
