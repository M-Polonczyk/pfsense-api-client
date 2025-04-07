# PatchInterfaceGroupEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ifname** | **str** | The name of this interface group.&lt;br&gt; | [optional] 
**members** | **List[str]** | The member interfaces to assign to this interface group.&lt;br&gt; | [optional] 
**descr** | **str** | The description for this interface group.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_interface_group_endpoint_request import PatchInterfaceGroupEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchInterfaceGroupEndpointRequest from a JSON string
patch_interface_group_endpoint_request_instance = PatchInterfaceGroupEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchInterfaceGroupEndpointRequest.to_json())

# convert the object into a dict
patch_interface_group_endpoint_request_dict = patch_interface_group_endpoint_request_instance.to_dict()
# create an instance of PatchInterfaceGroupEndpointRequest from a dict
patch_interface_group_endpoint_request_from_dict = PatchInterfaceGroupEndpointRequest.from_dict(patch_interface_group_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


