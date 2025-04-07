# DNSResolverApply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; when all DNS Resolver changes are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending DNS Resolver changes that have not been applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.dns_resolver_apply import DNSResolverApply

# TODO update the JSON string below
json = "{}"
# create an instance of DNSResolverApply from a JSON string
dns_resolver_apply_instance = DNSResolverApply.from_json(json)
# print the JSON string representation of the object
print(DNSResolverApply.to_json())

# convert the object into a dict
dns_resolver_apply_dict = dns_resolver_apply_instance.to_dict()
# create an instance of DNSResolverApply from a dict
dns_resolver_apply_from_dict = DNSResolverApply.from_dict(dns_resolver_apply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


