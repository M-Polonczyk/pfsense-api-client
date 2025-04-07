# PatchInterfaceVLANEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_if** | **str** | The real parent interface this VLAN will be applied to.&lt;br&gt; | [optional] 
**tag** | **int** | The VLAN ID tag to use. This must be unique from all other VLANs on the parent interface.&lt;br&gt; | [optional] 
**vlanif** | **str** | Displays the full interface VLAN. This value is automatically populated and cannot be set.&lt;br&gt; | [optional] 
**pcp** | **int** | The 802.1p VLAN priority code point (PCP) to assign to this VLAN.&lt;br&gt; | [optional] 
**descr** | **str** | A description to help document the purpose of this VLAN.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_interface_vlan_endpoint_request import PatchInterfaceVLANEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchInterfaceVLANEndpointRequest from a JSON string
patch_interface_vlan_endpoint_request_instance = PatchInterfaceVLANEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchInterfaceVLANEndpointRequest.to_json())

# convert the object into a dict
patch_interface_vlan_endpoint_request_dict = patch_interface_vlan_endpoint_request_instance.to_dict()
# create an instance of PatchInterfaceVLANEndpointRequest from a dict
patch_interface_vlan_endpoint_request_from_dict = PatchInterfaceVLANEndpointRequest.from_dict(patch_interface_vlan_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


