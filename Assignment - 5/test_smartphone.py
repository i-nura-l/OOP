import unittest
import pytest
from smartphone import Smartphone
from device import Device

class TestSmartphone(unittest.TestCase):
    def test_smartphone_creation(self):
        smart = Smartphone('iPhone', 800, 90, 10, 6, 8)
        self.assertEqual(smart.name, "iPhone")
        self.assertEqual(smart.screen_size, 6)
        self.assertEqual(smart.battery_life, 8)

    def test_make_call(self):
        smart = Smartphone('iPhone', 800, 90, 10, 6, 8)
        self.assertEqual(smart.make_call(), "iPhone can make a call.")

    def test_install_app(self):
        smart = Smartphone('iPhone', 800, 90, 10, 6, 8)
        self.assertEqual(smart.install_app(), "iPhone can install apps.")

# not matching spaces...
    def test_str(self):
        smart = Smartphone('iPhone', 800, 90, 10, 6, 8)
        self.assertEqual(smart.__str__(), "Device name: iPhone, Price: $800, Stock: 90, Warranty: 10 months, Screen Size: 6 inches, Battery Life: 8 hours.\n")


