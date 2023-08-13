#!/usr/bin/python3
"""This defines unittest for models/user.py"""

import os
import models
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """unittest for testing user"""

    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_new_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_users_unique_ids(self):
        my_us1 = User()
        my_us2 = User()
        self.assertNotEqual(my_us1.id, my_us2.id)
