# DNSForwarderHostOverrideAlias


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The hostname of this override alias.&lt;br&gt; | [optional] 
**domain** | **str** | The domain of this override alias.&lt;br&gt; | [optional] 
**description** | **str** | The description of this override alias.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.dns_forwarder_host_override_alias import DNSForwarderHostOverrideAlias

# TODO update the JSON string below
json = "{}"
# create an instance of DNSForwarderHostOverrideAlias from a JSON string
dns_forwarder_host_override_alias_instance = DNSForwarderHostOverrideAlias.from_json(json)
# print the JSON string representation of the object
print(DNSForwarderHostOverrideAlias.to_json())

# convert the object into a dict
dns_forwarder_host_override_alias_dict = dns_forwarder_host_override_alias_instance.to_dict()
# create an instance of DNSForwarderHostOverrideAlias from a dict
dns_forwarder_host_override_alias_from_dict = DNSForwarderHostOverrideAlias.from_dict(dns_forwarder_host_override_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


