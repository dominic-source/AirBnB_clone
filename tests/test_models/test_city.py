#!/usr/bin/python3
"""This defines unittest for models/user.py"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """unittest for testing user"""

    def test_without_args(self):
        self.assertEqual(City, type(City()))

    def test_new_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_two_cities_unique_ids(self):
        my_cy1 = City()
        my_cy2 = City()
        self.assertNotEqual(my_cy1.id, my_cy2.id)

    def test_to_dict_keys(self):
        my_cy = City()
        self.assertIn("id", my_cy.to_dict())
        self.assertIn("created_at", my_cy.to_dict())
        self.assertIn("updated_at", my_cy.to_dict())
        self.assertIn("__class__", my_cy.to_dict())
