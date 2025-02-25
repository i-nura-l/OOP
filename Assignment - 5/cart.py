class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            return True
        else:
            return print(f'Not sufficient stock of {device.name}. Try ordering less.')

    def remove_device(self, device, amount):
        for i, (item, qty) in enumerate(self.items):
            if item == device:
                if qty > amount:
                    self.items[i] = (item, qty - amount)
                    self.total_price -= device.price * amount
                    #self.add_device(device, qty - amount)
                else:
                    self.items.pop(i)
                    self.total_price -= device.price * qty
                return True

        return False

    def get_total_price(self):
        return print(f'Total price: ${self.total_price}')

    def print_items(self):
        '''pair = (device, amount)
        # pair [0] - device
        # pair [1] - amount
        self.items.append(pair)
        self.total_price += device.price * amount
        for pair in self.items:
            device = pair [0]
            amount = pair [1]
            print(device, ',Amount:', amount)'''
        for device, amount in self.items:
            print(f'{device.name} x{amount} - ${device.price * amount}')

    def checkout(self):
        for device, amount in self.items:
            if not device.is_available(amount):
                return f"Checkout failed: Not enough stock for {device.name}."
        print('Total price: ', self.total_price)

        # Reduce stock for all items in the cart
        for device, amount in self.items:
            device.reduce_stock(amount)

        # Clear the cart after purchase
        self.items = []
        self.total_price = 0
        return "Purchase successful! \n"
