# PatchServicesDNSForwarderHostOverrideEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The hostname of this override.&lt;br&gt; | [optional] 
**domain** | **str** | The domain of this override.&lt;br&gt; | [optional] 
**ip** | **str** | The IP address of this override.&lt;br&gt; | [optional] 
**descr** | **str** | The description for this override.&lt;br&gt; | [optional] 
**aliases** | [**List[DNSForwarderHostOverrideAliasesInner]**](DNSForwarderHostOverrideAliasesInner.md) | The aliases for this override.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_dns_forwarder_host_override_endpoint_request import PatchServicesDNSForwarderHostOverrideEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesDNSForwarderHostOverrideEndpointRequest from a JSON string
patch_services_dns_forwarder_host_override_endpoint_request_instance = PatchServicesDNSForwarderHostOverrideEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesDNSForwarderHostOverrideEndpointRequest.to_json())

# convert the object into a dict
patch_services_dns_forwarder_host_override_endpoint_request_dict = patch_services_dns_forwarder_host_override_endpoint_request_instance.to_dict()
# create an instance of PatchServicesDNSForwarderHostOverrideEndpointRequest from a dict
patch_services_dns_forwarder_host_override_endpoint_request_from_dict = PatchServicesDNSForwarderHostOverrideEndpointRequest.from_dict(patch_services_dns_forwarder_host_override_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


