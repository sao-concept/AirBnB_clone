#!/usr/bin/python3

import json
import unittest

from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))

    def test_default_values(self):
        self.assertEqual(self.state.name, "")

    def test_str_method(self):
        expected_str = "[{}] ({}) {}".format(
            self.state.__class__.__name__, self.state.id, self.state.name
        )
        self.assertEqual(str(self.state), expected_str)

    def test_to_dict_method(self):
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)
        self.assertIsInstance(state_dict['name'], str)

    def test_json_serialization(self):
        state_dict = self.state.to_dict()
        state_json = json.dumps(state_dict)
        new_state = State(**json.loads(state_json))
        self.assertIsInstance(new_state, State)
        self.assertEqual(self.state.id, new_state.id)
        self.assertEqual(self.state.created_at, new_state.created_at)
        self.assertEqual(self.state.updated_at, new_state.updated_at)
        self.assertEqual(self.state.name, new_state.name)

if __name__ == '__main__':
    unittest.main()
