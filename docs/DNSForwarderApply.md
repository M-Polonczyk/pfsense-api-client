# DNSForwarderApply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; when all DNS Forwarder changes are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending DNS Forwarder changes that have not been applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.dns_forwarder_apply import DNSForwarderApply

# TODO update the JSON string below
json = "{}"
# create an instance of DNSForwarderApply from a JSON string
dns_forwarder_apply_instance = DNSForwarderApply.from_json(json)
# print the JSON string representation of the object
print(DNSForwarderApply.to_json())

# convert the object into a dict
dns_forwarder_apply_dict = dns_forwarder_apply_instance.to_dict()
# create an instance of DNSForwarderApply from a dict
dns_forwarder_apply_from_dict = DNSForwarderApply.from_dict(dns_forwarder_apply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


