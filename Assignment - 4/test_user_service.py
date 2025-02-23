import unittest
import pytest
from datetime import datetime
from user_util import UserUtil
from user import User
from user_service import UserService

class TestUserService(unittest.TestCase):
    def test_add(self):
        user = User(123456789, "Test", "User", (2000, 1, 1))
        UserService.add_user(user)

    def test_find(self):
        user = User(123456789, "Test", "User", (2000, 1, 1))
        UserService.add_user(user)
        self.assertEqual(UserService.find_user(123456789), user)

    def test_delete_user(self):
        user = User(987654321, "Delete", "User", (1995, 5, 24))
        UserService.add_user(user)
        UserService.delete_user(987654321)
        self.assertIsNone(UserService.find_user(987654321))

    def test_update_user(self):
        user = User(111222333, "Old", "Name", (1990, 3, 15))
        UserService.add_user(user)
        UserService.update_user(111222333, name= "New")
        updated_user = UserService.find_user(111222333)
        self.assertEqual(updated_user.name, "New")

    def test_get_number(self):
        UserService.users.clear()
        user1 = User(222333444, "User1", "Test", (1985, 7, 10))
        user2 = User(333444555, "User2", "Test", (1992, 8, 20))
        UserService.add_user(user1)
        UserService.add_user(user2)
        self.assertEqual(UserService.get_number(), 2)