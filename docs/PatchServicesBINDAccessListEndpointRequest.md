# PatchServicesBINDAccessListEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the access list.&lt;br&gt; | [optional] 
**description** | **str** | A description for the access list.&lt;br&gt; | [optional] 
**entries** | [**List[BINDAccessListEntriesInner]**](BINDAccessListEntriesInner.md) | The network entries for this access list.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_bind_access_list_endpoint_request import PatchServicesBINDAccessListEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesBINDAccessListEndpointRequest from a JSON string
patch_services_bind_access_list_endpoint_request_instance = PatchServicesBINDAccessListEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesBINDAccessListEndpointRequest.to_json())

# convert the object into a dict
patch_services_bind_access_list_endpoint_request_dict = patch_services_bind_access_list_endpoint_request_instance.to_dict()
# create an instance of PatchServicesBINDAccessListEndpointRequest from a dict
patch_services_bind_access_list_endpoint_request_from_dict = PatchServicesBINDAccessListEndpointRequest.from_dict(patch_services_bind_access_list_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


