# DNSResolverAccessList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this access list.&lt;br&gt; | [optional] 
**action** | **str** | The action to take when an access list match is found.&lt;br&gt; | [optional] 
**description** | **str** | A description for this access list.&lt;br&gt; | [optional] 
**networks** | [**List[DNSResolverAccessListNetworksInner]**](DNSResolverAccessListNetworksInner.md) | The DNS Resolver access list network entries to include in this access list.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.dns_resolver_access_list import DNSResolverAccessList

# TODO update the JSON string below
json = "{}"
# create an instance of DNSResolverAccessList from a JSON string
dns_resolver_access_list_instance = DNSResolverAccessList.from_json(json)
# print the JSON string representation of the object
print(DNSResolverAccessList.to_json())

# convert the object into a dict
dns_resolver_access_list_dict = dns_resolver_access_list_instance.to_dict()
# create an instance of DNSResolverAccessList from a dict
dns_resolver_access_list_from_dict = DNSResolverAccessList.from_dict(dns_resolver_access_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


