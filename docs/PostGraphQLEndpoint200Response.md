# PostGraphQLEndpoint200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PostAuthJWTEndpoint401ResponseAllOfData**](PostAuthJWTEndpoint401ResponseAllOfData.md) |  | [optional] 
**errors** | [**List[GraphQLResponseErrorsInner]**](GraphQLResponseErrorsInner.md) | The GraphQL response errors. | [optional] 

## Example

```python
from pfsense_api_client.models.post_graph_ql_endpoint200_response import PostGraphQLEndpoint200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostGraphQLEndpoint200Response from a JSON string
post_graph_ql_endpoint200_response_instance = PostGraphQLEndpoint200Response.from_json(json)
# print the JSON string representation of the object
print(PostGraphQLEndpoint200Response.to_json())

# convert the object into a dict
post_graph_ql_endpoint200_response_dict = post_graph_ql_endpoint200_response_instance.to_dict()
# create an instance of PostGraphQLEndpoint200Response from a dict
post_graph_ql_endpoint200_response_from_dict = PostGraphQLEndpoint200Response.from_dict(post_graph_ql_endpoint200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


