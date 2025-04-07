# PatchServicesDNSResolverAccessListEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this access list.&lt;br&gt; | [optional] 
**action** | **str** | The action to take when an access list match is found.&lt;br&gt; | [optional] 
**description** | **str** | A description for this access list.&lt;br&gt; | [optional] 
**networks** | [**List[DNSResolverAccessListNetworksInner]**](DNSResolverAccessListNetworksInner.md) | The DNS Resolver access list network entries to include in this access list.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_dns_resolver_access_list_endpoint_request import PatchServicesDNSResolverAccessListEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesDNSResolverAccessListEndpointRequest from a JSON string
patch_services_dns_resolver_access_list_endpoint_request_instance = PatchServicesDNSResolverAccessListEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesDNSResolverAccessListEndpointRequest.to_json())

# convert the object into a dict
patch_services_dns_resolver_access_list_endpoint_request_dict = patch_services_dns_resolver_access_list_endpoint_request_instance.to_dict()
# create an instance of PatchServicesDNSResolverAccessListEndpointRequest from a dict
patch_services_dns_resolver_access_list_endpoint_request_from_dict = PatchServicesDNSResolverAccessListEndpointRequest.from_dict(patch_services_dns_resolver_access_list_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


