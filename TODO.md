- Miscellaneous:
    - [x] Make scanner actually search for what it scans.
    - [x] Setup printer with dialog to handle printing labels:
        - [x] For storage locations.
        - [x] Develop better scheme using 1" labels and some flavor of 2D barcode.
    - [x] Setup scale:
        - [x] Bring in library from other Python kiosk.
        - [x] Setup dialog to handle calibrating part weight.
        - [x] Setup dialog for counting parts by weight.
            - [x] Include option to tare drawer weight.
        - [x] What happens when no scale is connected?
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
    - [ ] Change the Location Widget from side buttons to context menu.
    - [ ] Attributes do strange things when adding second, third, etc.
    - [x] Add URL fetch for part images to allow getting them from Mouser...
        - [x] Is it possible to support drag and drop from the internets?
    - [x] Add a drag/drop for documents that matches what I just did for Part images!
    - [ ] Is there a way to paginate/lazy load Parts such that they are only loaded from DB as needed?
- Storage:
    - [x] Give ability to move a slot to a new location/unit.
        - Cut/paste doesn't work because `remove` isn't supported when parts are assigned to Location.
        - [x] Ensure that the ID is preserved as that is what is tied to the barcodes.
    - [x] Give ability to move a part to a new slot.
        - [ ] Add ability to define new Slot from Relocate Dialog.
        - [ ] Switch lengthy dropdown to tree or alternate widget.
            - [ ] What about adding a custom widget for selecting/adding a slot (to be shared with location_mapping)?
    - [x] Highlight slots without any parts assigned.
    - [-] Give ability to add/remove columns/rows in slots widget - context menu?
        - This can already be done from this Unit table.
    - [x] Rework storage tab:
        - [x] Make parts load on demand or only for slots.  They are very slow to load for areas with lots of parts.
        - [x] Give slots more screen space.  Big units with long slot names require scrolling.
        - [x] Does it make more sense to migrate Areas, Slots, etc. to dialogs instead of widgets?
            - Should help with loading times and make more reusable.
            - What about putting widgets into dialogs to make the best of both?
    - [x] In LocationMappingDialog, swap the lengthy dropdown for a column view or some kinda of filter/autocomplete.
    - [x] Support cut/copy/paste for Slots within table view - will help with relocating.
- Projects:
    - [ ] Update the part matching on BOM import to better match attributes with weighting for things like package and part number over category (as opposed to either summery vs part number matching as it's done now).
    - [ ] In project BOM view:
        - [ ] Allow remapping a part for a given designator.
        - [ ] Support a custom context menu for removing a Material and remapping a part.
    - [x] Use the modified time from the BOM file to set the revision date on BOM import.
    - [ ] Add option to filter existing entries from BOM import (for updates/re-import).
- New tabs/features:
    - [ ] A feature to view parts from a supplier that are single-sourced (with quantities visible).
        - Such that when looking to fill up an order with a supplier, with whom I place infrequent orders, it might be easy to find additional items to stock up on or to tip over the free shipping threshold.
    - [x] Need to refresh parts when switching tabs.
    - [x] Setup filename widget to allow drag and drop of files from Explorer.
        - [x] Lazy load them too, then.
