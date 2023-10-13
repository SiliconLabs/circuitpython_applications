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

from adafruit_as726x import AS726x_I2C
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement, Advertisement
from LightSensingService import LightSensingService

class SensorApp:
    def __init__(
        self,
        sensor: AS726x_I2C,
        service: LightSensingService,
        ble: BLERadio,
    ) -> None:
        print("Initialize application...")
        self.sensor = sensor
        self.service = service
        self.adv = ProvideServicesAdvertisement(self.service)
        self.ble = ble

    def main_function(self, *args, **kwargs) -> None:

        if not self.ble.connected and not self.ble.advertising:

            self.ble.start_advertising(self.adv)
            print(self.adv)
            print(
                f"Start advertising with a device name of '{self.adv.short_name}'..."
            )

        elif self.ble.connected and self.ble.advertising:

            self.ble.stop_advertising()
            print("Stop advertising...")
            print("Device connected...")

        if self.ble.connected and self.sensor.data_ready:

            print("Read sensor ---------------------")
            self.log_sensor_data()
            self.service.color_R = int(self.sensor.red)
            self.service.color_O = int(self.sensor.orange)
            self.service.color_Y = int(self.sensor.yellow)
            self.service.color_G = int(self.sensor.green)
            self.service.color_B = int(self.sensor.blue)
            self.service.color_V = int(self.sensor.violet)

    def configure_advertisement(self, device_name, connectable=True) -> None:
        self.adv.short_name = device_name
        self.adv.connectable = connectable
        print(
            f"Advertisement configured: '{self.adv.short_name}', connectable='{self.adv.connectable}'"
        )

    def log_sensor_data(self) -> None:
        print("red: " + str(self.sensor.red))
        print("orange: " + str(self.sensor.orange))
        print("yellow: " + str(self.sensor.yellow))
        print("green: " + str(self.sensor.green))
        print("blue: " + str(self.sensor.blue))
        print("violet " + str(int(self.sensor.violet)))