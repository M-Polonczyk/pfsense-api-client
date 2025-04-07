# InterfaceGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ifname** | **str** | The name of this interface group.&lt;br&gt; | [optional] 
**members** | **List[str]** | The member interfaces to assign to this interface group.&lt;br&gt; | [optional] 
**descr** | **str** | The description for this interface group.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.interface_group import InterfaceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceGroup from a JSON string
interface_group_instance = InterfaceGroup.from_json(json)
# print the JSON string representation of the object
print(InterfaceGroup.to_json())

# convert the object into a dict
interface_group_dict = interface_group_instance.to_dict()
# create an instance of InterfaceGroup from a dict
interface_group_from_dict = InterfaceGroup.from_dict(interface_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


