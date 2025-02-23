import unittest
import pytest
from datetime import datetime
from user_util import UserUtil
from user import User

class TestUser(unittest.TestCase):
    def test_user_initialization(self):
        """Test if User is initialized correctly"""
        user = User(user_id=1, name="Test", surname="User", birthday=(2000, 1, 1))
        assert user.user_id == 1
        assert user.name == "Test"
        assert user.surname == "User"
        assert user.birthday == (2000, 1, 1)

    def test_get_age(self):
        user = User(user_id=2, name="Test", surname="User", birthday=(2000, 1, 1))

        today = datetime.today()
        expected_age = today.year - 2000
        if today.month < 1 or (today.month == 1 and today.day < 1):
            expected_age -= 1

        assert user.get_age() == expected_age

    def test_get_details(self):
        user = User(3, 'Nurali', 'Bakytbek', (2005, 8, 22), email=None, password=None)
        expected_details = f"User ID: 3\nName: Nurali Bakytbek\nBirthday: (2005, 8, 22) \nPassword: None\nEmail: None"

        assert user.get_details() == expected_details

