# PostServicesDNSResolverAccessListNetworkEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | The network address of this access list entry.&lt;br&gt; | 
**mask** | **int** | The subnet mask of this access list entry&#39;s network.&lt;br&gt; | 
**description** | **str** | A description for this access list entry.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 

## Example

```python
from pfsense_api_client.models.post_services_dns_resolver_access_list_network_endpoint_request import PostServicesDNSResolverAccessListNetworkEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesDNSResolverAccessListNetworkEndpointRequest from a JSON string
post_services_dns_resolver_access_list_network_endpoint_request_instance = PostServicesDNSResolverAccessListNetworkEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesDNSResolverAccessListNetworkEndpointRequest.to_json())

# convert the object into a dict
post_services_dns_resolver_access_list_network_endpoint_request_dict = post_services_dns_resolver_access_list_network_endpoint_request_instance.to_dict()
# create an instance of PostServicesDNSResolverAccessListNetworkEndpointRequest from a dict
post_services_dns_resolver_access_list_network_endpoint_request_from_dict = PostServicesDNSResolverAccessListNetworkEndpointRequest.from_dict(post_services_dns_resolver_access_list_network_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


