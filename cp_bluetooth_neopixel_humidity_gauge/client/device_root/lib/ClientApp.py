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
from time import monotonic
from adafruit_ble import BLERadio
from SleepTimer import SleepTimer
from NeoPixelDisplay import NeoPixel_Display
from EnvSensingService import EnvironmentalSensingService
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement


class ClientApp():
   def __init__(self) -> None:
      
      self.service = None
      self.connection = None
      self.ble = BLERadio()
      self.current_tick = 0
      self.appNeoPixel = NeoPixel_Display()
      self.ble_read_humidity = 0.0
      self.neopixel_trigger_blink = True
      SleepTimer.setup_timer(self.neopixel_control, 0.5)

   def neopixel_control(self, *args, **kwargs):
      if not self.ble.connected:
         if self.neopixel_trigger_blink:
            self.neopixel_trigger_blink = False
            self.appNeoPixel.fill_full_color()
         else:
            self.neopixel_trigger_blink = True
            self.appNeoPixel.clear()
      else:
         self.appNeoPixel.humidity_display(self.ble_read_humidity) 
         
         
   def main_function(self):
       
      SleepTimer.main_function()
      tick = monotonic()
      
      if (tick - self.current_tick) >= 1:
         
         self.current_tick = tick
         if not self.ble.connected:
            print('>>> Scanning sensor device...\r')
         
            for adv in self.ble.start_scan(ProvideServicesAdvertisement):
               if EnvironmentalSensingService in adv.services:
                  print('>>> Found sensor device !!!\r')
                  print('>>> Stop scanning sensor device\r')
                  self.ble.stop_scan()
                  self.connection = self.ble.connect(adv)
                  break
            
         if self.ble.connected:
               self.service = self.connection[EnvironmentalSensingService]
               self.ble_read_humidity = self.service.humidity / 100.0
               print(f"BLE read humidity = {self.ble_read_humidity}")
               

      








