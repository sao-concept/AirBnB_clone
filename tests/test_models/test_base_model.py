#!/usr/bin/python3

import json
import unittest
from datetime import datetime

from models.base_model import BaseModel

# Test Cases
class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_generation(self):
        new_model = BaseModel()
        self.assertNotEqual(self.base_model.id, new_model.id)

    def test_created_at_type(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str_method(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_json_serialization(self):
        model_dict = self.base_model.to_dict()
        model_json = json.dumps(model_dict)
        new_model = BaseModel(**json.loads(model_json))
        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(self.base_model.id, new_model.id)
        self.assertEqual(self.base_model.created_at, new_model.created_at)
        self.assertEqual(self.base_model.updated_at, new_model.updated_at)

if __name__ == '__main__':
    unittest.main()
