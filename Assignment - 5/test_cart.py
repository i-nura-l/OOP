import unittest
from cart import Cart
from smartphone import Smartphone
from laptop import Laptop

class TestCart(unittest.TestCase):
    def setUp(self):
        self.smartphone = Smartphone('iPhone', 800, 10, 10, 6, 8)
        self.laptop = Laptop("MacBook", 2000, 5, 24, 16, 3.2)
        self.cart = Cart()

    def test_add_device(self):
        self.cart.add_device(self.smartphone, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.total_price, 1600)

    def test_remove_device(self):
        self.cart.add_device(self.smartphone, 3)
        self.cart.remove_device(self.smartphone, 1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0][1], 2)

    def test_checkout(self):
        self.cart.add_device(self.smartphone, 2)
        self.cart.add_device(self.laptop, 1)
        result = self.cart.checkout()
        self.assertEqual(result, "Purchase successful! \n")
        self.assertEqual(self.smartphone.stock, 8)
        self.assertEqual(self.laptop.stock, 4)
