# PostServicesDNSResolverAccessListEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this access list.&lt;br&gt; | 
**action** | **str** | The action to take when an access list match is found.&lt;br&gt; | 
**description** | **str** | A description for this access list.&lt;br&gt; | [optional] 
**networks** | [**List[DNSResolverAccessListNetworksInner]**](DNSResolverAccessListNetworksInner.md) | The DNS Resolver access list network entries to include in this access list.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.post_services_dns_resolver_access_list_endpoint_request import PostServicesDNSResolverAccessListEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesDNSResolverAccessListEndpointRequest from a JSON string
post_services_dns_resolver_access_list_endpoint_request_instance = PostServicesDNSResolverAccessListEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesDNSResolverAccessListEndpointRequest.to_json())

# convert the object into a dict
post_services_dns_resolver_access_list_endpoint_request_dict = post_services_dns_resolver_access_list_endpoint_request_instance.to_dict()
# create an instance of PostServicesDNSResolverAccessListEndpointRequest from a dict
post_services_dns_resolver_access_list_endpoint_request_from_dict = PostServicesDNSResolverAccessListEndpointRequest.from_dict(post_services_dns_resolver_access_list_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


