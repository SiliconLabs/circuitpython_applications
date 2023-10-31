<table border="0">
  <tr>
    <td align="left" valign="middle">
    <h1>EFR32 CircuitPython Application Examples</h1>
  </td>
  <td align="left" valign="middle">
    <a href="https://www.silabs.com/wireless/bluetooth">
      <img src="http://pages.silabs.com/rs/634-SLU-379/images/WGX-transparent.png"  title="Silicon Labs Wireless Gecko MCUs" alt="EFM32 32-bit Microcontrollers" width="250"/>
    </a>
  </td>
  </tr>
</table>

# Silicon Labs CircuitPython Applications #

[![Version Badge](https://img.shields.io/badge/-v1.3.0-green)](https://github.com/SiliconLabs/circuitpython_applications/releases)
[![CircuitPython](https://img.shields.io/badge/CircuitPython-v8.2.0+-green)](https://circuitpython.org/downloads?q=silabs)
![License badge](https://img.shields.io/badge/License-Zlib-green)

This repository contains example projects that demonstrate various applications using CircuitPython on Silicon Labs Development Kits.
All examples in this repository are considered to be EXPERIMENTAL QUALITY, which implies that the code provided in the repository has not been formally tested and is provided as-is. It is not suitable for production environments.

## Examples ##

| No | Example name | Link to example |
|:--:|:-------------|:---------------:|
|  1 | CircuitPython - Bluetooth - SoC - Blinky | [Click Here](./cp_bluetooth_blinky) |
|  2 | CircuitPython - Bluetooth - Distance Monitor (VL53L1X) | [Click Here](./cp_bluetooth_distance_monitor)|
|  3 | CircuitPython - Bluetooth - Environmental Sensing (CCS811/BME280) | [Click Here](./cp_bluetooth_environmental_sensing) |
|  4 | CircuitPython - Bluetooth - Neopixel Humidity Gauge (SHTC3) | [Click Here](./cp_bluetooth_neopixel_humidity_gauge) |
|  5 | CircuitPython - Bluetooth - Light Detector (AS7265x) | [Click Here](./cp_bluetooth_light_detector) |
|  6 | CircuitPython - Non-Wireless Display Demo (IS31FL3741) | [Click Here](./cp_non_wireless_display_demo) |
|  7 | CircuitPython - RGB Display Drawing (ILI9341) | [Click Here](./cp_rgb_display_drawing_ili9341) |
|  8 | CircuitPython - Temperature and Humidity Monitor with LED Matrix Display (SI2071/IS31FL3741) | [Click Here](./cp_temperature_and_humidty_monitor) |
|  9 | CircuitPython - xG24 Dev Kit Sensors (ILI9341) | [Click Here](./cp_xg24_dev_kit_sensors) |



## Get CircuitPython firmware ##

Official binaries for all Silicon Labs supported boards are available through
[circuitpython.org/downloads](https://circuitpython.org/downloads?q=silabs). The site includes stable, unstable and
continuous builds. Full release notes are available through
[GitHub releases](https://github.com/adafruit/circuitpython/releases) as well.


> **_NOTE:_** The examples in this repository require CircuitPython v8.2.0 or higher.


## Project structure

* **device_root**
  * This folder contains all of the required files to run the project. The files and folders should be copied into the root folder of the device.
  * **lib**
    * The lib folder contains precompiled libraries provided by Adafruit, this folder provides the application logic related files too. These libraries and files are required to run the project.


Ensure that the files and folders from the device_root folder are copied into the root of the target board's file system. 


## Documentation ##

Getting started with [CircuitPython on EFR32 boards](doc/running_circuitpython.md).

For more information, visit the [Developer documentation](https://docs.silabs.com/application-examples/latest/) portal of Silicon Laboratories.

## Reporting Bugs/Issues and Posting Questions and Comments ##

To report bugs in the Application Examples projects, please create a new "Issue" in the "Issues" section of this repo. Please reference the board, project, and source files associated with the bug, and reference line numbers. If you are proposing a fix, also include information on the proposed fix. Since these examples are provided as-is, there is no guarantee that these examples will be updated to fix these issues.

Questions and comments related to these examples should be made by creating a new "Issue" in the "Issues" section of this repo.
