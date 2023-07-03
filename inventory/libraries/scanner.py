# ======================================================================================================================
#      File:  /inventory/libraries/scanner.py
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
"""Support for connecting directly to a USB barcode scanner.

Scanner typically emulate a keyboard device but for this application we would rather monitor for scans in the background
when on any tab.

Note: This implementation was developed for Windows and needs a [libusb filter driver](
https://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.6.0/) to be installed for the barcode
scanner of interest.  Otherwise, the scanner will appear as an HID keyboard device (as they are really designed) and
will not be found by the ScannerWorked class, resulting in the printed warning.


Inspiration originally taken from [Adafruit's LS2208 USB Barcode Scanner](
https://github.com/adafruit/LS2208-USB-Barcode-Scanner/blob/master/HID.py) but that turned out to be pretty old (Python
2.x).

Ultimately switched to [PyUSB](
https://stackoverflow.com/questions/37134686/how-can-i-get-raw-usb-keyboard-data-with-python) when the aforementioned
Adafruit example didn't work.

HID decoding help pulled from [this Gist](https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2).

Help with threading from [Python GUIs](
https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/).
"""

# ======================================================================================================================
# Imports
# ----------------------------------------------------------------------------------------------------------------------
import usb.core
import usb.util


from PySide6 import QtCore




# ======================================================================================================================
# Scanner Worker Class
# ----------------------------------------------------------------------------------------------------------------------
class ScannerWorker(QtCore.QObject, QtCore.QRunnable):
    """This worker can be started and added to the application thread pool and will process requests from a USB barcode
    scanner in the background.  Received messages are emitted via the `received` signal.

    Signals:
        received: Emits the received string from the barcode scanner each time a carriage return is received.
    """
    received = QtCore.Signal(str)

    def __init__(self, vid: int, pid: int):
        QtCore.QObject.__init__(self)
        QtCore.QRunnable.__init__(self)

        self._running = False

        self.device = usb.core.find(idVendor=vid, idProduct=pid)
        if self.device:
            self._running = True

            self.device.set_configuration()

            # TODO: This seems kinda hacky to always assume descriptor/endpoint zero?
            self.endpoint = self.device[0][(0, 0)][0]
        else:
            print(f'Unable to locate USB scanner with VID 0x{vid:04X} and PID 0x{pid:04X}, scanner service not started')


# ----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _decode(data: bytes) -> str:
        """Decode an HID report into the key press it simulates.

        The USB scanner emulates a keyboard HID device and as such, the format of data matches.  The first byte is
        the modifier(s) and the third byte is the key code.  The lookup table below is ued to perform the translation.

        Arguments:
            data: Raw bytes of data received from the HID device.

        Returns:
            A single character decided from the data or an empty string if no "key" was pressed (a common occurrence in
            the world of HID devices).
        """
        KeyCodes = {
            0x04: ('a', 'A'),
            0x05: ('b', 'B'),
            0x06: ('c', 'C'),
            0x07: ('d', 'D'),
            0x08: ('e', 'E'),
            0x09: ('f', 'F'),
            0x0A: ('g', 'G'),
            0x0B: ('h', 'H'),
            0x0C: ('i', 'I'),
            0x0D: ('j', 'J'),
            0x0E: ('k', 'K'),
            0x0F: ('l', 'L'),
            0x10: ('m', 'M'),
            0x11: ('n', 'N'),
            0x12: ('o', 'O'),
            0x13: ('p', 'P'),
            0x14: ('q', 'Q'),
            0x15: ('r', 'R'),
            0x16: ('s', 'S'),
            0x17: ('t', 'T'),
            0x18: ('u', 'U'),
            0x19: ('v', 'V'),
            0x1A: ('w', 'W'),
            0x1B: ('x', 'X'),
            0x1C: ('y', 'Y'),
            0x1D: ('z', 'Z'),
            0x1E: ('1', '!'),
            0x1F: ('2', '@'),
            0x20: ('3', '#'),
            0x21: ('4', '$'),
            0x22: ('5', '%'),
            0x23: ('6', '^'),
            0x24: ('7', '&'),
            0x25: ('8', '*'),
            0x26: ('9', '('),
            0x27: ('0', ')'),
            0x28: ('\n','\n'),
            0x29: ('\nEscape\n', '\nEscape\n'),
            0x2A: ('\nDelete\n','\nDelete\n'),
            0x2B: ('\t','\t'),
            0x2C: (' ', ' '),
            0x2D: ('-', '_'),
            0x2E: ('=', '+'),
            0x2F: ('[', '{'),
            0x30: (']', '}'),
            0x31: ('\\', '|'),
            0x32: ('#','~'),
            0x33: (';', ':'),
            0x34: ('\'', '"'),
            0x35: ('`', '~'),
            0x36: (',', '<'),
            0x37: ('.', '>'),
            0x38: ('/', '?'),
            # 0x39: Capslock
            0x3A: ('F1', 'F1'),
            0x3B: ('F2', 'F2'),
            0x3C: ('F3', 'F3'),
            0x3D: ('F4', 'F4'),
            0x3E: ('F5', 'F5'),
            0x3F: ('F6', 'F6'),
            0x40: ('F7', 'F7'),
            0x41: ('F8', 'F8'),
            0x42: ('F9', 'F9'),
            0x43: ('F10', 'F10'),
            0x44: ('F11', 'F11'),
            0x45: ('F12', 'F12'),
            0x49: ('\nInsert\n', '\nInsert\n'),
            0x4A: ('\nHome\n', '\nHome\n'),
            0x4B: ('\nPageUp\n','\nPageUp\n'),
            0x4C: ('\nFwdDelete\n', '\nFwdDelete\n'),
            0x4D: ('\nEnd\n','\nEnd\n'),
            0x4E: ('\nPageDown\n','\nPageDown\n'),
            0x4F: (u'→',u'→'),
            0x50: (u'←',u'←'),
            0x51: (u'↓',u'↓'),
            0x52: (u'↑',u'↑')
        }

        shift = int(bool(data[0] & 0x22))
        key = int(data[2])

        if key == 0:
            return ''

        return KeyCodes[key][shift]


# ----------------------------------------------------------------------------------------------------------------------
    def stop(self):
        """Terminate this thread and stop receiving messages."""
        self._running = False


# ----------------------------------------------------------------------------------------------------------------------
    @QtCore.Slot()
    def run(self):
        string = ''
        while self._running:
            try:
                data = self.device.read(self.endpoint.bEndpointAddress, self.endpoint.wMaxPacketSize).tobytes()
            except usb.core.USBError as error:
                if error.errno is None:
                    continue

            char = self._decode(data)
            if char == '\n':
                self.received.emit(string)
                string = ''
            else:
                string += char




# End of File
