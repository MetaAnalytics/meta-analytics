# alphaqubo_client.QuboApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_qubo_heartbeat_get**](QuboApi.md#api_qubo_heartbeat_get) | **GET** /api/Qubo/heartbeat | Heartbeat -- Used to verify the container is running.
[**api_qubo_solve_qubo_async_using_s3_post**](QuboApi.md#api_qubo_solve_qubo_async_using_s3_post) | **POST** /api/Qubo/solveQUBOAsyncUsingS3 | Use the inputs to locate a file in S3 and solve the QUBO within it. The file may be a .txt file or a .gz file.
[**api_qubo_solve_qubo_post**](QuboApi.md#api_qubo_solve_qubo_post) | **POST** /api/Qubo/solveQUBO | Use the inputs to define a QUBO and solve it synchronously.

# **api_qubo_heartbeat_get**
> api_qubo_heartbeat_get()

Heartbeat -- Used to verify the container is running.

### Example
```python
from __future__ import print_function
import time
import alphaqubo_client
from alphaqubo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = alphaqubo_client.QuboApi()

try:
    # Heartbeat -- Used to verify the container is running.
    api_instance.api_qubo_heartbeat_get()
except ApiException as e:
    print("Exception when calling QuboApi->api_qubo_heartbeat_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_qubo_solve_qubo_async_using_s3_post**
> SolverAsyncResponse api_qubo_solve_qubo_async_using_s3_post(body=body)

Use the inputs to locate a file in S3 and solve the QUBO within it. The file may be a .txt file or a .gz file.

The input for the matrix is define insert doc here.

### Example
```python
from __future__ import print_function
import time
import alphaqubo_client
from alphaqubo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = alphaqubo_client.QuboApi()
body = alphaqubo_client.SolverAsyncRequest() # SolverAsyncRequest |  (optional)

try:
    # Use the inputs to locate a file in S3 and solve the QUBO within it. The file may be a .txt file or a .gz file.
    api_response = api_instance.api_qubo_solve_qubo_async_using_s3_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuboApi->api_qubo_solve_qubo_async_using_s3_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SolverAsyncRequest**](SolverAsyncRequest.md)|  | [optional] 

### Return type

[**SolverAsyncResponse**](SolverAsyncResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_qubo_solve_qubo_post**
> SolverAPI api_qubo_solve_qubo_post(body=body)

Use the inputs to define a QUBO and solve it synchronously.

The input for the matrix is define insert doc here.

### Example
```python
from __future__ import print_function
import time
import alphaqubo_client
from alphaqubo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = alphaqubo_client.QuboApi()
body = alphaqubo_client.SolverAPI() # SolverAPI |  (optional)

try:
    # Use the inputs to define a QUBO and solve it synchronously.
    api_response = api_instance.api_qubo_solve_qubo_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuboApi->api_qubo_solve_qubo_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SolverAPI**](SolverAPI.md)|  | [optional] 

### Return type

[**SolverAPI**](SolverAPI.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

