# DNSResolverHostOverrideAliasesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The hostname portion of the host override alias.&lt;br&gt; | 
**domain** | **str** | The hostname portion of the host override alias.&lt;br&gt; | 
**descr** | **str** | A detailed description for this host override alias.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.dns_resolver_host_override_aliases_inner import DNSResolverHostOverrideAliasesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DNSResolverHostOverrideAliasesInner from a JSON string
dns_resolver_host_override_aliases_inner_instance = DNSResolverHostOverrideAliasesInner.from_json(json)
# print the JSON string representation of the object
print(DNSResolverHostOverrideAliasesInner.to_json())

# convert the object into a dict
dns_resolver_host_override_aliases_inner_dict = dns_resolver_host_override_aliases_inner_instance.to_dict()
# create an instance of DNSResolverHostOverrideAliasesInner from a dict
dns_resolver_host_override_aliases_inner_from_dict = DNSResolverHostOverrideAliasesInner.from_dict(dns_resolver_host_override_aliases_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


