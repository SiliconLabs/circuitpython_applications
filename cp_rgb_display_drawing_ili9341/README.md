# CircuitPython - RGB Display Drawing (ILI9341) #

## Summary ##

This example application code demonstrates how to use CircuitPython and the adafruit_rgb_display and adafruit_touchscreen drivers on Silabs development kits, such as "Sparkfun ThingPlus Matter board," the "xG24 explorer kit," and the "xG24 devkit."

The demo shows how to draw on a 2.4" TFT LCD with Touchscreen Breakout w/MicroSD Socket - ILI9341 using Silabs development kits.

## Hardware Required ##

- [SparkFun Thing Plus Matter - MGM240P](https://www.sparkfun.com/products/20270)

- [Adafruit 2.4" TFT LCD with Touchscreen Breakout w/MicroSD Socket - ILI9341](https://www.adafruit.com/product/2478)

## Connections Required ##

The TFT LCD can easily connected with Sparkfun Thing Plus for Matter - MGM240 development kits via jumper wire like this picture.

The following picture shows how the system works.

![overview](docs/overview.png)

Listed below are the port and pin mappings for working with this example.

- Board: **BRD2704A - Sparkfun Thing Plus Matter - MGM240P**

    | Pin | Connection | Pin function |
    |:---:|:-------------:|:---------------|
    | PC0 | D/C | GPIO |
    | PC1 | CS | SPI CS |
    | PC2 | CLK | SPI SCK |
    | PC3 | MISO | SPI MISO |
    | PC6 | MOSI | SPI MOSI |
    | PA0 | XP(X+) | AN |
    | PA4 | YP(Y+) | AN |
    | PB0 | YM(Y-) | AN |
    | PB1 | XM(Y+) | AN |

## Setup ##

To run the example you need to install **Thonny** editor and then follow the steps below:

1. Install the necessary libraries from Adafruit CircuitPython bundle. You can download the bundle from [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle). To upload the libraries to CircuitPython device.

2. Upload all the files in lib folder in to CircuitPython device.

3. Copy the content of the **code.py** file in the src folder and paste it to the **code.py** file on the CircuitPython device.

4. Run the scripts on the board.

**Note:** Make sure that you have flashed the corresponding CircuitPython firmware for your board. You can visit [circuitpython.org](https://circuitpython.org/) to download the firmware.

## How it Works ##

- ### Initialization ###

    ![Initialization](docs/init.png).

- ### Runtime operation ###

    ![Runtime operation](docs/run_time.png).

## Testing ##

Run the **code.py** file.
- After start, you can see the logo of Silicon Labs and CircuitPython for 5 second.  
- Then it show the logo and color selector at the bottom side of the screen.
- You can start to draw or pick color by tab the color you want in color pallete and the present pen color will show in small rectangle at the top left of screen.
- Or you can clear all the screen by tab the Silabs logo. 

![result](docs/result.gif)