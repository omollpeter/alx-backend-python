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


GithubOrgClient = __import__("client").GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for GithubOrgClient
    """
    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"})
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected_payload, mock_get_json):
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)

        org_data = client.org

        self.assertEqual(org_data, expected_payload)

        url = "https://api.github.com/orgs/"
        mock_get_json.assert_called_once_with(f"{url}{org_name}")
