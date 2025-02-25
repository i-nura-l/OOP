class Device:
    def __init__(self, name, price, stock, warranty_period):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period

    def display_info(self):
        return f"{self.name} - ${self.price}, Stock: {self.stock}, Warranty: {self.warranty_period} months"

    def __str__(self):
        return self.display_info()

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)

    def is_available(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount
            return True
        return False


class Smartphone(Device):
    def __init__(self, name, price, stock, warranty_period, screen_size, battery_life):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return f"{super().__str__()}, Screen: {self.screen_size} inches, Battery: {self.battery_life} hours"

    def make_call(self):
        return "Making a call..."

    def install_app(self):
        return "Installing an app..."


class Laptop(Device):
    def __init__(self, name, price, stock, warranty_period, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return f"{super().__str__()}, RAM: {self.ram_size}GB, Processor: {self.processor_speed}GHz"

    def run_program(self):
        return "Running a program..."

    def use_keyboard(self):
        return "Typing on keyboard..."


class Tablet(Device):
    def __init__(self, name, price, stock, warranty_period, screen_resolution, weight):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def __str__(self):
        return f"{super().__str__()}, Resolution: {self.screen_resolution}, Weight: {self.weight}g"

    def browse_internet(self):
        return "Browsing the internet..."

    def use_touchscreen(self):
        return "Using touchscreen..."


class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            return True
        return False

    def remove_device(self, device, amount):
        for item in self.items:
            if item[0] == device:
                self.items.remove(item)
                self.total_price -= device.price * amount
                return True
        return False

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        for device, amount in self.items:
            print(f"{device.name} x{amount} - ${device.price * amount}")

    def checkout(self):
        for device, amount in self.items:
            if not device.reduce_stock(amount):
                return "Checkout failed: Not enough stock"
        self.items = []
        self.total_price = 0
        return "Purchase successful!"
