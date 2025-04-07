# GraphQL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The GraphQL query/mutation to execute.&lt;br&gt; | [optional] 
**variables** | **object** | The variables to pass to the GraphQL query or mutation. In general, this will be an object containing the variables to pass to the query or mutation.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.graph_ql import GraphQL

# TODO update the JSON string below
json = "{}"
# create an instance of GraphQL from a JSON string
graph_ql_instance = GraphQL.from_json(json)
# print the JSON string representation of the object
print(GraphQL.to_json())

# convert the object into a dict
graph_ql_dict = graph_ql_instance.to_dict()
# create an instance of GraphQL from a dict
graph_ql_from_dict = GraphQL.from_dict(graph_ql_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


