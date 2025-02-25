from device import Device

class Tablet(Device):
    def __init__(self, name, price, stock, warranty, screen_res, weight):
        super().__init__(name, price, stock, warranty)
        self.screen_res = screen_res
        self.weight = weight

    def __str__(self):
        return f'{super().__str__()}, Resolution: {self.screen_res} pixels, Weight: {self.weight} kg \n'

    def browse_internet(self):
        return "Browsing the internet..."

    def use_touchscreen(self):
        return "Using touchscreen..."
