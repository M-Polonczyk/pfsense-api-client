# DNSResolverAccessListNetworksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | The network address of this access list entry.&lt;br&gt; | 
**mask** | **int** | The subnet mask of this access list entry&#39;s network.&lt;br&gt; | 
**description** | **str** | A description for this access list entry.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.dns_resolver_access_list_networks_inner import DNSResolverAccessListNetworksInner

# TODO update the JSON string below
json = "{}"
# create an instance of DNSResolverAccessListNetworksInner from a JSON string
dns_resolver_access_list_networks_inner_instance = DNSResolverAccessListNetworksInner.from_json(json)
# print the JSON string representation of the object
print(DNSResolverAccessListNetworksInner.to_json())

# convert the object into a dict
dns_resolver_access_list_networks_inner_dict = dns_resolver_access_list_networks_inner_instance.to_dict()
# create an instance of DNSResolverAccessListNetworksInner from a dict
dns_resolver_access_list_networks_inner_from_dict = DNSResolverAccessListNetworksInner.from_dict(dns_resolver_access_list_networks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


