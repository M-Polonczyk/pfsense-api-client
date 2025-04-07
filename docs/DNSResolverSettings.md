# DNSResolverSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enables or disables the DNS Resolver service.&lt;br&gt; | [optional] 
**port** | **str** | The port on which the DNS Resolver service listens. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '53']
**enablessl** | **bool** | Enables or disables SSL/TLS for the DNS Resolver service.&lt;br&gt; | [optional] 
**sslcertref** | **str** | The SSL/TLS certificate to use for the DNS Resolver service.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;enablessl&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**tlsport** | **str** | The port on which the DNS Resolver service listens for SSL/TLS connections. Valid options are: a TCP/UDP port number&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;enablessl&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] [default to '853']
**active_interface** | **List[str]** | The interface on which the DNS Resolver service listens for DNS queries. Set empty value \&quot;.                 \&quot;to listen on all interfaces.&lt;br&gt; | [optional] 
**outgoing_interface** | **List[str]** | The interface on which the DNS Resolver service sends outgoing DNS queries. Set empty value \&quot;.                 \&quot;to use any interface.&lt;br&gt; | [optional] 
**strictout** | **bool** | Enables or disables sending recursive queries if none of the selected Outgoing Network \&quot;.                 \&quot;Interfaces are available.&lt;br&gt; | [optional] 
**system_domain_local_zone_type** | **str** | The type of local zone used for the system domain.&lt;br&gt; | [optional] [default to 'transparent']
**dnssec** | **bool** | Enables or disables DNSSEC validation.&lt;br&gt; | [optional] 
**python** | **bool** | Enables or disables the Python module.&lt;br&gt; | [optional] 
**python_order** | **str** | The order in which the Python module is loaded.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;python&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] [default to 'pre_validator']
**python_script** | **str** | The Python module to utilize.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;python&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**forwarding** | **bool** | Enables or disables DNS Resolver forwarding mode.&lt;br&gt; | [optional] 
**regdhcp** | **bool** | Enables or disables registering DHCP leases in the DNS Resolver service.&lt;br&gt; | [optional] 
**regdhcpstatic** | **bool** | Enables or disables registering static DHCP mappings in the DNS Resolver service.&lt;br&gt; | [optional] 
**regovpnclients** | **bool** | Enables or disables registering OpenVPN clients in the DNS Resolver service.&lt;br&gt; | [optional] 
**custom_options** | **str** | Custom options to add to the DNS Resolver configuration.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.dns_resolver_settings import DNSResolverSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DNSResolverSettings from a JSON string
dns_resolver_settings_instance = DNSResolverSettings.from_json(json)
# print the JSON string representation of the object
print(DNSResolverSettings.to_json())

# convert the object into a dict
dns_resolver_settings_dict = dns_resolver_settings_instance.to_dict()
# create an instance of DNSResolverSettings from a dict
dns_resolver_settings_from_dict = DNSResolverSettings.from_dict(dns_resolver_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


