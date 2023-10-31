# CircuitPython - Bluetooth - Environmental Sensing (CCS811/BME280) #

![Type badge](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/SiliconLabs/application_examples_ci/master/circuitpython/cp_bluetooth_environmental_sensing_common.json&label=Type&query=type&color=green)
![Technology badge](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/SiliconLabs/application_examples_ci/master/circuitpython/cp_bluetooth_environmental_sensing_common.json&label=Technology&query=technology&color=green)
![License badge](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/SiliconLabs/application_examples_ci/master/circuitpython/cp_bluetooth_environmental_sensing_common.json&label=License&query=license&color=green)
## Overview ##

This project aims to implement an environmental sensing system using Sparkfun Thing Plus for Matter - MGM240 development kits and external sensors integrated with the BLE wireless stack and CircuitPython.

The block diagram of this application is shown in the image below:

![overview](docs/overview.png)

The wireless environment sensing system is composed of a sensor and minimum one client device. The sensor device continuously monitors the ambient temperature, humidity and the air quality. The sensor continuously sends the measured data to the client device.

### Sensor Device ###

At first, the sensor device broadcasts its advertisement package that includes its name (CP_ENV_SENSOR) and the UUID of the **Environmental Sensing Service (0x181A)**. A client device can scan and connect to the sensor device; the sensor device can periodically notify the client.

### Client Device ###

The client device scans periodically the BLE network. Once it found the sender device, it tries to connect to it and reads all the characteristics in the **Environmental Sensing Service (0x181A)**, then it is visible on the OLED display.

Note: Any other BLE-capable device can be a client device, for instance a simple cell phone.

## Hardware Required ##

### Sensor ###

- [SparkFun Thing Plus Matter - MGM240P](https://www.sparkfun.com/products/20270)
- [SparkFun Environmental Combo Breakout - CCS811/BME280 (Qwiic)](https://www.sparkfun.com/products/14348)

### Client ###

- [SparkFun Thing Plus Matter - MGM240P](https://www.sparkfun.com/products/20270)
- [OLED Display - SSD1306](https://www.sparkfun.com/products/14532)

## Connections Required ##

The environmental combo, OLED display and SparkFun Thing Plus Matter board can easily connect to each other via Qwiic I2C connector.

## Prerequisites ##

Getting started with [CircuitPython on EFR32 boards](../doc/running_circuitpython.md).

## Setup ##

To run the example you need to install **[Thonny](https://thonny.org/)** editor and then follow the steps below:

1. Flash the corresponding CircuitPython binary for your board. You can visit [circuitpython.org/downloads](https://circuitpython.org/downloads?q=silabs) to download the binary.

> **_NOTE:_** The examples in this repository require CircuitPython v8.2.0 or higher.

2. The lib folder on github contains the necessary library files. You can get updates from the bundle [here](https://circuitpython.org/libraries). The libraries used in this project are listed below.

    - Sensor device

      | Library           | Version           |
      |:----------------- |:------------------|
      | adafruit_register |       1.9.15      |
      | adafruit_bme280   |       2.6.20      |
      | adafruit_ccs811   |       1.3.13      |

    - Client device 

      | Library           | Version           |
      |:----------------- |:------------------|
      | adafruit_framebuf |       1.6.1       |
      | adafruit_ssd1306  |       2.12.12     |


3. Upload all the files and folders from the device_root folder to the CircuitPython device. The files and folders should be copied into the root of the file system on the target device.

4. Run the scripts on the board.

## How it Works ##

### Sensor ###

- **Initialization process**

    ![Initialization](docs/sensor_init.png)

- **GATT Database:**
  - [Service] Environmental Sensing
    - [Char] Temperature
      - [R, N] Get temperature value (e.g.: 25.5  C => 255)
    - [Char] Humidity
      - [R, N] Get humidity value (e.g.: 25.5 % => 255)
    - [Char] TVOC
      - [R, N] Get TVOC value in ppm
    - [Char] CO2
      - [R, N] Get CO2 value in ppm

- **Runtime operation**

    ![Runtime operation](docs/sensor_runtime.png)

### Client ###

- **Initialization process**

    ![Initialization](docs/client_init.png)

- **Runtime operation**

    ![Runtime operation](docs/client_runtime.png)

## Output ##

Run the **code.py** file on both sensor and client device and monitor the OLED you will see the result like below.

  ![result](docs/result.GIF)
