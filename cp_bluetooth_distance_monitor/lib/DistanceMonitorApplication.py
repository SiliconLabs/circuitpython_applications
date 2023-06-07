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

from time import sleep
from adafruit_vl53l1x import VL53L1X
from adafruit_ble import BLERadio
from adafruit_ble.advertising import Advertisement

from Nvm import NvmStorage
from OledDisplay import Display
from Configuration import Configuration
from DistanceMonitorService import DistanceMonitorService

APP_VALUE_LIMITS = {
    "lower_threshold": (40, 36000),
    "upper_threshold": (40, 36000),
    "threshold_mode": (0, 3),
    "range_mode": (1, 2),
    "notification_status": (0, 1),
}

VL53L1X_LOWER_LIMIT = 40

THRESHOLD_MODE_BELOW = 0
THRESHOLD_MODE_ABOVE = 1
THRESHOLD_MODE_IN = 2
THRESHOLD_MODE_OUT = 3


class DistanceMonitorApplication:
    def __init__(
        self,
        nvm: NvmStorage,
        display: Display,
        sensor: VL53L1X,
        advertisement: Advertisement,
        service: DistanceMonitorService,
        ble: BLERadio,
    ) -> None:
        self.notified = False
        self.in_range = False
        self.notification_callbacks = []
        self.logger("Initialize application...")
        self.nvm: NvmStorage = nvm
        self.display: Display = display
        self.sensor: VL53L1X = sensor
        self.advertisement: Advertisement = advertisement
        self.service: DistanceMonitorService = service
        self.ble: BLERadio = ble

        self.logger("Loading configuration from NVM...")
        self.config = self.load_configuration()

        self.sensor.distance_mode = self.config.range_mode

        self.logger("Initialization done.")
        self.logger("Start distance ranging...")
        self.sensor.start_ranging()

    def register_notification_callback(self, callback_function):
        if callable(callback_function):
            self.notification_callbacks.append(callback_function)

    def notify(self):
        if not self.notified:
            for notification_callback in self.notification_callbacks:
                if callable(notification_callback):
                    notification_callback()
            self.notified = True

    def show_silabs_logo(self) -> None:
        # Display SiliconLabs logo
        with open("siliconlabs_logo.bin", "rb") as file:
            silabs_logo = file.read()
        self.display.draw_xbitmap(0, 10, 64, 23, silabs_logo)
        self.logger("Show Silabs logo for 3 second...")
        sleep(3)

        self.display.init_screen()

    def main_function(self, *args, **kwargs) -> None:
        if not self.ble.connected and not self.ble.advertising:
            self.ble.start_advertising(self.advertisement)
            self.logger(
                f"Start advertising with a device name of '{self.advertisement.short_name}'..."
            )
        elif self.ble.connected and self.ble.advertising:
            self.ble.stop_advertising()
            self.logger("Stop advertising...")
            self.logger("Device connected...")

        if self.ble.connected:
            # Workaround for missing BLE characteristic callbacks...
            if self.config != self.service:
                self.save_nvm_configuration()

        if self.sensor.data_ready:
            self.application_logic(self.sensor.distance)

    def application_logic(self, distance) -> None:
        text = " "

        if distance is not None:
            # Convert to mm
            distance = int(distance * 10)

        old_in_range = self.in_range
        self.in_range = False

        if distance is not None:
            # Validate distance value
            if VL53L1X_LOWER_LIMIT <= distance:
                self.display.display_distance(distance)

                if self.config.threshold_mode == THRESHOLD_MODE_BELOW:
                    text = f"BELOW {self.config.lower_threshold}mm"
                    if distance <= self.config.lower_threshold:
                        self.in_range = True
                elif self.config.threshold_mode == THRESHOLD_MODE_ABOVE:
                    text = f"ABOVE {self.config.upper_threshold}mm"
                    if distance >= self.config.upper_threshold:
                        self.in_range = True
                elif self.config.threshold_mode == THRESHOLD_MODE_IN:
                    text = f"IN {self.config.lower_threshold}-{self.config.upper_threshold}mm"
                    if (
                        self.config.lower_threshold
                        <= distance
                        <= self.config.upper_threshold
                    ):
                        self.in_range = True
                elif self.config.threshold_mode == THRESHOLD_MODE_OUT:
                    text = f"OUT OF {self.config.lower_threshold}-{self.config.upper_threshold}mm RANGE"
                    if (
                        distance < self.config.lower_threshold
                        or distance > self.config.upper_threshold
                    ):
                        self.in_range = True
            else:
                self.display.display_out_of_range()

        else:
            self.display.display_out_of_range()

        if old_in_range != self.in_range and not self.in_range:
            self.notified = False

        if self.in_range and self.config.notification_status:
            self.display.blink_text("RANGE", 40)
            self.notify()
        else:
            self.display.scrolling_text(text)

    def load_configuration(self) -> Configuration:
        # Assign values to the BLE characteristics
        self.service.lower_threshold = self.nvm.lower_threshold
        self.service.upper_threshold = self.nvm.upper_threshold
        self.service.threshold_mode = self.nvm.threshold_mode
        self.service.range_mode = self.nvm.range_mode
        self.service.notification_status = self.nvm.notification_status

        return Configuration(
            lower_threshold=self.nvm.lower_threshold,
            upper_threshold=self.nvm.upper_threshold,
            threshold_mode=self.nvm.threshold_mode,
            range_mode=self.nvm.range_mode,
            notification_status=self.nvm.notification_status,
        )

    def save_nvm_configuration(self) -> None:
        for key, value in self.config.changes(self.service).items():
            # Check parameter ranges
            lower_limit, upper_limit = APP_VALUE_LIMITS.get(key, (None, None))
            if None not in [lower_limit, upper_limit]:
                if not (lower_limit <= value <= upper_limit):
                    setattr(self.service, key, getattr(self.config, key))
                    self.logger(
                        f"Invalid parameter for key='{key}', value='{value}', valid range=({lower_limit}, {upper_limit}), restoring previous value='{getattr(self.config, key)}'"
                    )
                    continue

            self.logger(f"Save new parameter for key='{key}', value='{value}'")

            self.nvm.update(key, value)
            self.config.update(key, value)

            # Update sensor distance mode configuration
            if key == "range_mode":
                self.sensor.distance_mode = value
        self.nvm.flush()

    def configure_advertisement(self, device_name, connectable=True) -> None:
        self.advertisement.short_name = device_name
        self.advertisement.connectable = connectable
        self.logger(
            f"Advertisement configured: '{self.advertisement.short_name}', connectable='{self.advertisement.connectable}'"
        )

    def logger(self, text):
        print(f"{self.__class__}: {text}")
