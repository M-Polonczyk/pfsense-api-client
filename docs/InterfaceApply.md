# InterfaceApply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; when all interfaces are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending interface changes that have not been applied.&lt;br&gt; | [optional] [readonly] 
**pending_interfaces** | **List[str]** | Displays a list of interfaces that have pending changes waiting to be applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.interface_apply import InterfaceApply

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceApply from a JSON string
interface_apply_instance = InterfaceApply.from_json(json)
# print the JSON string representation of the object
print(InterfaceApply.to_json())

# convert the object into a dict
interface_apply_dict = interface_apply_instance.to_dict()
# create an instance of InterfaceApply from a dict
interface_apply_from_dict = InterfaceApply.from_dict(interface_apply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


