# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import blockmate
from blockmate.paths.v1_account_provider_connect import post  # noqa: E501
from blockmate import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1AccountProviderConnect(ApiTestMixin, unittest.TestCase):
    """
    V1AccountProviderConnect unit test stubs
        Connect new account  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
