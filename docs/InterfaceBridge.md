# InterfaceBridge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | **List[str]** | The member interfaces to include in this bridge.&lt;br&gt; | [optional] 
**descr** | **str** | A description for this interface bridge.&lt;br&gt; | [optional] 
**bridgeif** | **str** | The real interface name for this bridge interface.&lt;br&gt; | [optional] [readonly] [default to 'bridge0']

## Example

```python
from pfsense_api_client.models.interface_bridge import InterfaceBridge

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceBridge from a JSON string
interface_bridge_instance = InterfaceBridge.from_json(json)
# print the JSON string representation of the object
print(InterfaceBridge.to_json())

# convert the object into a dict
interface_bridge_dict = interface_bridge_instance.to_dict()
# create an instance of InterfaceBridge from a dict
interface_bridge_from_dict = InterfaceBridge.from_dict(interface_bridge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


