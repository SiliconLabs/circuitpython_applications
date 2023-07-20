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

from adafruit_ble.services import Service
from adafruit_ble.uuid import VendorUUID, StandardUUID
from adafruit_ble.attributes import Attribute
from adafruit_ble.characteristics import Characteristic
from adafruit_ble.characteristics.int import Uint32Characteristic

class LightSensingService(Service):
    uuid=StandardUUID(0x181A)

    color_R = Uint32Characteristic(
        uuid = VendorUUID("51ad213f-e568-4e35-84e4-67af89c79ef0"),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    color_O = Uint32Characteristic(
        uuid = VendorUUID("51ad213f-e568-4e35-84e4-67af89c79ef1"),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    color_Y = Uint32Characteristic(
        uuid = VendorUUID("51ad213f-e568-4e35-84e4-67af89c79ef2"),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    color_G = Uint32Characteristic(
        uuid = VendorUUID("51ad213f-e568-4e35-84e4-67af89c79ef3"),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    color_B = Uint32Characteristic(
        uuid = VendorUUID("51ad213f-e568-4e35-84e4-67af89c79ef4"),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )
    color_V = Uint32Characteristic(
        uuid = VendorUUID("51ad213f-e568-4e35-84e4-67af89c79ef5"),
        properties=(Characteristic.READ | Characteristic.NOTIFY),
        write_perm=Attribute.NO_ACCESS,
    )

    def __init__(self, service=None):
        super().__init__(service=service)
        self.connectable = True
