# PostInterfaceBridgeEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | **List[str]** | The member interfaces to include in this bridge.&lt;br&gt; | 
**descr** | **str** | A description for this interface bridge.&lt;br&gt; | [optional] 
**bridgeif** | **str** | The real interface name for this bridge interface.&lt;br&gt; | [optional] [readonly] [default to 'bridge0']

## Example

```python
from pfsense_api_client.models.post_interface_bridge_endpoint_request import PostInterfaceBridgeEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostInterfaceBridgeEndpointRequest from a JSON string
post_interface_bridge_endpoint_request_instance = PostInterfaceBridgeEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostInterfaceBridgeEndpointRequest.to_json())

# convert the object into a dict
post_interface_bridge_endpoint_request_dict = post_interface_bridge_endpoint_request_instance.to_dict()
# create an instance of PostInterfaceBridgeEndpointRequest from a dict
post_interface_bridge_endpoint_request_from_dict = PostInterfaceBridgeEndpointRequest.from_dict(post_interface_bridge_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


