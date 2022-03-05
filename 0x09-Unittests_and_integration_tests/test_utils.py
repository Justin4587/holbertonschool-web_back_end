#!/usr/bin/env python3
"""All the tests from everywhere have gathered here"""
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """ im just picturing a group of old school maps huddled together """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        """checks nested map return"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """checks exception status"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """testing function ability to get json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])

    def test_get_json(self, test_url, test_payload):
        """its in the def"""
        with patch("requests.get") as mock:
            mock().json.return_value = test_payload
            mock.assert_called_once()
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
