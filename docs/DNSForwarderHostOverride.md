# DNSForwarderHostOverride


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The hostname of this override.&lt;br&gt; | [optional] 
**domain** | **str** | The domain of this override.&lt;br&gt; | [optional] 
**ip** | **str** | The IP address of this override.&lt;br&gt; | [optional] 
**descr** | **str** | The description for this override.&lt;br&gt; | [optional] 
**aliases** | [**List[DNSForwarderHostOverrideAliasesInner]**](DNSForwarderHostOverrideAliasesInner.md) | The aliases for this override.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.dns_forwarder_host_override import DNSForwarderHostOverride

# TODO update the JSON string below
json = "{}"
# create an instance of DNSForwarderHostOverride from a JSON string
dns_forwarder_host_override_instance = DNSForwarderHostOverride.from_json(json)
# print the JSON string representation of the object
print(DNSForwarderHostOverride.to_json())

# convert the object into a dict
dns_forwarder_host_override_dict = dns_forwarder_host_override_instance.to_dict()
# create an instance of DNSForwarderHostOverride from a dict
dns_forwarder_host_override_from_dict = DNSForwarderHostOverride.from_dict(dns_forwarder_host_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


