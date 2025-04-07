# openapi_client.AUTHApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_auth_key_endpoint**](AUTHApi.md#delete_auth_key_endpoint) | **DELETE** /api/v2/auth/key | 
[**delete_auth_keys_endpoint**](AUTHApi.md#delete_auth_keys_endpoint) | **DELETE** /api/v2/auth/keys | 
[**get_auth_keys_endpoint**](AUTHApi.md#get_auth_keys_endpoint) | **GET** /api/v2/auth/keys | 
[**post_auth_jwt_endpoint**](AUTHApi.md#post_auth_jwt_endpoint) | **POST** /api/v2/auth/jwt | 
[**post_auth_key_endpoint**](AUTHApi.md#post_auth_key_endpoint) | **POST** /api/v2/auth/key | 


# **delete_auth_key_endpoint**
> PostAuthKeyEndpoint200Response delete_auth_key_endpoint(id)

<h3>Description:</h3>Deletes an existing REST API Key.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RESTAPIKey<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed privileges**: [ page-all, api-v2-auth-key-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Basic Authentication (BasicAuth):

```python
import openapi_client
from pfsense_api_client.models.post_auth_key_endpoint200_response import PostAuthKeyEndpoint200Response
from pfsense_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AUTHApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.delete_auth_key_endpoint(id)
        print("The response of AUTHApi->delete_auth_key_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AUTHApi->delete_auth_key_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**PostAuthKeyEndpoint200Response**](PostAuthKeyEndpoint200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | The client has failed to authenticate the API call. |  -  |
**409** | The client&#39;s request cannot be fulfilled due to one or more conflicts. |  -  |
**424** | The client has requested a resource that requires a dependency which is not installed. |  -  |
**403** | The client does not have sufficient privileges to make this API call. |  -  |
**200** | The client has made a successful request. |  -  |
**415** | The client has requested a content-type that is not supported by the server. |  -  |
**405** | The client has requested an HTTP method that is not supported by the current URL. |  -  |
**406** | The client has requested content in a format that is not supported. |  -  |
**404** | The client has requested a resource that could not be found. |  -  |
**500** | The server encountered an unexpected error and cannot complete the request. |  -  |
**503** | The requested service is temporarily unavailable. |  -  |
**422** | The client has requested a resource that requires a dependency which is not installed. |  -  |
**400** | The client request data has one or more input validation errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth_keys_endpoint**
> GetAuthKeysEndpoint200Response delete_auth_keys_endpoint(limit=limit, offset=offset, query=query)

<h3>Description:</h3>Deletes multiple existing REST API Keys using a query.<br><br>WARNING: This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: RESTAPIKey<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-auth-keys-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_auth_keys_endpoint200_response import GetAuthKeysEndpoint200Response
from pfsense_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: KeyAuth
configuration.api_key['KeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['KeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): JWTAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AUTHApi(api_client)
    limit = 0 # int | The maximum number of objects to delete at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.delete_auth_keys_endpoint(limit=limit, offset=offset, query=query)
        print("The response of AUTHApi->delete_auth_keys_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AUTHApi->delete_auth_keys_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to delete at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetAuthKeysEndpoint200Response**](GetAuthKeysEndpoint200Response.md)

### Authorization

[KeyAuth](../README.md#KeyAuth), [BasicAuth](../README.md#BasicAuth), [JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | The client has failed to authenticate the API call. |  -  |
**409** | The client&#39;s request cannot be fulfilled due to one or more conflicts. |  -  |
**424** | The client has requested a resource that requires a dependency which is not installed. |  -  |
**403** | The client does not have sufficient privileges to make this API call. |  -  |
**200** | The client has made a successful request. |  -  |
**415** | The client has requested a content-type that is not supported by the server. |  -  |
**405** | The client has requested an HTTP method that is not supported by the current URL. |  -  |
**406** | The client has requested content in a format that is not supported. |  -  |
**404** | The client has requested a resource that could not be found. |  -  |
**500** | The server encountered an unexpected error and cannot complete the request. |  -  |
**503** | The requested service is temporarily unavailable. |  -  |
**422** | The client has requested a resource that requires a dependency which is not installed. |  -  |
**400** | The client request data has one or more input validation errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_keys_endpoint**
> GetAuthKeysEndpoint200Response get_auth_keys_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing REST API Keys.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: RESTAPIKey<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-auth-keys-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_auth_keys_endpoint200_response import GetAuthKeysEndpoint200Response
from pfsense_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: KeyAuth
configuration.api_key['KeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['KeyAuth'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization (JWT): JWTAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AUTHApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_auth_keys_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of AUTHApi->get_auth_keys_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AUTHApi->get_auth_keys_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of objects to obtain at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **sort_by** | [**List[str]**](str.md)| The fields to sort response data by. | [optional] 
 **sort_order** | **str**| The order to sort response data by. | [optional] 
 **sort_flags** | **str**| The sort flag to use to customize the behavior of the sort. | [optional] 
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define a real parameter (e.g. there is no &#x60;query&#x60; parameter), rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetAuthKeysEndpoint200Response**](GetAuthKeysEndpoint200Response.md)

### Authorization

[KeyAuth](../README.md#KeyAuth), [BasicAuth](../README.md#BasicAuth), [JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | The client has failed to authenticate the API call. |  -  |
**409** | The client&#39;s request cannot be fulfilled due to one or more conflicts. |  -  |
**424** | The client has requested a resource that requires a dependency which is not installed. |  -  |
**403** | The client does not have sufficient privileges to make this API call. |  -  |
**200** | The client has made a successful request. |  -  |
**415** | The client has requested a content-type that is not supported by the server. |  -  |
**405** | The client has requested an HTTP method that is not supported by the current URL. |  -  |
**406** | The client has requested content in a format that is not supported. |  -  |
**404** | The client has requested a resource that could not be found. |  -  |
**500** | The server encountered an unexpected error and cannot complete the request. |  -  |
**503** | The requested service is temporarily unavailable. |  -  |
**422** | The client has requested a resource that requires a dependency which is not installed. |  -  |
**400** | The client request data has one or more input validation errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_jwt_endpoint**
> PostAuthJWTEndpoint200Response post_auth_jwt_endpoint(post_auth_jwt_endpoint_request=post_auth_jwt_endpoint_request)

<h3>Description:</h3>Creates REST API JWT.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RESTAPIJWT<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed privileges**: [ page-all, api-v2-auth-jwt-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Basic Authentication (BasicAuth):

```python
import openapi_client
from pfsense_api_client.models.post_auth_jwt_endpoint200_response import PostAuthJWTEndpoint200Response
from pfsense_api_client.models.post_auth_jwt_endpoint_request import PostAuthJWTEndpointRequest
from pfsense_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AUTHApi(api_client)
    post_auth_jwt_endpoint_request = openapi_client.PostAuthJWTEndpointRequest() # PostAuthJWTEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_auth_jwt_endpoint(post_auth_jwt_endpoint_request=post_auth_jwt_endpoint_request)
        print("The response of AUTHApi->post_auth_jwt_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AUTHApi->post_auth_jwt_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_auth_jwt_endpoint_request** | [**PostAuthJWTEndpointRequest**](PostAuthJWTEndpointRequest.md)|  | [optional] 

### Return type

[**PostAuthJWTEndpoint200Response**](PostAuthJWTEndpoint200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | The client has failed to authenticate the API call. |  -  |
**409** | The client&#39;s request cannot be fulfilled due to one or more conflicts. |  -  |
**424** | The client has requested a resource that requires a dependency which is not installed. |  -  |
**403** | The client does not have sufficient privileges to make this API call. |  -  |
**200** | The client has made a successful request. |  -  |
**415** | The client has requested a content-type that is not supported by the server. |  -  |
**405** | The client has requested an HTTP method that is not supported by the current URL. |  -  |
**406** | The client has requested content in a format that is not supported. |  -  |
**404** | The client has requested a resource that could not be found. |  -  |
**500** | The server encountered an unexpected error and cannot complete the request. |  -  |
**503** | The requested service is temporarily unavailable. |  -  |
**422** | The client has requested a resource that requires a dependency which is not installed. |  -  |
**400** | The client request data has one or more input validation errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_key_endpoint**
> PostAuthKeyEndpoint200Response post_auth_key_endpoint(post_auth_key_endpoint_request=post_auth_key_endpoint_request)

<h3>Description:</h3>Creates a new REST API Key.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RESTAPIKey<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed privileges**: [ page-all, api-v2-auth-key-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Basic Authentication (BasicAuth):

```python
import openapi_client
from pfsense_api_client.models.post_auth_key_endpoint200_response import PostAuthKeyEndpoint200Response
from pfsense_api_client.models.post_auth_key_endpoint_request import PostAuthKeyEndpointRequest
from pfsense_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AUTHApi(api_client)
    post_auth_key_endpoint_request = openapi_client.PostAuthKeyEndpointRequest() # PostAuthKeyEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_auth_key_endpoint(post_auth_key_endpoint_request=post_auth_key_endpoint_request)
        print("The response of AUTHApi->post_auth_key_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AUTHApi->post_auth_key_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_auth_key_endpoint_request** | [**PostAuthKeyEndpointRequest**](PostAuthKeyEndpointRequest.md)|  | [optional] 

### Return type

[**PostAuthKeyEndpoint200Response**](PostAuthKeyEndpoint200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | The client has failed to authenticate the API call. |  -  |
**409** | The client&#39;s request cannot be fulfilled due to one or more conflicts. |  -  |
**424** | The client has requested a resource that requires a dependency which is not installed. |  -  |
**403** | The client does not have sufficient privileges to make this API call. |  -  |
**200** | The client has made a successful request. |  -  |
**415** | The client has requested a content-type that is not supported by the server. |  -  |
**405** | The client has requested an HTTP method that is not supported by the current URL. |  -  |
**406** | The client has requested content in a format that is not supported. |  -  |
**404** | The client has requested a resource that could not be found. |  -  |
**500** | The server encountered an unexpected error and cannot complete the request. |  -  |
**503** | The requested service is temporarily unavailable. |  -  |
**422** | The client has requested a resource that requires a dependency which is not installed. |  -  |
**400** | The client request data has one or more input validation errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

