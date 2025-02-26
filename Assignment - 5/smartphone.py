
from device import Device
class Smartphone(Device):
    def __init__(self, name, price, stock, warranty, screen_size, battery_life):
        super().__init__(name, price, stock, warranty)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return f'{super().__str__()}, Screen Size: {self.screen_size} inches, Battery Life: {self.battery_life} hours.\n'

    def make_call(self):
        return f'{self.name} can make a call.'

    def install_app(self):
        return f'{self.name} can install apps.'