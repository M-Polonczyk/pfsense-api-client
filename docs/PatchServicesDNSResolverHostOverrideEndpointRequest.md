# PatchServicesDNSResolverHostOverrideEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The hostname portion of the host override.&lt;br&gt; | [optional] 
**domain** | **str** | The hostname portion of the host override.&lt;br&gt; | [optional] 
**ip** | **List[str]** | The IP addresses this host override will resolve.&lt;br&gt; | [optional] 
**descr** | **str** | A detailed description for this host override.&lt;br&gt; | [optional] 
**aliases** | [**List[DNSResolverHostOverrideAliasesInner]**](DNSResolverHostOverrideAliasesInner.md) | Additional alias hostnames that should resolve the same IP(s).&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_dns_resolver_host_override_endpoint_request import PatchServicesDNSResolverHostOverrideEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesDNSResolverHostOverrideEndpointRequest from a JSON string
patch_services_dns_resolver_host_override_endpoint_request_instance = PatchServicesDNSResolverHostOverrideEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesDNSResolverHostOverrideEndpointRequest.to_json())

# convert the object into a dict
patch_services_dns_resolver_host_override_endpoint_request_dict = patch_services_dns_resolver_host_override_endpoint_request_instance.to_dict()
# create an instance of PatchServicesDNSResolverHostOverrideEndpointRequest from a dict
patch_services_dns_resolver_host_override_endpoint_request_from_dict = PatchServicesDNSResolverHostOverrideEndpointRequest.from_dict(patch_services_dns_resolver_host_override_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


