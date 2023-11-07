# ======================================================================================================================
#      File:  /inventory/libraries/printers/printer.py
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
"""Support for the Dymo LabelWriter 450 in pure Python with PyUSB as the interface.

This class came about because support for the Dymo LabelWriter printers from Windows is a bit flaky.  We needed the
ability to print custom labels directly from the inventory software and there were no libraries available to do that.

This implementation was reverse engineered from the [Dymo Technical Reference]
(docs\reference\Dymo_LabelWriter_450Series_TechnicalReference.pdf) using libusb0 and PyUSB to send raw read/write
commands directly to the bulk OUT/IN endpoints.  As it turns out, the protocols for communicating with printers aren't
all that complicated.

There are a number of commands associated with configuring the printer and feeding the label to cut but the real meat
and potatoes is the `print_line` method which takes a `bytes` array corresponding to the pixels for one row of bitmap
data.  These rows are then repeated to build a bitmap image on the label.

This class does not handle label width or height.  The Dymo can print all sorts of different label sizes and it is the
responsibility of the user to handle the proper widths and line counts.  For this project that is handled in the Label
class, defined in [[inventory/libraries/printer/labels]].
"""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
from enum import Enum

import usb




# ======================================================================================================================
# Exceptions
# ----------------------------------------------------------------------------------------------------------------------
class PrinterError(Exception):
    """Parent for all other printer errors."""


# ----------------------------------------------------------------------------------------------------------------------
class PrinterNotFound(PrinterError):
    """Raised when a LabelWriter 450 couldn't be found.

    This may be the result of a driver error.  Please use Zadig (et. al.) to install the libusb0 drivers in place of
    the standard printer drivers for your Dymo device.  This library requires the use of this non-standard drivers to
    allow PyUSB to access and control the device instead.
    """


# ----------------------------------------------------------------------------------------------------------------------
class PrinterNotReady(PrinterError):
    """Raised when the printer status indicated it is not ready to accept prints."""




# ======================================================================================================================
# Constants
# ----------------------------------------------------------------------------------------------------------------------
ESC = b'\x1b'
SYN = b'\x16'




# ======================================================================================================================
# Enumerations
# ----------------------------------------------------------------------------------------------------------------------
class PrintDensity(Enum):
    Light = b'c'
    Medium = b'd'
    Normal = b'e'
    Dark = b'g'




# ======================================================================================================================
# Printer Base Class
# ----------------------------------------------------------------------------------------------------------------------
class Printer:
    def __init__(self):
        self._device = usb.core.find(idVendor=self.VID, idProduct=self.PID)
        if not self._device:
            raise PrinterNotFound

        self._device.set_configuration()
        self._device.reset()




# ======================================================================================================================
# Label Writer 450 Printer Class
# ----------------------------------------------------------------------------------------------------------------------
class LabelWriter450(Printer):
    """Interface to a Dymo LabelWriter 450 via USB using libusb to raw/write raw data."""
    # This class may work with others too, YMMV.
    VID = 0x0922 # Dymo
    PID = 0x0020 # LabelWriter 450

    OUT_EP = 0x02
    IN_EP = 0x82

    TIMEOUT = 50 # ms

    def __init__(self):
        super().__init__()
        self.reset()
        if self.status() != 3:
            raise PrinterNotReady

        # The printer default is 84 bytes of data equating to the entire width of the printer.
        self.bit_width = 84 * 8


# ----------------------------------------------------------------------------------------------------------------------
    @property
    def byte_width(self) -> int:
        """Return the number of bytes needed to represent the bit width set using `set_width`.

        This value is rounded up to the next integer number of bytes that can contain at least the number of bits that
        were previously set using the
        """
        return (self.bit_width + 7) // 8


# ----------------------------------------------------------------------------------------------------------------------
    def reset(self) -> None:
        """Send a reset request to the printer.

        This command resets the dot tabs, line tabs, bytes per line, and so on to their default values and sets
        top-of-form as true.
        """
        self._device.write(self.OUT_EP, ESC + b'@', self.TIMEOUT)


# ----------------------------------------------------------------------------------------------------------------------
    def status(self) -> int:
        """Read and return the printer status.

        Returns:
            The status byte from the printer as an int.  A value of "3" means the printer is ready to accept commands.
        """
        self._device.write(self.OUT_EP, ESC + b'A', self.TIMEOUT)
        return int(self._device.read(self.IN_EP, 1, self.TIMEOUT)[0])


# ----------------------------------------------------------------------------------------------------------------------
    def set_width(self, pixels: int) -> int:
        """Set the width of the label in pixels.

        The printer expects an integer number of bytes of pixel data related to this value when printing lines.

        Note: This "width" is typically more the "height" of a label as most Dymo labels go through the printer
        sideways.

        Arguments:
            pixels: The horizontal width of the printed area in pixels.

        Raises:
            ValueError: If `pixels` is not within the range [1, 672] pixels.
        """
        if not 0 < pixels <= (84 * 8):
            raise ValueError('Pixel width must be in range [1, 672]')
        self.bit_width = pixels
        self.set_bytes_per_line(self.byte_width)


# ----------------------------------------------------------------------------------------------------------------------
    def set_bytes_per_line(self, count: int):
        """Tell the printer how many bytes to expect per line when printing.

        The default is 84 bytes x 8 bits = 672 pixels.  This corresponds to the width across the print head and not all
        label are wide enough to take advantage of all of the pixels.  Ergo, it makes more sense to tailor this width to
        suit the label."""
        self._device.write(self.OUT_EP, ESC + b'D' + bytes([count]))


# ----------------------------------------------------------------------------------------------------------------------
    def form_feed(self) -> None:
        """Feed the label to a point where it's ready to tear."""
        self._device.write(self.OUT_EP, ESC + b'E', self.TIMEOUT)


# ----------------------------------------------------------------------------------------------------------------------
    def short_form_feed(self) -> None:
        """Feed the label to start the next.

        Use this command to advance to the next label if you plan to print another.  This helps save a little time.
        """
        self._device.write(self.OUT_EP, ESC + b'G', self.TIMEOUT)


# ----------------------------------------------------------------------------------------------------------------------
    def text_speed_mode(self) -> None:
        """Instructs the printer to print in text quality mode (300x300 dpi)."""
        self._device.write(self.OUT_EP, ESC + b'h', self.TIMEOUT)


# ----------------------------------------------------------------------------------------------------------------------
    def graphics_speed_mode(self) -> None:
        """Instructs the printer to print in graphics quality mode (300x600 dpi)."""
        self._device.write(self.OUT_EP, ESC + b'i', self.TIMEOUT)


# ----------------------------------------------------------------------------------------------------------------------
    def set_print_density(self, density: PrintDensity) -> None:
        """Set the print density to one of the specified levels."""
        self._device.write(self.OUT_EP, ESC + density.value)


# ----------------------------------------------------------------------------------------------------------------------
    def print_line(self, pixels: bytes) -> None:
        """Print a single line of pixels on the label.

        The number of bytes provided as the `pixels` argument must match the byte_width for the printer or a ValueError
        will be thrown.  If your label is smaller than the full width of the printer, use the `set_width` method to
        reduce the width.
        """
        if len(pixels) != self.byte_width:
            raise ValueError('set pixel count using `set_width` if less than 84 bytes')
        pixels = bytes([~b & 0xFF for b in pixels])
        self._device.write(self.OUT_EP, SYN + pixels)




# End of File
