#!/usr/bin/python3

import json
import unittest

from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_default_values(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str_method(self):
        expected_str = "[{}] ({}) {} {}".format(
            self.user.__class__.__name__, self.user.id, self.user.first_name, self.user.last_name
        )
        self.assertEqual(str(self.user), expected_str)

    def test_to_dict_method(self):
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)
        self.assertIsInstance(user_dict['email'], str)
        self.assertIsInstance(user_dict['password'], str)
        self.assertIsInstance(user_dict['first_name'], str)
        self.assertIsInstance(user_dict['last_name'], str)

    def test_json_serialization(self):
        user_dict = self.user.to_dict()
        user_json = json.dumps(user_dict)
        new_user = User(**json.loads(user_json))
        self.assertIsInstance(new_user, User)
        self.assertEqual(self.user.id, new_user.id)
        self.assertEqual(self.user.created_at, new_user.created_at)
        self.assertEqual(self.user.updated_at, new_user.updated_at)
        self.assertEqual(self.user.email, new_user.email)
        self.assertEqual(self.user.password, new_user.password)
        self.assertEqual(self.user.first_name, new_user.first_name)
        self.assertEqual(self.user.last_name, new_user.last_name)

if __name__ == '__main__':
    unittest.main()
