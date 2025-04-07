# DNSResolverHostOverrideAlias


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The hostname portion of the host override alias.&lt;br&gt; | [optional] 
**domain** | **str** | The hostname portion of the host override alias.&lt;br&gt; | [optional] 
**descr** | **str** | A detailed description for this host override alias.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.dns_resolver_host_override_alias import DNSResolverHostOverrideAlias

# TODO update the JSON string below
json = "{}"
# create an instance of DNSResolverHostOverrideAlias from a JSON string
dns_resolver_host_override_alias_instance = DNSResolverHostOverrideAlias.from_json(json)
# print the JSON string representation of the object
print(DNSResolverHostOverrideAlias.to_json())

# convert the object into a dict
dns_resolver_host_override_alias_dict = dns_resolver_host_override_alias_instance.to_dict()
# create an instance of DNSResolverHostOverrideAlias from a dict
dns_resolver_host_override_alias_from_dict = DNSResolverHostOverrideAlias.from_dict(dns_resolver_host_override_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


