# openapi_client.DIAGNOSTICSApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_diagnostics_arp_table_endpoint**](DIAGNOSTICSApi.md#delete_diagnostics_arp_table_endpoint) | **DELETE** /api/v2/diagnostics/arp_table | 
[**delete_diagnostics_arp_table_entry_endpoint**](DIAGNOSTICSApi.md#delete_diagnostics_arp_table_entry_endpoint) | **DELETE** /api/v2/diagnostics/arp_table/entry | 
[**delete_diagnostics_config_history_revision_endpoint**](DIAGNOSTICSApi.md#delete_diagnostics_config_history_revision_endpoint) | **DELETE** /api/v2/diagnostics/config_history/revision | 
[**delete_diagnostics_config_history_revisions_endpoint**](DIAGNOSTICSApi.md#delete_diagnostics_config_history_revisions_endpoint) | **DELETE** /api/v2/diagnostics/config_history/revisions | 
[**get_diagnostics_arp_table_endpoint**](DIAGNOSTICSApi.md#get_diagnostics_arp_table_endpoint) | **GET** /api/v2/diagnostics/arp_table | 
[**get_diagnostics_arp_table_entry_endpoint**](DIAGNOSTICSApi.md#get_diagnostics_arp_table_entry_endpoint) | **GET** /api/v2/diagnostics/arp_table/entry | 
[**get_diagnostics_config_history_revision_endpoint**](DIAGNOSTICSApi.md#get_diagnostics_config_history_revision_endpoint) | **GET** /api/v2/diagnostics/config_history/revision | 
[**get_diagnostics_config_history_revisions_endpoint**](DIAGNOSTICSApi.md#get_diagnostics_config_history_revisions_endpoint) | **GET** /api/v2/diagnostics/config_history/revisions | 
[**post_diagnostics_command_prompt_endpoint**](DIAGNOSTICSApi.md#post_diagnostics_command_prompt_endpoint) | **POST** /api/v2/diagnostics/command_prompt | 
[**post_diagnostics_halt_system_endpoint**](DIAGNOSTICSApi.md#post_diagnostics_halt_system_endpoint) | **POST** /api/v2/diagnostics/halt_system | 
[**post_diagnostics_reboot_endpoint**](DIAGNOSTICSApi.md#post_diagnostics_reboot_endpoint) | **POST** /api/v2/diagnostics/reboot | 


# **delete_diagnostics_arp_table_endpoint**
> GetDiagnosticsARPTableEndpoint200Response delete_diagnostics_arp_table_endpoint(limit=limit, offset=offset, query=query)

<h3>Description:</h3>Deletes multiple existing ARP Table Entries using a query.<br><br>WARNING: This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: ARPTable<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-arp-table-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_diagnostics_arp_table_endpoint200_response import GetDiagnosticsARPTableEndpoint200Response
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
    api_instance = openapi_client.DIAGNOSTICSApi(api_client)
    limit = 0 # int | The maximum number of objects to delete at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.delete_diagnostics_arp_table_endpoint(limit=limit, offset=offset, query=query)
        print("The response of DIAGNOSTICSApi->delete_diagnostics_arp_table_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DIAGNOSTICSApi->delete_diagnostics_arp_table_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to delete at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetDiagnosticsARPTableEndpoint200Response**](GetDiagnosticsARPTableEndpoint200Response.md)

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

# **delete_diagnostics_arp_table_entry_endpoint**
> GetDiagnosticsARPTableEntryEndpoint200Response delete_diagnostics_arp_table_entry_endpoint(id)

<h3>Description:</h3>Deletes an existing ARP Table Entry.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: ARPTable<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-arp-table-entry-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_diagnostics_arp_table_entry_endpoint200_response import GetDiagnosticsARPTableEntryEndpoint200Response
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
    api_instance = openapi_client.DIAGNOSTICSApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.delete_diagnostics_arp_table_entry_endpoint(id)
        print("The response of DIAGNOSTICSApi->delete_diagnostics_arp_table_entry_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DIAGNOSTICSApi->delete_diagnostics_arp_table_entry_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetDiagnosticsARPTableEntryEndpoint200Response**](GetDiagnosticsARPTableEntryEndpoint200Response.md)

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

# **delete_diagnostics_config_history_revision_endpoint**
> GetDiagnosticsConfigHistoryRevisionEndpoint200Response delete_diagnostics_config_history_revision_endpoint(id)

<h3>Description:</h3>Deletes a configuration revision along with it's associated backup file.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: ConfigHistoryRevision<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-config-history-revision-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_diagnostics_config_history_revision_endpoint200_response import GetDiagnosticsConfigHistoryRevisionEndpoint200Response
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
    api_instance = openapi_client.DIAGNOSTICSApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.delete_diagnostics_config_history_revision_endpoint(id)
        print("The response of DIAGNOSTICSApi->delete_diagnostics_config_history_revision_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DIAGNOSTICSApi->delete_diagnostics_config_history_revision_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetDiagnosticsConfigHistoryRevisionEndpoint200Response**](GetDiagnosticsConfigHistoryRevisionEndpoint200Response.md)

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

# **delete_diagnostics_config_history_revisions_endpoint**
> GetDiagnosticsConfigHistoryRevisionsEndpoint200Response delete_diagnostics_config_history_revisions_endpoint(limit=limit, offset=offset, query=query)

<h3>Description:</h3>Deletes multiple existing Configuration History Entries using a query.<br><br>WARNING: This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: ConfigHistoryRevision<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-config-history-revisions-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_diagnostics_config_history_revisions_endpoint200_response import GetDiagnosticsConfigHistoryRevisionsEndpoint200Response
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
    api_instance = openapi_client.DIAGNOSTICSApi(api_client)
    limit = 0 # int | The maximum number of objects to delete at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.delete_diagnostics_config_history_revisions_endpoint(limit=limit, offset=offset, query=query)
        print("The response of DIAGNOSTICSApi->delete_diagnostics_config_history_revisions_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DIAGNOSTICSApi->delete_diagnostics_config_history_revisions_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to delete at once. Set to 0 for no limit. | [optional] [default to 0]
 **offset** | **int**| The starting point in the dataset to begin fetching objects. | [optional] [default to 0]
 **query** | [**Dict[str, str]**](str.md)| The arbitrary query parameters to include in the request.&lt;br&gt;&lt;br&gt;Note: This does not define an actual parameter, rather it allows for any arbitrary query parameters to be included in the request. | [optional] 

### Return type

[**GetDiagnosticsConfigHistoryRevisionsEndpoint200Response**](GetDiagnosticsConfigHistoryRevisionsEndpoint200Response.md)

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

# **get_diagnostics_arp_table_endpoint**
> GetDiagnosticsARPTableEndpoint200Response get_diagnostics_arp_table_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing ARP Table Entries.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: ARPTable<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-arp-table-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_diagnostics_arp_table_endpoint200_response import GetDiagnosticsARPTableEndpoint200Response
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
    api_instance = openapi_client.DIAGNOSTICSApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_diagnostics_arp_table_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of DIAGNOSTICSApi->get_diagnostics_arp_table_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DIAGNOSTICSApi->get_diagnostics_arp_table_endpoint: %s\n" % e)
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

[**GetDiagnosticsARPTableEndpoint200Response**](GetDiagnosticsARPTableEndpoint200Response.md)

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

# **get_diagnostics_arp_table_entry_endpoint**
> GetDiagnosticsARPTableEntryEndpoint200Response get_diagnostics_arp_table_entry_endpoint(id)

<h3>Description:</h3>Reads an existing ARP Table Entry.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: ARPTable<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-arp-table-entry-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_diagnostics_arp_table_entry_endpoint200_response import GetDiagnosticsARPTableEntryEndpoint200Response
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
    api_instance = openapi_client.DIAGNOSTICSApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_diagnostics_arp_table_entry_endpoint(id)
        print("The response of DIAGNOSTICSApi->get_diagnostics_arp_table_entry_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DIAGNOSTICSApi->get_diagnostics_arp_table_entry_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetDiagnosticsARPTableEntryEndpoint200Response**](GetDiagnosticsARPTableEntryEndpoint200Response.md)

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

# **get_diagnostics_config_history_revision_endpoint**
> GetDiagnosticsConfigHistoryRevisionEndpoint200Response get_diagnostics_config_history_revision_endpoint(id)

<h3>Description:</h3>Reads an existing Configuration History Entry.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: ConfigHistoryRevision<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-config-history-revision-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_diagnostics_config_history_revision_endpoint200_response import GetDiagnosticsConfigHistoryRevisionEndpoint200Response
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
    api_instance = openapi_client.DIAGNOSTICSApi(api_client)
    id = openapi_client.DeleteAuthKeyEndpointIdParameter() # DeleteAuthKeyEndpointIdParameter | The ID of the object to target.

    try:
        api_response = api_instance.get_diagnostics_config_history_revision_endpoint(id)
        print("The response of DIAGNOSTICSApi->get_diagnostics_config_history_revision_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DIAGNOSTICSApi->get_diagnostics_config_history_revision_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**DeleteAuthKeyEndpointIdParameter**](.md)| The ID of the object to target. | 

### Return type

[**GetDiagnosticsConfigHistoryRevisionEndpoint200Response**](GetDiagnosticsConfigHistoryRevisionEndpoint200Response.md)

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

# **get_diagnostics_config_history_revisions_endpoint**
> GetDiagnosticsConfigHistoryRevisionsEndpoint200Response get_diagnostics_config_history_revisions_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)

<h3>Description:</h3>Reads all existing Configuration History Entries.<br><h3>Details:</h3>**Endpoint type**: Plural<br>**Associated model**: ConfigHistoryRevision<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-config-history-revisions-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.get_diagnostics_config_history_revisions_endpoint200_response import GetDiagnosticsConfigHistoryRevisionsEndpoint200Response
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
    api_instance = openapi_client.DIAGNOSTICSApi(api_client)
    limit = 0 # int | The number of objects to obtain at once. Set to 0 for no limit. (optional) (default to 0)
    offset = 0 # int | The starting point in the dataset to begin fetching objects. (optional) (default to 0)
    sort_by = ['sort_by_example'] # List[str] | The fields to sort response data by. (optional)
    sort_order = 'sort_order_example' # str | The order to sort response data by. (optional)
    sort_flags = 'sort_flags_example' # str | The sort flag to use to customize the behavior of the sort. (optional)
    query = {'key': 'query_example'} # Dict[str, str] | The arbitrary query parameters to include in the request.<br><br>Note: This does not define a real parameter (e.g. there is no `query` parameter), rather it allows for any arbitrary query parameters to be included in the request. (optional)

    try:
        api_response = api_instance.get_diagnostics_config_history_revisions_endpoint(limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, sort_flags=sort_flags, query=query)
        print("The response of DIAGNOSTICSApi->get_diagnostics_config_history_revisions_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DIAGNOSTICSApi->get_diagnostics_config_history_revisions_endpoint: %s\n" % e)
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

[**GetDiagnosticsConfigHistoryRevisionsEndpoint200Response**](GetDiagnosticsConfigHistoryRevisionsEndpoint200Response.md)

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

# **post_diagnostics_command_prompt_endpoint**
> PostDiagnosticsCommandPromptEndpoint200Response post_diagnostics_command_prompt_endpoint(post_diagnostics_command_prompt_endpoint_request=post_diagnostics_command_prompt_endpoint_request)

<h3>Description:</h3>Executes a shell command.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: CommandPrompt<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-command-prompt-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.post_diagnostics_command_prompt_endpoint200_response import PostDiagnosticsCommandPromptEndpoint200Response
from pfsense_api_client.models.post_diagnostics_command_prompt_endpoint_request import PostDiagnosticsCommandPromptEndpointRequest
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
    api_instance = openapi_client.DIAGNOSTICSApi(api_client)
    post_diagnostics_command_prompt_endpoint_request = openapi_client.PostDiagnosticsCommandPromptEndpointRequest() # PostDiagnosticsCommandPromptEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_diagnostics_command_prompt_endpoint(post_diagnostics_command_prompt_endpoint_request=post_diagnostics_command_prompt_endpoint_request)
        print("The response of DIAGNOSTICSApi->post_diagnostics_command_prompt_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DIAGNOSTICSApi->post_diagnostics_command_prompt_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_diagnostics_command_prompt_endpoint_request** | [**PostDiagnosticsCommandPromptEndpointRequest**](PostDiagnosticsCommandPromptEndpointRequest.md)|  | [optional] 

### Return type

[**PostDiagnosticsCommandPromptEndpoint200Response**](PostDiagnosticsCommandPromptEndpoint200Response.md)

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

# **post_diagnostics_halt_system_endpoint**
> PostDiagnosticsHaltSystemEndpoint200Response post_diagnostics_halt_system_endpoint(post_diagnostics_halt_system_endpoint_request=post_diagnostics_halt_system_endpoint_request)

<h3>Description:</h3>Initiates a System Halt.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: SystemHalt<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-halt-system-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.post_diagnostics_halt_system_endpoint200_response import PostDiagnosticsHaltSystemEndpoint200Response
from pfsense_api_client.models.post_diagnostics_halt_system_endpoint_request import PostDiagnosticsHaltSystemEndpointRequest
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
    api_instance = openapi_client.DIAGNOSTICSApi(api_client)
    post_diagnostics_halt_system_endpoint_request = openapi_client.PostDiagnosticsHaltSystemEndpointRequest() # PostDiagnosticsHaltSystemEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_diagnostics_halt_system_endpoint(post_diagnostics_halt_system_endpoint_request=post_diagnostics_halt_system_endpoint_request)
        print("The response of DIAGNOSTICSApi->post_diagnostics_halt_system_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DIAGNOSTICSApi->post_diagnostics_halt_system_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_diagnostics_halt_system_endpoint_request** | [**PostDiagnosticsHaltSystemEndpointRequest**](PostDiagnosticsHaltSystemEndpointRequest.md)|  | [optional] 

### Return type

[**PostDiagnosticsHaltSystemEndpoint200Response**](PostDiagnosticsHaltSystemEndpoint200Response.md)

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

# **post_diagnostics_reboot_endpoint**
> PostDiagnosticsRebootEndpoint200Response post_diagnostics_reboot_endpoint(post_diagnostics_reboot_endpoint_request=post_diagnostics_reboot_endpoint_request)

<h3>Description:</h3>Initiates a System Reboot.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: SystemReboot<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-reboot-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.post_diagnostics_reboot_endpoint200_response import PostDiagnosticsRebootEndpoint200Response
from pfsense_api_client.models.post_diagnostics_reboot_endpoint_request import PostDiagnosticsRebootEndpointRequest
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
    api_instance = openapi_client.DIAGNOSTICSApi(api_client)
    post_diagnostics_reboot_endpoint_request = openapi_client.PostDiagnosticsRebootEndpointRequest() # PostDiagnosticsRebootEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_diagnostics_reboot_endpoint(post_diagnostics_reboot_endpoint_request=post_diagnostics_reboot_endpoint_request)
        print("The response of DIAGNOSTICSApi->post_diagnostics_reboot_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DIAGNOSTICSApi->post_diagnostics_reboot_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_diagnostics_reboot_endpoint_request** | [**PostDiagnosticsRebootEndpointRequest**](PostDiagnosticsRebootEndpointRequest.md)|  | [optional] 

### Return type

[**PostDiagnosticsRebootEndpoint200Response**](PostDiagnosticsRebootEndpoint200Response.md)

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

