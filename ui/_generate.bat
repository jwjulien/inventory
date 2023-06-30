cd ..
start poetry run pyside6-uic -o inventory/gui/base/main_window.py ui/main_window.ui

start poetry run pyside6-uic -o inventory/gui/base/page_parts.py ui/page_parts.ui

start poetry run pyside6-uic -o inventory/gui/base/dialog_category.py ui/dialog_category.ui
start poetry run pyside6-uic -o inventory/gui/base/dialog_part.py ui/dialog_part.ui
