"""
*****************************************************************************
Copyright 2023 Silicon Laboratories Inc. www.silabs.com
*****************************************************************************
SPDX-License-Identifier: Zlib

The licensor of this software is Silicon Laboratories Inc.

This software is provided \'as-is\', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgment in the product documentation would be
   appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be
   misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.

*****************************************************************************
# EXPERIMENTAL QUALITY
This code has not been formally tested and is provided as-is. It is not
suitable for production environments. In addition, this code will not be
maintained and there may be no bug maintenance planned for these resources.
Silicon Labs may update projects from time to time.
******************************************************************************
"""

from adafruit_is31fl3741 import _IS3741_ADDR_DEFAULT, NO_BUFFER, IS3741_BGR
from adafruit_is31fl3741.adafruit_rgbmatrixqt import Adafruit_RGBMatrixQT
from adafruit_framebuf import BitmapFont

class LedMatrixBuffer(Adafruit_RGBMatrixQT):
    def __init__(self, i2c, address = _IS3741_ADDR_DEFAULT, allocate = NO_BUFFER, order = IS3741_BGR):
        super().__init__(i2c, address, allocate, order)
        self.rotation = 0
        self._pixel_buffer = bytearray(352)
        self._pixel_buffer[0] = 0
        self._font = None

    def pixel(self, x, y, color):
        if color is not None and 0 <= x < self.width and 0 <= y < self.height:
            addrs = self.pixel_addrs(x, y)
            self._pixel_buffer[1 + addrs[self.r_offset]] = (color >> 16) & 0xFF
            self._pixel_buffer[1 + addrs[self.g_offset]] = (color >> 8) & 0xFF
            self._pixel_buffer[1 + addrs[self.b_offset]] = color & 0xFF

    def fill_rect(self, x, y, width, height, color):
        for i in range(width):
            for j in range(height):
                self.pixel(x + i, y + j, color)

    def text(self, string, x, y, color, *, font_name="font5x8.bin", size=1):
        frame_width = self.width
        frame_height = self.height
        if self.rotation in (1, 3):
            frame_width, frame_height = frame_height, frame_width

        for chunk in string.split("\n"):
            if not self._font or self._font.font_name != font_name:
                # load the font!
                self._font = BitmapFont(font_name)
            width = self._font.font_width
            height = self._font.font_height
            for i, char in enumerate(chunk):
                char_x = x + (i * (width + 1)) * size
                if (
                    char_x + (width * size) > 0
                    and char_x < frame_width
                    and y + (height * size) > 0
                    and y < frame_height
                ):
                    self._font.draw_char(char, char_x, y, self, color, size=size)
            y += height * size

