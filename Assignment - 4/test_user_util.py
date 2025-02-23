import unittest
from user_util import UserUtil

class TestUserUtil(unittest.TestCase):
    def test_generate_password(self):
        password = UserUtil.generate_password()
        self.assertTrue(UserUtil.is_strong_password(password))

    def test_is_strong_password(self):
        self.assertTrue(UserUtil.is_strong_password("A1@strong"))
        self.assertFalse(UserUtil.is_strong_password("weakpass"))
        self.assertFalse(UserUtil.is_strong_password("NOLOWER1!"))
        self.assertFalse(UserUtil.is_strong_password("noupper1!"))
        self.assertFalse(UserUtil.is_strong_password("NoNumber!"))
        self.assertFalse(UserUtil.is_strong_password("NoSpecial1"))

    def test_generate_email(self):
        email = UserUtil.generate_email("John", "Doe", "example.com")
        self.assertEqual(email, "john.doe@gmailexample.com")

    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertTrue(isinstance(user_id, int))
        self.assertEqual(len(str(user_id)), 9)

    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("test.user@example.com"))
        self.assertFalse(UserUtil.validate_email("invalid-email"))