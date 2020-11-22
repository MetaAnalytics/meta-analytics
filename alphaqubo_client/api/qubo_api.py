# coding: utf-8

"""
    QUBO API solvers

    QUBO solvers from Meta Analytics  # noqa: E501

    OpenAPI spec version: v1
    Contact: rajesh@craftingdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from alphaqubo_client.api_client import ApiClient


class QuboApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_qubo_heartbeat_get(self, **kwargs):  # noqa: E501
        """Heartbeat -- Used to verify the container is running.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_qubo_heartbeat_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_qubo_heartbeat_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_qubo_heartbeat_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_qubo_heartbeat_get_with_http_info(self, **kwargs):  # noqa: E501
        """Heartbeat -- Used to verify the container is running.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_qubo_heartbeat_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_qubo_heartbeat_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Qubo/heartbeat', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_qubo_solve_qubo_async_using_s3_post(self, **kwargs):  # noqa: E501
        """Use the inputs to locate a file in S3 and solve the QUBO within it. The file may be a .txt file or a .gz file.  # noqa: E501

        The input for the matrix is define insert doc here.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_qubo_solve_qubo_async_using_s3_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SolverAsyncRequest body:
        :return: SolverAsyncResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_qubo_solve_qubo_async_using_s3_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_qubo_solve_qubo_async_using_s3_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_qubo_solve_qubo_async_using_s3_post_with_http_info(self, **kwargs):  # noqa: E501
        """Use the inputs to locate a file in S3 and solve the QUBO within it. The file may be a .txt file or a .gz file.  # noqa: E501

        The input for the matrix is define insert doc here.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_qubo_solve_qubo_async_using_s3_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SolverAsyncRequest body:
        :return: SolverAsyncResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_qubo_solve_qubo_async_using_s3_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Qubo/solveQUBOAsyncUsingS3', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SolverAsyncResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_qubo_solve_qubo_post(self, **kwargs):  # noqa: E501
        """Use the inputs to define a QUBO and solve it synchronously.  # noqa: E501

        The input for the matrix is define insert doc here.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_qubo_solve_qubo_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SolverAPI body:
        :return: SolverAPI
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_qubo_solve_qubo_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_qubo_solve_qubo_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_qubo_solve_qubo_post_with_http_info(self, **kwargs):  # noqa: E501
        """Use the inputs to define a QUBO and solve it synchronously.  # noqa: E501

        The input for the matrix is define insert doc here.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_qubo_solve_qubo_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SolverAPI body:
        :return: SolverAPI
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_qubo_solve_qubo_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Qubo/solveQUBO', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SolverAPI',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)