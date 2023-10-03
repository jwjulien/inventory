cd ..

start /b poetry run pyside6-uic -o inventory/gui/base/main_window.py ui/main_window.ui

start /b poetry run pyside6-uic -o inventory/gui/base/tab_categories.py ui/tab_categories.ui
start /b poetry run pyside6-uic -o inventory/gui/base/tab_lost.py ui/tab_lost.ui
start /b poetry run pyside6-uic -o inventory/gui/base/tab_parts.py ui/tab_parts.ui
start /b poetry run pyside6-uic -o inventory/gui/base/tab_projects.py ui/tab_projects.ui
start /b poetry run pyside6-uic -o inventory/gui/base/tab_storage.py ui/tab_storage.ui
start /b poetry run pyside6-uic -o inventory/gui/base/tab_suppliers.py ui/tab_suppliers.ui

start /b poetry run pyside6-uic -o inventory/gui/base/dialog_category.py ui/dialog_category.ui
start /b poetry run pyside6-uic -o inventory/gui/base/dialog_location_mapping.py ui/dialog_location_mapping.ui
start /b poetry run pyside6-uic -o inventory/gui/base/dialog_part.py ui/dialog_part.ui
start /b poetry run pyside6-uic -o inventory/gui/base/dialog_part_select.py ui/dialog_part_select.ui
start /b poetry run pyside6-uic -o inventory/gui/base/dialog_relocate.py ui/dialog_relocate.ui
start /b poetry run pyside6-uic -o inventory/gui/base/dialog_supplier.py ui/dialog_supplier.ui
start /b poetry run pyside6-uic -o inventory/gui/base/dialog_supplier_mapping.py ui/dialog_supplier_mapping.ui

start /b poetry run pyside6-uic -o inventory/gui/base/widget_areas.py ui/widget_areas.ui
start /b poetry run pyside6-uic -o inventory/gui/base/widget_attributes.py ui/widget_attributes.ui
start /b poetry run pyside6-uic -o inventory/gui/base/widget_location.py ui/widget_location.ui
start /b poetry run pyside6-uic -o inventory/gui/base/widget_parts.py ui/widget_parts.ui
start /b poetry run pyside6-uic -o inventory/gui/base/widget_projects.py ui/widget_projects.ui
start /b poetry run pyside6-uic -o inventory/gui/base/widget_revisions.py ui/widget_revisions.ui
start /b poetry run pyside6-uic -o inventory/gui/base/widget_slots.py ui/widget_slots.ui
start /b poetry run pyside6-uic -o inventory/gui/base/widget_suppliers.py ui/widget_suppliers.ui
