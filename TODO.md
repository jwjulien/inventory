- Miscellaneous:
    - [ ] Make scanner actually search for what it scans.
    - [ ] Setup printer with tab to handle printing labels:
        - [ ] For storage locations.
    - [x] Setup scale:
        - [x] Bring in library from other Python kiosk.
        - [x] Setup dialog to handle calibrating part weight.
        - [x] Setup dialog for counting parts by weight.
            - [x] Include option to tare drawer weight.
    - [ ] Setup configuration storage:
        - [ ] Drawer tare weight.
        - [ ] Scanner VID/PID.
        - [ ] Database location.
        - [ ] File store location.
- Parts:
    - [x] Change attributes to allow capital letters.
    - [x] Support datasheets and technical drawings.
        - [x] Documents should be n:n w/ Parts - some Parts may share Documents.
    - [ ] Support part images.
    - [x] Support adding new categories from the parts dialog.
    - [x] When adding parts, get attributes from the same category and offer them as suggestions.
    - [x] Modify parts dialog [Save] to be [Apply] and [Ok] to allow saving.
        - [x] Don't allow locations/suppliers/projects to be added to new parts until saved (as no ID throws error).
    - [ ] Add ability to delete a part.
    - [ ] Perform validation on part before accepting [Save] or [Apply] from the PartDialog.
    - [ ] Disable the [Apply] and [Save] buttons in the PartsDialog until a change has been made.
- Storage:
    - [ ] Give ability to move a slot to a new location/unit.
        - [ ] Ensure that the ID is preserved as that is what is tied to the barcodes.
    - [ ] Give ability to move a part to a new slot.
    - [ ] Highlight slots without any parts assigned.
    - [ ] Give ability to add/remove columns/rows in slots widget - context menu?
    - [ ] Rework storage tab:
        - [ ] Make parts load on demand or only for slots.  They are very slow to load for areas with lots of parts.
        - [ ] Give slots more screen space.  The splitter is nice, but bigger units with long slot names still require scrolling.  I think it might be nice to collapse the areas and units, breadcrumb style.
    - [ ] In LocationMappingDialog, consider swapping the lengthy dropdown for a column view or some kinda of filter/autocomplete.
- Projects:
    - [ ] Update the part matching on BOM import to better match attributes with weighting for things like package and part number over category (as opposed to either summery vs part number matching as it's done now).
    - [ ] In project BOM view:
        - [ ] Allow remapping a part for a given designator.
        - [ ] Support a custom context menu for removing a Material and remapping a part.
- New tabs/features:
    - [ ] A feature to view parts from a supplier that are single-sourced (with quantities visible).
        - Such that when looking to fill up an order with a supplier, with whom I place infrequent orders, it might be easy to find additional items to stock up on or to tip over the free shipping threshold.