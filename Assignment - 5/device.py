class Device:
    def __init__(self, name , price, stock, warranty):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty = warranty


    def __str__(self):
        return f'Device name :{self.name}, Price:{self.price}'

    def apply_discount(self, percentage):
        self.price = self.price - self. price * percentage/100

    def is_available(self, amount):
        if self.stock >=amount:
            return True
        return False

    def reduce_stock(self, amount):
        self.stock = self.stock - amount