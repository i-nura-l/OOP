class Device:
    def __init__(self, name , price, stock, warranty):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty = warranty

    def display_info(self):
        return f'Device name: {self.name}, Price: ${self.price}, Stock: {self.stock}, Warranty: {self.warranty} months'

    def __str__(self):
        return self.display_info()

    def apply_discount(self, percentage):
        self.price -= self. price * (percentage/100)

    def is_available(self, amount):
        if self.stock >=amount:
            return True
        return False

    def reduce_stock(self, amount):
        self.stock -= amount