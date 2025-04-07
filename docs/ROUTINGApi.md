# openapi_client.ROUTINGApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_routing_gateway_endpoint**](ROUTINGApi.md#delete_routing_gateway_endpoint) | **DELETE** /api/v2/routing/gateway | 
[**delete_routing_gateway_group_endpoint**](ROUTINGApi.md#delete_routing_gateway_group_endpoint) | **DELETE** /api/v2/routing/gateway/group | 
[**delete_routing_gateway_group_priority_endpoint**](ROUTINGApi.md#delete_routing_gateway_group_priority_endpoint) | **DELETE** /api/v2/routing/gateway/group/priority | 
[**delete_routing_gateway_groups_endpoint**](ROUTINGApi.md#delete_routing_gateway_groups_endpoint) | **DELETE** /api/v2/routing/gateway/groups | 
[**delete_routing_gateways_endpoint**](ROUTINGApi.md#delete_routing_gateways_endpoint) | **DELETE** /api/v2/routing/gateways | 
[**delete_routing_static_route_endpoint**](ROUTINGApi.md#delete_routing_static_route_endpoint) | **DELETE** /api/v2/routing/static_route | 
[**delete_routing_static_routes_endpoint**](ROUTINGApi.md#delete_routing_static_routes_endpoint) | **DELETE** /api/v2/routing/static_routes | 
[**get_routing_apply_endpoint**](ROUTINGApi.md#get_routing_apply_endpoint) | **GET** /api/v2/routing/apply | 
[**get_routing_gateway_default_endpoint**](ROUTINGApi.md#get_routing_gateway_default_endpoint) | **GET** /api/v2/routing/gateway/default | 
[**get_routing_gateway_endpoint**](ROUTINGApi.md#get_routing_gateway_endpoint) | **GET** /api/v2/routing/gateway | 
[**get_routing_gateway_group_endpoint**](ROUTINGApi.md#get_routing_gateway_group_endpoint) | **GET** /api/v2/routing/gateway/group | 
[**get_routing_gateway_group_priority_endpoint**](ROUTINGApi.md#get_routing_gateway_group_priority_endpoint) | **GET** /api/v2/routing/gateway/group/priority | 
[**get_routing_gateway_groups_endpoint**](ROUTINGApi.md#get_routing_gateway_groups_endpoint) | **GET** /api/v2/routing/gateway/groups | 
[**get_routing_gateways_endpoint**](ROUTINGApi.md#get_routing_gateways_endpoint) | **GET** /api/v2/routing/gateways | 
[**get_routing_static_route_endpoint**](ROUTINGApi.md#get_routing_static_route_endpoint) | **GET** /api/v2/routing/static_route | 
[**get_routing_static_routes_endpoint**](ROUTINGApi.md#get_routing_static_routes_endpoint) | **GET** /api/v2/routing/static_routes | 
[**patch_routing_gateway_default_endpoint**](ROUTINGApi.md#patch_routing_gateway_default_endpoint) | **PATCH** /api/v2/routing/gateway/default | 
[**patch_routing_gateway_endpoint**](ROUTINGApi.md#patch_routing_gateway_endpoint) | **PATCH** /api/v2/routing/gateway | 
[**patch_routing_gateway_group_endpoint**](ROUTINGApi.md#patch_routing_gateway_group_endpoint) | **PATCH** /api/v2/routing/gateway/group | 
[**patch_routing_gateway_group_priority_endpoint**](ROUTINGApi.md#patch_routing_gateway_group_priority_endpoint) | **PATCH** /api/v2/routing/gateway/group/priority | 
[**patch_routing_static_route_endpoint**](ROUTINGApi.md#patch_routing_static_route_endpoint) | **PATCH** /api/v2/routing/static_route | 
[**post_routing_apply_endpoint**](ROUTINGApi.md#post_routing_apply_endpoint) | **POST** /api/v2/routing/apply | 
[**post_routing_gateway_endpoint**](ROUTINGApi.md#post_routing_gateway_endpoint) | **POST** /api/v2/routing/gateway | 
[**post_routing_gateway_group_endpoint**](ROUTINGApi.md#post_routing_gateway_group_endpoint) | **POST** /api/v2/routing/gateway/group | 
[**post_routing_gateway_group_priority_endpoint**](ROUTINGApi.md#post_routing_gateway_group_priority_endpoint) | **POST** /api/v2/routing/gateway/group/priority | 
[**post_routing_static_route_endpoint**](ROUTINGApi.md#post_routing_static_route_endpoint) | **POST** /api/v2/routing/static_route | 


# **delete_routing_gateway_endpoint**
> GetRoutingGatewayEndpoint200Response delete_routing_gateway_endpoint(id, apply=apply)

<h3>Description:</h3>Deletes an existing Routing Gateway.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RoutingGateway<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_endpoint200_response import GetRoutingGatewayEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.
    apply = False # bool | Apply this deletion immediately. (optional) (default to False)

    try:
        api_response = api_instance.delete_routing_gateway_endpoint(id, apply=apply)
        print("The response of ROUTINGApi->delete_routing_gateway_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->delete_routing_gateway_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 
 **apply** | **bool**| Apply this deletion immediately. | [optional] [default to False]

### Return type

[**GetRoutingGatewayEndpoint200Response**](GetRoutingGatewayEndpoint200Response.md)

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

# **delete_routing_gateway_group_endpoint**
> GetRoutingGatewayGroupEndpoint200Response delete_routing_gateway_group_endpoint(id, apply=apply)

<h3>Description:</h3>Deletes an existing Routing Gateway Group.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_group_endpoint200_response import GetRoutingGatewayGroupEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.
    apply = False # bool | Apply this deletion immediately. (optional) (default to False)

    try:
        api_response = api_instance.delete_routing_gateway_group_endpoint(id, apply=apply)
        print("The response of ROUTINGApi->delete_routing_gateway_group_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->delete_routing_gateway_group_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 
 **apply** | **bool**| Apply this deletion immediately. | [optional] [default to False]

### Return type

[**GetRoutingGatewayGroupEndpoint200Response**](GetRoutingGatewayGroupEndpoint200Response.md)

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

# **delete_routing_gateway_group_priority_endpoint**
> GetRoutingGatewayGroupPriorityEndpoint200Response delete_routing_gateway_group_priority_endpoint(parent_id, id, apply=apply)

<h3>Description:</h3>Deletes an existing Routing Gateway Group Priority.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RoutingGatewayGroupPriority<br>**Parent model**: RoutingGatewayGroup<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-priority-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_group_priority_endpoint200_response import GetRoutingGatewayGroupPriorityEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    parent_id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the parent this object is nested under.
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.
    apply = False # bool | Apply this deletion immediately. (optional) (default to False)

    try:
        api_response = api_instance.delete_routing_gateway_group_priority_endpoint(parent_id, id, apply=apply)
        print("The response of ROUTINGApi->delete_routing_gateway_group_priority_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->delete_routing_gateway_group_priority_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the parent this object is nested under. | 
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 
 **apply** | **bool**| Apply this deletion immediately. | [optional] [default to False]

### Return type

[**GetRoutingGatewayGroupPriorityEndpoint200Response**](GetRoutingGatewayGroupPriorityEndpoint200Response.md)

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

# **delete_routing_gateway_groups_endpoint**
> GetRoutingGatewayGroupsEndpoint200Response delete_routing_gateway_groups_endpoint(limit=limit, offset=offset, query=query)

<h3>Description:</h3>Deletes multiple existing Routing Gateway Groups using a query.<br><br>WARNING: This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-groups-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_groups_endpoint200_response import GetRoutingGatewayGroupsEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    limit = 0 # int | The maximum number of objects to delete at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.delete_routing_gateway_groups_endpoint(limit=limit, offset=offset, query=query)
        print("The response of ROUTINGApi->delete_routing_gateway_groups_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->delete_routing_gateway_groups_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to delete at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetRoutingGatewayGroupsEndpoint200Response**](GetRoutingGatewayGroupsEndpoint200Response.md)

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

# **delete_routing_gateways_endpoint**
> GetRoutingGatewaysEndpoint200Response delete_routing_gateways_endpoint(limit=limit, offset=offset, query=query)

<h3>Description:</h3>Deletes multiple existing Routing Gatewaies using a query.<br><br>WARNING: This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: RoutingGateway<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateways-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateways_endpoint200_response import GetRoutingGatewaysEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    limit = 0 # int | The maximum number of objects to delete at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.delete_routing_gateways_endpoint(limit=limit, offset=offset, query=query)
        print("The response of ROUTINGApi->delete_routing_gateways_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->delete_routing_gateways_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to delete at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetRoutingGatewaysEndpoint200Response**](GetRoutingGatewaysEndpoint200Response.md)

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

# **delete_routing_static_route_endpoint**
> GetRoutingStaticRouteEndpoint200Response delete_routing_static_route_endpoint(id, apply=apply)

<h3>Description:</h3>Deletes an existing Static Route.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_static_route_endpoint200_response import GetRoutingStaticRouteEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.
    apply = False # bool | Apply this deletion immediately. (optional) (default to False)

    try:
        api_response = api_instance.delete_routing_static_route_endpoint(id, apply=apply)
        print("The response of ROUTINGApi->delete_routing_static_route_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->delete_routing_static_route_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 
 **apply** | **bool**| Apply this deletion immediately. | [optional] [default to False]

### Return type

[**GetRoutingStaticRouteEndpoint200Response**](GetRoutingStaticRouteEndpoint200Response.md)

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

# **delete_routing_static_routes_endpoint**
> GetRoutingStaticRoutesEndpoint200Response delete_routing_static_routes_endpoint(limit=limit, offset=offset, query=query)

<h3>Description:</h3>Deletes multiple existing Static Routes using a query.<br><br>WARNING: This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-routes-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_static_routes_endpoint200_response import GetRoutingStaticRoutesEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    limit = 0 # int | The maximum number of objects to delete at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.delete_routing_static_routes_endpoint(limit=limit, offset=offset, query=query)
        print("The response of ROUTINGApi->delete_routing_static_routes_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->delete_routing_static_routes_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to delete at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetRoutingStaticRoutesEndpoint200Response**](GetRoutingStaticRoutesEndpoint200Response.md)

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

# **get_routing_apply_endpoint**
> GetRoutingApplyEndpoint200Response get_routing_apply_endpoint()

<h3>Description:</h3>Reads current Routing Apply.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RoutingApply<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-apply-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_apply_endpoint200_response import GetRoutingApplyEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)

    try:
        api_response = api_instance.get_routing_apply_endpoint()
        print("The response of ROUTINGApi->get_routing_apply_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->get_routing_apply_endpoint: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetRoutingApplyEndpoint200Response**](GetRoutingApplyEndpoint200Response.md)

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

# **get_routing_gateway_default_endpoint**
> GetRoutingGatewayDefaultEndpoint200Response get_routing_gateway_default_endpoint()

<h3>Description:</h3>Reads current Default Gateway.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: DefaultGateway<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-default-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_default_endpoint200_response import GetRoutingGatewayDefaultEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)

    try:
        api_response = api_instance.get_routing_gateway_default_endpoint()
        print("The response of ROUTINGApi->get_routing_gateway_default_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->get_routing_gateway_default_endpoint: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetRoutingGatewayDefaultEndpoint200Response**](GetRoutingGatewayDefaultEndpoint200Response.md)

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

# **get_routing_gateway_endpoint**
> GetRoutingGatewayEndpoint200Response get_routing_gateway_endpoint(id)

<h3>Description:</h3>Reads an existing Routing Gateway.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RoutingGateway<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_endpoint200_response import GetRoutingGatewayEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_routing_gateway_endpoint(id)
        print("The response of ROUTINGApi->get_routing_gateway_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->get_routing_gateway_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetRoutingGatewayEndpoint200Response**](GetRoutingGatewayEndpoint200Response.md)

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

# **get_routing_gateway_group_endpoint**
> GetRoutingGatewayGroupEndpoint200Response get_routing_gateway_group_endpoint(id)

<h3>Description:</h3>Reads an existing Routing Gateway Group.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_group_endpoint200_response import GetRoutingGatewayGroupEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_routing_gateway_group_endpoint(id)
        print("The response of ROUTINGApi->get_routing_gateway_group_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->get_routing_gateway_group_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetRoutingGatewayGroupEndpoint200Response**](GetRoutingGatewayGroupEndpoint200Response.md)

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

# **get_routing_gateway_group_priority_endpoint**
> GetRoutingGatewayGroupPriorityEndpoint200Response get_routing_gateway_group_priority_endpoint(parent_id, id)

<h3>Description:</h3>Reads an existing Routing Gateway Group Priority.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RoutingGatewayGroupPriority<br>**Parent model**: RoutingGatewayGroup<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-priority-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_group_priority_endpoint200_response import GetRoutingGatewayGroupPriorityEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    parent_id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the parent this object is nested under.
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_routing_gateway_group_priority_endpoint(parent_id, id)
        print("The response of ROUTINGApi->get_routing_gateway_group_priority_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->get_routing_gateway_group_priority_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the parent this object is nested under. | 
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetRoutingGatewayGroupPriorityEndpoint200Response**](GetRoutingGatewayGroupPriorityEndpoint200Response.md)

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

# **get_routing_gateway_groups_endpoint**
> GetRoutingGatewayGroupsEndpoint200Response get_routing_gateway_groups_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing Routing Gateway Groups.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-groups-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_groups_endpoint200_response import GetRoutingGatewayGroupsEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_routing_gateway_groups_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of ROUTINGApi->get_routing_gateway_groups_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->get_routing_gateway_groups_endpoint: %s\n" % e)
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

[**GetRoutingGatewayGroupsEndpoint200Response**](GetRoutingGatewayGroupsEndpoint200Response.md)

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

# **get_routing_gateways_endpoint**
> GetRoutingGatewaysEndpoint200Response get_routing_gateways_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing Routing Gatewaies.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: RoutingGateway<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateways-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateways_endpoint200_response import GetRoutingGatewaysEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_routing_gateways_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of ROUTINGApi->get_routing_gateways_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->get_routing_gateways_endpoint: %s\n" % e)
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

[**GetRoutingGatewaysEndpoint200Response**](GetRoutingGatewaysEndpoint200Response.md)

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

# **get_routing_static_route_endpoint**
> GetRoutingStaticRouteEndpoint200Response get_routing_static_route_endpoint(id)

<h3>Description:</h3>Reads an existing Static Route.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_static_route_endpoint200_response import GetRoutingStaticRouteEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_routing_static_route_endpoint(id)
        print("The response of ROUTINGApi->get_routing_static_route_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->get_routing_static_route_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetRoutingStaticRouteEndpoint200Response**](GetRoutingStaticRouteEndpoint200Response.md)

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

# **get_routing_static_routes_endpoint**
> GetRoutingStaticRoutesEndpoint200Response get_routing_static_routes_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing Static Routes.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-routes-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_static_routes_endpoint200_response import GetRoutingStaticRoutesEndpoint200Response
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_routing_static_routes_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of ROUTINGApi->get_routing_static_routes_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->get_routing_static_routes_endpoint: %s\n" % e)
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

[**GetRoutingStaticRoutesEndpoint200Response**](GetRoutingStaticRoutesEndpoint200Response.md)

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

# **patch_routing_gateway_default_endpoint**
> GetRoutingGatewayDefaultEndpoint200Response patch_routing_gateway_default_endpoint(patch_routing_gateway_default_endpoint_request=patch_routing_gateway_default_endpoint_request)

<h3>Description:</h3>Updates current Default Gateway.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: DefaultGateway<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-default-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_default_endpoint200_response import GetRoutingGatewayDefaultEndpoint200Response
from pfsense_api_client.models.patch_routing_gateway_default_endpoint_request import PatchRoutingGatewayDefaultEndpointRequest
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    patch_routing_gateway_default_endpoint_request = openapi_client.PatchRoutingGatewayDefaultEndpointRequest() # PatchRoutingGatewayDefaultEndpointRequest |  (optional)

    try:
        api_response = api_instance.patch_routing_gateway_default_endpoint(patch_routing_gateway_default_endpoint_request=patch_routing_gateway_default_endpoint_request)
        print("The response of ROUTINGApi->patch_routing_gateway_default_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->patch_routing_gateway_default_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_routing_gateway_default_endpoint_request** | [**PatchRoutingGatewayDefaultEndpointRequest**](PatchRoutingGatewayDefaultEndpointRequest.md)|  | [optional] 

### Return type

[**GetRoutingGatewayDefaultEndpoint200Response**](GetRoutingGatewayDefaultEndpoint200Response.md)

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

# **patch_routing_gateway_endpoint**
> GetRoutingGatewayEndpoint200Response patch_routing_gateway_endpoint(patch_routing_gateway_endpoint_request=patch_routing_gateway_endpoint_request)

<h3>Description:</h3>Updates an existing Routing Gateway.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RoutingGateway<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_endpoint200_response import GetRoutingGatewayEndpoint200Response
from pfsense_api_client.models.patch_routing_gateway_endpoint_request import PatchRoutingGatewayEndpointRequest
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    patch_routing_gateway_endpoint_request = openapi_client.PatchRoutingGatewayEndpointRequest() # PatchRoutingGatewayEndpointRequest |  (optional)

    try:
        api_response = api_instance.patch_routing_gateway_endpoint(patch_routing_gateway_endpoint_request=patch_routing_gateway_endpoint_request)
        print("The response of ROUTINGApi->patch_routing_gateway_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->patch_routing_gateway_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_routing_gateway_endpoint_request** | [**PatchRoutingGatewayEndpointRequest**](PatchRoutingGatewayEndpointRequest.md)|  | [optional] 

### Return type

[**GetRoutingGatewayEndpoint200Response**](GetRoutingGatewayEndpoint200Response.md)

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

# **patch_routing_gateway_group_endpoint**
> GetRoutingGatewayGroupEndpoint200Response patch_routing_gateway_group_endpoint(patch_routing_gateway_group_endpoint_request=patch_routing_gateway_group_endpoint_request)

<h3>Description:</h3>Updates an existing Routing Gateway Group.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_group_endpoint200_response import GetRoutingGatewayGroupEndpoint200Response
from pfsense_api_client.models.patch_routing_gateway_group_endpoint_request import PatchRoutingGatewayGroupEndpointRequest
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    patch_routing_gateway_group_endpoint_request = openapi_client.PatchRoutingGatewayGroupEndpointRequest() # PatchRoutingGatewayGroupEndpointRequest |  (optional)

    try:
        api_response = api_instance.patch_routing_gateway_group_endpoint(patch_routing_gateway_group_endpoint_request=patch_routing_gateway_group_endpoint_request)
        print("The response of ROUTINGApi->patch_routing_gateway_group_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->patch_routing_gateway_group_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_routing_gateway_group_endpoint_request** | [**PatchRoutingGatewayGroupEndpointRequest**](PatchRoutingGatewayGroupEndpointRequest.md)|  | [optional] 

### Return type

[**GetRoutingGatewayGroupEndpoint200Response**](GetRoutingGatewayGroupEndpoint200Response.md)

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

# **patch_routing_gateway_group_priority_endpoint**
> GetRoutingGatewayGroupPriorityEndpoint200Response patch_routing_gateway_group_priority_endpoint(patch_routing_gateway_group_priority_endpoint_request=patch_routing_gateway_group_priority_endpoint_request)

<h3>Description:</h3>Updates an existing Routing Gateway Group Priority.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RoutingGatewayGroupPriority<br>**Parent model**: RoutingGatewayGroup<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-priority-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_group_priority_endpoint200_response import GetRoutingGatewayGroupPriorityEndpoint200Response
from pfsense_api_client.models.patch_routing_gateway_group_priority_endpoint_request import PatchRoutingGatewayGroupPriorityEndpointRequest
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    patch_routing_gateway_group_priority_endpoint_request = openapi_client.PatchRoutingGatewayGroupPriorityEndpointRequest() # PatchRoutingGatewayGroupPriorityEndpointRequest |  (optional)

    try:
        api_response = api_instance.patch_routing_gateway_group_priority_endpoint(patch_routing_gateway_group_priority_endpoint_request=patch_routing_gateway_group_priority_endpoint_request)
        print("The response of ROUTINGApi->patch_routing_gateway_group_priority_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->patch_routing_gateway_group_priority_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_routing_gateway_group_priority_endpoint_request** | [**PatchRoutingGatewayGroupPriorityEndpointRequest**](PatchRoutingGatewayGroupPriorityEndpointRequest.md)|  | [optional] 

### Return type

[**GetRoutingGatewayGroupPriorityEndpoint200Response**](GetRoutingGatewayGroupPriorityEndpoint200Response.md)

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

# **patch_routing_static_route_endpoint**
> GetRoutingStaticRouteEndpoint200Response patch_routing_static_route_endpoint(patch_routing_static_route_endpoint_request=patch_routing_static_route_endpoint_request)

<h3>Description:</h3>Updates an existing Static Route.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_static_route_endpoint200_response import GetRoutingStaticRouteEndpoint200Response
from pfsense_api_client.models.patch_routing_static_route_endpoint_request import PatchRoutingStaticRouteEndpointRequest
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    patch_routing_static_route_endpoint_request = openapi_client.PatchRoutingStaticRouteEndpointRequest() # PatchRoutingStaticRouteEndpointRequest |  (optional)

    try:
        api_response = api_instance.patch_routing_static_route_endpoint(patch_routing_static_route_endpoint_request=patch_routing_static_route_endpoint_request)
        print("The response of ROUTINGApi->patch_routing_static_route_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->patch_routing_static_route_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_routing_static_route_endpoint_request** | [**PatchRoutingStaticRouteEndpointRequest**](PatchRoutingStaticRouteEndpointRequest.md)|  | [optional] 

### Return type

[**GetRoutingStaticRouteEndpoint200Response**](GetRoutingStaticRouteEndpoint200Response.md)

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

# **post_routing_apply_endpoint**
> GetRoutingApplyEndpoint200Response post_routing_apply_endpoint(post_routing_apply_endpoint_request=post_routing_apply_endpoint_request)

<h3>Description:</h3>Creates Routing Apply.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RoutingApply<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-apply-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_apply_endpoint200_response import GetRoutingApplyEndpoint200Response
from pfsense_api_client.models.post_routing_apply_endpoint_request import PostRoutingApplyEndpointRequest
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    post_routing_apply_endpoint_request = openapi_client.PostRoutingApplyEndpointRequest() # PostRoutingApplyEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_routing_apply_endpoint(post_routing_apply_endpoint_request=post_routing_apply_endpoint_request)
        print("The response of ROUTINGApi->post_routing_apply_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->post_routing_apply_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_routing_apply_endpoint_request** | [**PostRoutingApplyEndpointRequest**](PostRoutingApplyEndpointRequest.md)|  | [optional] 

### Return type

[**GetRoutingApplyEndpoint200Response**](GetRoutingApplyEndpoint200Response.md)

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

# **post_routing_gateway_endpoint**
> GetRoutingGatewayEndpoint200Response post_routing_gateway_endpoint(post_routing_gateway_endpoint_request=post_routing_gateway_endpoint_request)

<h3>Description:</h3>Creates a new Routing Gateway.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RoutingGateway<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_endpoint200_response import GetRoutingGatewayEndpoint200Response
from pfsense_api_client.models.post_routing_gateway_endpoint_request import PostRoutingGatewayEndpointRequest
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    post_routing_gateway_endpoint_request = openapi_client.PostRoutingGatewayEndpointRequest() # PostRoutingGatewayEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_routing_gateway_endpoint(post_routing_gateway_endpoint_request=post_routing_gateway_endpoint_request)
        print("The response of ROUTINGApi->post_routing_gateway_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->post_routing_gateway_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_routing_gateway_endpoint_request** | [**PostRoutingGatewayEndpointRequest**](PostRoutingGatewayEndpointRequest.md)|  | [optional] 

### Return type

[**GetRoutingGatewayEndpoint200Response**](GetRoutingGatewayEndpoint200Response.md)

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

# **post_routing_gateway_group_endpoint**
> GetRoutingGatewayGroupEndpoint200Response post_routing_gateway_group_endpoint(post_routing_gateway_group_endpoint_request=post_routing_gateway_group_endpoint_request)

<h3>Description:</h3>Creates a new Routing Gateway Group.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RoutingGatewayGroup<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_group_endpoint200_response import GetRoutingGatewayGroupEndpoint200Response
from pfsense_api_client.models.post_routing_gateway_group_endpoint_request import PostRoutingGatewayGroupEndpointRequest
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    post_routing_gateway_group_endpoint_request = openapi_client.PostRoutingGatewayGroupEndpointRequest() # PostRoutingGatewayGroupEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_routing_gateway_group_endpoint(post_routing_gateway_group_endpoint_request=post_routing_gateway_group_endpoint_request)
        print("The response of ROUTINGApi->post_routing_gateway_group_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->post_routing_gateway_group_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_routing_gateway_group_endpoint_request** | [**PostRoutingGatewayGroupEndpointRequest**](PostRoutingGatewayGroupEndpointRequest.md)|  | [optional] 

### Return type

[**GetRoutingGatewayGroupEndpoint200Response**](GetRoutingGatewayGroupEndpoint200Response.md)

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

# **post_routing_gateway_group_priority_endpoint**
> GetRoutingGatewayGroupPriorityEndpoint200Response post_routing_gateway_group_priority_endpoint(post_routing_gateway_group_priority_endpoint_request=post_routing_gateway_group_priority_endpoint_request)

<h3>Description:</h3>Creates a new Routing Gateway Group Priority.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: RoutingGatewayGroupPriority<br>**Parent model**: RoutingGatewayGroup<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-gateway-group-priority-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_gateway_group_priority_endpoint200_response import GetRoutingGatewayGroupPriorityEndpoint200Response
from pfsense_api_client.models.post_routing_gateway_group_priority_endpoint_request import PostRoutingGatewayGroupPriorityEndpointRequest
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    post_routing_gateway_group_priority_endpoint_request = openapi_client.PostRoutingGatewayGroupPriorityEndpointRequest() # PostRoutingGatewayGroupPriorityEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_routing_gateway_group_priority_endpoint(post_routing_gateway_group_priority_endpoint_request=post_routing_gateway_group_priority_endpoint_request)
        print("The response of ROUTINGApi->post_routing_gateway_group_priority_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->post_routing_gateway_group_priority_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_routing_gateway_group_priority_endpoint_request** | [**PostRoutingGatewayGroupPriorityEndpointRequest**](PostRoutingGatewayGroupPriorityEndpointRequest.md)|  | [optional] 

### Return type

[**GetRoutingGatewayGroupPriorityEndpoint200Response**](GetRoutingGatewayGroupPriorityEndpoint200Response.md)

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

# **post_routing_static_route_endpoint**
> GetRoutingStaticRouteEndpoint200Response post_routing_static_route_endpoint(post_routing_static_route_endpoint_request=post_routing_static_route_endpoint_request)

<h3>Description:</h3>Creates a new Static Route.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_routing_static_route_endpoint200_response import GetRoutingStaticRouteEndpoint200Response
from pfsense_api_client.models.post_routing_static_route_endpoint_request import PostRoutingStaticRouteEndpointRequest
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
    api_instance = openapi_client.ROUTINGApi(api_client)
    post_routing_static_route_endpoint_request = openapi_client.PostRoutingStaticRouteEndpointRequest() # PostRoutingStaticRouteEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_routing_static_route_endpoint(post_routing_static_route_endpoint_request=post_routing_static_route_endpoint_request)
        print("The response of ROUTINGApi->post_routing_static_route_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ROUTINGApi->post_routing_static_route_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_routing_static_route_endpoint_request** | [**PostRoutingStaticRouteEndpointRequest**](PostRoutingStaticRouteEndpointRequest.md)|  | [optional] 

### Return type

[**GetRoutingStaticRouteEndpoint200Response**](GetRoutingStaticRouteEndpoint200Response.md)

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

