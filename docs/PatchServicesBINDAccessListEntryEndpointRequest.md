# PatchServicesBINDAccessListEntryEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The network CIDR to allow.&lt;br&gt; | [optional] 
**description** | **str** | A description of the access list entry.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_bind_access_list_entry_endpoint_request import PatchServicesBINDAccessListEntryEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesBINDAccessListEntryEndpointRequest from a JSON string
patch_services_bind_access_list_entry_endpoint_request_instance = PatchServicesBINDAccessListEntryEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesBINDAccessListEntryEndpointRequest.to_json())

# convert the object into a dict
patch_services_bind_access_list_entry_endpoint_request_dict = patch_services_bind_access_list_entry_endpoint_request_instance.to_dict()
# create an instance of PatchServicesBINDAccessListEntryEndpointRequest from a dict
patch_services_bind_access_list_entry_endpoint_request_from_dict = PatchServicesBINDAccessListEntryEndpointRequest.from_dict(patch_services_bind_access_list_entry_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


