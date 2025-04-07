# OpenVPNClientSpecificOverride


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | The X.509 common name for the client certificate, or the username for VPNs utilizing password authentication.&lt;br&gt; | [optional] 
**disable** | **bool** | Disables this client specific override.&lt;br&gt; | [optional] 
**block** | **bool** | Enables or disables the client from connecting to this server. Do not use this option to permanently disable a client due to a compromised key or password. Use a CRL instead.&lt;br&gt; | [optional] 
**description** | **str** | The description for this client specific override.&lt;br&gt; | [optional] 
**server_list** | **List[str]** | The OpenVPN servers that will utilize this override. When no servers are specified, the override will apply to all servers.&lt;br&gt; | [optional] 
**tunnel_network** | **str** | The IPv4 virtual network used for private communications between the server and client hosts.&lt;br&gt; | [optional] 
**tunnel_networkv6** | **str** | The IPv6 virtual network used for private communications between the server and client hosts.&lt;br&gt; | [optional] 
**local_network** | **List[str]** | The IPv4 server-side networks that will be accessible from this particular client.&lt;br&gt; | [optional] 
**local_networkv6** | **List[str]** | the IPv6 server-side networks that will be accessible from this particular client.&lt;br&gt; | [optional] 
**remote_network** | **List[str]** | The IPv4 client-side networks that will be routed to this client specifically using iroute, so that a site-to-site VPN can be established.&lt;br&gt; | [optional] 
**remote_networkv6** | **List[str]** | The IPv6 client-side networks that will be routed to this client specifically using iroute, so that a site-to-site VPN can be established.&lt;br&gt; | [optional] 
**gwredir** | **bool** | Enable forcing all client-generated traffic through the tunnel.&lt;br&gt; | [optional] 
**push_reset** | **bool** | Enables or disables preventing this client from receiving any server-defined client settings.&lt;br&gt; | [optional] 
**remove_route** | **bool** | Enables or disables preventing this client from receiving any server-defined routes without removing any other options.&lt;br&gt; | [optional] 
**dns_domain** | **str** | The default domain to provide to the client.&lt;br&gt; | [optional] 
**dns_server1** | **str** | The primary DNS server to provide to the client.&lt;br&gt; | [optional] 
**dns_server2** | **str** | The secondary DNS server to provide to the client.&lt;br&gt; | [optional] 
**dns_server3** | **str** | The tertiary DNS server to provide to the client.&lt;br&gt; | [optional] 
**dns_server4** | **str** | The quaternary DNS server to provide to the client.&lt;br&gt; | [optional] 
**ntp_server1** | **str** | The primary NTP server to provide to the client.&lt;br&gt; | [optional] 
**ntp_server2** | **str** | The secondary NTP server to provide to the client.&lt;br&gt; | [optional] 
**netbios_enable** | **bool** | Enables or disables NetBIOS over TCP/IP.&lt;br&gt; | [optional] 
**netbios_ntype** | **int** | The NetBIOS node type.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;netbios_enable&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**netbios_scope** | **str** | The NetBIOS Scope ID. This provides an extended naming service for NetBIOS over TCP/IP. The NetBIOS scope ID isolates NetBIOS traffic on a single network to only those nodes with the same NetBIOS scope ID.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;netbios_enable&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**wins_server1** | **str** | The primary WINS server to provide to the client.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;netbios_enable&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**wins_server2** | **str** | The secondary WINS server to provide to the client.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;netbios_enable&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**custom_options** | **List[str]** | Additional OpenVPN options to add for this client.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.open_vpn_client_specific_override import OpenVPNClientSpecificOverride

# TODO update the JSON string below
json = "{}"
# create an instance of OpenVPNClientSpecificOverride from a JSON string
open_vpn_client_specific_override_instance = OpenVPNClientSpecificOverride.from_json(json)
# print the JSON string representation of the object
print(OpenVPNClientSpecificOverride.to_json())

# convert the object into a dict
open_vpn_client_specific_override_dict = open_vpn_client_specific_override_instance.to_dict()
# create an instance of OpenVPNClientSpecificOverride from a dict
open_vpn_client_specific_override_from_dict = OpenVPNClientSpecificOverride.from_dict(open_vpn_client_specific_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


