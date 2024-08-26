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


access_nested_map = __import__("utils").access_nested_map


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
    ) -> str:
        """
        Tests expected results for three different inputs
        """
        result = access_nested_map(mapping, keys)
        self.assertEqual(result, expected)
