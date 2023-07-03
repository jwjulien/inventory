cd ..
start poetry run pyside6-uic -o inventory/gui/base/main_window.py ui/main_window.ui

start poetry run pyside6-uic -o inventory/gui/base/tab_parts.py ui/tab_parts.ui
start poetry run pyside6-uic -o inventory/gui/base/tab_categories.py ui/tab_categories.ui

start poetry run pyside6-uic -o inventory/gui/base/dialog_category.py ui/dialog_category.ui
start poetry run pyside6-uic -o inventory/gui/base/dialog_part.py ui/dialog_part.ui

start poetry run pyside6-uic -o inventory/gui/base/widget_attributes.py ui/widget_attributes.ui
