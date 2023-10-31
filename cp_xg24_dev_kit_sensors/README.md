# CircuitPython - xG24 Dev Kit Sensors (ILI9341) #

![Type badge](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/SiliconLabs/application_examples_ci/master/circuitpython/cp_xg24_dev_kit_sensors_common.json&label=Type&query=type&color=green)
![Technology badge](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/SiliconLabs/application_examples_ci/master/circuitpython/cp_xg24_dev_kit_sensors_common.json&label=Technology&query=technology&color=green)
![License badge](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/SiliconLabs/application_examples_ci/master/circuitpython/cp_xg24_dev_kit_sensors_common.json&label=License&query=license&color=green)
## Summary ##

This project demonstrates how to use the Silicon Labs xG24 Dev Kit with CircuitPython language.

The sensor data is read from the built-in sensors of the Silicon Labs xG24 Dev Kit, including the SI2071 RHT, ICM-20689 accelerometer, and BMP384 barometer, then the data is displayed on the ILI9341 RGB screen using the ILI9341 RGB Display driver.

The block diagram of this application is shown in the image below:
![overview](docs/overview.png)

## Hardware Required ##

- [EFR32xG24 Dev Kit - BRD2601B](https://www.silabs.com/development-tools/wireless/efr32xg24-dev-kit?tab=overview)

- [Adafruit 2.4" TFT LCD with Touchscreen Breakout w/MicroSD Socket - ILI9341](https://www.adafruit.com/product/1770)

## Connection Required ##

The xG24 Dev Kit and TFT display can connect via SPI interface. You can make the connection according to the table below:

| xG24 Dev Kit | TFT LCD display | 
|:-------|:------:|
|  2 (VMCU)  |  Vin  |
|  1 (GND)  |  GND  |
|  8 (SCLK)  |  CLK  |
| 6 (CIPO)  |  MISO  |
|  4 (COPI)  |  MOSI  |
|  9 (PB0)  |  CS  |
|  3 (PB2)  |  D/C  |

## Prerequisites ##

Getting started with [CircuitPython on EFR32 boards](../doc/running_circuitpython.md).

## Setup ##

To run the example you need to install **[Thonny](https://thonny.org/)** editor and then follow the steps below:

1. Flash the corresponding CircuitPython binary for your board. You can visit [circuitpython.org/downloads](https://circuitpython.org/downloads?q=silabs) to download the binary.

> **_NOTE:_** The examples in this repository require CircuitPython v8.2.0 or higher.

2. The lib folder on github contains the necessary library files. You can get updates from the bundle [here](https://circuitpython.org/libraries). The libraries used in this project are listed below.

    | Library           | Version           |
    |:----------------- |:------------------|
    | adafruit_display_text |       2.28.1       |
    | adafruit_ili9341  |       1.3.8      |

3. Upload all the files and folders from the device_root folder to the CircuitPython device. The files and folders should be copied into the root of the file system on the target device.

4. Run the scripts on the board.

## How it works ##

This project demonstrates the use of the CircuitPython IL9341 RGB Display driver with the Silicon Labs xG24 Dev Kit.

For the beginning, the screen will show the Silicon Labs logo and CircuitPython logo for 5 seconds.

After that, the parameters of built-in sensors on xG24 Dev Kit will show on the screen.

**Application Initialization**

![application_init](docs/application_init.png)

**Application Logic**

![application_logic](docs/application_logic.png)

## Output ##

After you powered the devices, the boot screen is visible for 5 seconds. Then the parameters of built-in sensors on xG24 Dev Kit are visible on the application screen every 3 seconds.

You can run the code.py file or press the Reset button. On the display, you will see the result below:

![demo](docs/demo.gif)
