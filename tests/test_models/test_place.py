#!/usr/bin/python3
"""This defines unittest for models/user.py"""

import os
import models
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """unittest for testing user"""

    def test_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_new_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(Place().id))

    def test_places_unique_ids(self):
        my_pl1 = Place()
        my_pl2 = Place()
        self.assertNotEqual(my_pl1.id, my_pl2.id)

    def test_args_not_nused(self):
        my_pl = Place(None)
        self.assertNotIn(None, my_pl.__dict__.values())
