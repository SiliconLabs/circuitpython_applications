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
import neopixel_spi as neopixel


# Update this to match the number of LEDs.
NUMPIXELS_DEFAULT = 15 

#start pixel position of each color on neopixel
pixel_offset=[0, 2, 4, 6, 9, 12]

#number pixels present for each color from start position
num_pixel_by_color = [2, 2, 2, 3, 3, 3]

#color code in rgb
rgb_code = [
    [255, 0, 0], #red
    [242, 140, 4], #orange
    [255, 255, 0], #yellow
    [0, 255, 0], #green
    [0, 0, 255], #blue
    [255, 0, 255], #violet
]

class Display(neopixel.NeoPixel_SPI):
    def __init__(self, spi, brightness) -> None:
        super().__init__(spi, NUMPIXELS_DEFAULT, brightness=brightness, bpp=4, auto_write=False)

    def fill_color(self, color):
        self.fill(color)
        self.show()

    def clear(self):
        self.fill(0x00)
        self.show()

    def draw_pixels(self, num_pixel:int, position:int, intensity:int, rgb_code:list):
        color = int(intensity*rgb_code[0]/255)<<16 | int(intensity*rgb_code[1]/255)<<8 | int(intensity*rgb_code[2]/255) 
        for i in range(num_pixel):
            self[i+position] = color
            self.show()

    def draw_LightSensingData(self, data_channel:list):
        for color in range(6):
            intensity = data_channel[color]/10000*255
            self.draw_pixels(num_pixel_by_color[color],
                             pixel_offset[color],
                             intensity,
                             rgb_code[color])



