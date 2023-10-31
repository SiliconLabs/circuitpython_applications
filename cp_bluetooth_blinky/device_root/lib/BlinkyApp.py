from adafruit_ble.advertising.standard import Advertisement
from adafruit_ble import BLERadio
import digitalio
import board


class BlinkyApp():
    def __init__(self,
                service: BlinkyService,
                ble: BLERadio,
                led_pin: microcontroller.Pin,
                button_pin: microcontroller.Pin) -> None:
        self.service = service
        self.adv = Advertisement()
        self.ble = ble
        self.button = digitalio.DigitalInOut(button_pin)
        self.button.direction = digitalio.Direction.INPUT
        self.led = digitalio.DigitalInOut(led_pin)
        self.led.direction = digitalio.Direction.OUTPUT


    def configure_advertisement(self,
                               device_name,
                               connectable = True) -> None:
        self.adv.short_name = device_name
        self.adv.connectable = connectable
      
    def main_function(self):
        if not self.ble.connected and not self.ble.advertising:
            print('>>> Start advertising')
            self.ble.start_advertising(self.adv)

        if self.ble.connected:
            if self.ble.advertising:
                self.ble.stop_advertising()
                print('>>> Connected, stop advertising')
                
            if self.service.report_button != int(self.button.value):
                self.service.report_button = int(self.button.value)
                print("Button: {0}".format(int(self.button.value)))
                
            if self.service.led_control == 0 and self.led.value == False:
                self.led.value = True
                print("LED on.");
            elif self.service.led_control == 1 and self.led.value == True:
                self.led.value = False
                print("LED off.");
