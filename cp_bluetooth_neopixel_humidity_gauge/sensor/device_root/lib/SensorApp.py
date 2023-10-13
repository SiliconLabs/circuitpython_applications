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
import adafruit_shtc3
from time import monotonic
from adafruit_ble import BLERadio
from EnvSensingService import EnvironmentalSensingService
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement


class SensorApp():
   def __init__(self,
                service: EnvironmentalSensingService,
                ble: BLERadio, ) -> None:
      
      self.sht = adafruit_shtc3.SHTC3(board.I2C())
      self.service = service
      self.adv = ProvideServicesAdvertisement(service)
      self.ble = ble
      self.current_tick = 0


   def configure_advertisement(self,
                               device_name,
                               connectable = True) -> None:
      
      self.adv.short_name = device_name
      self.adv.connectable = connectable


   def main_function(self):
       
      temperature, relative_humidity = (0.0, 0.0)
      tick = monotonic()
      ble_send_data = 0
      
      if (tick - self.current_tick) >= 1:
         
         self.current_tick = tick
         temperature, relative_humidity = self.sht.measurements
         print("Temperature: %0.1f C" % temperature)
         print("Humidity: %0.1f %%" % relative_humidity)
         print("--------------------------------------")
         ble_send_data = int(relative_humidity * 100)

         
         if not self.ble.connected and not self.ble.advertising:
             print('>>> Start advertising')
             self.ble.start_advertising(self.adv)
            
         if self.ble.connected:
               if self.ble.advertising:
                  self.ble.stop_advertising()
                  print('>>> Connected, stop advertising')
                  
               self.service.humidity = (ble_send_data)
      



