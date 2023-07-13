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
import board
import busio
import neopixel_spi as neopixel


# Update this to match the number of LEDs.
NUMPIXELS_DEFAULT = 12 

# A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
BRIGHTNESS_DEFAULT = 0.1 

# This is the data out pin NeoPixel connect to host
DATA_PIN = board.PD0 

# Set the pixel color channel order
ORDER = neopixel.GRB 

COLORS_PALETTE = (0x00eaff, 0x00e5e4, 0x00dfc2, 0x00d79c, 0x40cd72, 0x67c145, 
                  0x85b400, 0xa1a300, 0xbc8f00, 0xd67600, 0xed5300, 0xff0000 )

class NeoPixel_Display():
    
    def __init__(self) -> None:
        
        _spi = busio.SPI(clock = board.SCK, MOSI = DATA_PIN, MISO = board.MISO)
       
        self.pixels = neopixel.NeoPixel_SPI(
            spi = _spi, 
            n = NUMPIXELS_DEFAULT,
            brightness = BRIGHTNESS_DEFAULT,
            auto_write = False,
            pixel_order = ORDER
        )
        
    def fill_full_color(self):
        for i in range (0, len(COLORS_PALETTE)):
            self.pixels[i] = COLORS_PALETTE[i]
        
        self.pixels.show()
        
    def clear(self):
        self.pixels.fill(0)
        self.pixels.show()
        
    def humidity_display(self, humidity):
        
        index_display = humidity / 8;
        if humidity % 8 != 0:
            index_display += 1
            
        if index_display > (len(COLORS_PALETTE) - 1):
           index_display =  len(COLORS_PALETTE) - 1
           
        self.pixels.fill(0)
        for i in range(0, int(index_display)):
            self.pixels[i] = COLORS_PALETTE[i]
    
        self.pixels.show()


