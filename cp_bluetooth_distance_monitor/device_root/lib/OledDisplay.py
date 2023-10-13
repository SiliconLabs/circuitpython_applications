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


class Display(SSD1306_I2C):
    def __init__(self, width, height, i2c, addr) -> None:
        self.status = False
        self.x_pos = 64
        super().__init__(width, height, i2c, addr=addr)

    def init_screen(self):
        self.fill(0)
        self.text("DISTANCE", 9, 0, 1)
        self.line(0, 10, 64, 10, 1)
        self.line(0, 36, 64, 36, 1)
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

    def display_out_of_range(self):
        self.fill_rect(0, 11, 64, 25, 0)
        self.text("OUT", 17, 14, 1)
        self.text("OF", 38, 14, 1)
        self.text("RANGE", 17, 24, 1)
        self.show()

    def display_no_data(self):
        self.fill_rect(0, 11, 64, 25, 0)
        string = "NO DATA"
        self.text(string, (64 - len(string) * 6 + 1) // 2, 19, 1)
        self.show()

    def display_distance(self, distance):
        self.fill_rect(0, 11, 64, 25, 0)
        string = "{} mm".format(distance)
        self.text(string, (64 - len(string) * 6 + 1) // 2, 19, 1)
        self.show()

    def scrolling_text(self, text):
        self.fill_rect(0, 40, 64, 8, 0)
        self.text(text, self.x_pos, 40, 1)
        self.show()
        self.x_pos = self.x_pos - 1
        if self.x_pos == -len(text) * 6 + 1:
            self.x_pos = 64

    def blink_text(self, text, y_pos):
        self.fill_rect(0, 40, 64, 8, 0)
        if self.status:
            self.fill_rect(0, 40, 64, 8, 0)
        else:
            self.text(text, ((64 - len(text) * 6 + 1) // 2), y_pos, 1)
        self.show()
        self.status = not self.status
