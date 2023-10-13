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

from displayio import FourWire, Bitmap, Palette, TileGrid, Group
from adafruit_ili9341 import ILI9341
from adafruit_imageload import load
from adafruit_touchscreen import Touchscreen
from gc import collect
from time import sleep

DISPLAY_WIDTH = 320
DISPLAY_HEIGHT = 240

DRAW_PRESS = 18000
CLEAR_PRESS = 30000

class DrawApplication():
    def __init__(self,
                 spi,
                 DC,
                 CS,
                 XM,
                 XP,
                 YP,
                 YM                
    )->None:
        self.display_bus = FourWire(spi,
                                    command = DC,
                                    chip_select = CS)
        self.display = ILI9341(self.display_bus,
                               width = DISPLAY_WIDTH,
                               height = DISPLAY_HEIGHT)
        
        self.pen_color = 1       
        self.bitmap = Bitmap(DISPLAY_WIDTH, DISPLAY_HEIGHT, 6)      
        self.color_palette = Palette(6)
        self.color_palette[0] = 0x000000 # black
        self.color_palette[1] = 0xFF0000 # red
        self.color_palette[2] = 0x00FF00 # green
        self.color_palette[3] = 0x0000FF # blue
        self.color_palette[4] = 0xFFFF00 # yellow
        self.color_palette[5] = 0xFFFFFF # white
        
        self.screen = TileGrid(self.bitmap,
                               pixel_shader = self.color_palette,
                               x=0, y=0)
        self.group = Group()
        # init display
        self.group.append(self.screen)
        self.display.show(self.group)
        # touch screen
        self.touch_screen = Touchscreen(XM, XP, YP, YM,
                                        x_resistance = 280,
                                        calibration=((5000, 59000), (5000, 57000)),
                                        size=(DISPLAY_WIDTH, DISPLAY_HEIGHT))
    def show_start_up(self):
        
        # show Silabs big logo
        image, palette = load("silabs80.bmp")
        logo_silabs80 = TileGrid(image, pixel_shader = palette,
                                 x=80, y=60)
        self.group.append(logo_silabs80)

        image, palette = load("lib/cpython.bmp")
        logo_cpython = TileGrid(image, pixel_shader = palette,
                                x=180, y=140)
        self.group.append(logo_cpython)
        
        sleep(5)
        
        # delete unused to save memory space
        self.group.pop(self.group.index(logo_cpython))
        self.group.pop(self.group.index(logo_silabs80))
        collect()
        
    def show_color_palette(self):
        # draw color palette
        for i in range(90,120):
            for j in range(200,230):
                self.bitmap[i,j] = 1
        for i in range(120,150):
            for j in range(200,230):
                self.bitmap[i,j] = 2
        for i in range(150,180):
            for j in range(200,230):
                self.bitmap[i,j] = 3
        for i in range(180,210):
            for j in range(200,230):
                self.bitmap[i,j] = 4
        for i in range(210,240):
            for j in range(200,230):
                self.bitmap[i,j] = 5       
        
        # draw present color rectangle        
        for i in range(0,20):
            for j in range(0,20):
                self.bitmap[i,j] = self.pen_color
    
    def show_footer_logo(self):
        image, palette = load("cpython.bmp")
        logo_cpython = TileGrid(image, pixel_shader = palette,
                                x=0, y=200)
        self.group.append(logo_cpython)

        image, palette = load("silabs.bmp")
        logo_silabs = TileGrid(image, pixel_shader = palette,
                               x=240, y=200)
        self.group.append(logo_silabs)
        del(image)
        del(palette)
    
    def clear_screen(self):
        for i in range(0,320):
            for j in range(0,200):
                self.bitmap[i,j] = 0
    
    def show_pen_color(self):
        for i in range(0,20):
            for j in range(0,20):
                self.bitmap[i,j] = self.pen_color
                
    def touch_handle(self, point):
        x = point[0] 
        y = point[1]
        if (y>210):
            if (x<90+30):
                self.pen_color = 1 
            elif (x<90+2*30):
                self.pen_color = 2
            elif (x<90+3*30):
                self.pen_color = 3 
            elif (x<90+4*30):
                self.pen_color = 4  
            elif (x<90+5*30):
                self.pen_color = 5
            self.show_pen_color()  
        else:
            self.bitmap[x,y] = self.pen_color
            
    def main_function(self):
        point = self.touch_screen.touch_point
        if(point):
            if(point[0]>280 and point[1]>210 and point[2]>CLEAR_PRESS):
                self.clear_screen()
            elif(point[2]>DRAW_PRESS):
                self.touch_handle(point)
