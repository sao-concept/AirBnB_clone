#!/usr/bin/python3

import json
import unittest

from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_attributes(self):
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_default_values(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_str_method(self):
        expected_str = "[{}] ({}) {} - {}".format(
            self.place.__class__.__name__, self.place.id, self.place.name, self.place.city_id
        )
        self.assertEqual(str(self.place), expected_str)

    def test_to_dict_method(self):
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)
        self.assertIsInstance(place_dict['city_id'], str)
        self.assertIsInstance(place_dict['user_id'], str)
        self.assertIsInstance(place_dict['name'], str)
        self.assertIsInstance(place_dict['description'], str)
        self.assertIsInstance(place_dict['number_rooms'], int)
        self.assertIsInstance(place_dict['number_bathrooms'], int)
        self.assertIsInstance(place_dict['max_guest'], int)
        self.assertIsInstance(place_dict['price_by_night'], int)
        self.assertIsInstance(place_dict['latitude'], float)
        self.assertIsInstance(place_dict['longitude'], float)
        self.assertIsInstance(place_dict['amenity_ids'], list)

    def test_json_serialization(self):
        place_dict = self.place.to_dict()
        place_json = json.dumps(place_dict)
        new_place = Place(**json.loads(place_json))
        self.assertIsInstance(new_place, Place)
        self.assertEqual(self.place.id, new_place.id)
        self.assertEqual(self.place.created_at, new_place.created_at)
        self.assertEqual(self.place.updated_at, new_place.updated_at)
        self.assertEqual(self.place.city_id, new_place.city_id)
        self.assertEqual(self.place.user_id, new_place.user_id)
        self.assertEqual(self.place.name, new_place.name)
        self.assertEqual(self.place.description, new_place.description)
        self.assertEqual(self.place.number_rooms, new_place.number_rooms)
        self.assertEqual(self.place.number_bathrooms, new_place.number_bathrooms)
        self.assertEqual(self.place.max_guest, new_place.max_guest)
        self.assertEqual(self.place.price_by_night, new_place.price_by_night)
        self.assertEqual(self.place.latitude, new_place.latitude)
        self.assertEqual(self.place.longitude, new_place.longitude)
        self.assertEqual(self.place.amenity_ids, new_place.amenity_ids)

if __name__ == '__main__':
    unittest.main()
