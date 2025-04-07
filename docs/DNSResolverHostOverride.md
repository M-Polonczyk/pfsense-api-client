# DNSResolverHostOverride


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The hostname portion of the host override.&lt;br&gt; | [optional] 
**domain** | **str** | The hostname portion of the host override.&lt;br&gt; | [optional] 
**ip** | **List[str]** | The IP addresses this host override will resolve.&lt;br&gt; | [optional] 
**descr** | **str** | A detailed description for this host override.&lt;br&gt; | [optional] 
**aliases** | [**List[DNSResolverHostOverrideAliasesInner]**](DNSResolverHostOverrideAliasesInner.md) | Additional alias hostnames that should resolve the same IP(s).&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.dns_resolver_host_override import DNSResolverHostOverride

# TODO update the JSON string below
json = "{}"
# create an instance of DNSResolverHostOverride from a JSON string
dns_resolver_host_override_instance = DNSResolverHostOverride.from_json(json)
# print the JSON string representation of the object
print(DNSResolverHostOverride.to_json())

# convert the object into a dict
dns_resolver_host_override_dict = dns_resolver_host_override_instance.to_dict()
# create an instance of DNSResolverHostOverride from a dict
dns_resolver_host_override_from_dict = DNSResolverHostOverride.from_dict(dns_resolver_host_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


