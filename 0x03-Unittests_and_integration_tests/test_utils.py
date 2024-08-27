#!/usr/bin/env python3
"""
This module contains tests for functions in utils.py
"""


import unittest
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from unittest.mock import Mock, patch


access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Contains tests for access_nested_map function
    """

    @parameterized.expand([
        ("Non-nested mapping", {"a": 1}, ("a",), 1),
        ("Nested dict", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("Nested mapping", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self, name: str, mapping: Mapping, keys: Sequence, expected: Any
    ) -> None:
        """
        Tests expected results for three different inputs
        """
        result = access_nested_map(mapping, keys)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ("Empty dict", {}, ("a",)),
        ("Non existent key", {"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
        self, name: str, mapping: Mapping, keys: Sequence
    ) -> None:
        with self.assertRaises(KeyError) as context:
            access_nested_map(mapping, keys)
        self.assertEqual(str(context.exception).strip("'"), str(keys[-1]))


class TestGetJson(unittest.TestCase):
    """
    Contains tests for get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        # Create a mock response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)
