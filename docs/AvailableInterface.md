# AvailableInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_if** | **str** | The name of the interface.&lt;br&gt; | [optional] 
**mac** | **str** | The MAC address of the interface.&lt;br&gt; | [optional] 
**dmesg** | **str** | The description of the interface.&lt;br&gt; | [optional] 
**in_use_by** | **str** | The pfSense interface ID that is using this interface.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.available_interface import AvailableInterface

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableInterface from a JSON string
available_interface_instance = AvailableInterface.from_json(json)
# print the JSON string representation of the object
print(AvailableInterface.to_json())

# convert the object into a dict
available_interface_dict = available_interface_instance.to_dict()
# create an instance of AvailableInterface from a dict
available_interface_from_dict = AvailableInterface.from_dict(available_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


