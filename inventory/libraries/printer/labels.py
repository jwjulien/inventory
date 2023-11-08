# ======================================================================================================================
#      File:  /inventory/libraries/printer/labels.py
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
"""Support for various label sizes to be printed."""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from PIL import Image, ImageDraw, ImageFont

from inventory.libraries.printer.printers import Printer



# ======================================================================================================================
# Label Base Class
# ----------------------------------------------------------------------------------------------------------------------
class Label:
    """Composer to assist with creating bitmap labels and printing them using a Dymo LabelWriter printer.

    Examples:
        To create a label and preview it:
            # Create a new label - this is a Dymo 30346 1/2" x 1-7/8" return address label.
            label = Label(1.875, 0.5)

            # Insert a 2D barcode.
            text = 'Aztec Code 2D :)'
            aztec_code = AztecCode(text)
            aztec = aztec_code.image()
            aztec = aztec.resize((label.height, label.height))
            label.blit(0, 0, aztec)

            # Populate with some text.
            label.set_font('calibri', 22)
            label.text(aztec.width + 20, 10, '5k Resistor')
            label.text(aztec.width + 20, 40, 'ID: 12345')
            label.text(aztec.width + 20, 70, '71-CRCW06035K00FKEA')
            label.text(aztec.width + 20, 100, 'Package: 0603')

            # Show it without printing so we can see what it will look like.
            label.preview()

        When ready to print:
            printer = LabelWriter450()
            label.print(printer)
    """
    # These margins have been optimized to provide the maximum, symmetric printable area.
    SideMargin_in = 0.2175 # in
    TopMargin_in = 0.03125 # in

    # Dymo printers offer a "graphics mode" which is 300x600 DPI, but that is ignored in this implementation to keep
    # things symmetrical.
    Dpi = 300

    def __init__(self, width_in: float, height_in: float):
        # Convert width/height inputs from inches to pixels/DPI and scale down for margins.
        self.width = int((self.Dpi * (width_in - (self.SideMargin_in * 2))) + 0.5)
        self.height = int((self.Dpi * (height_in - (self.TopMargin_in * 2))) + 0.5)

        # Generate a canvas to draw on that is the same size as the label printable area.  This will be manipulated to
        # best suit the printer when the print method is called later.
        self._canvas = Image.new('1', (self.width, self.height), 1)
        self._draw = ImageDraw.Draw(self._canvas)

        # Set a default font to get started - change using the `set_font` method, if needed.
        self._font = ImageFont.truetype('arial', size=12)


# ----------------------------------------------------------------------------------------------------------------------
    def set_font(self, font: str, size: int = 12) -> None:
        """Set the font to be used with future calls to the `text` method.

        The font set using this method is saved and will be used for all calls to `text` until `set_font` is called
        again.

        Arguments:
            font: The name or path to a TrueType font to be used.  Can be a system font or an absolute or relative path
                to an .ttf font file.
            size: Size of the font in px - default is 12 points.
        """
        self._font = ImageFont.truetype(font, size=size)


# ----------------------------------------------------------------------------------------------------------------------
    def text(self, x: int, y: int, text: str):
        """Insert text into the label at the specified position using the stored font.

        The text is always left aligned in this implementation.

        To change the font, use the `set_font` method.

        Arguments:
            x: Horizontal offset to the left edge of the text.
            y: Vertical offset to the top edge of the text.
            text: Text to be placed on the label.
        """
        self._draw.text((x, y), text, font=self._font)


# ----------------------------------------------------------------------------------------------------------------------
    def blit(self, x: int, y: int, image: Image) -> None:
        """Copy the provided Image into this label.

        The provided image should be resized appropriately  before calling this method.

        Arguments:
            x: Horizontal offset to the left edge of the image on the label, in units of pixels.
            y: Vertical offset to the top edge of the image on the label, in units of pixels.
            image: A PIL Image instance to be pasted into the label at the specified coordinates.
        """
        self._canvas.paste(image, (x, y))


# ----------------------------------------------------------------------------------------------------------------------
    def _prep_document(self, printer: Printer) -> Image:
        """Prepare a "document" image to be printed."""
        # Define a new canvas that is the full printer width by label height (remember: rotated).
        full = Image.new('1', (printer.bit_width, self.width), 1)

        # Rotate the label 90 degrees (they are printed sideways on the Dymo) and paste into new canvas.
        rotated = self._canvas.rotate(90, expand=True)
        full.paste(rotated, (0, 0))

        return full


# ----------------------------------------------------------------------------------------------------------------------
    def image(self) -> Image:
        """Return the PIL Image that represents this Label."""
        return self._canvas


# ----------------------------------------------------------------------------------------------------------------------
    def preview(self) -> None:
        """For debugging.  Preview this label."""
        self._canvas.show()


# ----------------------------------------------------------------------------------------------------------------------
    def print_preview(self, printer: Printer) -> None:
        """For debugging.  Preview this label as it would be printed on `printer`."""
        self._prep_document(printer).show()


# ----------------------------------------------------------------------------------------------------------------------
    def print(self, printer: Printer) -> None:
        """Print this label on the passed `printer`.

        Arguments:
            An instance of the Printer class upon which this label shall be printed.
        """
        document = self._prep_document(printer)
        data = document.tobytes()

        # Loop through each line in the label.
        for row in range(document.height):
            # Get a single row of data.
            index = row * printer.byte_width
            line = data[index:index + printer.byte_width]

            # Pad the line out to the required width with white space, if needed.
            while len(line) < printer.byte_width:
                line += b'\x00'

            # Send this line to the printer.
            printer.print_line(line)

        # Feed label to cut line.
        printer.form_feed()




# ======================================================================================================================
# Dymo Label Classes
# ----------------------------------------------------------------------------------------------------------------------
# The following are just convenience methods that map various Dymo labels to proper Label sizes.
def Dymo30346():
    """1/2" x 1-7/8" "return address" labels."""
    return Label(width_in=1.875, height_in=0.5)


# ----------------------------------------------------------------------------------------------------------------------
def Dymo30332():
    """1" x 1" "multipurpose" labels."""
    return Label(width_in=1.0, height_in=1.0)


# ----------------------------------------------------------------------------------------------------------------------
def Dymo30323():
    """2-1/8" x 4" "shipping/name badge" labels."""
    return Label(width_in=4, height_in=2.125)




# End of File
