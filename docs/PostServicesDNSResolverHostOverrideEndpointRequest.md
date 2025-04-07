# PostServicesDNSResolverHostOverrideEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The hostname portion of the host override.&lt;br&gt; | 
**domain** | **str** | The hostname portion of the host override.&lt;br&gt; | 
**ip** | **List[str]** | The IP addresses this host override will resolve.&lt;br&gt; | 
**descr** | **str** | A detailed description for this host override.&lt;br&gt; | [optional] 
**aliases** | [**List[DNSResolverHostOverrideAliasesInner]**](DNSResolverHostOverrideAliasesInner.md) | Additional alias hostnames that should resolve the same IP(s).&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_services_dns_resolver_host_override_endpoint_request import PostServicesDNSResolverHostOverrideEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesDNSResolverHostOverrideEndpointRequest from a JSON string
post_services_dns_resolver_host_override_endpoint_request_instance = PostServicesDNSResolverHostOverrideEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesDNSResolverHostOverrideEndpointRequest.to_json())

# convert the object into a dict
post_services_dns_resolver_host_override_endpoint_request_dict = post_services_dns_resolver_host_override_endpoint_request_instance.to_dict()
# create an instance of PostServicesDNSResolverHostOverrideEndpointRequest from a dict
post_services_dns_resolver_host_override_endpoint_request_from_dict = PostServicesDNSResolverHostOverrideEndpointRequest.from_dict(post_services_dns_resolver_host_override_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


