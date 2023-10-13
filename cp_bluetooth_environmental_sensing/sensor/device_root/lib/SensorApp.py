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
from adafruit_ccs811 import CCS811
from adafruit_bme280.basic import Adafruit_BME280_I2C 
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from EnvSensingService import EnvironmentalSensingService
from time import monotonic

class SensorApp():
   def __init__(
      self,
      temp_sensor: Adafruit_BME280_I2C,
      air_sensor: CCS811,
      service: EnvironmentalSensingService,
      ble: BLERadio,
   ) -> None:
      self.temp_sensor = temp_sensor,
      self.air_sensor = air_sensor,
      self.service = service
      self.adv = ProvideServicesAdvertisement(self.service)
      self.ble = ble
      self.current = 0

   def configure_advertisement(self, device_name, connectable = True) -> None:
      self.adv.short_name = device_name
      self.adv.connectable = connectable

   def main_function(self):
      if monotonic() - self.current >= 1:       
         if not self.ble.connected and not self.ble.advertising:
            print('start advertising')
            self.ble.start_advertising(self.adv)
         if self.ble.connected:
            if self.ble.advertising:
               self.ble.stop_advertising()
               print('connected, stop advertising')
            self.service.temperature = int(self.temp_sensor.temperature)
            self.service.humidity = int(self.temp_sensor.relative_humidity)
            self.service.tvoc = str(self.air_sensor.tvoc)
            self.service.co2 = str(self.air_sensor.eco2)
         self.current = monotonic()
