#!/usr/bin/python3
"""Test FileStorage documentation and functionality"""

import unittest
import models
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import pep8

classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}

class TestFileStorageDocs(unittest.TestCase):
    """Tests for FileStorage documentation and style"""

    @classmethod
    def setUpClass(cls):
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")

    def test_pep8_conformance_test_file_storage(self):
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")

    def test_file_storage_module_docstring(self):
        self.assertIsNot(file_storage.__doc__, None, "Missing docstring for file_storage.py")
        self.assertTrue(len(file_storage.__doc__) >= 1, "file_storage.py docstring too short")

    def test_file_storage_class_docstring(self):
        self.assertIsNot(FileStorage.__doc__, None, "Missing docstring for FileStorage class")
        self.assertTrue(len(FileStorage.__doc__) >= 1, "FileStorage class docstring too short")

    def test_fs_func_docstrings(self):
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None, f"Missing docstring for {func[0]} method")
            self.assertTrue(len(func[1].__doc__) >= 1, f"{func[0]} method docstring too short")

class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class functionality"""

    @unittest.skipIf(models.storage_t == 'db', "Not testing file storage")
    def test_all_returns_dict(self):
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    @unittest.skipIf(models.storage_t == 'db', "Not testing file storage")
    def test_new(self):
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = f"{instance.__class__.__name__}.{instance.id}"
            storage.new(instance)
            test_dict[instance_key] = instance
            self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    @unittest.skipIf(models.storage_t == 'db', "Not testing file storage")
    def test_save(self):
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = f"{instance.__class__.__name__}.{instance.id}"
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))

    @unittest.skipIf(models.storage_t == 'db', "Not testing file storage")
    def test_get(self):
        state = State()
        state.name = "State_name"
        storage = models.storage
        storage.new(state)
        storage.save()
        self.assertTrue(storage.get(State, state.id))
        self.assertEqual(storage.get(State, state.id), state)
        storage.close()

    @unittest.skipIf(models.storage_t == 'db', "Not testing file storage")
    def test_count(self):
        state = State()
        state.name = "State_name"
        storage = models.storage
        storage.new(state)
        storage.save()
        self.assertTrue(storage.count(State) > 0)

