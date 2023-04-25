#!/usr/bin/env python3
"""
A unittest module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    A TestAccessNestedMap class that inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        _summary_
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expection):
        """
        _summary_
        """
        with self.assertRaises(expection):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """A class to test the get_json function."""

    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    def test_get_json(self, url, expected_result):
        """A method to test that get_json returns the expected result."""
        mock_get = Mock()
        mock_get.json.return_value = expected_result
        with patch('requests.get', return_value=mock_get):
            response = get_json(url)
            self.assertEqual(response, expected_result)


if __name__ == "__main__":
    unittest.main()
