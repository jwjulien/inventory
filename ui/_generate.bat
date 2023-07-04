cd ..
start poetry run pyside6-uic -o inventory/gui/base/main_window.py ui/main_window.ui

start poetry run pyside6-uic -o inventory/gui/base/tab_categories.py ui/tab_categories.ui
start poetry run pyside6-uic -o inventory/gui/base/tab_lost.py ui/tab_lost.ui
start poetry run pyside6-uic -o inventory/gui/base/tab_parts.py ui/tab_parts.ui
start poetry run pyside6-uic -o inventory/gui/base/tab_storage.py ui/tab_storage.ui

start poetry run pyside6-uic -o inventory/gui/base/dialog_category.py ui/dialog_category.ui
start poetry run pyside6-uic -o inventory/gui/base/dialog_location_mapping.py ui/dialog_location_mapping.ui
start poetry run pyside6-uic -o inventory/gui/base/dialog_part.py ui/dialog_part.ui
start poetry run pyside6-uic -o inventory/gui/base/dialog_relocate.py ui/dialog_relocate.ui

start poetry run pyside6-uic -o inventory/gui/base/widget_areas.py ui/widget_areas.ui
start poetry run pyside6-uic -o inventory/gui/base/widget_attributes.py ui/widget_attributes.ui
start poetry run pyside6-uic -o inventory/gui/base/widget_location.py ui/widget_location.ui
start poetry run pyside6-uic -o inventory/gui/base/widget_parts.py ui/widget_parts.ui
start poetry run pyside6-uic -o inventory/gui/base/widget_slots.py ui/widget_slots.ui
start poetry run pyside6-uic -o inventory/gui/base/widget_units.py ui/widget_units.ui
