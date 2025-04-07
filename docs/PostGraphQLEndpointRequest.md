# PostGraphQLEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The GraphQL query/mutation to execute.&lt;br&gt; | [optional] 
**variables** | **object** | The variables to pass to the GraphQL query or mutation. In general, this will be an object containing the variables to pass to the query or mutation.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_graph_ql_endpoint_request import PostGraphQLEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGraphQLEndpointRequest from a JSON string
post_graph_ql_endpoint_request_instance = PostGraphQLEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostGraphQLEndpointRequest.to_json())

# convert the object into a dict
post_graph_ql_endpoint_request_dict = post_graph_ql_endpoint_request_instance.to_dict()
# create an instance of PostGraphQLEndpointRequest from a dict
post_graph_ql_endpoint_request_from_dict = PostGraphQLEndpointRequest.from_dict(post_graph_ql_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


