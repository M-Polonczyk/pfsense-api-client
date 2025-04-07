# RoutingApply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; when all routing changes are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending routing changes that have not been applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.routing_apply import RoutingApply

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingApply from a JSON string
routing_apply_instance = RoutingApply.from_json(json)
# print the JSON string representation of the object
print(RoutingApply.to_json())

# convert the object into a dict
routing_apply_dict = routing_apply_instance.to_dict()
# create an instance of RoutingApply from a dict
routing_apply_from_dict = RoutingApply.from_dict(routing_apply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


