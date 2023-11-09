#!/usr/bin/python3

import json
import os
import unittest

from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Tear down test environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new(self):
        """Test the new method of FileStorage."""
        new_model = BaseModel()
        storage.new(new_model)
        objects = storage.all()
        self.assertIn("BaseModel.{}".format(new_model.id), objects)

    def test_save_reload(self):
        """Test saving and reloading from JSON file."""
        new_model = BaseModel()
        new_model.save()
        storage.reload()
        objects = storage.all()
        self.assertIn("BaseModel.{}".format(new_model.id), objects)

    def test_save_file_content(self):
        """Test if the file storage file has correct content."""
        new_model = BaseModel()
        storage.new(new_model)
        storage.save()
        with open(self.file_path, "r") as file:
            content = file.read()
            self.assertIn("BaseModel.{}".format(new_model.id), content)

    def test_reload_no_file(self):
        """Test reloading with no existing file."""
        storage.reload()
        objects = storage.all()
        self.assertEqual(len(objects), 0)

    def test_save_reload_attributes(self):
        """Test if attributes are correctly loaded after reload."""
        new_model = BaseModel()
        new_model.save()
        storage.reload()
        loaded_model = storage.find("BaseModel", new_model.id)
        self.assertEqual(new_model.id, loaded_model.id)
        self.assertEqual(new_model.created_at, loaded_model.created_at)
        self.assertEqual(new_model.updated_at, loaded_model.updated_at)

    def test_save_reload_custom_attributes(self):
        """Test if custom attributes are correctly loaded after reload."""
        class CustomModel(BaseModel):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.custom_attribute = "test_value"

        new_model = CustomModel()
        new_model.save()
        storage.reload()
        loaded_model = storage.find("CustomModel", new_model.id)
        self.assertEqual(loaded_model.custom_attribute, "test_value")

    def test_update(self):
        """Test the update method of FileStorage."""
        new_model = BaseModel()
        storage.new(new_model)
        storage.update("BaseModel", new_model.id, "name", "updated_name")
        updated_model = storage.find("BaseModel", new_model.id)
        self.assertEqual(updated_model.name, "updated_name")

    def test_update_non_existing_instance(self):
        """Test updating non-existing instance."""
        with self.assertRaises(KeyError):
            storage.update("BaseModel", "non_existing_id", "name", "updated_name")

    def test_delete(self):
        """Test the delete method of FileStorage."""
        new_model = BaseModel()
        storage.new(new_model)
        storage.save()
        storage.delete("BaseModel", new_model.id)
        deleted_model = storage.find("BaseModel", new_model.id)
        self.assertIsNone(deleted_model)

    def test_delete_non_existing_instance(self):
        """Test deleting non-existing instance."""
        with self.assertRaises(KeyError):
            storage.delete("BaseModel", "non_existing_id")

if __name__ == "__main__":
    unittest.main()
