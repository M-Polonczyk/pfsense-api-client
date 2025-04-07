# WireGuardApply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; when all WireGuard changes are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending WireGuard changes that have not been applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.wire_guard_apply import WireGuardApply

# TODO update the JSON string below
json = "{}"
# create an instance of WireGuardApply from a JSON string
wire_guard_apply_instance = WireGuardApply.from_json(json)
# print the JSON string representation of the object
print(WireGuardApply.to_json())

# convert the object into a dict
wire_guard_apply_dict = wire_guard_apply_instance.to_dict()
# create an instance of WireGuardApply from a dict
wire_guard_apply_from_dict = WireGuardApply.from_dict(wire_guard_apply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


