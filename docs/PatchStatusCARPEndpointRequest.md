# PatchStatusCARPEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enables or disables CARP on this system.&lt;br&gt; | 
**maintenance_mode** | **bool** | Enables or disables CARP maintenance mode on this system.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.patch_status_carp_endpoint_request import PatchStatusCARPEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchStatusCARPEndpointRequest from a JSON string
patch_status_carp_endpoint_request_instance = PatchStatusCARPEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchStatusCARPEndpointRequest.to_json())

# convert the object into a dict
patch_status_carp_endpoint_request_dict = patch_status_carp_endpoint_request_instance.to_dict()
# create an instance of PatchStatusCARPEndpointRequest from a dict
patch_status_carp_endpoint_request_from_dict = PatchStatusCARPEndpointRequest.from_dict(patch_status_carp_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


