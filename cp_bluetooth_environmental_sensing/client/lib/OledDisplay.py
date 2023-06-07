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
from adafruit_ssd1306 import SSD1306_I2C
import adafruit_framebuf

class OledDisplay(SSD1306_I2C):
    def __init__(self ,width, height, i2c, addr) -> None:
        super().__init__(width, height, i2c, addr = addr)

    def init_screen(self):
        self.fill(0)
        self.text('ENVIRONMENT', 5, 0, 1, font_name = 'font4x6.bin')
        self.line(0, 7, 64, 7, 1)
        self.line(0, 28, 64, 28, 1)
        self.show()

    def draw_xbitmap(self, x, y, w, h, bitmap):
        byteWidth = (w + 7) // 8
        b = 0
        for j in range(h):
            for i in range(w):
                if i & 7:
                    b >>= 1
                else:
                    b = bitmap[j * byteWidth + i // 8]
                if b & 0x01:
                    self.pixel(x + i, y, 1)
            y += 1
        self.show()

    def disconnected_display(self):
        self.rect(0, 8, 64, 20, 0, fill = True)
        self.rect(0, 29, 64, 19, 0, fill = True)
        self.text('-- {char:s}C'.format(char = chr(0xF8)), 15, 10, 1)
        self.text('-- %', 15, 19, 1)
        self.text('-- ppm', 15, 31, 1)
        self.text("-- ppm", 15, 40, 1)
        self.show()

    def display_data(self, data: list[int, int, int, int]):
        self.rect(0, 8, 64, 20, 0, fill = True)
        self.rect(0, 29, 64, 19, 0, fill = True)
        self.text("{0:3d} {1:s}C".format(data[0], chr(0xF8)), 14, 10, 1)
        self.text("{0:3d} %".format(data[1]), 14, 19, 1)
        self.text("{0:4d} ppm".format(data[2]), 8, 31, 1)
        self.text("{0:4d} ppm".format(data[3]), 8, 40, 1)
        self.show()
