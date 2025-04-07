# PostServicesHAProxySettingsDNSResolverEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The descriptive name for this DNS server.&lt;br&gt; | 
**server** | **str** | The IP or hostname of the DNS server.&lt;br&gt; | 
**port** | **str** | The port used by this DNS server. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '53']

## Example

```python
from pfsense_api_client.models.post_services_ha_proxy_settings_dns_resolver_endpoint_request import PostServicesHAProxySettingsDNSResolverEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesHAProxySettingsDNSResolverEndpointRequest from a JSON string
post_services_ha_proxy_settings_dns_resolver_endpoint_request_instance = PostServicesHAProxySettingsDNSResolverEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesHAProxySettingsDNSResolverEndpointRequest.to_json())

# convert the object into a dict
post_services_ha_proxy_settings_dns_resolver_endpoint_request_dict = post_services_ha_proxy_settings_dns_resolver_endpoint_request_instance.to_dict()
# create an instance of PostServicesHAProxySettingsDNSResolverEndpointRequest from a dict
post_services_ha_proxy_settings_dns_resolver_endpoint_request_from_dict = PostServicesHAProxySettingsDNSResolverEndpointRequest.from_dict(post_services_ha_proxy_settings_dns_resolver_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


