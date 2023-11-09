#!/usr/bin/python3

import unittest
import json
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_name_attribute(self):
        self.assertEqual(self.amenity.name, "")

    def test_str_method(self):
        expected_str = "[{}] ({}) {}".format(self.amenity.__class__.__name__, self.amenity.id, self.amenity.name)
        self.assertEqual(str(self.amenity), expected_str)

    def test_to_dict_method(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)
        self.assertIsInstance(amenity_dict['name'], str)

    def test_json_serialization(self):
        amenity_dict = self.amenity.to_dict()
        amenity_json = json.dumps(amenity_dict)
        new_amenity = Amenity(**json.loads(amenity_json))
        self.assertIsInstance(new_amenity, Amenity)
        self.assertEqual(self.amenity.id, new_amenity.id)
        self.assertEqual(self.amenity.created_at, new_amenity.created_at)
        self.assertEqual(self.amenity.updated_at, new_amenity.updated_at)
        self.assertEqual(self.amenity.name, new_amenity.name)

if __name__ == '__main__':
    unittest.main()
