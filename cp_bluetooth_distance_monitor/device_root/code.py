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

from busio import I2C
from board import SCL, SDA
from adafruit_ble import BLERadio
from adafruit_ble.advertising import Advertisement
from adafruit_vl53l1x import VL53L1X

from Nvm import NvmStorage, Uint8, Uint16
from OledDisplay import Display
from SleepTimer import SleepTimer
from DistanceMonitorService import DistanceMonitorService
from DistanceMonitorApplication import DistanceMonitorApplication


# Configuration parameters
DEVICE_NAME = "DISTANCE MONITOR"

DISPLAY_WIDTH = 64
DISPLAY_HEIGHT = 48

DISPLAY_I2C_ADDRESS = 0x3D
SENSOR_I2C_ADDRESS = 0x29

## Notification callback, this function invoked by the application logic once the measured value is in the configured range
def app_notification_callback():
    print("Here we go, value in the range.")

## Initialize drivers, application
i2c = I2C(SCL, SDA)

application = DistanceMonitorApplication(
    nvm=NvmStorage(
        fields=[
            Uint16("lower_threshold", default_value=150),
            Uint16("upper_threshold", default_value=250),
            Uint8("threshold_mode", default_value=0),
            Uint8("range_mode", default_value=1),
            Uint8("notification_status", default_value=1),
        ]
    ),
    display=Display(
        DISPLAY_WIDTH,
        DISPLAY_HEIGHT,
        i2c,
        DISPLAY_I2C_ADDRESS,
    ),
    sensor=VL53L1X(
        i2c,
        SENSOR_I2C_ADDRESS,
    ),
    advertisement=Advertisement(),
    service=DistanceMonitorService(),
    ble=BLERadio(),
)

# Register a notification callback
application.register_notification_callback(app_notification_callback)

# Configure BLE advertisement
application.configure_advertisement(DEVICE_NAME, connectable=True)

# Show Silabs logo on the connected display
application.show_silabs_logo()

# Setup a periodic timer for the application logic (100 ms)
SleepTimer.setup_timer(application.main_function, 0.100)

while True:
    SleepTimer.main_function()