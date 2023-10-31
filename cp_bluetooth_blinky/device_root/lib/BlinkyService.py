from adafruit_ble.services import Service
from adafruit_ble.uuid import VendorUUID
from adafruit_ble.attributes import Attribute
from adafruit_ble.characteristics import Characteristic
from adafruit_ble.characteristics.int import Uint8Characteristic

class BlinkyService(Service):
    uuid = VendorUUID('de8a5aac-a99b-c315-0c80-60d4cbb51224')

    led_control = Uint8Characteristic(
        uuid = VendorUUID('5b026510-4088-c297-46d8-be6c736a087a'),
        properties = (Characteristic.READ | Characteristic.WRITE),
        write_perm = Attribute.NO_ACCESS,
    )
    
    report_button = Uint8Characteristic(
        uuid = VendorUUID('61a885a4-41c3-60d0-9a53-6d652a70d29c'),
        properties = (Characteristic.READ | Characteristic.NOTIFY),
        write_perm = Attribute.NO_ACCESS,
    )
        
 
    def __init__(self, service=None):
        super().__init__(service=service)
        self.connectable = True