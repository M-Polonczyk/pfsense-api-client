# SystemDNS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsallowoverride** | **bool** | Allow DNS servers to be overwritten by DHCP on WAN interfaces.&lt;br&gt; | [optional] 
**dnslocalhost** | **str** | Use local DNS server (DNS Resover or DNS Forwarder) as the primary DNS, or use only remote DNS servers specified in &#x60;dnsserver&#x60;. Set to &#x60;null&#x60; to use local DNS server as the primary and remote DNS servers as backup.&lt;br&gt; | [optional] 
**dnsserver** | **List[str]** | The remote DNS server IPv4 or IPv6 addresses.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.system_dns import SystemDNS

# TODO update the JSON string below
json = "{}"
# create an instance of SystemDNS from a JSON string
system_dns_instance = SystemDNS.from_json(json)
# print the JSON string representation of the object
print(SystemDNS.to_json())

# convert the object into a dict
system_dns_dict = system_dns_instance.to_dict()
# create an instance of SystemDNS from a dict
system_dns_from_dict = SystemDNS.from_dict(system_dns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


