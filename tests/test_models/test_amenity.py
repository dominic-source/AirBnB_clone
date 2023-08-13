#!/usr/bin/python3
"""This defines unittest for models/user.py"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """unittest for testing user"""

    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_two_amenities_have_different_created_at(self):
        my_am1 = Amenity()
        sleep(0.07)
        my_am2 = Amenity()
        self.assertLess(my_am1.created_at, my_am2.created_at)

    def test_two_amenities_have_different_updated_at(self):
        my_am1 = Amenity()
        sleep(0.07)
        my_am2 = Amenity()
        self.assertLess(my_am1.updated_at, my_am2.updated_at)

    def test_instantiates_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        am = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(am.id, "345")
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)
