# GraphQLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | The GraphQL response data. | [optional] 
**errors** | [**List[GraphQLResponseErrorsInner]**](GraphQLResponseErrorsInner.md) | The GraphQL response errors. | [optional] 

## Example

```python
from pfsense_api_client.models.graph_ql_response import GraphQLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GraphQLResponse from a JSON string
graph_ql_response_instance = GraphQLResponse.from_json(json)
# print the JSON string representation of the object
print(GraphQLResponse.to_json())

# convert the object into a dict
graph_ql_response_dict = graph_ql_response_instance.to_dict()
# create an instance of GraphQLResponse from a dict
graph_ql_response_from_dict = GraphQLResponse.from_dict(graph_ql_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


