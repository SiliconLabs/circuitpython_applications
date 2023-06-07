# Running Circuitpython
## Dowload CircuitPython Firmware 

Official binaries for all supported boards are available through [circuitpython.org/downloads](https://circuitpython.org/downloads?q=silabs). The site includes stable,unstable and continuous builds.

If you want to make changes, you might clone and re-build the source and firmware.bin file can be found in the build folder corresponding to the appropriate board, such as build-sparkfun_thingplus_matter_mgm240p_brd2704a

## Flash firmware

To flash the firmware file into the board, you need to use Simplicity Commander.
You can install Simplicity Commander using Simplicity Studio or downloading standalone versions by following [UG162: Simplicity Commander Reference Guide](https://www.silabs.com/documents/public/user-guides/ug162-simplicity-commander-reference-guide.pdf).

To flash the firmware into the xG24 kit using Simplicity Commander, follow these simple steps:

**1.** Connect your xG24 kit to your computer and ensure that it is recognized by your programming tool.

**2.** Browse and select the firmware file that you wish to upload to the board.

**3.** Initiate the flashing process to upload the firmware to the xG24 kit.

![Commander](cp_commander.png)

## Getting a REPL prompt ##

Connect the devkit to the PC via the USB cable. The board uses serial for REPL access and debugging because the EFR32 chips has no USB support.

### Windows ###

On Windows, we need to install a serial console e.g., PuTTY, MobaXterm. The JLink CDC UART Port can be found in the Device Manager.

### Linux ###

Open a terminal and issue the following command: 
```bash
$ ls /dev/ttyACM*
```
Then note down the correct name and substitute com-port-name in the following command with it: 
```bash
$ screen /dev/'com-port-name'
```
### Using the REPL prompt ###

After flashing the firmware to the board, at your first connecting to the board, you might see a blank screen. Press enter and you should be presented with a Circuitpython prompt, >>>. If not, try to reset the board (see instructions below).

You can now type in simple commands such as: 

```sh
>>> print("Hello world!") 

Hello world
```

If something goes wrong with the board, you can reset it. Pressing CTRL+D when the prompt is open performs a soft reset.

## Recommended editors ##

**Thonny** is a simple code editor that works with the Adafruit CircuitPython boards. 

Config serial: Tools > Options > Interpreter > Select Circuitpython(generic) > Select Port Jlink CDC UART Port

### Running CircuitPython scripts ###

At the boot stage, two scripts will be run (if not booting in safe mode). First, the file  boot.py  will be executed. The file **boot.py** can be used to perform the initial setup. Then, after boot.py has been completed, the file **code.py** will be executed.  

After code.py has finished executing, a REPL prompt will be presented on the serial port. Other files can also be executed by using the **Thonny** editors or using **Ampy** tool.

![Thony](cp_thony.png)

With the boards which support USB mass storage, we can drag the files to the board file system. However, because the EFR32 boards don’t support USB mass storage, we need to use a tool like **Ampy** to copy the file to the board. You can use the latest version of **Ampy** and its  command to copy the module directories to the board.

Refer to the guideline below for installing the **Ampy** tool: 

https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy  