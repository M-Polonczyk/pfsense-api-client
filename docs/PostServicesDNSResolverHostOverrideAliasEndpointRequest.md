# PostServicesDNSResolverHostOverrideAliasEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The hostname portion of the host override alias.&lt;br&gt; | 
**domain** | **str** | The hostname portion of the host override alias.&lt;br&gt; | 
**descr** | **str** | A detailed description for this host override alias.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 

## Example

```python
from pfsense_api_client.models.post_services_dns_resolver_host_override_alias_endpoint_request import PostServicesDNSResolverHostOverrideAliasEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesDNSResolverHostOverrideAliasEndpointRequest from a JSON string
post_services_dns_resolver_host_override_alias_endpoint_request_instance = PostServicesDNSResolverHostOverrideAliasEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesDNSResolverHostOverrideAliasEndpointRequest.to_json())

# convert the object into a dict
post_services_dns_resolver_host_override_alias_endpoint_request_dict = post_services_dns_resolver_host_override_alias_endpoint_request_instance.to_dict()
# create an instance of PostServicesDNSResolverHostOverrideAliasEndpointRequest from a dict
post_services_dns_resolver_host_override_alias_endpoint_request_from_dict = PostServicesDNSResolverHostOverrideAliasEndpointRequest.from_dict(post_services_dns_resolver_host_override_alias_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


