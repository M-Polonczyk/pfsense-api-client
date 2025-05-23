# HAProxyFrontendAExtaddrInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extaddr** | **str** | The external address to use.&lt;br&gt; | 
**extaddr_custom** | **str** | The custom IPv4 or IPv6 address to use as the external address.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;extaddr&#x60; must be equal to &#x60;&#39;custom&#39;&#x60;&lt;br&gt; | 
**extaddr_port** | **str** | The port to bind to for this address. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] 
**extaddr_ssl** | **bool** | Enables or disables using SSL/TLS for this address.&lt;br&gt; | [optional] 
**exaddr_advanced** | **str** | The advanced configuration to apply to this address.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.ha_proxy_frontend_a_extaddr_inner import HAProxyFrontendAExtaddrInner

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxyFrontendAExtaddrInner from a JSON string
ha_proxy_frontend_a_extaddr_inner_instance = HAProxyFrontendAExtaddrInner.from_json(json)
# print the JSON string representation of the object
print(HAProxyFrontendAExtaddrInner.to_json())

# convert the object into a dict
ha_proxy_frontend_a_extaddr_inner_dict = ha_proxy_frontend_a_extaddr_inner_instance.to_dict()
# create an instance of HAProxyFrontendAExtaddrInner from a dict
ha_proxy_frontend_a_extaddr_inner_from_dict = HAProxyFrontendAExtaddrInner.from_dict(ha_proxy_frontend_a_extaddr_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


