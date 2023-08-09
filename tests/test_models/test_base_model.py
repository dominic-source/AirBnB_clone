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
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertLess(base1.created_at, base2.created_at)
