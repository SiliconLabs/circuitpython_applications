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

from terminalio import FONT
from displayio import Bitmap, Palette, TileGrid, Group, FourWire, OnDiskBitmap
from adafruit_display_text import label
from adafruit_ili9341 import ILI9341
import board
import busio

WHITE_COLOR = 0xFFFFFF

CS = board.PB0
SCK = board.PC1
MISO = board.PC2
MOSI = board.PC3
DC = board.PB2

class TFTDisplay(ILI9341):
    def __init__(self,  width, height, **kwargs) -> None:
        spi = busio.SPI(clock = SCK, MISO = MISO, MOSI = MOSI)
        display_bus = FourWire(spi, command=DC, chip_select=CS, baudrate = 15000)
        super().__init__(display_bus, width = width, height = height)
        self.splash = Group()
        self.show(self.splash)

    def draw_text(self, text : str,  x : int,  y : int, scale = 1, color = WHITE_COLOR):
        text_area = label.Label(font = FONT, text = text, color = color, scale = scale)
        text_area.x = x
        text_area.y = y
        self.splash.append(text_area)

    def draw_vline(self, x : int, y: int, width : int, height: int, color = WHITE_COLOR) -> None:
        inner_bitmap = Bitmap(width, height, 1)
        inner_palette = Palette(1)
        inner_palette[0] = color
        inner_sprite = TileGrid(inner_bitmap, pixel_shader=inner_palette, x = x, y = y)
        self.splash.append(inner_sprite)

    def draw_image(self, file_name: str, x : int , y : int):
        image = OnDiskBitmap(file_name)
        tile_grid = TileGrid(image, pixel_shader = image.pixel_shader, x = x, y = y)
        self.splash.append(tile_grid)
