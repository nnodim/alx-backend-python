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
    def test_get_json(self, url, test_payload):
        """A method to test that get_json returns the expected result."""
        mock_get = Mock()
        mock_get.json.return_value = test_payload
        with patch('requests.get', return_value=mock_get):
            response = get_json(url)
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """
    A class with a method and a memoized property
    """

    def test_memoize(self):
        """Test memoize"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        test_instance = TestClass()
        with patch.object(TestClass, 'a_method') as mock:
            mock.return_value = 42

            result1 = test_instance.a_property
            result2 = test_instance.a_property
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
