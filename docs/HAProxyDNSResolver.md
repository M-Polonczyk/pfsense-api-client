# HAProxyDNSResolver


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The descriptive name for this DNS server.&lt;br&gt; | [optional] 
**server** | **str** | The IP or hostname of the DNS server.&lt;br&gt; | [optional] 
**port** | **str** | The port used by this DNS server. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '53']

## Example

```python
from pfsense_api_client.models.ha_proxy_dns_resolver import HAProxyDNSResolver

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxyDNSResolver from a JSON string
ha_proxy_dns_resolver_instance = HAProxyDNSResolver.from_json(json)
# print the JSON string representation of the object
print(HAProxyDNSResolver.to_json())

# convert the object into a dict
ha_proxy_dns_resolver_dict = ha_proxy_dns_resolver_instance.to_dict()
# create an instance of HAProxyDNSResolver from a dict
ha_proxy_dns_resolver_from_dict = HAProxyDNSResolver.from_dict(ha_proxy_dns_resolver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


