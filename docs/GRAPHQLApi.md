# openapi_client.GRAPHQLApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_graph_ql_endpoint**](GRAPHQLApi.md#post_graph_ql_endpoint) | **POST** /api/v2/graphql | 


# **post_graph_ql_endpoint**
> PostGraphQLEndpoint200Response post_graph_ql_endpoint(post_graph_ql_endpoint_request=post_graph_ql_endpoint_request)

<h3>Description:</h3>Execute a GraphQL query. For more information on utilizing the GraphQL API, please refer to https://pfrest.org/graphql.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: GraphQL<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-graphql-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

### Example

* Api Key Authentication (KeyAuth):
* Basic Authentication (BasicAuth):
* Bearer (JWT) Authentication (JWTAuth):

```python
import openapi_client
from pfsense_api_client.models.post_graph_ql_endpoint200_response import PostGraphQLEndpoint200Response
from pfsense_api_client.models.post_graph_ql_endpoint_request import PostGraphQLEndpointRequest
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
    api_instance = openapi_client.GRAPHQLApi(api_client)
    post_graph_ql_endpoint_request = openapi_client.PostGraphQLEndpointRequest() # PostGraphQLEndpointRequest |  (optional)

    try:
        api_response = api_instance.post_graph_ql_endpoint(post_graph_ql_endpoint_request=post_graph_ql_endpoint_request)
        print("The response of GRAPHQLApi->post_graph_ql_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GRAPHQLApi->post_graph_ql_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_graph_ql_endpoint_request** | [**PostGraphQLEndpointRequest**](PostGraphQLEndpointRequest.md)|  | [optional] 

### Return type

[**PostGraphQLEndpoint200Response**](PostGraphQLEndpoint200Response.md)

### Authorization

[KeyAuth](../README.md#KeyAuth), [BasicAuth](../README.md#BasicAuth), [JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The GraphQL query execution completed. All GraphQL responses return a 200 OK regardless of whether the query was successful or not. Use the \&quot;errors\&quot; field in the response data to determine if the query was successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

