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
from adafruit_ble.characteristics import Characteristic
from adafruit_ble.attributes import Attribute
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services import Service
from adafruit_ble.uuid import StandardUUID, VendorUUID
from adafruit_ble.characteristics.int import Int16Characteristic
from adafruit_ble.characteristics.string import StringCharacteristic

tvoc_uuid = bytearray(
    [
        0xd7,
        0xee,
        0xf0,
        0x43,
        0x3a,
        0xe6,
        0x4f,
        0x6a,
        0x8d,
        0x6c,
        0x67,
        0xd8,
        0x88,
        0x8b,
        0xb5,
        0x36,
    ]
)
co2_uuid = bytearray(
    [
        0x5e,
        0x9d,
        0x22,
        0x53,
        0xb2,
        0xde,
        0x49,
        0xab,
        0x9c,
        0x36,
        0xe4,
        0xf9,
        0x8b,
        0xe0,
        0x8e,
        0x48,
    ]
)

class EnvironmentalSensingService(Service):
    uuid = StandardUUID(0x181A)

    temperature = Int16Characteristic(
        uuid = StandardUUID(0x2A6E),
        properties = (Characteristic.READ | Characteristic.NOTIFY),
        write_perm = Attribute.NO_ACCESS,
    )

    humidity = Int16Characteristic(
        uuid = StandardUUID(0x2A6F),
        properties = (Characteristic.READ | Characteristic.NOTIFY),
        write_perm = Attribute.NO_ACCESS,
    )

    tvoc = StringCharacteristic(
        uuid = VendorUUID(tvoc_uuid),
        properties = (Characteristic.READ | Characteristic.NOTIFY),
        write_perm = Attribute.NO_ACCESS,
    )

    co2 = StringCharacteristic(
        uuid = VendorUUID(co2_uuid),
        properties = (Characteristic.READ | Characteristic.NOTIFY),
        write_perm = Attribute.NO_ACCESS,
    )
    
    def __init__(self, service=None):
        super().__init__(service=service)
        self.connectable = True

