# PatchServicesDHCPServerCustomOptionEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | The DHCP option number to configure.&lt;br&gt; | [optional] 
**type** | **str** | The type of value to configure for the option.&lt;br&gt; | [optional] 
**value** | **str** | The value to configure for the option.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_dhcp_server_custom_option_endpoint_request import PatchServicesDHCPServerCustomOptionEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesDHCPServerCustomOptionEndpointRequest from a JSON string
patch_services_dhcp_server_custom_option_endpoint_request_instance = PatchServicesDHCPServerCustomOptionEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesDHCPServerCustomOptionEndpointRequest.to_json())

# convert the object into a dict
patch_services_dhcp_server_custom_option_endpoint_request_dict = patch_services_dhcp_server_custom_option_endpoint_request_instance.to_dict()
# create an instance of PatchServicesDHCPServerCustomOptionEndpointRequest from a dict
patch_services_dhcp_server_custom_option_endpoint_request_from_dict = PatchServicesDHCPServerCustomOptionEndpointRequest.from_dict(patch_services_dhcp_server_custom_option_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


