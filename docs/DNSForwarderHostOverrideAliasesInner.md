# DNSForwarderHostOverrideAliasesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The hostname of this override alias.&lt;br&gt; | 
**domain** | **str** | The domain of this override alias.&lt;br&gt; | 
**description** | **str** | The description of this override alias.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.dns_forwarder_host_override_aliases_inner import DNSForwarderHostOverrideAliasesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DNSForwarderHostOverrideAliasesInner from a JSON string
dns_forwarder_host_override_aliases_inner_instance = DNSForwarderHostOverrideAliasesInner.from_json(json)
# print the JSON string representation of the object
print(DNSForwarderHostOverrideAliasesInner.to_json())

# convert the object into a dict
dns_forwarder_host_override_aliases_inner_dict = dns_forwarder_host_override_aliases_inner_instance.to_dict()
# create an instance of DNSForwarderHostOverrideAliasesInner from a dict
dns_forwarder_host_override_aliases_inner_from_dict = DNSForwarderHostOverrideAliasesInner.from_dict(dns_forwarder_host_override_aliases_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


