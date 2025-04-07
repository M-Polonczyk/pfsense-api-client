# PostInterfaceVLANEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_if** | **str** | The real parent interface this VLAN will be applied to.&lt;br&gt; | 
**tag** | **int** | The VLAN ID tag to use. This must be unique from all other VLANs on the parent interface.&lt;br&gt; | 
**vlanif** | **str** | Displays the full interface VLAN. This value is automatically populated and cannot be set.&lt;br&gt; | [optional] 
**pcp** | **int** | The 802.1p VLAN priority code point (PCP) to assign to this VLAN.&lt;br&gt; | [optional] 
**descr** | **str** | A description to help document the purpose of this VLAN.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_interface_vlan_endpoint_request import PostInterfaceVLANEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostInterfaceVLANEndpointRequest from a JSON string
post_interface_vlan_endpoint_request_instance = PostInterfaceVLANEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostInterfaceVLANEndpointRequest.to_json())

# convert the object into a dict
post_interface_vlan_endpoint_request_dict = post_interface_vlan_endpoint_request_instance.to_dict()
# create an instance of PostInterfaceVLANEndpointRequest from a dict
post_interface_vlan_endpoint_request_from_dict = PostInterfaceVLANEndpointRequest.from_dict(post_interface_vlan_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


