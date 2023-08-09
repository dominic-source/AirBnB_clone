#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime

class TestBase(unittest.TestCase):
    """class of functions to run unittests"""

    def test_save(self):
        """test the save function"""
        sv = BaseModel()
        sv.save()
        self.assertEqual(sv.updated_at, datetime.now())
