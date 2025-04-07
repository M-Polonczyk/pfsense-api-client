# PostServicesWakeOnLANSendEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | The interface the host to be woken up is connected to.&lt;br&gt; | 
**mac_addr** | **str** | The MAC address of the host to be awoken.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.post_services_wake_on_lan_send_endpoint_request import PostServicesWakeOnLANSendEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesWakeOnLANSendEndpointRequest from a JSON string
post_services_wake_on_lan_send_endpoint_request_instance = PostServicesWakeOnLANSendEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesWakeOnLANSendEndpointRequest.to_json())

# convert the object into a dict
post_services_wake_on_lan_send_endpoint_request_dict = post_services_wake_on_lan_send_endpoint_request_instance.to_dict()
# create an instance of PostServicesWakeOnLANSendEndpointRequest from a dict
post_services_wake_on_lan_send_endpoint_request_from_dict = PostServicesWakeOnLANSendEndpointRequest.from_dict(post_services_wake_on_lan_send_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


