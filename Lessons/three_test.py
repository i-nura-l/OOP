import unittest
from three_mathutil import Mathutil


class TestMathutil(unittest.TestCase):

   def test_even(self):
       self.assertTrue(Mathutil.is_even(24))
       self.assertFalse(Mathutil.is_even(23))


   def test_prime(self):
       self.assertEqual(Mathutil.is_prime(25), False)
       self.assertEqual(Mathutil.is_prime(29), True)
       self.assertEqual(Mathutil.is_prime(2), True)

'''


class TestMathUtil(unittest.TestCase):

   def test_sum(self):
       self.assertEqual( Mathutil.sum(2, 3), 5, ' Something wrong ' )
       self.assertNotEqual( Mathutil.sum(0,0), 1)

   def test_div(self):
       self.assertAlmostEqual(Mathutil.div(10, 3), 3.333, delta=0.000001)
       #self.assertEqual( Mathutil.div(10, 3), 3.333, ' test with decimals ')

   def test_prime(self):
       self.assertTrue( Mathutil.is_prime(23) )
       self.assertFalse( Mathutil.is_prime(29) )
       
'''