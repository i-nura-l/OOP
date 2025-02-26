import unittest
from tablet import Tablet

class TestTablet(unittest.TestCase):
    def test_tablet_creation(self):
        tablet = Tablet("Samsung Tablet", 500, 10, 12, "2048x1536", 500)
        self.assertEqual(tablet.screen_res, "2048x1536")
        self.assertEqual(tablet.weight, 500)

    def test_browse_internet(self):
        tablet = Tablet("Samsung Tablet", 500, 10, 12, "2048x1536", 500)
        self.assertEqual(tablet.browse_internet(), "Browsing the internet...")

    def test_str(self):
        tablet = Tablet("Samsung Tablet", 500, 10, 12, "2048x1536", 500)
        expected = "Device name: Samsung Tablet, Price: $500, Stock: 10, Warranty: 12 months, Resolution: 2048x1536 pixels, Weight: 500 kg \n"
        self.assertEqual(tablet.__str__(), expected)
