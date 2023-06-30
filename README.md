Inventory
========================================================================================================================
There have been many version os an inventory management system for my collection of electronic components.  I continue to strive to build something that ticks all of the boxes and the result has been a multitude of tools that all barely do anything.  At this point, I just need a functional tool to start cataloging parts that are seriously piling up.

The primary purpose of this tool is to allow me to catalog all of the electronic components that I have on hand.


This tool must:

- Support generating/printing labels for storage location using my Dymo printer.
- Support scanning location barcodes to pull up parts.
- Easily increment/decrement inventory numbers using GUI.

The tool should:

- Connect parts to their storage location(s), so that I can find them.
- Link to their supplier(s).
- Link to the project(s) that use the part so I can cross reference.
- Support categories in a tree form with linkage to a single part.
- Support browsing parts by: location, category, supplier, project.
- Allow me to count parts using my USB scale.
- Allow me to calibrate part weight using USB scale.
- Include a wizard to handle periodically checking inventory for parts.
- Support a reorder-report - show a list of parts whose quantities are LESS than their reorder threshold.
    - Consider including a tolerance such that parts that are getting close to the threshold can be viewed too.
        - Don't show any parts with a `threshold` of zero - they are non-stocked.

The tool could:

- Provide a representative picture of the part.
- Store the datasheet and supporting docs (design whitepapers, drawings, etc.)
- Easily decrement multiple parts when a project is build, using a stored BOM for the project.
    - Can BOMs be imported from .md files?
- Export HTML report of parts that can be used to lookup parts.  Read-only doc to publish to parts.exsystems.net.




Why another version of this tool?
------------------------------------------------------------------------------------------------------------------------
This tool was originally a web application but has hit a bit of a development wall as the complexity and scope has increased.  I have attempted to solve the problem by building Qt based supplements and even switching frameworks on the wab side (Angular), all of which are sitting in a state of limbo.

I then considered building a REST API for the web interface to support using multiple tools but ultimately decided that a standalone tool might actually be better.
