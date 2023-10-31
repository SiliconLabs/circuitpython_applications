import digitalio
import board
from adafruit_ble import BLERadio
from BlinkyApp import BlinkyApp
from BlinkyService import BlinkyService

DEVICE_NAME = 'Blinky Example'


# application init
app = BlinkyApp(
   BlinkyService(),
   BLERadio(),
   board.LEDG,
   board.BTN0
)

# config the advertisement
app.configure_advertisement(DEVICE_NAME)

# start looping the main function
while True:
    app.main_function()