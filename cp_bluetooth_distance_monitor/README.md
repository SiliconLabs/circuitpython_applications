# CircuitPython - Bluetooth - Distance Monitor (VL53L1X) #

![Type badge](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/SiliconLabs/application_examples_ci/master/circuitpython/cp_bluetooth_distance_monitor_common.json&label=Type&query=type&color=green)
![Technology badge](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/SiliconLabs/application_examples_ci/master/circuitpython/cp_bluetooth_distance_monitor_common.json&label=Technology&query=technology&color=green)
![License badge](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/SiliconLabs/application_examples_ci/master/circuitpython/cp_bluetooth_distance_monitor_common.json&label=License&query=license&color=green)
## Overview ##

This project shows a demonstration of a Bluetooth Low Energy distance monitor system using SparkFun Thing Plus Matter - MGM240P development kit and the integrated CircuitPython BLE Stack.

The block diagram of this application is shown in the image below:

![overview](docs/overview.png)

## Hardware Required ##

- [SparkFun Thing Plus Matter - MGM240P](https://www.sparkfun.com/products/20270)

- [SparkFun Distance Sensor Breakout - 4 Meter, VL53L1X (Qwiic)](https://www.sparkfun.com/products/14722)

- [OLED Display - SSD1306](https://www.sparkfun.com/products/14532)

## Connections Required ##

The sensor and OLED display can easily connected with Sparkfun Thing Plus for Matter - MGM240 development kits via Qwiic connector.

## Prerequisites ##

Getting started with [CircuitPython on EFR32 boards](../doc/running_circuitpython.md).

## Setup ##

To run the example you need to install **[Thonny](https://thonny.org/)** editor and then follow the steps below:

1. Flash the corresponding CircuitPython binary for your board. You can visit [circuitpython.org/downloads](https://circuitpython.org/downloads?q=silabs) to download the binary.

> **_NOTE:_** The examples in this repository require CircuitPython v8.2.0 or higher.

2. The lib folder on github contains the necessary library files. You can get updates from the bundle [here](https://circuitpython.org/libraries). The libraries used in this project are listed below.

    | Library           | Version           |
    |:----------------- |:------------------|
    | adafruit_framebuf |       1.6.1       |
    | adafruit_ssd1306  |       2.12.2      |
    | adafruit_vl53l1x  |       1.1.10      |

3. Upload all the files and folders from the device_root folder to the CircuitPython device. The files and folders should be copied into the root of the file system on the target device.

4. Run the scripts on the board.


## How it Works ##

- ### Initialization ###

    ![Initialization](docs/init.png).

- ### Runtime operation ###

    ![Runtime operation](docs/run_time.png).

- ### GATT database ###

  - [Service] Distance Monitor
    - [Char] Lower Threshold Value - threshold_value_lower
      - [R] Get lower threshold value (mm)
      - [W] Set lower threshold value (mm)
    - [Char] Upper Threshold Value - threshold_value_upper
      - [R] Get upper threshold value (mm)
      - [W] Set upper threshold value (mm)
    - [Char] Threshold Mode - threshold_mode
      - [R] Get threshold mode (0-2)
      - [W] Set threshold mode (0-2)
    - [Char] Range Mode - range_mode
      - [R] Get configured range mode (0-1)
      - [W] Set range mode (0-1)
    - [Char] Notification Status - notification_status
      - [R] Get configured notification status (0-2)
      - [W] Set notification status (0-2)

## Output  ##

Run the **code.py** file, monitor the OLED, and try to place your hand beyond the sensor you will see the result below.

![result](docs/result.GIF)
