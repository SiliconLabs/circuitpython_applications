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
from OledDisplay import OledDisplay
from EnvSensingService import EnvironmentalSensingService
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble import BLERadio
from time import sleep, monotonic

class ClientApp():
    def __init__(
        self,
        oled: OledDisplay,
        ble: BLERadio,
    ) -> None:
        self.oled: OledDisplay = oled
        self.ble: BLERadio = ble
        self.found = False
        self.connection = None
        self.service = None
        self.current = 0
    
    def show_silabs_logo(self) -> None:
        # Display SiliconLabs logo
        with open("siliconlabs_logo.bin", "rb") as file:
            silabs_logo = file.read()
        self.oled.draw_xbitmap(0, 10, 64, 23, silabs_logo)
        sleep(3)
        self.oled.init_screen()

    def main_function(self) -> None:
        if monotonic() - self.current >= 1:
            if not self.ble.connected:
                print('scanning sensor device...\r')
                self.oled.disconnected_display()
                for adv in self.ble.start_scan(ProvideServicesAdvertisement):
                    if EnvironmentalSensingService in adv.services:
                        print('found sensor device !!!\r')
                        print('stop scanning sensor device\r')
                        self.ble.stop_scan()
                        self.connection = self.ble.connect(adv)
                        self.found = True
                        break
            if self.ble.connected:
                self.service = self.connection[EnvironmentalSensingService]
                read_data = [
                    self.service.temperature,
                    self.service.humidity,
                    int(float(self.service.tvoc)),
                    int(float(self.service.co2))
                ]
                self.oled.display_data(read_data)
            self.current = monotonic()

        
