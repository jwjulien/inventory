Inventory GUI Base Directory
========================================================================================================================
**DO NOT DIRECTLY EDIT THE FILES IN THIS DIRECTORY!**

These files are generated using the UIC command provided by PySide.



How to make changes
------------------------------------------------------------------------------------------------------------------------
To update the files in this directory:

1. Launch Qt Designer from the .venv/Scripts directory (named PySide6-designer.exe).
2. Open the corresponding .ui file to be updated from the /ui direcory at the root of this project.
3. Make the required changes/updates using Qt Designer and save changes back to .ui file.
4. Use the Gui.py script (available via poetry as the "ui" command from Poetry shell/virtual environment) to regenerate:

    (.venv) $ ui update

The update command will update the .py files in c-compiler style, only updating the ./py files that are older than their .ui counterparts.  If you want to regenerate all of the .ui/.py files, then issue a `clean` command first.
