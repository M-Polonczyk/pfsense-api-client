# GraphQLResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The error message. | [optional] 
**extensions** | [**GraphQLResponseErrorsInnerExtensions**](GraphQLResponseErrorsInnerExtensions.md) |  | [optional] 
**locations** | [**List[GraphQLResponseErrorsInnerLocationsInner]**](GraphQLResponseErrorsInnerLocationsInner.md) | The error locations. | [optional] 
**path** | **List[str]** | The error path. | [optional] 

## Example

```python
from pfsense_api_client.models.graph_ql_response_errors_inner import GraphQLResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GraphQLResponseErrorsInner from a JSON string
graph_ql_response_errors_inner_instance = GraphQLResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(GraphQLResponseErrorsInner.to_json())

# convert the object into a dict
graph_ql_response_errors_inner_dict = graph_ql_response_errors_inner_instance.to_dict()
# create an instance of GraphQLResponseErrorsInner from a dict
graph_ql_response_errors_inner_from_dict = GraphQLResponseErrorsInner.from_dict(graph_ql_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


