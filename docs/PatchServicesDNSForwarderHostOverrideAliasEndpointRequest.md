# PatchServicesDNSForwarderHostOverrideAliasEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The hostname of this override alias.&lt;br&gt; | [optional] 
**domain** | **str** | The domain of this override alias.&lt;br&gt; | [optional] 
**description** | **str** | The description of this override alias.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_dns_forwarder_host_override_alias_endpoint_request import PatchServicesDNSForwarderHostOverrideAliasEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesDNSForwarderHostOverrideAliasEndpointRequest from a JSON string
patch_services_dns_forwarder_host_override_alias_endpoint_request_instance = PatchServicesDNSForwarderHostOverrideAliasEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesDNSForwarderHostOverrideAliasEndpointRequest.to_json())

# convert the object into a dict
patch_services_dns_forwarder_host_override_alias_endpoint_request_dict = patch_services_dns_forwarder_host_override_alias_endpoint_request_instance.to_dict()
# create an instance of PatchServicesDNSForwarderHostOverrideAliasEndpointRequest from a dict
patch_services_dns_forwarder_host_override_alias_endpoint_request_from_dict = PatchServicesDNSForwarderHostOverrideAliasEndpointRequest.from_dict(patch_services_dns_forwarder_host_override_alias_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


