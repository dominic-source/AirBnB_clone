#!/usr/bin/python3
"""Defines unittest for models/engine/file_storage.py"""

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instances(unittest.TestCase):
    """This class will test file storage"""

    def test_FileStorage_instantiation_without_arg(self):
        """This method tests the file on file storage"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_file_path_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_does_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests to test methods of the FileStorage."""

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        my_bm = BaseModel()
        my_us = User()
        my_st = State()
        my_pl = Place()
        my_cy = City()
        my_am = Amenity()
        my_rv = Review()
        models.storage.new(my_bm)
        models.storage.new(my_us)
        models.storage.new(my_st)
        models.storage.new(my_pl)
        models.storage.new(my_cy)
        models.storage.new(my_am)
        models.storage.new(my_rv)
        self.assertIn("BaseModel." + my_bm.id, models.storage.all().keys())
        self.assertIn(my_bm, models.storage.all().values())
        self.assertIn("User." + my_us.id, models.storage.all().keys())
        self.assertIn(my_us, models.storage.all().values())
        self.assertIn("State." + my_st.id, models.storage.all().keys())
        self.assertIn(my_st, models.storage.all().values())
        self.assertIn("Place." + my_pl.id, models.storage.all().keys())
        self.assertIn(my_pl, models.storage.all().values())
        self.assertIn("City." + my_cy.id, models.storage.all().keys())
        self.assertIn(my_cy, models.storage.all().values())
        self.assertIn("Amenity." + my_am.id, models.storage.all().keys())
        self.assertIn(my_am, models.storage.all().values())
        self.assertIn("Review." + my_rv.id, models.storage.all().keys())
        self.assertIn(my_rv, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        my_bm = BaseModel()
        my_us = User()
        my_st = State()
        my_pl = Place()
        my_cy = City()
        my_am = Amenity()
        my_rv = Review()
        models.storage.new(my_bm)
        models.storage.new(my_us)
        models.storage.new(my_st)
        models.storage.new(my_pl)
        models.storage.new(my_cy)
        models.storage.new(my_am)
        models.storage.new(my_rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + my_bm.id, save_text)
            self.assertIn("User." + my_us.id, save_text)
            self.assertIn("State." + my_st.id, save_text)
            self.assertIn("Place." + my_pl.id, save_text)
            self.assertIn("City." + my_cy.id, save_text)
            self.assertIn("Amenity." + my_am.id, save_text)
            self.assertIn("Review." + my_rv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        my_bm = BaseModel()
        my_us = User()
        my_st = State()
        my_pl = Place()
        my_cy = City()
        my_am = Amenity()
        my_rv = Review()
        models.storage.new(my_bm)
        models.storage.new(my_us)
        models.storage.new(my_st)
        models.storage.new(my_pl)
        models.storage.new(my_cy)
        models.storage.new(my_am)
        models.storage.new(my_rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + my_bm.id, objs)
        self.assertIn("User." + my_us.id, objs)
        self.assertIn("State." + my_st.id, objs)
        self.assertIn("Place." + my_pl.id, objs)
        self.assertIn("City." + my_cy.id, objs)
        self.assertIn("Amenity." + my_am.id, objs)
        self.assertIn("Review." + my_rv.id, objs)
