#!/usr/bin/python3
"""Defines unittest for base_model"""

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
        """unittest for created_at is datetime"""

        self.assertEqual(datetime, type(self.base.created_at))

    def test_updated_at_is_datetime(self):
        """unittest for updated_at is datetime"""

        self.assertEqual(datetime, type(self.base.updated_at))

    def test_unique_id(self):
        """unittest to check id is unique"""

        base2 = BaseModel()
        self.assertNotEqual(self.base.id, base2.id)

    def test_different_created_at(self):
        """unittest checking different created_at"""

        base2 = BaseModel()
        self.assertLessEqual(self.base.created_at, base2.created_at)

    def test_different_updated_at(self):
        """unittest to check different updated_at"""

        base2 = BaseModel()
        self.assertLessEqual(self.base.updated_at, base2.updated_at)

    def test_save_updates_updated_at(self):
        """unittest to check save updates updated_at"""

        check = self.base.updated_at
        self.base.save()
        self.assertLessEqual(check, self.base.updated_at)

    def test_id_is_str(self):
        """unittest that id is a str"""

        self.assertEqual(str, type(self.base.id))

    def test_return_str(self):
        """unittest to check return is str"""

        self.assertIn(type(self.base).__name__, self.base.__str__())
        self.assertIn(self.base.id, self.base.__str__())
        self.assertIn(str(self.base.__dict__), self.base.__str__())

    def test_return_str_custom_id(self):
        """unit test custom_id in return"""

        self.base.id = "random123"
        self.assertIn("random123", self.base.__str__())

    def test_class_in_my_dict(self):
        """unittest class exist in my_dict"""

        self.assertIn('__class__', self.base.to_dict())

    def test_updated_at_and_created_at_is_isoformat(self):
        """unittest updated_at and created_at is isoformat"""

        my_dict = self.base.to_dict()
        self.assertEqual(str, type(my_dict['updated_at']))
        self.assertEqual(str, type(my_dict['created_at']))

    def test_to_dict_type(self):
        """unittest for type of to_dict"""

        blake = BaseModel()
        self.assertTrue(dict, type(blake.to_dict()))

    def test_to_dict_has_correct_keys(self):
        """unittest that to_dict has correct keys"""

        blake = BaseModel()
        self.assertIn("id", blake.to_dict())
        self.assertIn("created_at", blake.to_dict())
        self.assertIn("updated_at", blake.to_dict())
        self.assertIn("__class__", blake.to_dict())

    def test_to_dict_has_new_attributes(self):
        """unittest that to_dict has new attributes"""

        blake = BaseModel()
        blake.name = "Ohafia"
        blake.my_number = 20493
        self.assertIn("name", blake.to_dict())
        self.assertIn("my_number", blake.to_dict())

    def test_args_unused(self):
        """unittest if args is not used"""

        blake = BaseModel(None)
        self.assertNotIn(None, blake.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """unittest instantiation with kwargs"""

        tm = datetime.now()
        tm_iso = tm.isoformat()
        bm = BaseModel(id="WhoAmI", created_at=tm_iso, updated_at=tm_iso)
        self.assertEqual(bm.id, "WhoAmI")
        self.assertEqual(bm.created_at, tm)
        self.assertEqual(bm.updated_at, tm)

    def test_update_and_create_time(self):
        """unittest to check file created before updated"""
        my_bm = BaseModel()
        my_bm.save()
        self.assertLess(my_bm.created_at, my_bm.updated_at)


if __name__ == "__main__":
    unittest.main()
