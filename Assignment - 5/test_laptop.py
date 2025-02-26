import unittest
from laptop import Laptop

class TestLaptop(unittest.TestCase):
    def test_laptop_creation(self):
        laptop = Laptop("MacBook", 2000, 5, 24, 16, 3.2)
        self.assertEqual(laptop.ram, 16)
        self.assertEqual(laptop.processor, 3.2)

    def test_run_program(self):
        laptop = Laptop("MacBook", 2000, 5, 24, 16, 3.2)
        self.assertEqual(laptop.run_program(), "Running a program")

    def test_use(self):
        laptop = Laptop("MacBook", 2000, 5, 24, 16, 3.2)
        self.assertEqual(laptop.use_keyboard(), "Using on keyboard")

    def test_str(self):
        laptop = Laptop("MacBook", 2000, 5, 24, 16, 3.2)
        expected = "Device name: MacBook, Price: $2000, Stock: 5, Warranty: 24 months, RAM: 16GB, Processor speed: 3.2GHz.\n"
        self.assertEqual(laptop.__str__(), expected)
