# PatchSystemTunableEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tunable** | **str** | The name of the tunable to set.&lt;br&gt; | [optional] 
**value** | **str** | The value to assign this tunable.&lt;br&gt; | [optional] 
**descr** | **str** | A description for this tunable.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_system_tunable_endpoint_request import PatchSystemTunableEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSystemTunableEndpointRequest from a JSON string
patch_system_tunable_endpoint_request_instance = PatchSystemTunableEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchSystemTunableEndpointRequest.to_json())

# convert the object into a dict
patch_system_tunable_endpoint_request_dict = patch_system_tunable_endpoint_request_instance.to_dict()
# create an instance of PatchSystemTunableEndpointRequest from a dict
patch_system_tunable_endpoint_request_from_dict = PatchSystemTunableEndpointRequest.from_dict(patch_system_tunable_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


