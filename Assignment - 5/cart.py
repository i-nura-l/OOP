


class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        pair = (device, amount)
        # pair [0] - device
        # pair [1] - amount
        self.items.append(pair)
        self.total_price += device.price * amount



    def remove_device(self, device, amount):
        pair = (device, amount)
        # search pair from self.items, if found delete it

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        for pair in self.items:
            device = pair [0]
            amount = pair [1]
            print(device, ',Amount:', amount)

    def checkout(self):
        for pair in self.items:
            device = pair [0]
            amount = pair [1]

            if ( device.is_available(amount)):
                device.reduce_stock(amount)
                print(device, ', Amount: ', amount)
            else:
                # write a
                pass


        print('Total price: ', self.total_price)