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

from time import monotonic
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from LightSensingService import LightSensingService
from NeoPixelDisplay import Display

class ClientApp:
    def __init__(
        self,
        display: Display,
        ble: BLERadio,
    ) -> None:
        print("Initialize application...")
        self.display = display
        self.ble = ble
        self.connection = None
        self.service = None
        self.sensor_data = None
        self.current = 0
        self.display.clear()
        self.display.fill_color(0xffffff)

    def main_function(self, *args, **kwargs) -> None:
        if monotonic() - self.current >= 0.5:
            if not self.ble.connected:
                print("start scanning...")
                for adv in self.ble.start_scan(ProvideServicesAdvertisement):
                    if  LightSensingService in adv.services:
                        print("sensor device found.")
                        self.ble.stop_scan()
                        self.connection = self.ble.connect(adv)
            elif self.ble.connected:
                self.service = self.connection[LightSensingService]
                self.sensor_data = [
                    int(self.service.color_R),
                    int(self.service.color_O),
                    int(self.service.color_Y),
                    int(self.service.color_G),
                    int(self.service.color_B),
                    int(self.service.color_V),
                ]
                print("Updating data from sensor device.")
                self.display.draw_LightSensingData(self.sensor_data)
            self.current = monotonic()
