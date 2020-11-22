# coding: utf-8

"""
    QUBO API solvers

    QUBO solvers from Meta Analytics  # noqa: E501

    OpenAPI spec version: v1
    Contact: rajesh@craftingdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import alphaqubo_client
from api.qubo_api import QuboApi  # noqa: E501
from alphaqubo_client.rest import ApiException


class TestQuboApi(unittest.TestCase):
    """QuboApi unit test stubs"""

    def setUp(self):
        self.api = api.qubo_api.QuboApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_qubo_heartbeat_get(self):
        """Test case for api_qubo_heartbeat_get

        Heartbeat -- Used to verify the container is running.  # noqa: E501
        """
        pass

    def test_api_qubo_solve_qubo_async_using_s3_post(self):
        """Test case for api_qubo_solve_qubo_async_using_s3_post

        Use the inputs to locate a file in S3 and solve the QUBO within it. The file may be a .txt file or a .gz file.  # noqa: E501
        """
        pass

    def test_api_qubo_solve_qubo_post(self):
        """Test case for api_qubo_solve_qubo_post

        Use the inputs to define a QUBO and solve it synchronously.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
