# openapi_client.INTERFACEApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_interface_bridge_endpoint**](INTERFACEApi.md#delete_interface_bridge_endpoint) | **DELETE** /api/v2/interface/bridge | 
[**delete_interface_gre_endpoint**](INTERFACEApi.md#delete_interface_gre_endpoint) | **DELETE** /api/v2/interface/gre | 
[**delete_interface_gres_endpoint**](INTERFACEApi.md#delete_interface_gres_endpoint) | **DELETE** /api/v2/interface/gres | 
[**delete_interface_group_endpoint**](INTERFACEApi.md#delete_interface_group_endpoint) | **DELETE** /api/v2/interface/group | 
[**delete_interface_groups_endpoint**](INTERFACEApi.md#delete_interface_groups_endpoint) | **DELETE** /api/v2/interface/groups | 
[**delete_interface_lagg_endpoint**](INTERFACEApi.md#delete_interface_lagg_endpoint) | **DELETE** /api/v2/interface/lagg | 
[**delete_interface_laggs_endpoint**](INTERFACEApi.md#delete_interface_laggs_endpoint) | **DELETE** /api/v2/interface/laggs | 
[**delete_interface_vlan_endpoint**](INTERFACEApi.md#delete_interface_vlan_endpoint) | **DELETE** /api/v2/interface/vlan | 
[**delete_interface_vlans_endpoint**](INTERFACEApi.md#delete_interface_vlans_endpoint) | **DELETE** /api/v2/interface/vlans | 
[**delete_network_interface_endpoint**](INTERFACEApi.md#delete_network_interface_endpoint) | **DELETE** /api/v2/interface | 
[**delete_network_interfaces_endpoint**](INTERFACEApi.md#delete_network_interfaces_endpoint) | **DELETE** /api/v2/interfaces | 
[**get_interface_apply_endpoint**](INTERFACEApi.md#get_interface_apply_endpoint) | **GET** /api/v2/interface/apply | 
[**get_interface_available_interfaces_endpoint**](INTERFACEApi.md#get_interface_available_interfaces_endpoint) | **GET** /api/v2/interface/available_interfaces | 
[**get_interface_bridge_endpoint**](INTERFACEApi.md#get_interface_bridge_endpoint) | **GET** /api/v2/interface/bridge | 
[**get_interface_bridges_endpoint**](INTERFACEApi.md#get_interface_bridges_endpoint) | **GET** /api/v2/interface/bridges | 
[**get_interface_gre_endpoint**](INTERFACEApi.md#get_interface_gre_endpoint) | **GET** /api/v2/interface/gre | 
[**get_interface_gres_endpoint**](INTERFACEApi.md#get_interface_gres_endpoint) | **GET** /api/v2/interface/gres | 
[**get_interface_group_endpoint**](INTERFACEApi.md#get_interface_group_endpoint) | **GET** /api/v2/interface/group | 
[**get_interface_groups_endpoint**](INTERFACEApi.md#get_interface_groups_endpoint) | **GET** /api/v2/interface/groups | 
[**get_interface_lagg_endpoint**](INTERFACEApi.md#get_interface_lagg_endpoint) | **GET** /api/v2/interface/lagg | 
[**get_interface_laggs_endpoint**](INTERFACEApi.md#get_interface_laggs_endpoint) | **GET** /api/v2/interface/laggs | 
[**get_interface_vlan_endpoint**](INTERFACEApi.md#get_interface_vlan_endpoint) | **GET** /api/v2/interface/vlan | 
[**get_interface_vlans_endpoint**](INTERFACEApi.md#get_interface_vlans_endpoint) | **GET** /api/v2/interface/vlans | 
[**get_network_interface_endpoint**](INTERFACEApi.md#get_network_interface_endpoint) | **GET** /api/v2/interface | 
[**get_network_interfaces_endpoint**](INTERFACEApi.md#get_network_interfaces_endpoint) | **GET** /api/v2/interfaces | 
[**patch_interface_bridge_endpoint**](INTERFACEApi.md#patch_interface_bridge_endpoint) | **PATCH** /api/v2/interface/bridge | 
[**patch_interface_gre_endpoint**](INTERFACEApi.md#patch_interface_gre_endpoint) | **PATCH** /api/v2/interface/gre | 
[**patch_interface_group_endpoint**](INTERFACEApi.md#patch_interface_group_endpoint) | **PATCH** /api/v2/interface/group | 
[**patch_interface_lagg_endpoint**](INTERFACEApi.md#patch_interface_lagg_endpoint) | **PATCH** /api/v2/interface/lagg | 
[**patch_interface_vlan_endpoint**](INTERFACEApi.md#patch_interface_vlan_endpoint) | **PATCH** /api/v2/interface/vlan | 
[**patch_network_interface_endpoint**](INTERFACEApi.md#patch_network_interface_endpoint) | **PATCH** /api/v2/interface | 
[**post_interface_apply_endpoint**](INTERFACEApi.md#post_interface_apply_endpoint) | **POST** /api/v2/interface/apply | 
[**post_interface_bridge_endpoint**](INTERFACEApi.md#post_interface_bridge_endpoint) | **POST** /api/v2/interface/bridge | 
[**post_interface_gre_endpoint**](INTERFACEApi.md#post_interface_gre_endpoint) | **POST** /api/v2/interface/gre | 
[**post_interface_group_endpoint**](INTERFACEApi.md#post_interface_group_endpoint) | **POST** /api/v2/interface/group | 
[**post_interface_lagg_endpoint**](INTERFACEApi.md#post_interface_lagg_endpoint) | **POST** /api/v2/interface/lagg | 
[**post_interface_vlan_endpoint**](INTERFACEApi.md#post_interface_vlan_endpoint) | **POST** /api/v2/interface/vlan | 
[**post_network_interface_endpoint**](INTERFACEApi.md#post_network_interface_endpoint) | **POST** /api/v2/interface | 
[**put_interface_groups_endpoint**](INTERFACEApi.md#put_interface_groups_endpoint) | **PUT** /api/v2/interface/groups | 


# **delete_interface_bridge_endpoint**
> GetInterfaceBridgeEndpoint200Response delete_interface_bridge_endpoint(id)

<h3>Description:</h3>Deletes an existing Interface Bridge.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceBridge<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-bridge-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_bridge_endpoint200_response import GetInterfaceBridgeEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.delete_interface_bridge_endpoint(id)
        print("The response of INTERFACEApi->delete_interface_bridge_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->delete_interface_bridge_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetInterfaceBridgeEndpoint200Response**](GetInterfaceBridgeEndpoint200Response.md)

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

# **delete_interface_gre_endpoint**
> GetInterfaceGREEndpoint200Response delete_interface_gre_endpoint(id)

<h3>Description:</h3>Deletes an existing Interface GRE.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceGRE<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-gre-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_gre_endpoint200_response import GetInterfaceGREEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.delete_interface_gre_endpoint(id)
        print("The response of INTERFACEApi->delete_interface_gre_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->delete_interface_gre_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetInterfaceGREEndpoint200Response**](GetInterfaceGREEndpoint200Response.md)

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

# **delete_interface_gres_endpoint**
> GetInterfaceGREsEndpoint200Response delete_interface_gres_endpoint(limit=limit, offset=offset, query=query)

<h3>Description:</h3>Deletes multiple existing Interface GREs using a query.<br><br>WARNING: This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: InterfaceGRE<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-gres-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_gres_endpoint200_response import GetInterfaceGREsEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    limit = 0 # int | The maximum number of objects to delete at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.delete_interface_gres_endpoint(limit=limit, offset=offset, query=query)
        print("The response of INTERFACEApi->delete_interface_gres_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->delete_interface_gres_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to delete at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetInterfaceGREsEndpoint200Response**](GetInterfaceGREsEndpoint200Response.md)

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

# **delete_interface_group_endpoint**
> GetInterfaceGroupEndpoint200Response delete_interface_group_endpoint(id)

<h3>Description:</h3>Deletes an existing Interface Group.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-group-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_group_endpoint200_response import GetInterfaceGroupEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.delete_interface_group_endpoint(id)
        print("The response of INTERFACEApi->delete_interface_group_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->delete_interface_group_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetInterfaceGroupEndpoint200Response**](GetInterfaceGroupEndpoint200Response.md)

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

# **delete_interface_groups_endpoint**
> GetInterfaceGroupsEndpoint200Response delete_interface_groups_endpoint(limit=limit, offset=offset, query=query)

<h3>Description:</h3>Deletes multiple existing Interface Groups using a query.<br><br>WARNING: This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-groups-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_groups_endpoint200_response import GetInterfaceGroupsEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    limit = 0 # int | The maximum number of objects to delete at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.delete_interface_groups_endpoint(limit=limit, offset=offset, query=query)
        print("The response of INTERFACEApi->delete_interface_groups_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->delete_interface_groups_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to delete at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetInterfaceGroupsEndpoint200Response**](GetInterfaceGroupsEndpoint200Response.md)

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

# **delete_interface_lagg_endpoint**
> GetInterfaceLAGGEndpoint200Response delete_interface_lagg_endpoint(id)

<h3>Description:</h3>Deletes an existing Interface LAGG.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceLAGG<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-lagg-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_lagg_endpoint200_response import GetInterfaceLAGGEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.delete_interface_lagg_endpoint(id)
        print("The response of INTERFACEApi->delete_interface_lagg_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->delete_interface_lagg_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetInterfaceLAGGEndpoint200Response**](GetInterfaceLAGGEndpoint200Response.md)

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

# **delete_interface_laggs_endpoint**
> GetInterfaceLAGGsEndpoint200Response delete_interface_laggs_endpoint(limit=limit, offset=offset, query=query)

<h3>Description:</h3>Deletes multiple existing Interface LAGGs using a query.<br><br>WARNING: This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: InterfaceLAGG<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-laggs-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_laggs_endpoint200_response import GetInterfaceLAGGsEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    limit = 0 # int | The maximum number of objects to delete at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.delete_interface_laggs_endpoint(limit=limit, offset=offset, query=query)
        print("The response of INTERFACEApi->delete_interface_laggs_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->delete_interface_laggs_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to delete at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetInterfaceLAGGsEndpoint200Response**](GetInterfaceLAGGsEndpoint200Response.md)

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

# **delete_interface_vlan_endpoint**
> GetInterfaceVLANEndpoint200Response delete_interface_vlan_endpoint(id)

<h3>Description:</h3>Deletes an existing Interface VLAN.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlan-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_vlan_endpoint200_response import GetInterfaceVLANEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.delete_interface_vlan_endpoint(id)
        print("The response of INTERFACEApi->delete_interface_vlan_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->delete_interface_vlan_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetInterfaceVLANEndpoint200Response**](GetInterfaceVLANEndpoint200Response.md)

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

# **delete_interface_vlans_endpoint**
> GetInterfaceVLANsEndpoint200Response delete_interface_vlans_endpoint(limit=limit, offset=offset, query=query)

<h3>Description:</h3>Deletes multiple existing Interface VLANs using a query.<br><br>WARNING: This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlans-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_vlans_endpoint200_response import GetInterfaceVLANsEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    limit = 0 # int | The maximum number of objects to delete at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.delete_interface_vlans_endpoint(limit=limit, offset=offset, query=query)
        print("The response of INTERFACEApi->delete_interface_vlans_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->delete_interface_vlans_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to delete at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetInterfaceVLANsEndpoint200Response**](GetInterfaceVLANsEndpoint200Response.md)

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

# **delete_network_interface_endpoint**
> GetNetworkInterfaceEndpoint200Response delete_network_interface_endpoint(id, apply=apply)

<h3>Description:</h3>Deletes an existing Network Interface.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: NetworkInterface<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_network_interface_endpoint200_response import GetNetworkInterfaceEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.
    apply = False # bool | Apply this deletion immediately. (optional) (default to False)

    try:
        api_response = api_instance.delete_network_interface_endpoint(id, apply=apply)
        print("The response of INTERFACEApi->delete_network_interface_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->delete_network_interface_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 
 **apply** | **bool**| Apply this deletion immediately. | [optional] [default to False]

### Return type

[**GetNetworkInterfaceEndpoint200Response**](GetNetworkInterfaceEndpoint200Response.md)

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

# **delete_network_interfaces_endpoint**
> GetNetworkInterfacesEndpoint200Response delete_network_interfaces_endpoint(limit=limit, offset=offset, query=query)

<h3>Description:</h3>Deletes multiple existing Network Interfaces using a query.<br><br>WARNING: This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: NetworkInterface<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interfaces-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_network_interfaces_endpoint200_response import GetNetworkInterfacesEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    limit = 0 # int | The maximum number of objects to delete at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.delete_network_interfaces_endpoint(limit=limit, offset=offset, query=query)
        print("The response of INTERFACEApi->delete_network_interfaces_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->delete_network_interfaces_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to delete at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetNetworkInterfacesEndpoint200Response**](GetNetworkInterfacesEndpoint200Response.md)

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

# **get_interface_apply_endpoint**
> GetInterfaceApplyEndpoint200Response get_interface_apply_endpoint()

<h3>Description:</h3>Read pending interfaces status.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceApply<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-apply-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_apply_endpoint200_response import GetInterfaceApplyEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)

    try:
        api_response = api_instance.get_interface_apply_endpoint()
        print("The response of INTERFACEApi->get_interface_apply_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->get_interface_apply_endpoint: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetInterfaceApplyEndpoint200Response**](GetInterfaceApplyEndpoint200Response.md)

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

# **get_interface_available_interfaces_endpoint**
> GetInterfaceAvailableInterfacesEndpoint200Response get_interface_available_interfaces_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing Available Interfaces.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: AvailableInterface<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-available-interfaces-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_available_interfaces_endpoint200_response import GetInterfaceAvailableInterfacesEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_interface_available_interfaces_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of INTERFACEApi->get_interface_available_interfaces_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->get_interface_available_interfaces_endpoint: %s\n" % e)
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

[**GetInterfaceAvailableInterfacesEndpoint200Response**](GetInterfaceAvailableInterfacesEndpoint200Response.md)

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

# **get_interface_bridge_endpoint**
> GetInterfaceBridgeEndpoint200Response get_interface_bridge_endpoint(id)

<h3>Description:</h3>Reads an existing Interface Bridge.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceBridge<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-bridge-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_bridge_endpoint200_response import GetInterfaceBridgeEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_interface_bridge_endpoint(id)
        print("The response of INTERFACEApi->get_interface_bridge_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->get_interface_bridge_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetInterfaceBridgeEndpoint200Response**](GetInterfaceBridgeEndpoint200Response.md)

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

# **get_interface_bridges_endpoint**
> GetInterfaceBridgesEndpoint200Response get_interface_bridges_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing Interface Bridges.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: InterfaceBridge<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-bridges-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_bridges_endpoint200_response import GetInterfaceBridgesEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_interface_bridges_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of INTERFACEApi->get_interface_bridges_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->get_interface_bridges_endpoint: %s\n" % e)
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

[**GetInterfaceBridgesEndpoint200Response**](GetInterfaceBridgesEndpoint200Response.md)

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

# **get_interface_gre_endpoint**
> GetInterfaceGREEndpoint200Response get_interface_gre_endpoint(id)

<h3>Description:</h3>Reads an existing Interface GRE.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceGRE<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-gre-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_gre_endpoint200_response import GetInterfaceGREEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_interface_gre_endpoint(id)
        print("The response of INTERFACEApi->get_interface_gre_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->get_interface_gre_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetInterfaceGREEndpoint200Response**](GetInterfaceGREEndpoint200Response.md)

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

# **get_interface_gres_endpoint**
> GetInterfaceGREsEndpoint200Response get_interface_gres_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing Interface GREs.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: InterfaceGRE<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-gres-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_gres_endpoint200_response import GetInterfaceGREsEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_interface_gres_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of INTERFACEApi->get_interface_gres_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->get_interface_gres_endpoint: %s\n" % e)
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

[**GetInterfaceGREsEndpoint200Response**](GetInterfaceGREsEndpoint200Response.md)

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

# **get_interface_group_endpoint**
> GetInterfaceGroupEndpoint200Response get_interface_group_endpoint(id)

<h3>Description:</h3>Reads an existing Interface Group.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-group-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_group_endpoint200_response import GetInterfaceGroupEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_interface_group_endpoint(id)
        print("The response of INTERFACEApi->get_interface_group_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->get_interface_group_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetInterfaceGroupEndpoint200Response**](GetInterfaceGroupEndpoint200Response.md)

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

# **get_interface_groups_endpoint**
> GetInterfaceGroupsEndpoint200Response get_interface_groups_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing Interface Groups.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-groups-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_groups_endpoint200_response import GetInterfaceGroupsEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_interface_groups_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of INTERFACEApi->get_interface_groups_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->get_interface_groups_endpoint: %s\n" % e)
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

[**GetInterfaceGroupsEndpoint200Response**](GetInterfaceGroupsEndpoint200Response.md)

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

# **get_interface_lagg_endpoint**
> GetInterfaceLAGGEndpoint200Response get_interface_lagg_endpoint(id)

<h3>Description:</h3>Reads an existing Interface LAGG.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceLAGG<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-lagg-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_lagg_endpoint200_response import GetInterfaceLAGGEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_interface_lagg_endpoint(id)
        print("The response of INTERFACEApi->get_interface_lagg_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->get_interface_lagg_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetInterfaceLAGGEndpoint200Response**](GetInterfaceLAGGEndpoint200Response.md)

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

# **get_interface_laggs_endpoint**
> GetInterfaceLAGGsEndpoint200Response get_interface_laggs_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing Interface LAGGs.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: InterfaceLAGG<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-laggs-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_laggs_endpoint200_response import GetInterfaceLAGGsEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_interface_laggs_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of INTERFACEApi->get_interface_laggs_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->get_interface_laggs_endpoint: %s\n" % e)
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

[**GetInterfaceLAGGsEndpoint200Response**](GetInterfaceLAGGsEndpoint200Response.md)

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

# **get_interface_vlan_endpoint**
> GetInterfaceVLANEndpoint200Response get_interface_vlan_endpoint(id)

<h3>Description:</h3>Reads an existing Interface VLAN.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlan-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_vlan_endpoint200_response import GetInterfaceVLANEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_interface_vlan_endpoint(id)
        print("The response of INTERFACEApi->get_interface_vlan_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->get_interface_vlan_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetInterfaceVLANEndpoint200Response**](GetInterfaceVLANEndpoint200Response.md)

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

# **get_interface_vlans_endpoint**
> GetInterfaceVLANsEndpoint200Response get_interface_vlans_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing Interface VLANs.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlans-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_vlans_endpoint200_response import GetInterfaceVLANsEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_interface_vlans_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of INTERFACEApi->get_interface_vlans_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->get_interface_vlans_endpoint: %s\n" % e)
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

[**GetInterfaceVLANsEndpoint200Response**](GetInterfaceVLANsEndpoint200Response.md)

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

# **get_network_interface_endpoint**
> GetNetworkInterfaceEndpoint200Response get_network_interface_endpoint(id)

<h3>Description:</h3>Reads an existing Network Interface.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: NetworkInterface<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_network_interface_endpoint200_response import GetNetworkInterfaceEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_network_interface_endpoint(id)
        print("The response of INTERFACEApi->get_network_interface_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->get_network_interface_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetNetworkInterfaceEndpoint200Response**](GetNetworkInterfaceEndpoint200Response.md)

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

# **get_network_interfaces_endpoint**
> GetNetworkInterfacesEndpoint200Response get_network_interfaces_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing Network Interfaces.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: NetworkInterface<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interfaces-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_network_interfaces_endpoint200_response import GetNetworkInterfacesEndpoint200Response
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_network_interfaces_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of INTERFACEApi->get_network_interfaces_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->get_network_interfaces_endpoint: %s\n" % e)
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

[**GetNetworkInterfacesEndpoint200Response**](GetNetworkInterfacesEndpoint200Response.md)

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

# **patch_interface_bridge_endpoint**
> GetInterfaceBridgeEndpoint200Response patch_interface_bridge_endpoint(patch_interface_bridge_endpoint_request=patch_interface_bridge_endpoint_request)

<h3>Description:</h3>Updates an existing Interface Bridge.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceBridge<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-bridge-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_bridge_endpoint200_response import GetInterfaceBridgeEndpoint200Response
from pfsense_api_client.models.patch_interface_bridge_endpoint_request import PatchInterfaceBridgeEndpointRequest
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    patch_interface_bridge_endpoint_request = openapi_client.PatchInterfaceBridgeEndpointRequest() # PatchInterfaceBridgeEndpointRequest |  (optional)

    try:
        api_response = api_instance.patch_interface_bridge_endpoint(patch_interface_bridge_endpoint_request=patch_interface_bridge_endpoint_request)
        print("The response of INTERFACEApi->patch_interface_bridge_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->patch_interface_bridge_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_interface_bridge_endpoint_request** | [**PatchInterfaceBridgeEndpointRequest**](PatchInterfaceBridgeEndpointRequest.md)|  | [optional] 

### Return type

[**GetInterfaceBridgeEndpoint200Response**](GetInterfaceBridgeEndpoint200Response.md)

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

# **patch_interface_gre_endpoint**
> GetInterfaceGREEndpoint200Response patch_interface_gre_endpoint(patch_interface_gre_endpoint_request=patch_interface_gre_endpoint_request)

<h3>Description:</h3>Updates an existing Interface GRE.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceGRE<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-gre-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_gre_endpoint200_response import GetInterfaceGREEndpoint200Response
from pfsense_api_client.models.patch_interface_gre_endpoint_request import PatchInterfaceGREEndpointRequest
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    patch_interface_gre_endpoint_request = openapi_client.PatchInterfaceGREEndpointRequest() # PatchInterfaceGREEndpointRequest |  (optional)

    try:
        api_response = api_instance.patch_interface_gre_endpoint(patch_interface_gre_endpoint_request=patch_interface_gre_endpoint_request)
        print("The response of INTERFACEApi->patch_interface_gre_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->patch_interface_gre_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_interface_gre_endpoint_request** | [**PatchInterfaceGREEndpointRequest**](PatchInterfaceGREEndpointRequest.md)|  | [optional] 

### Return type

[**GetInterfaceGREEndpoint200Response**](GetInterfaceGREEndpoint200Response.md)

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

# **patch_interface_group_endpoint**
> GetInterfaceGroupEndpoint200Response patch_interface_group_endpoint(patch_interface_group_endpoint_request=patch_interface_group_endpoint_request)

<h3>Description:</h3>Updates an existing Interface Group.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-group-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_group_endpoint200_response import GetInterfaceGroupEndpoint200Response
from pfsense_api_client.models.patch_interface_group_endpoint_request import PatchInterfaceGroupEndpointRequest
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    patch_interface_group_endpoint_request = openapi_client.PatchInterfaceGroupEndpointRequest() # PatchInterfaceGroupEndpointRequest |  (optional)

    try:
        api_response = api_instance.patch_interface_group_endpoint(patch_interface_group_endpoint_request=patch_interface_group_endpoint_request)
        print("The response of INTERFACEApi->patch_interface_group_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->patch_interface_group_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_interface_group_endpoint_request** | [**PatchInterfaceGroupEndpointRequest**](PatchInterfaceGroupEndpointRequest.md)|  | [optional] 

### Return type

[**GetInterfaceGroupEndpoint200Response**](GetInterfaceGroupEndpoint200Response.md)

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

# **patch_interface_lagg_endpoint**
> GetInterfaceLAGGEndpoint200Response patch_interface_lagg_endpoint(patch_interface_lagg_endpoint_request=patch_interface_lagg_endpoint_request)

<h3>Description:</h3>Updates an existing Interface LAGG.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceLAGG<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-lagg-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_lagg_endpoint200_response import GetInterfaceLAGGEndpoint200Response
from pfsense_api_client.models.patch_interface_lagg_endpoint_request import PatchInterfaceLAGGEndpointRequest
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    patch_interface_lagg_endpoint_request = openapi_client.PatchInterfaceLAGGEndpointRequest() # PatchInterfaceLAGGEndpointRequest |  (optional)

    try:
        api_response = api_instance.patch_interface_lagg_endpoint(patch_interface_lagg_endpoint_request=patch_interface_lagg_endpoint_request)
        print("The response of INTERFACEApi->patch_interface_lagg_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->patch_interface_lagg_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_interface_lagg_endpoint_request** | [**PatchInterfaceLAGGEndpointRequest**](PatchInterfaceLAGGEndpointRequest.md)|  | [optional] 

### Return type

[**GetInterfaceLAGGEndpoint200Response**](GetInterfaceLAGGEndpoint200Response.md)

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

# **patch_interface_vlan_endpoint**
> GetInterfaceVLANEndpoint200Response patch_interface_vlan_endpoint(patch_interface_vlan_endpoint_request=patch_interface_vlan_endpoint_request)

<h3>Description:</h3>Updates an existing Interface VLAN.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlan-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_vlan_endpoint200_response import GetInterfaceVLANEndpoint200Response
from pfsense_api_client.models.patch_interface_vlan_endpoint_request import PatchInterfaceVLANEndpointRequest
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    patch_interface_vlan_endpoint_request = openapi_client.PatchInterfaceVLANEndpointRequest() # PatchInterfaceVLANEndpointRequest |  (optional)

    try:
        api_response = api_instance.patch_interface_vlan_endpoint(patch_interface_vlan_endpoint_request=patch_interface_vlan_endpoint_request)
        print("The response of INTERFACEApi->patch_interface_vlan_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->patch_interface_vlan_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_interface_vlan_endpoint_request** | [**PatchInterfaceVLANEndpointRequest**](PatchInterfaceVLANEndpointRequest.md)|  | [optional] 

### Return type

[**GetInterfaceVLANEndpoint200Response**](GetInterfaceVLANEndpoint200Response.md)

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

# **patch_network_interface_endpoint**
> GetNetworkInterfaceEndpoint200Response patch_network_interface_endpoint(patch_network_interface_endpoint_request=patch_network_interface_endpoint_request)

<h3>Description:</h3>Updates an existing Network Interface.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: NetworkInterface<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_network_interface_endpoint200_response import GetNetworkInterfaceEndpoint200Response
from pfsense_api_client.models.patch_network_interface_endpoint_request import PatchNetworkInterfaceEndpointRequest
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    patch_network_interface_endpoint_request = openapi_client.PatchNetworkInterfaceEndpointRequest() # PatchNetworkInterfaceEndpointRequest |  (optional)

    try:
        api_response = api_instance.patch_network_interface_endpoint(patch_network_interface_endpoint_request=patch_network_interface_endpoint_request)
        print("The response of INTERFACEApi->patch_network_interface_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->patch_network_interface_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_network_interface_endpoint_request** | [**PatchNetworkInterfaceEndpointRequest**](PatchNetworkInterfaceEndpointRequest.md)|  | [optional] 

### Return type

[**GetNetworkInterfaceEndpoint200Response**](GetNetworkInterfaceEndpoint200Response.md)

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

# **post_interface_apply_endpoint**
> GetInterfaceApplyEndpoint200Response post_interface_apply_endpoint(post_interface_apply_endpoint_request=post_interface_apply_endpoint_request)

<h3>Description:</h3>Apply pending interface changes.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceApply<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-apply-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_apply_endpoint200_response import GetInterfaceApplyEndpoint200Response
from pfsense_api_client.models.post_interface_apply_endpoint_request import PostInterfaceApplyEndpointRequest
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    post_interface_apply_endpoint_request = openapi_client.PostInterfaceApplyEndpointRequest() # PostInterfaceApplyEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_interface_apply_endpoint(post_interface_apply_endpoint_request=post_interface_apply_endpoint_request)
        print("The response of INTERFACEApi->post_interface_apply_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->post_interface_apply_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_interface_apply_endpoint_request** | [**PostInterfaceApplyEndpointRequest**](PostInterfaceApplyEndpointRequest.md)|  | [optional] 

### Return type

[**GetInterfaceApplyEndpoint200Response**](GetInterfaceApplyEndpoint200Response.md)

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

# **post_interface_bridge_endpoint**
> GetInterfaceBridgeEndpoint200Response post_interface_bridge_endpoint(post_interface_bridge_endpoint_request=post_interface_bridge_endpoint_request)

<h3>Description:</h3>Creates a new Interface Bridge.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceBridge<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-bridge-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_bridge_endpoint200_response import GetInterfaceBridgeEndpoint200Response
from pfsense_api_client.models.post_interface_bridge_endpoint_request import PostInterfaceBridgeEndpointRequest
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    post_interface_bridge_endpoint_request = openapi_client.PostInterfaceBridgeEndpointRequest() # PostInterfaceBridgeEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_interface_bridge_endpoint(post_interface_bridge_endpoint_request=post_interface_bridge_endpoint_request)
        print("The response of INTERFACEApi->post_interface_bridge_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->post_interface_bridge_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_interface_bridge_endpoint_request** | [**PostInterfaceBridgeEndpointRequest**](PostInterfaceBridgeEndpointRequest.md)|  | [optional] 

### Return type

[**GetInterfaceBridgeEndpoint200Response**](GetInterfaceBridgeEndpoint200Response.md)

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

# **post_interface_gre_endpoint**
> GetInterfaceGREEndpoint200Response post_interface_gre_endpoint(post_interface_gre_endpoint_request=post_interface_gre_endpoint_request)

<h3>Description:</h3>Creates a new Interface GRE.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceGRE<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-gre-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_gre_endpoint200_response import GetInterfaceGREEndpoint200Response
from pfsense_api_client.models.post_interface_gre_endpoint_request import PostInterfaceGREEndpointRequest
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    post_interface_gre_endpoint_request = openapi_client.PostInterfaceGREEndpointRequest() # PostInterfaceGREEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_interface_gre_endpoint(post_interface_gre_endpoint_request=post_interface_gre_endpoint_request)
        print("The response of INTERFACEApi->post_interface_gre_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->post_interface_gre_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_interface_gre_endpoint_request** | [**PostInterfaceGREEndpointRequest**](PostInterfaceGREEndpointRequest.md)|  | [optional] 

### Return type

[**GetInterfaceGREEndpoint200Response**](GetInterfaceGREEndpoint200Response.md)

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

# **post_interface_group_endpoint**
> GetInterfaceGroupEndpoint200Response post_interface_group_endpoint(post_interface_group_endpoint_request=post_interface_group_endpoint_request)

<h3>Description:</h3>Creates a new Interface Group.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-group-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_group_endpoint200_response import GetInterfaceGroupEndpoint200Response
from pfsense_api_client.models.post_interface_group_endpoint_request import PostInterfaceGroupEndpointRequest
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    post_interface_group_endpoint_request = openapi_client.PostInterfaceGroupEndpointRequest() # PostInterfaceGroupEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_interface_group_endpoint(post_interface_group_endpoint_request=post_interface_group_endpoint_request)
        print("The response of INTERFACEApi->post_interface_group_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->post_interface_group_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_interface_group_endpoint_request** | [**PostInterfaceGroupEndpointRequest**](PostInterfaceGroupEndpointRequest.md)|  | [optional] 

### Return type

[**GetInterfaceGroupEndpoint200Response**](GetInterfaceGroupEndpoint200Response.md)

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

# **post_interface_lagg_endpoint**
> GetInterfaceLAGGEndpoint200Response post_interface_lagg_endpoint(post_interface_lagg_endpoint_request=post_interface_lagg_endpoint_request)

<h3>Description:</h3>Creates a new Interface LAGG.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceLAGG<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-lagg-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_lagg_endpoint200_response import GetInterfaceLAGGEndpoint200Response
from pfsense_api_client.models.post_interface_lagg_endpoint_request import PostInterfaceLAGGEndpointRequest
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    post_interface_lagg_endpoint_request = openapi_client.PostInterfaceLAGGEndpointRequest() # PostInterfaceLAGGEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_interface_lagg_endpoint(post_interface_lagg_endpoint_request=post_interface_lagg_endpoint_request)
        print("The response of INTERFACEApi->post_interface_lagg_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->post_interface_lagg_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_interface_lagg_endpoint_request** | [**PostInterfaceLAGGEndpointRequest**](PostInterfaceLAGGEndpointRequest.md)|  | [optional] 

### Return type

[**GetInterfaceLAGGEndpoint200Response**](GetInterfaceLAGGEndpoint200Response.md)

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

# **post_interface_vlan_endpoint**
> GetInterfaceVLANEndpoint200Response post_interface_vlan_endpoint(post_interface_vlan_endpoint_request=post_interface_vlan_endpoint_request)

<h3>Description:</h3>Creates a new Interface VLAN.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlan-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_vlan_endpoint200_response import GetInterfaceVLANEndpoint200Response
from pfsense_api_client.models.post_interface_vlan_endpoint_request import PostInterfaceVLANEndpointRequest
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    post_interface_vlan_endpoint_request = openapi_client.PostInterfaceVLANEndpointRequest() # PostInterfaceVLANEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_interface_vlan_endpoint(post_interface_vlan_endpoint_request=post_interface_vlan_endpoint_request)
        print("The response of INTERFACEApi->post_interface_vlan_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->post_interface_vlan_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_interface_vlan_endpoint_request** | [**PostInterfaceVLANEndpointRequest**](PostInterfaceVLANEndpointRequest.md)|  | [optional] 

### Return type

[**GetInterfaceVLANEndpoint200Response**](GetInterfaceVLANEndpoint200Response.md)

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

# **post_network_interface_endpoint**
> GetNetworkInterfaceEndpoint200Response post_network_interface_endpoint(post_network_interface_endpoint_request=post_network_interface_endpoint_request)

<h3>Description:</h3>Creates a new Network Interface.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: NetworkInterface<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_network_interface_endpoint200_response import GetNetworkInterfaceEndpoint200Response
from pfsense_api_client.models.post_network_interface_endpoint_request import PostNetworkInterfaceEndpointRequest
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    post_network_interface_endpoint_request = openapi_client.PostNetworkInterfaceEndpointRequest() # PostNetworkInterfaceEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_network_interface_endpoint(post_network_interface_endpoint_request=post_network_interface_endpoint_request)
        print("The response of INTERFACEApi->post_network_interface_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->post_network_interface_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_network_interface_endpoint_request** | [**PostNetworkInterfaceEndpointRequest**](PostNetworkInterfaceEndpointRequest.md)|  | [optional] 

### Return type

[**GetNetworkInterfaceEndpoint200Response**](GetNetworkInterfaceEndpoint200Response.md)

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

# **put_interface_groups_endpoint**
> GetInterfaceGroupsEndpoint200Response put_interface_groups_endpoint(post_interface_group_endpoint_request=post_interface_group_endpoint_request)

<h3>Description:</h3>Replaces all existing Interface Groups.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: InterfaceGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-interface-groups-put ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_interface_groups_endpoint200_response import GetInterfaceGroupsEndpoint200Response
from pfsense_api_client.models.post_interface_group_endpoint_request import PostInterfaceGroupEndpointRequest
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
    api_instance = openapi_client.INTERFACEApi(api_client)
    post_interface_group_endpoint_request = [openapi_client.PostInterfaceGroupEndpointRequest()] # List[PostInterfaceGroupEndpointRequest] |  (optional)

    try:
        api_response = api_instance.put_interface_groups_endpoint(post_interface_group_endpoint_request=post_interface_group_endpoint_request)
        print("The response of INTERFACEApi->put_interface_groups_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling INTERFACEApi->put_interface_groups_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_interface_group_endpoint_request** | [**List[PostInterfaceGroupEndpointRequest]**](PostInterfaceGroupEndpointRequest.md)|  | [optional] 

### Return type

[**GetInterfaceGroupsEndpoint200Response**](GetInterfaceGroupsEndpoint200Response.md)

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

