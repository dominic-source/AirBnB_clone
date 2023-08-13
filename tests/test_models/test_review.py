#!/usr/bin/python3
"""This defines unittest for models/user.py"""

import os
import models
import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """unittest for testing user"""

    def test_no_arg(self):
        self.assertEqual(Review, type(Review()))

    def test_new_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_reviews_unique_ids(self):
        my_rv1 = Review()
        my_rv2 = Review()
        self.assertNotEqual(my_rv1.id, my_rv2.id)
