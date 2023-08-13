#!/usr/bin/python3
"""This defines unittest for models/user.py"""

import os
import models
import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """unittest for testing user"""

    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_new_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_states_unique_ids(self):
        my_st1 = State()
        my_st2 = State()
        self.assertNotEqual(my_st1.id, my_st2.id)
