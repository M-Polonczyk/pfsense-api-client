# openapi_client.USERApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_auth_server_endpoint**](USERApi.md#delete_user_auth_server_endpoint) | **DELETE** /api/v2/user/auth_server | 
[**delete_user_auth_servers_endpoint**](USERApi.md#delete_user_auth_servers_endpoint) | **DELETE** /api/v2/user/auth_servers | 
[**delete_user_endpoint**](USERApi.md#delete_user_endpoint) | **DELETE** /api/v2/user | 
[**delete_user_group_endpoint**](USERApi.md#delete_user_group_endpoint) | **DELETE** /api/v2/user/group | 
[**delete_user_groups_endpoint**](USERApi.md#delete_user_groups_endpoint) | **DELETE** /api/v2/user/groups | 
[**delete_users_endpoint**](USERApi.md#delete_users_endpoint) | **DELETE** /api/v2/users | 
[**get_user_auth_server_endpoint**](USERApi.md#get_user_auth_server_endpoint) | **GET** /api/v2/user/auth_server | 
[**get_user_auth_servers_endpoint**](USERApi.md#get_user_auth_servers_endpoint) | **GET** /api/v2/user/auth_servers | 
[**get_user_endpoint**](USERApi.md#get_user_endpoint) | **GET** /api/v2/user | 
[**get_user_group_endpoint**](USERApi.md#get_user_group_endpoint) | **GET** /api/v2/user/group | 
[**get_user_groups_endpoint**](USERApi.md#get_user_groups_endpoint) | **GET** /api/v2/user/groups | 
[**get_users_endpoint**](USERApi.md#get_users_endpoint) | **GET** /api/v2/users | 
[**patch_user_auth_server_endpoint**](USERApi.md#patch_user_auth_server_endpoint) | **PATCH** /api/v2/user/auth_server | 
[**patch_user_endpoint**](USERApi.md#patch_user_endpoint) | **PATCH** /api/v2/user | 
[**patch_user_group_endpoint**](USERApi.md#patch_user_group_endpoint) | **PATCH** /api/v2/user/group | 
[**post_user_auth_server_endpoint**](USERApi.md#post_user_auth_server_endpoint) | **POST** /api/v2/user/auth_server | 
[**post_user_endpoint**](USERApi.md#post_user_endpoint) | **POST** /api/v2/user | 
[**post_user_group_endpoint**](USERApi.md#post_user_group_endpoint) | **POST** /api/v2/user/group | 
[**put_user_auth_servers_endpoint**](USERApi.md#put_user_auth_servers_endpoint) | **PUT** /api/v2/user/auth_servers | 
[**put_user_groups_endpoint**](USERApi.md#put_user_groups_endpoint) | **PUT** /api/v2/user/groups | 


# **delete_user_auth_server_endpoint**
> GetUserAuthServerEndpoint200Response delete_user_auth_server_endpoint(id)

<h3>Description:</h3>Deletes an existing authentication server.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-server-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_auth_server_endpoint200_response import GetUserAuthServerEndpoint200Response
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
    api_instance = openapi_client.USERApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.delete_user_auth_server_endpoint(id)
        print("The response of USERApi->delete_user_auth_server_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->delete_user_auth_server_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetUserAuthServerEndpoint200Response**](GetUserAuthServerEndpoint200Response.md)

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

# **delete_user_auth_servers_endpoint**
> GetUserAuthServersEndpoint200Response delete_user_auth_servers_endpoint(limit=limit, offset=offset, query=query)

<h3>Description:</h3>Deletes multiple existing authentication servers using a query.<br><br>WARNING: This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-servers-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_auth_servers_endpoint200_response import GetUserAuthServersEndpoint200Response
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
    api_instance = openapi_client.USERApi(api_client)
    limit = 0 # int | The maximum number of objects to delete at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.delete_user_auth_servers_endpoint(limit=limit, offset=offset, query=query)
        print("The response of USERApi->delete_user_auth_servers_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->delete_user_auth_servers_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to delete at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetUserAuthServersEndpoint200Response**](GetUserAuthServersEndpoint200Response.md)

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

# **delete_user_endpoint**
> GetUserEndpoint200Response delete_user_endpoint(id)

<h3>Description:</h3>Deletes an existing User.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_endpoint200_response import GetUserEndpoint200Response
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
    api_instance = openapi_client.USERApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.delete_user_endpoint(id)
        print("The response of USERApi->delete_user_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->delete_user_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetUserEndpoint200Response**](GetUserEndpoint200Response.md)

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

# **delete_user_group_endpoint**
> GetUserGroupEndpoint200Response delete_user_group_endpoint(id)

<h3>Description:</h3>Deletes an existing User Group.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-group-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_group_endpoint200_response import GetUserGroupEndpoint200Response
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
    api_instance = openapi_client.USERApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.delete_user_group_endpoint(id)
        print("The response of USERApi->delete_user_group_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->delete_user_group_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetUserGroupEndpoint200Response**](GetUserGroupEndpoint200Response.md)

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

# **delete_user_groups_endpoint**
> GetUserGroupsEndpoint200Response delete_user_groups_endpoint(limit=limit, offset=offset, query=query)

<h3>Description:</h3>Deletes multiple existing User Groups using a query.<br><br>WARNING: This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-groups-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_groups_endpoint200_response import GetUserGroupsEndpoint200Response
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
    api_instance = openapi_client.USERApi(api_client)
    limit = 0 # int | The maximum number of objects to delete at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.delete_user_groups_endpoint(limit=limit, offset=offset, query=query)
        print("The response of USERApi->delete_user_groups_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->delete_user_groups_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to delete at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetUserGroupsEndpoint200Response**](GetUserGroupsEndpoint200Response.md)

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

# **delete_users_endpoint**
> GetUsersEndpoint200Response delete_users_endpoint(limit=limit, offset=offset, query=query)

<h3>Description:</h3>Deletes multiple existing Users using a query.<br><br>WARNING: This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-users-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_users_endpoint200_response import GetUsersEndpoint200Response
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
    api_instance = openapi_client.USERApi(api_client)
    limit = 0 # int | The maximum number of objects to delete at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.delete_users_endpoint(limit=limit, offset=offset, query=query)
        print("The response of USERApi->delete_users_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->delete_users_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to delete at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetUsersEndpoint200Response**](GetUsersEndpoint200Response.md)

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

# **get_user_auth_server_endpoint**
> GetUserAuthServerEndpoint200Response get_user_auth_server_endpoint(id)

<h3>Description:</h3>Reads an existing authentication server.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-server-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_auth_server_endpoint200_response import GetUserAuthServerEndpoint200Response
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
    api_instance = openapi_client.USERApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_user_auth_server_endpoint(id)
        print("The response of USERApi->get_user_auth_server_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->get_user_auth_server_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetUserAuthServerEndpoint200Response**](GetUserAuthServerEndpoint200Response.md)

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

# **get_user_auth_servers_endpoint**
> GetUserAuthServersEndpoint200Response get_user_auth_servers_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing authentication servers.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-servers-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_auth_servers_endpoint200_response import GetUserAuthServersEndpoint200Response
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
    api_instance = openapi_client.USERApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_user_auth_servers_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of USERApi->get_user_auth_servers_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->get_user_auth_servers_endpoint: %s\n" % e)
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

[**GetUserAuthServersEndpoint200Response**](GetUserAuthServersEndpoint200Response.md)

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

# **get_user_endpoint**
> GetUserEndpoint200Response get_user_endpoint(id)

<h3>Description:</h3>Reads an existing User.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_endpoint200_response import GetUserEndpoint200Response
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
    api_instance = openapi_client.USERApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_user_endpoint(id)
        print("The response of USERApi->get_user_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->get_user_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetUserEndpoint200Response**](GetUserEndpoint200Response.md)

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

# **get_user_group_endpoint**
> GetUserGroupEndpoint200Response get_user_group_endpoint(id)

<h3>Description:</h3>Reads an existing User Group.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-group-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_group_endpoint200_response import GetUserGroupEndpoint200Response
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
    api_instance = openapi_client.USERApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_user_group_endpoint(id)
        print("The response of USERApi->get_user_group_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->get_user_group_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetUserGroupEndpoint200Response**](GetUserGroupEndpoint200Response.md)

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

# **get_user_groups_endpoint**
> GetUserGroupsEndpoint200Response get_user_groups_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing User Groups.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-groups-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_groups_endpoint200_response import GetUserGroupsEndpoint200Response
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
    api_instance = openapi_client.USERApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_user_groups_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of USERApi->get_user_groups_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->get_user_groups_endpoint: %s\n" % e)
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

[**GetUserGroupsEndpoint200Response**](GetUserGroupsEndpoint200Response.md)

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

# **get_users_endpoint**
> GetUsersEndpoint200Response get_users_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing Users.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-users-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_users_endpoint200_response import GetUsersEndpoint200Response
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
    api_instance = openapi_client.USERApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_users_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of USERApi->get_users_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->get_users_endpoint: %s\n" % e)
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

[**GetUsersEndpoint200Response**](GetUsersEndpoint200Response.md)

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

# **patch_user_auth_server_endpoint**
> GetUserAuthServerEndpoint200Response patch_user_auth_server_endpoint(patch_user_auth_server_endpoint_request=patch_user_auth_server_endpoint_request)

<h3>Description:</h3>Updates an existing authentication server.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-server-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_auth_server_endpoint200_response import GetUserAuthServerEndpoint200Response
from pfsense_api_client.models.patch_user_auth_server_endpoint_request import PatchUserAuthServerEndpointRequest
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
    api_instance = openapi_client.USERApi(api_client)
    patch_user_auth_server_endpoint_request = openapi_client.PatchUserAuthServerEndpointRequest() # PatchUserAuthServerEndpointRequest |  (optional)

    try:
        api_response = api_instance.patch_user_auth_server_endpoint(patch_user_auth_server_endpoint_request=patch_user_auth_server_endpoint_request)
        print("The response of USERApi->patch_user_auth_server_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->patch_user_auth_server_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_user_auth_server_endpoint_request** | [**PatchUserAuthServerEndpointRequest**](PatchUserAuthServerEndpointRequest.md)|  | [optional] 

### Return type

[**GetUserAuthServerEndpoint200Response**](GetUserAuthServerEndpoint200Response.md)

### Authorization

[KeyAuth](../README.md#KeyAuth), [BasicAuth](../README.md#BasicAuth), [JWTAuth](../README.md#JWTAuth)

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

# **patch_user_endpoint**
> GetUserEndpoint200Response patch_user_endpoint(patch_user_endpoint_request=patch_user_endpoint_request)

<h3>Description:</h3>Updates an existing User.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_endpoint200_response import GetUserEndpoint200Response
from pfsense_api_client.models.patch_user_endpoint_request import PatchUserEndpointRequest
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
    api_instance = openapi_client.USERApi(api_client)
    patch_user_endpoint_request = openapi_client.PatchUserEndpointRequest() # PatchUserEndpointRequest |  (optional)

    try:
        api_response = api_instance.patch_user_endpoint(patch_user_endpoint_request=patch_user_endpoint_request)
        print("The response of USERApi->patch_user_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->patch_user_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_user_endpoint_request** | [**PatchUserEndpointRequest**](PatchUserEndpointRequest.md)|  | [optional] 

### Return type

[**GetUserEndpoint200Response**](GetUserEndpoint200Response.md)

### Authorization

[KeyAuth](../README.md#KeyAuth), [BasicAuth](../README.md#BasicAuth), [JWTAuth](../README.md#JWTAuth)

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

# **patch_user_group_endpoint**
> GetUserGroupEndpoint200Response patch_user_group_endpoint(patch_user_group_endpoint_request=patch_user_group_endpoint_request)

<h3>Description:</h3>Updates an existing User Group.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-group-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_group_endpoint200_response import GetUserGroupEndpoint200Response
from pfsense_api_client.models.patch_user_group_endpoint_request import PatchUserGroupEndpointRequest
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
    api_instance = openapi_client.USERApi(api_client)
    patch_user_group_endpoint_request = openapi_client.PatchUserGroupEndpointRequest() # PatchUserGroupEndpointRequest |  (optional)

    try:
        api_response = api_instance.patch_user_group_endpoint(patch_user_group_endpoint_request=patch_user_group_endpoint_request)
        print("The response of USERApi->patch_user_group_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->patch_user_group_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_user_group_endpoint_request** | [**PatchUserGroupEndpointRequest**](PatchUserGroupEndpointRequest.md)|  | [optional] 

### Return type

[**GetUserGroupEndpoint200Response**](GetUserGroupEndpoint200Response.md)

### Authorization

[KeyAuth](../README.md#KeyAuth), [BasicAuth](../README.md#BasicAuth), [JWTAuth](../README.md#JWTAuth)

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

# **post_user_auth_server_endpoint**
> GetUserAuthServerEndpoint200Response post_user_auth_server_endpoint(post_user_auth_server_endpoint_request=post_user_auth_server_endpoint_request)

<h3>Description:</h3>Creates a new authentication server.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-server-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_auth_server_endpoint200_response import GetUserAuthServerEndpoint200Response
from pfsense_api_client.models.post_user_auth_server_endpoint_request import PostUserAuthServerEndpointRequest
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
    api_instance = openapi_client.USERApi(api_client)
    post_user_auth_server_endpoint_request = openapi_client.PostUserAuthServerEndpointRequest() # PostUserAuthServerEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_user_auth_server_endpoint(post_user_auth_server_endpoint_request=post_user_auth_server_endpoint_request)
        print("The response of USERApi->post_user_auth_server_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->post_user_auth_server_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_user_auth_server_endpoint_request** | [**PostUserAuthServerEndpointRequest**](PostUserAuthServerEndpointRequest.md)|  | [optional] 

### Return type

[**GetUserAuthServerEndpoint200Response**](GetUserAuthServerEndpoint200Response.md)

### Authorization

[KeyAuth](../README.md#KeyAuth), [BasicAuth](../README.md#BasicAuth), [JWTAuth](../README.md#JWTAuth)

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

# **post_user_endpoint**
> GetUserEndpoint200Response post_user_endpoint(post_user_endpoint_request=post_user_endpoint_request)

<h3>Description:</h3>Creates a new User.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_endpoint200_response import GetUserEndpoint200Response
from pfsense_api_client.models.post_user_endpoint_request import PostUserEndpointRequest
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
    api_instance = openapi_client.USERApi(api_client)
    post_user_endpoint_request = openapi_client.PostUserEndpointRequest() # PostUserEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_user_endpoint(post_user_endpoint_request=post_user_endpoint_request)
        print("The response of USERApi->post_user_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->post_user_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_user_endpoint_request** | [**PostUserEndpointRequest**](PostUserEndpointRequest.md)|  | [optional] 

### Return type

[**GetUserEndpoint200Response**](GetUserEndpoint200Response.md)

### Authorization

[KeyAuth](../README.md#KeyAuth), [BasicAuth](../README.md#BasicAuth), [JWTAuth](../README.md#JWTAuth)

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

# **post_user_group_endpoint**
> GetUserGroupEndpoint200Response post_user_group_endpoint(post_user_group_endpoint_request=post_user_group_endpoint_request)

<h3>Description:</h3>Creates a new User Group.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-group-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_group_endpoint200_response import GetUserGroupEndpoint200Response
from pfsense_api_client.models.post_user_group_endpoint_request import PostUserGroupEndpointRequest
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
    api_instance = openapi_client.USERApi(api_client)
    post_user_group_endpoint_request = openapi_client.PostUserGroupEndpointRequest() # PostUserGroupEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_user_group_endpoint(post_user_group_endpoint_request=post_user_group_endpoint_request)
        print("The response of USERApi->post_user_group_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->post_user_group_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_user_group_endpoint_request** | [**PostUserGroupEndpointRequest**](PostUserGroupEndpointRequest.md)|  | [optional] 

### Return type

[**GetUserGroupEndpoint200Response**](GetUserGroupEndpoint200Response.md)

### Authorization

[KeyAuth](../README.md#KeyAuth), [BasicAuth](../README.md#BasicAuth), [JWTAuth](../README.md#JWTAuth)

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

# **put_user_auth_servers_endpoint**
> GetUserAuthServersEndpoint200Response put_user_auth_servers_endpoint(post_user_auth_server_endpoint_request=post_user_auth_server_endpoint_request)

<h3>Description:</h3>Replaces all existing authentication servers.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-servers-put ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_auth_servers_endpoint200_response import GetUserAuthServersEndpoint200Response
from pfsense_api_client.models.post_user_auth_server_endpoint_request import PostUserAuthServerEndpointRequest
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
    api_instance = openapi_client.USERApi(api_client)
    post_user_auth_server_endpoint_request = [openapi_client.PostUserAuthServerEndpointRequest()] # List[PostUserAuthServerEndpointRequest] |  (optional)

    try:
        api_response = api_instance.put_user_auth_servers_endpoint(post_user_auth_server_endpoint_request=post_user_auth_server_endpoint_request)
        print("The response of USERApi->put_user_auth_servers_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->put_user_auth_servers_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_user_auth_server_endpoint_request** | [**List[PostUserAuthServerEndpointRequest]**](PostUserAuthServerEndpointRequest.md)|  | [optional] 

### Return type

[**GetUserAuthServersEndpoint200Response**](GetUserAuthServersEndpoint200Response.md)

### Authorization

[KeyAuth](../README.md#KeyAuth), [BasicAuth](../README.md#BasicAuth), [JWTAuth](../README.md#JWTAuth)

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

# **put_user_groups_endpoint**
> GetUserGroupsEndpoint200Response put_user_groups_endpoint(post_user_group_endpoint_request=post_user_group_endpoint_request)

<h3>Description:</h3>Replaces all existing User Groups.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-user-groups-put ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_user_groups_endpoint200_response import GetUserGroupsEndpoint200Response
from pfsense_api_client.models.post_user_group_endpoint_request import PostUserGroupEndpointRequest
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
    api_instance = openapi_client.USERApi(api_client)
    post_user_group_endpoint_request = [openapi_client.PostUserGroupEndpointRequest()] # List[PostUserGroupEndpointRequest] |  (optional)

    try:
        api_response = api_instance.put_user_groups_endpoint(post_user_group_endpoint_request=post_user_group_endpoint_request)
        print("The response of USERApi->put_user_groups_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USERApi->put_user_groups_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_user_group_endpoint_request** | [**List[PostUserGroupEndpointRequest]**](PostUserGroupEndpointRequest.md)|  | [optional] 

### Return type

[**GetUserGroupsEndpoint200Response**](GetUserGroupsEndpoint200Response.md)

### Authorization

[KeyAuth](../README.md#KeyAuth), [BasicAuth](../README.md#BasicAuth), [JWTAuth](../README.md#JWTAuth)

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

