import unittest
from user_util import UserUtil

class TestUserUtil(unittest.TestCase):
    def test_generate_id(self):
        id = UserUtil.generate_user_id()
        self.assertEqual(len(str(id)), 9)
        self.assertEqual(str(id)[0:2], '24')