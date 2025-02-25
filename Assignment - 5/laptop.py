from device import Device

class Laptop(Device):
    def __init__(self, name, price, stock, warranty, ram, processor):
        super().__init__(name, price, stock, warranty)
        self.ram = ram
        self.processor = processor

    def __str__(self):
        return f'{super().__str__()}, RAM: {self.ram}GB, Processor speed: {self.processor}GHz \n'

    def run_program(self):
        return "Running a program"

    def use_keyboard(self):
        return 'Using on keyboard'
