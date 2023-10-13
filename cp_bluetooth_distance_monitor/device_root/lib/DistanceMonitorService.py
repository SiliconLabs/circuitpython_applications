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
from adafruit_ble.uuid import VendorUUID
from adafruit_ble.attributes import Attribute
from adafruit_ble.characteristics import Characteristic
from adafruit_ble.characteristics.int import Uint8Characteristic, Uint16Characteristic

service_uuid = bytearray(
    [
        0xDF,
        0xEF,
        0xFE,
        0x4F,
        0x3B,
        0xEF,
        0x8F,
        0x6A,
        0x8A,
        0x6F,
        0x69,
        0xDA,
        0x88,
        0x8B,
        0xBA,
        0x4B,
    ]
)
lower_threshold_uuid = bytearray(
    [
        0xD7,
        0xEE,
        0xF0,
        0x43,
        0x3A,
        0xE6,
        0x4F,
        0x6A,
        0x8D,
        0x6C,
        0x67,
        0xD8,
        0x88,
        0x8B,
        0xB6,
        0x40,
    ]
)
upper_threshold_uuid = bytearray(
    [
        0xDA,
        0xEE,
        0xFE,
        0x43,
        0x3A,
        0xE6,
        0x4E,
        0x2A,
        0x8D,
        0x6E,
        0x67,
        0xD4,
        0x88,
        0x8B,
        0xB6,
        0x40,
    ]
)
threshold_mode_uuid = bytearray(
    [
        0xDE,
        0x7E,
        0xF0,
        0x43,
        0x3A,
        0xE6,
        0x4F,
        0x4A,
        0x8D,
        0x6C,
        0x6F,
        0xD8,
        0x8A,
        0x8B,
        0x9D,
        0x42,
    ]
)
range_mode_uuid = bytearray(
    [
        0xDF,
        0xEE,
        0xFA,
        0x43,
        0x6A,
        0xE6,
        0x4F,
        0x9E,
        0x8D,
        0x6F,
        0x67,
        0xD8,
        0x88,
        0x8B,
        0xBF,
        0x4A,
    ]
)
notification_status_uuid = bytearray(
    [
        0xDA,
        0xEF,
        0xF0,
        0x43,
        0x3A,
        0xE9,
        0x8F,
        0x6A,
        0x8D,
        0x6C,
        0x67,
        0xDA,
        0x88,
        0x8B,
        0xBA,
        0x4B,
    ]
)


class DistanceMonitorService(Service):
    uuid = VendorUUID(service_uuid)

    lower_threshold = Uint16Characteristic(
        uuid=VendorUUID(lower_threshold_uuid),
        properties=(Characteristic.READ | Characteristic.WRITE),
        write_perm=Attribute.NO_ACCESS,
    )

    upper_threshold = Uint16Characteristic(
        uuid=VendorUUID(upper_threshold_uuid),
        properties=(Characteristic.READ | Characteristic.WRITE),
        write_perm=Attribute.NO_ACCESS,
    )

    threshold_mode = Uint8Characteristic(
        uuid=VendorUUID(threshold_mode_uuid),
        properties=(Characteristic.READ | Characteristic.WRITE),
        write_perm=Attribute.NO_ACCESS,
    )

    range_mode = Uint8Characteristic(
        uuid=VendorUUID(range_mode_uuid),
        properties=(Characteristic.READ | Characteristic.WRITE),
        write_perm=Attribute.NO_ACCESS,
    )

    notification_status = Uint8Characteristic(
        uuid=VendorUUID(notification_status_uuid),
        properties=(Characteristic.READ | Characteristic.WRITE),
        write_perm=Attribute.NO_ACCESS,
    )

    def __init__(self, service=None):
        super().__init__(service=service)
        self.connectable = True
