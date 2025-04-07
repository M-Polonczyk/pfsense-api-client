# VirtualIPApply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; when all virtual IP changes are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending virtual IP changes that have not been applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.virtual_ip_apply import VirtualIPApply

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualIPApply from a JSON string
virtual_ip_apply_instance = VirtualIPApply.from_json(json)
# print the JSON string representation of the object
print(VirtualIPApply.to_json())

# convert the object into a dict
virtual_ip_apply_dict = virtual_ip_apply_instance.to_dict()
# create an instance of VirtualIPApply from a dict
virtual_ip_apply_from_dict = VirtualIPApply.from_dict(virtual_ip_apply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


