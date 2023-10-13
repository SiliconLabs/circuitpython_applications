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

import adafruit_si7021
import adafruit_is31fl3741
import time
import sensor
from LedMatrixBuffer import LedMatrixBuffer
from time import sleep

class SensorApp():        
    def __init__(self, i2c,) -> None:
        self.matrix = LedMatrixBuffer(i2c = i2c, address = 0x30)
        self.matrix.set_led_scaling(0x60)
        self.matrix.global_current = 0x05
        self.matrix.enable = True
        print("Init LED Matrix RGB")

        sensor.init(i2c)
        print("Init board sensor")
        
        self.text = 'Si'
        self.text_length_in_pixel = len(self.text) * 6 - 1
        self.screen_width = 13
        self.i = self.screen_width
        self.color = 0x06F8FF
        
        self.matrix.fill(0)
        self.matrix.text(self.text, 2, 2, self.color)
        self.matrix.show()
        
        print("Si")
        #Delay for user see the "Si" text
        sleep(3)
        

    def read_sensor_data_callback(self, *args, **kwargs) -> None:
        data_string = "{0:0.1f}{1:s}C-{2:02d}%".format(sensor.temperature(),
                                                       chr(0xF8),
                                                       int(sensor.humidity()))
        self.text = data_string
        self.text_length_in_pixel = len(self.text) * 6 - 1
        print(data_string)
        
        
    def display_callback(self, *args, **kwargs) -> None:
        # the text will start scrolling from the right side of the screen (13th pixel)
        # if the whole text passed through the screen, the text will roll back to the
        # 13th pixel
        self.matrix.fill(0)
        self.matrix.text(self.text, self.i, 0, self.color)
        self.i = self.i - 1
        if self.i == -self.text_length_in_pixel:
            self.i = self.screen_width
        self.matrix.show()
    
        
    def main_function(self) -> None:
        pass
        
    



