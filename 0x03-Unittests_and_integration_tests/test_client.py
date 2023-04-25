#!/usr/bin/env python3
"""
Testing the client module.
"""
import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import (
    GithubOrgClient
)
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    4. Parameterize and patch as decorators
    """

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org_name: str, expected_response: Dict,
                 mocked_func: MagicMock) -> None:
        """
        Test GithubOrgClient.org.
        """
        mocked_func.return_value = MagicMock(
            return_value=expected_response)
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), expected_response)
        mocked_func.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )
