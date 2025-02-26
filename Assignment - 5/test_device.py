import unittest
import pytest
from device import Device

class TestDevice(unittest.TestCase):
    def test_device_creation(self):
        device = Device("Generic Device", 500, 20, 12)
        self.assertEqual(device.name, "Generic Device")
        self.assertEqual(device.price, 500)
        self.assertEqual(device.stock, 20)
        self.assertEqual(device.warranty, 12)

    def test_display_info(self):
        device = Device('Samsung', 200, 10, 3)
        expected_info = f'Device name: Samsung, Price: $200, Stock: 10, Warranty: 3 months'

        assert device.display_info() == expected_info

    def test_apply_discount(self):
        device = Device("Generic Device", 1000, 10, 12)
        device.apply_discount(20)  # 20% discount
        self.assertEqual(device.price, 800)  # 1000 - (1000 * 0.2)

    def test_is_available(self):
        device = Device("Generic Device", 500, 5, 12)
        self.assertTrue(device.is_available(3))
        self.assertFalse(device.is_available(6))  # More than stock


    def test_reduce_stock(self):
        device = Device("Generic Device", 500, 10, 12)
        device.reduce_stock(3)
        self.assertEqual(device.stock, 7)

