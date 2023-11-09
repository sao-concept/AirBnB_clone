#!/usr/bin/python3

import json
import unittest

from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_default_values(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_str_method(self):
        expected_str = "[{}] ({}) {} - {}".format(
            self.review.__class__.__name__, self.review.id, self.review.text, self.review.place_id
        )
        self.assertEqual(str(self.review), expected_str)

    def test_to_dict_method(self):
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)
        self.assertIsInstance(review_dict['place_id'], str)
        self.assertIsInstance(review_dict['user_id'], str)
        self.assertIsInstance(review_dict['text'], str)

    def test_json_serialization(self):
        review_dict = self.review.to_dict()
        review_json = json.dumps(review_dict)
        new_review = Review(**json.loads(review_json))
        self.assertIsInstance(new_review, Review)
        self.assertEqual(self.review.id, new_review.id)
        self.assertEqual(self.review.created_at, new_review.created_at)
        self.assertEqual(self.review.updated_at, new_review.updated_at)
        self.assertEqual(self.review.place_id, new_review.place_id)
        self.assertEqual(self.review.user_id, new_review.user_id)
        self.assertEqual(self.review.text, new_review.text)

if __name__ == '__main__':
    unittest.main()
