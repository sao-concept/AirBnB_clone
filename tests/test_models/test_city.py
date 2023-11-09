#!/usr/bin/python3

import json
import unittest

from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_state_id_attribute(self):
        self.assertEqual(self.city.state_id, "")

    def test_name_attribute(self):
        self.assertEqual(self.city.name, "")

    def test_str_method(self):
        expected_str = "[{}] ({}) {} - {}".format(
            self.city.__class__.__name__, self.city.id, self.city.name, self.city.state_id
        )
        self.assertEqual(str(self.city), expected_str)

    def test_to_dict_method(self):
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)
        self.assertIsInstance(city_dict['state_id'], str)
        self.assertIsInstance(city_dict['name'], str)

    def test_json_serialization(self):
        city_dict = self.city.to_dict()
        city_json = json.dumps(city_dict)
        new_city = City(**json.loads(city_json))
        self.assertIsInstance(new_city, City)
        self.assertEqual(self.city.id, new_city.id)
        self.assertEqual(self.city.created_at, new_city.created_at)
        self.assertEqual(self.city.updated_at, new_city.updated_at)
        self.assertEqual(self.city.state_id, new_city.state_id)
        self.assertEqual(self.city.name, new_city.name)

if __name__ == '__main__':
    unittest.main()
