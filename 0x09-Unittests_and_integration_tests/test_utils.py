#!/usr/bin/env python3
"""All the tests from everywhere have gathered here"""
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ im just picturing a group of old school maps huddled together """
    @parameterized([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        """checks nested map return"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
