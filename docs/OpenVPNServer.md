# OpenVPNServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpnid** | **int** | The unique ID for this OpenVPN server. This value is assigned by the system and cannot be changed.&lt;br&gt; | [optional] [readonly] 
**vpnif** | **str** | The VPN interface name for this OpenVPN server. This value is assigned by the system and cannot be changed.&lt;br&gt; | [optional] [readonly] 
**description** | **str** | The description for this OpenVPN server.&lt;br&gt; | [optional] 
**disable** | **bool** | Disables this OpenVPN server.&lt;br&gt; | [optional] 
**mode** | **str** | The OpenVPN server mode.&lt;br&gt; | [optional] 
**authmode** | **List[str]** | The name of the authentication server to use as the authentication backend for this OpenVPN server&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] [default to ["Local Database"]]
**dev_mode** | **str** | The carrier mode for this OpenVPN server. &#x60;tun&#x60; mode carries IPv4 and IPv6 (layer 3) and is the most common and compatible mode across all platforms. &#x60;tap&#x60; mode is capable of carrying 802.3 (layer 2).&lt;br&gt; | [optional] 
**protocol** | **str** | The protocol used by this OpenVPN server.&lt;br&gt; | [optional] 
**interface** | **str** | The interface or Virtual IP address where OpenVPN will receive client connections.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;protocol&#x60; must not be one of [ UDP, TCP ]&lt;br&gt; | [optional] 
**local_port** | **str** | The port used by OpenVPN to receive client connections. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '1194']
**use_tls** | **bool** | Enables or disables the use of a TLS key for this OpenVPN server.&lt;br&gt; | [optional] 
**tls** | **str** | The TLS key this OpenVPN server will use to sign control channel packets with an HMAC signature for authentication when establishing the tunnel.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;use_tls&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**tls_type** | **str** | The TLS key usage type. In &#x60;auth&#x60; mode, the TLS key is used only as HMAC authentication for the control channel, protecting the peers from unauthorized connections. The &#x60;crypt&#x60; mode encrypts the control channel communication in addition to providing authentication, providing more privacy and traffic control channel obfuscation.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;use_tls&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**tlsauth_keydir** | **str** | The TLS key direction. This must be set to complementary values on the client and server. For example, if the server is set to 0, the client must be set to 1. Both may be set to omit the direction, in which case the TLS Key will be used bidirectionally.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;use_tls&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] [default to 'default']
**caref** | **str** | The &#x60;refid&#x60; of the CA object to assume as the peer CA.&lt;br&gt; | [optional] 
**certref** | **str** | The &#x60;refid&#x60; of the certificate object to assume as the OpenVPN server certificate.&lt;br&gt; | [optional] 
**cert_depth** | **int** | The depth of the certificate chain to check when a certificate based client signs in. Certificates below this depth are not accepted. This is useful for denying certificates made with intermediate CAs generated from the same CA as the server. Set to null to use system default.&lt;br&gt; | [optional] [default to 1]
**dh_length** | **str** | The Diffie-Hellman (DH) parameter set used for key exchange.&lt;br&gt; | [optional] 
**ecdh_curve** | **str** | The Elliptic Curve to use for key exchange. The curve from the server certificate is used by default when the server uses an ECDSA certificate. Otherwise, secp384r1 is used as a fallback.&lt;br&gt; | [optional] 
**data_ciphers** | **List[str]** | The encryption algorithms/ciphers allowed by this OpenVPN server.&lt;br&gt; | [optional] 
**data_ciphers_fallback** | **str** | The fallback encryption algorithm/cipher used for data channel packets when communicating with clients that do not support data encryption algorithm negotiation (e.g. Shared Key).&lt;br&gt; | [optional] 
**digest** | **str** | The algorithm used to authenticate data channel packets, and control channel packets if a TLS Key is present.&lt;br&gt; | [optional] 
**strictusercn** | **bool** | Enables or disables enforcing a match between the common name of the client certificate and the username given at login.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] 
**remote_cert_tls** | **bool** | Enables or disables requiring hosts to have a client certificate to connect.&lt;br&gt; | [optional] [default to True]
**tunnel_network** | **str** | The IPv4 virtual network used for private communications between this server and client hosts.&lt;br&gt; | [optional] 
**tunnel_networkv6** | **str** | The IPv6 virtual network used for private communications between this server and client hosts.&lt;br&gt; | [optional] 
**serverbridge_dhcp** | **bool** | Enables or disables clients on the bridge to obtain DHCP.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;dev_mode&#x60; must be equal to &#x60;&#39;tap&#39;&#x60;&lt;br&gt; | [optional] 
**serverbridge_interface** | **str** | The interface to which this TAP instance will be bridged. This is not done automatically. This interface must be assigned and the bridge created separately. This setting controls which existing IP address and subnet mask are used by OpenVPN for the bridge.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;serverbridge_dhcp&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**serverbridge_routegateway** | **bool** | Enables or disables pushing the bridge interface&#39;s IPv4 address to connecting clients as a route gateway.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;serverbridge_dhcp&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**serverbridge_dhcp_start** | **str** | The bridge DHCP range&#39;s start address.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;serverbridge_dhcp&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**serverbridge_dhcp_end** | **str** | The bridge DHCP range&#39;s end address.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;serverbridge_dhcp&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**gwredir** | **bool** | Enable forcing all client-generated IPv4 traffic through the tunnel.&lt;br&gt; | [optional] 
**gwredir6** | **bool** | Enable forcing all client-generated IPv6 traffic through the tunnel.&lt;br&gt; | [optional] 
**local_network** | **List[str]** | The IPv4 networks that will be accessible from the remote endpoint. Expressed as a list of one or more CIDR ranges or host/network type aliases. This may be left blank if not adding a route to the local network through this tunnel on the remote machine. This is generally set to the LAN network.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;gwredir&#x60; must be equal to &#x60;false&#x60;&lt;br&gt; | [optional] 
**local_networkv6** | **List[str]** | The IPv6 networks that will be accessible from the remote endpoint. Expressed as a list of one or more CIDR ranges or host/network type aliases. This may be left blank if not adding a route to the local network through this tunnel on the remote machine. This is generally set to the LAN network.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;gwredir6&#x60; must be equal to &#x60;false&#x60;&lt;br&gt; | [optional] 
**remote_network** | **List[str]** | IPv4 networks that will be routed through the tunnel, so that a site-to-site VPN can be established without manually changing the routing tables. Expressed as a list of one or more CIDR ranges or host/network type aliases. If this is a site-to-site VPN, enter the remote LAN/s here. May be left empty for non site-to-site VPN.&lt;br&gt; | [optional] 
**remote_networkv6** | **List[str]** | IPv6 networks that will be routed through the tunnel, so that a site-to-site VPN can be established without manually changing the routing tables. Expressed as a list of one or more CIDR ranges or host/network type aliases. If this is a site-to-site VPN, enter the remote LAN/s here. May be left empty for non site-to-site VPN.&lt;br&gt; | [optional] 
**maxclients** | **int** | The maximum number of clients allowed to concurrently connect to this server.&lt;br&gt; | [optional] 
**allow_compression** | **str** | The compression mode allowed by this OpenVPN server. Compression can potentially increase throughput but may allow an attacker to extract secrets if they can control compressed plaintext traversing the VPN (e.g. HTTP)&lt;br&gt; | [optional] [default to 'no']
**passtos** | **bool** | Enables or disables setting the TOS IP header value of tunnel packets to match the encapsulated packet value.&lt;br&gt; | [optional] 
**client2client** | **bool** | Enables or disables allowing communication between clients connected to this server.&lt;br&gt; | [optional] 
**duplicate_cn** | **bool** | Enables or disable allowing the same user to connect multiple times.&lt;br&gt; | [optional] 
**connlimit** | **int** | The number of concurrent connections a single user can have.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;duplicate_cn&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**dynamic_ip** | **bool** | Enables or disables allowing connected clients to retain their connections if their IP address changes.&lt;br&gt; | [optional] 
**topology** | **str** | The method used to supply a virtual adapter IP address to clients when using TUN mode on IPv4.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;dev_mode&#x60; must be equal to &#x60;&#39;tun&#39;&#x60;&lt;br&gt; | [optional] [default to 'subnet']
**inactive_seconds** | **int** | The amount of time (in seconds) until a client connection is closed for inactivity.&lt;br&gt; | [optional] [default to 300]
**ping_method** | **str** | The method used to define ping configuration.&lt;br&gt; | [optional] [default to 'keepalive']
**keepalive_interval** | **int** | The keepalive interval parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;ping_method&#x60; must be equal to &#x60;&#39;keepalive&#39;&#x60;&lt;br&gt; | [optional] [default to 10]
**keepalive_timeout** | **int** | The keepalive timeout parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;ping_method&#x60; must be equal to &#x60;&#39;keepalive&#39;&#x60;&lt;br&gt; | [optional] [default to 60]
**ping_seconds** | **int** | The number of seconds to accept no packets before sending a ping to the remote peer over the TCP/UDP control channel.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;ping_method&#x60; must be equal to &#x60;&#39;ping&#39;&#x60;&lt;br&gt; | [optional] [default to 10]
**ping_push** | **bool** | Enables or disables push ping to the VPN client.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;ping_method&#x60; must be equal to &#x60;&#39;ping&#39;&#x60;&lt;br&gt; | [optional] 
**ping_action** | **str** | The action to take after a ping to the remote peer times-out.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;ping_method&#x60; must be equal to &#x60;&#39;ping&#39;&#x60;&lt;br&gt; | [optional] [default to 'ping_restart']
**ping_action_seconds** | **int** | The number of seconds that must elapse before the ping is considered a timeout and the configured &#x60;ping_action&#x60; is performed.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;ping_method&#x60; must be equal to &#x60;&#39;ping&#39;&#x60;&lt;br&gt; | [optional] [default to 60]
**ping_action_push** | **bool** | Enables or disables pushing the ping action to the VPN client.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;ping_method&#x60; must be equal to &#x60;&#39;ping&#39;&#x60;&lt;br&gt; | [optional] 
**dns_domain** | **str** | The default domain to provide to clients.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] 
**dns_server1** | **str** | The primary DNS server to provide to clients.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] 
**dns_server2** | **str** | The secondary DNS server to provide to clients.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] 
**dns_server3** | **str** | The tertiary DNS server to provide to clients.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] 
**dns_server4** | **str** | The quaternary DNS server to provide to clients.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] 
**push_blockoutsidedns** | **bool** | Enables or disables blocking Windows 10 clients&#39; access to DNS servers except across OpenVPN while connected, forcing clients to use only VPN DNS servers.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] 
**push_register_dns** | **bool** | Enables or disables running &#x60;net stop dnscache&#x60;, &#x60;net start dnscache&#x60;, &#x60;ipconfig /flushdns&#x60; and &#x60;ipconfig /registerdns&#x60; on connection initiation for Windows clients.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] 
**ntp_server1** | **str** | The primary NTP server to provide to clients.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] 
**ntp_server2** | **str** | The secondary NTP server to provide to clients.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] 
**netbios_enable** | **bool** | Enables or disables NetBIOS over TCP/IP.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] 
**netbios_ntype** | **int** | The NetBIOS node type.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;netbios_enable&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**netbios_scope** | **str** | The NetBIOS Scope ID. This provides an extended naming service for NetBIOS over TCP/IP. The NetBIOS scope ID isolates NetBIOS traffic on a single network to only those nodes with the same NetBIOS scope ID.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;netbios_enable&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**wins_server1** | **str** | The primary WINS server to provide to clients.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] 
**wins_server2** | **str** | The secondary WINS server to provide to clients.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] 
**custom_options** | **List[str]** | Additional options to add to the OpenVPN server configuration.&lt;br&gt; | [optional] 
**username_as_common_name** | **bool** | Enables or disable the username of the client being used in place of the certificate common name for purposes such as determining Client Specific Overrides.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ server_user, server_tls_user ]&lt;br&gt; | [optional] 
**sndrcvbuf** | **int** | The send and receive buffer size for OpenVPN. Set to null to use the system default.&lt;br&gt; | [optional] 
**create_gw** | **str** | The gateway type(s) that will be created when a virtual interface is assigned to this OpenVPN server&lt;br&gt; | [optional] [default to 'both']
**verbosity_level** | **int** | The OpenVPN logging verbosity level.&lt;br&gt; | [optional] [default to 1]

## Example

```python
from pfsense_api_client.models.open_vpn_server import OpenVPNServer

# TODO update the JSON string below
json = "{}"
# create an instance of OpenVPNServer from a JSON string
open_vpn_server_instance = OpenVPNServer.from_json(json)
# print the JSON string representation of the object
print(OpenVPNServer.to_json())

# convert the object into a dict
open_vpn_server_dict = open_vpn_server_instance.to_dict()
# create an instance of OpenVPNServer from a dict
open_vpn_server_from_dict = OpenVPNServer.from_dict(open_vpn_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


