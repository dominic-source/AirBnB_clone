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
        self.assertLessEqual(self.base.created_at, base2.created_at)

    def test_different_updated_at(self):
        base2 = BaseModel()
        self.assertLessEqual(self.base.updated_at, base2.updated_at)

    def test_save_updates_updated_at(self):
        check = self.base.updated_at
        self.base.save()
        self.assertLessEqual(check, self.base.updated_at)

    def test_id_is_str(self):
        self.assertEqual(str, type(self.base.id))

    def test_return_str(self):
        self.assertIn(type(self.base).__name__, self.base.__str__())
        self.assertIn(self.base.id, self.base.__str__())
        self.assertIn(str(self.base.__dict__), self.base.__str__())

    def test_return_str_custom_id(self):
        self.base.id = "random123"
        self.assertIn("random123", self.base.__str__())

    def test_class_in_my_dict(self):
        self.assertIn('__class__', self.base.to_dict())

    def test_updated_at_and_created_at_is_isoformat(self):
        my_dict = self.base.to_dict()
        self.assertEqual(str, type(my_dict['updated_at']))
        self.assertEqual(str, type(my_dict['created_at']))

    def test_to_dict_type(self):
        blake = BaseModel()
        self.assertTrue(dict, type(blake.to_dict()))

    def test_to_dict_has_correct_keys(self):
        blake = BaseModel()
        self.assertIn("id", blake.to_dict())
        self.assertIn("created_at", blake.to_dict())
        self.assertIn("updated_at", blake.to_dict())
        self.assertIn("__class__", blake.to_dict())

    def test_to_dict_has_new_attributes(self):
        blake = BaseModel()
        blake.name = "Ohafia"
        blake.my_number = 20493
        self.assertIn("name", blake.to_dict())
        self.assertIn("my_number", blake.to_dict())

    def test_args_unused(self):
        blake = BaseModel(None)
        self.assertNotIn(None, blake.__dict__.values())

    def test_instantiation_with_kwargs(self):
        tm = datetime.now()
        tm_iso = tm.isoformat()
        bm = BaseModel(id="WhoAmI", created_at=tm_iso, updated_at=tm_iso)
        self.assertEqual(bm.id, "WhoAmI")
        self.assertEqual(bm.created_at, tm)
        self.assertEqual(bm.updated_at, tm)
