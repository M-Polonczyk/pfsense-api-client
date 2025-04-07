# PatchServicesDHCPServerBackendEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcpbackend** | **str** | The backend DHCP server service to use. ISC DHCP is deprecate and will be removed in a future version of pfSense.&lt;br&gt; | [optional] [default to 'isc']

## Example

```python
from pfsense_api_client.models.patch_services_dhcp_server_backend_endpoint_request import PatchServicesDHCPServerBackendEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesDHCPServerBackendEndpointRequest from a JSON string
patch_services_dhcp_server_backend_endpoint_request_instance = PatchServicesDHCPServerBackendEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesDHCPServerBackendEndpointRequest.to_json())

# convert the object into a dict
patch_services_dhcp_server_backend_endpoint_request_dict = patch_services_dhcp_server_backend_endpoint_request_instance.to_dict()
# create an instance of PatchServicesDHCPServerBackendEndpointRequest from a dict
patch_services_dhcp_server_backend_endpoint_request_from_dict = PatchServicesDHCPServerBackendEndpointRequest.from_dict(patch_services_dhcp_server_backend_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


