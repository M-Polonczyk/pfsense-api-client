# DNSResolverAccessListNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | The network address of this access list entry.&lt;br&gt; | [optional] 
**mask** | **int** | The subnet mask of this access list entry&#39;s network.&lt;br&gt; | [optional] 
**description** | **str** | A description for this access list entry.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.dns_resolver_access_list_network import DNSResolverAccessListNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of DNSResolverAccessListNetwork from a JSON string
dns_resolver_access_list_network_instance = DNSResolverAccessListNetwork.from_json(json)
# print the JSON string representation of the object
print(DNSResolverAccessListNetwork.to_json())

# convert the object into a dict
dns_resolver_access_list_network_dict = dns_resolver_access_list_network_instance.to_dict()
# create an instance of DNSResolverAccessListNetwork from a dict
dns_resolver_access_list_network_from_dict = DNSResolverAccessListNetwork.from_dict(dns_resolver_access_list_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


