# PatchInterfaceBridgeEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | **List[str]** | The member interfaces to include in this bridge.&lt;br&gt; | [optional] 
**descr** | **str** | A description for this interface bridge.&lt;br&gt; | [optional] 
**bridgeif** | **str** | The real interface name for this bridge interface.&lt;br&gt; | [optional] [readonly] [default to 'bridge0']
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_interface_bridge_endpoint_request import PatchInterfaceBridgeEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchInterfaceBridgeEndpointRequest from a JSON string
patch_interface_bridge_endpoint_request_instance = PatchInterfaceBridgeEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchInterfaceBridgeEndpointRequest.to_json())

# convert the object into a dict
patch_interface_bridge_endpoint_request_dict = patch_interface_bridge_endpoint_request_instance.to_dict()
# create an instance of PatchInterfaceBridgeEndpointRequest from a dict
patch_interface_bridge_endpoint_request_from_dict = PatchInterfaceBridgeEndpointRequest.from_dict(patch_interface_bridge_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


