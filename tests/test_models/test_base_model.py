#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime

class TestBase(unittest.TestCase):
    """class of functions to run unittests"""

    def setUp(self):
        """function to initialize BaseModel"""
        self.base = BaseModel()

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(self.base.created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(self.base.updated_at))

    def test_unique_id(self):
        base2 = BaseModel()
        self.assertNotEqual(self.base.id, base2.id)

    def test_different_created_at(self):
        base2 = BaseModel()
        self.assertLess(self.base.created_at, base2.created_at)

    def test_different_updated_at(self):
        base2 = BaseModel()
        self.assertLess(self.base.updated_at, base2.updated_at)

    def test_save_updates_updated_at(self):
        check = self.base.updated_at
        self.base.save()
        self.assertLess(check, self.base.updated_at)
