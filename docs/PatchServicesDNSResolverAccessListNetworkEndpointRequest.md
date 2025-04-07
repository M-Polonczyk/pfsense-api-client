# PatchServicesDNSResolverAccessListNetworkEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | The network address of this access list entry.&lt;br&gt; | [optional] 
**mask** | **int** | The subnet mask of this access list entry&#39;s network.&lt;br&gt; | [optional] 
**description** | **str** | A description for this access list entry.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_dns_resolver_access_list_network_endpoint_request import PatchServicesDNSResolverAccessListNetworkEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesDNSResolverAccessListNetworkEndpointRequest from a JSON string
patch_services_dns_resolver_access_list_network_endpoint_request_instance = PatchServicesDNSResolverAccessListNetworkEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesDNSResolverAccessListNetworkEndpointRequest.to_json())

# convert the object into a dict
patch_services_dns_resolver_access_list_network_endpoint_request_dict = patch_services_dns_resolver_access_list_network_endpoint_request_instance.to_dict()
# create an instance of PatchServicesDNSResolverAccessListNetworkEndpointRequest from a dict
patch_services_dns_resolver_access_list_network_endpoint_request_from_dict = PatchServicesDNSResolverAccessListNetworkEndpointRequest.from_dict(patch_services_dns_resolver_access_list_network_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


