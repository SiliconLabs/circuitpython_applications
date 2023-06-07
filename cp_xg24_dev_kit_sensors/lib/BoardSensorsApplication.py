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
from TFTDisplay import TFTDisplay
import sensor
import board

class BoardSensorsApplication:
    def __init__(self,
                 display: TFTDisplay,
                 ) -> None:
        i2c = board.I2C()
        sensor.init(i2c)
        self.display: TFTDisplay = display
        self.update = False
        self.sensor_dict = {}
        self.logger("Application Initialization")
           
    def boot_screen(self):
        self.display.draw_image("lib/silabs_big_logo.bmp", x= 90, y = 80)
        self.display.draw_image("lib/cpython_logo.bmp", x = 220, y = 180)
        self.logger("Show Silabs logo and Circuit Python logo for 5 seconds...")
        sleep(5)
        for _ in range(2):
            self.display.splash.pop()

    def application_screen(self):
        self.display.draw_text(text = "xG24 Dev Kit - Board Sensors", x = 80, y = 10)
        self.display.draw_vline(x = 10, y = 20, width = 300, height = 2)
        self.display.draw_text(text = "Si7021 Relative Humidity \nand Temeperature Sensor", x = 20, y = 40)
        self.display.draw_text(text = "VEML6035 Ambient Light Sensor", x = 20, y = 80)
        self.display.draw_text(text = "Si7201 Hall Effect Sensor", x = 20, y = 100)
        self.display.draw_text(text = "BMP384 Barometric Pressure Sensor", x = 20, y = 120)
        self.display.draw_text(text = "ICM-20689 6 - Axis Inertial Sensor", x = 20, y = 140)
        self.display.draw_vline(x = 10, y = 150, width = 300, height = 2)
        self.display.draw_text(text = "Orientation", x = 10, y = 160)
        self.display.draw_text(text = "Acceleration", x = 230, y = 160)
        self.display.draw_vline(x = 10, y = 190, width = 300, height = 2)
        self.display.draw_image("lib/silabs_small_logo.bmp", x = 220, y = 195)
        self.display.draw_image("lib/cpython_logo.bmp", x = 40, y = 195)

    def get_sensor_param(self):
        self.sensor_dict["Temperature"] = sensor.temperature()
        self.sensor_dict["Humidity"] = sensor.humidity()
        self.sensor_dict["Ambient Light"] = sensor.lux()
        self.sensor_dict["Hall"] = sensor.hall()
        self.sensor_dict["Pressure"] = sensor.pressure()
        (orient, accel) = sensor.imu()
        self.sensor_dict["Orientation"] = list(item * 0.01 for item in orient)
        self.sensor_dict["Acceleration"] = list(item * 0.01 for item in accel)

    def main_function(self, *args, **kwargs) -> None:
        self.get_sensor_param()
        self.show_sensors()
        self.update = True
    
    def show_sensors(self):
        if self.update is True:
            self.display.splash.pop(-6)
        self.display.draw_text(text = "{:.2f} oC {:.2f} %" .format(self.sensor_dict["Temperature"],
                                                                   self.sensor_dict["Humidity"]),
                                                                   x = 220, y = 40)
        if self.update is True:
            self.display.splash.pop(-6)
        self.display.draw_text(text = "{:.2f} lx" .format(self.sensor_dict["Ambient Light"]),  x = 230, y = 80)
        if self.update is True:
            self.display.splash.pop(-6)
        self.display.draw_text(text = "{:.2f} mT" .format(self.sensor_dict["Hall"]),  x = 230, y = 100)
        if self.update is True:
            self.display.splash.pop(-6)
        self.display.draw_text(text = "{:.2f} mBar" .format(self.sensor_dict["Pressure"]),  x = 230, y = 120)
        if self.update is True:
            self.display.splash.pop(-6)
        self.display.draw_text(text = "{:.2f}o   {:.2f}o   {:.2f}o" .format(self.sensor_dict["Orientation"][0],
                                                                            self.sensor_dict["Orientation"][1],
                                                                            self.sensor_dict["Orientation"][2]),
                                                                            x = 10, y = 180)
        if self.update is True:
            self.display.splash.pop(-6)
        self.display.draw_text(text = "{:.2f}g   {:.2f}g   {:.2f}g" .format(self.sensor_dict["Acceleration"][0],
                                                                            self.sensor_dict["Acceleration"][1],
                                                                            self.sensor_dict["Acceleration"][2]),
                                                                            x = 170, y = 180)

    def init(self):
        self.boot_screen()
        self.application_screen()
        self.logger("The parameters of sensors will be updated every 3 seconds")

    def logger(self, text: str):
        print(f"{self.__class__}: {text}")
