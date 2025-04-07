# PostVPNOpenVPNClientEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpnid** | **int** | The unique ID for this OpenVPN client. This value is assigned by the system and cannot be changed.&lt;br&gt; | [optional] [readonly] 
**vpnif** | **str** | The VPN interface name for this OpenVPN client. This value is assigned by the system and cannot be changed.&lt;br&gt; | [optional] [readonly] 
**description** | **str** | The description for this OpenVPN client.&lt;br&gt; | [optional] 
**disable** | **bool** | Disables this OpenVPN client.&lt;br&gt; | [optional] 
**mode** | **str** | The OpenVPN client mode.&lt;br&gt; | 
**dev_mode** | **str** | The carrier mode for this OpenVPN client. &#x60;tun&#x60; mode carries IPv4 and IPv6 (layer 3) and is the most common and compatible mode across all platforms. &#x60;tap&#x60; mode is capable of carrying 802.3 (layer 2).&lt;br&gt; | 
**protocol** | **str** | The protocol used by this OpenVPN client.&lt;br&gt; | 
**interface** | **str** | The interface used by the firewall to originate this OpenVPN client connection.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;protocol&#x60; must not be one of [ UDP, TCP ]&lt;br&gt; | 
**server_addr** | **str** | The IP address or hostname of the OpenVPN server this client will connect to.&lt;br&gt; | 
**server_port** | **str** | The port used by the server to receive client connections. Valid options are: a TCP/UDP port number&lt;br&gt; | 
**local_port** | **str** | The port binding used by OpenVPN for client connections. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] 
**proxy_addr** | **str** | The address for an HTTP Proxy this client can use to connect to a remote server.&lt;br&gt; | [optional] 
**proxy_port** | **str** | The port used by the HTTP Proxy. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] 
**proxy_authtype** | **str** | The type of authentication used by the proxy server.&lt;br&gt; | [optional] [default to 'none']
**proxy_user** | **str** | The username to use for authentication to the remote proxy.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;proxy_authtype&#x60; must not be equal to &#x60;&#39;none&#39;&#x60;&lt;br&gt; | 
**proxy_passwd** | **str** | The username to use for authentication to the remote proxy.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;proxy_authtype&#x60; must not be equal to &#x60;&#39;none&#39;&#x60;&lt;br&gt; | 
**auth_user** | **str** | The username used to authenticate with the OpenVPN server.&lt;br&gt; | [optional] 
**auth_pass** | **str** | The password used to authenticate with the OpenVPN server.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;auth_user&#x60; must not be equal to &#x60;NULL&#x60;&lt;br&gt; | [optional] 
**auth_retry_none** | **bool** | Disables retrying authentication if an authentication failed error is received from the server&lt;br&gt; | [optional] 
**tls** | **str** | The TLS key this OpenVPN client will use to sign control channel packets with an HMAC signature for authentication when establishing the tunnel.&lt;br&gt; | [optional] 
**tls_type** | **str** | The TLS key usage type. In &#x60;auth&#x60; mode, the TLS key is used only as HMAC authentication for the control channel, protecting the peers from unauthorized connections. The &#x60;crypt&#x60; mode encrypts the control channel communication in addition to providing authentication, providing more privacy and traffic control channel obfuscation.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;tls&#x60; must not be equal to &#x60;NULL&#x60;&lt;br&gt; | 
**tlsauth_keydir** | **str** | The TLS key direction. This must be set to complementary values on the client and client. For example, if the client is set to 0, the client must be set to 1. Both may be set to omit the direction, in which case the TLS Key will be used bidirectionally.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;tls&#x60; must not be equal to &#x60;NULL&#x60;&lt;br&gt; | [optional] [default to 'default']
**caref** | **str** | The &#x60;refid&#x60; of the CA object to assume as the peer CA.&lt;br&gt; | 
**certref** | **str** | The &#x60;refid&#x60; of the certificate object to assume as the OpenVPN client certificate.&lt;br&gt; | [optional] 
**data_ciphers** | **List[str]** | The encryption algorithms/ciphers allowed by this OpenVPN client.&lt;br&gt; | 
**data_ciphers_fallback** | **str** | The fallback encryption algorithm/cipher used for data channel packets when communicating with clients that do not support data encryption algorithm negotiation (e.g. Shared Key).&lt;br&gt; | 
**digest** | **str** | The algorithm used to authenticate data channel packets, and control channel packets if a TLS Key is present.&lt;br&gt; | 
**remote_cert_tls** | **bool** | Enables or disables requiring hosts to have a client certificate to connect.&lt;br&gt; | [optional] [default to True]
**tunnel_network** | **str** | The IPv4 virtual network used for private communications between this client and client hosts.&lt;br&gt; | [optional] 
**tunnel_networkv6** | **str** | The IPv6 virtual network used for private communications between this client and client hosts.&lt;br&gt; | [optional] 
**remote_network** | **List[str]** | IPv4 networks that will be routed through the tunnel, so that a site-to-site VPN can be established without manually changing the routing tables. Expressed as a list of one or more CIDR ranges or host/network type aliases. If this is a site-to-site VPN, enter the remote LAN/s here. May be left empty for non site-to-site VPN.&lt;br&gt; | [optional] 
**remote_networkv6** | **List[str]** | IPv6 networks that will be routed through the tunnel, so that a site-to-site VPN can be established without manually changing the routing tables. Expressed as a list of one or more CIDR ranges or host/network type aliases. If this is a site-to-site VPN, enter the remote LAN/s here. May be left empty for non site-to-site VPN.&lt;br&gt; | [optional] 
**use_shaper** | **int** | Maximum outgoing bandwidth (in bytes per second) for this tunnel. Use &#x60;null&#x60; no limit.&lt;br&gt; | [optional] 
**allow_compression** | **str** | The compression mode allowed by this OpenVPN client. Compression can potentially increase throughput but may allow an attacker to extract secrets if they can control compressed plaintext traversing the VPN (e.g. HTTP)&lt;br&gt; | [optional] [default to 'no']
**passtos** | **bool** | Enables or disables setting the TOS IP header value of tunnel packets to match the encapsulated packet value.&lt;br&gt; | [optional] 
**route_no_pull** | **bool** | Enables or disables the servers ability to add routes to the client&#39;s routing table.&lt;br&gt; | [optional] 
**route_no_exec** | **bool** | Enables or disables adding/removing routes automatically.&lt;br&gt; | [optional] 
**dns_add** | **bool** | Enables or disables using the DNS server(s) provided by the OpenVPN server.&lt;br&gt; | [optional] 
**topology** | **str** | The method used to supply a virtual adapter IP address to clients when using TUN mode on IPv4.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;dev_mode&#x60; must be equal to &#x60;&#39;tun&#39;&#x60;&lt;br&gt; | [optional] [default to 'subnet']
**inactive_seconds** | **int** | The amount of time (in seconds) until a client connection is closed for inactivity.&lt;br&gt; | [optional] [default to 300]
**ping_method** | **str** | The method used to define ping configuration.&lt;br&gt; | [optional] [default to 'keepalive']
**keepalive_interval** | **int** | The keepalive interval parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;ping_method&#x60; must be equal to &#x60;&#39;keepalive&#39;&#x60;&lt;br&gt; | [optional] [default to 10]
**keepalive_timeout** | **int** | The keepalive timeout parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;ping_method&#x60; must be equal to &#x60;&#39;keepalive&#39;&#x60;&lt;br&gt; | [optional] [default to 60]
**ping_seconds** | **int** | The number of seconds to accept no packets before sending a ping to the remote peer over the TCP/UDP control channel.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;ping_method&#x60; must be equal to &#x60;&#39;ping&#39;&#x60;&lt;br&gt; | [optional] [default to 10]
**ping_action** | **str** | The action to take after a ping to the remote peer times-out.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;ping_method&#x60; must be equal to &#x60;&#39;ping&#39;&#x60;&lt;br&gt; | [optional] [default to 'ping_restart']
**ping_action_seconds** | **int** | The number of seconds that must elapse before the ping is considered a timeout and the configured &#x60;ping_action&#x60; is performed.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;ping_method&#x60; must be equal to &#x60;&#39;ping&#39;&#x60;&lt;br&gt; | [optional] [default to 60]
**custom_options** | **List[str]** | Additional options to add to the OpenVPN client configuration.&lt;br&gt; | [optional] 
**udp_fast_io** | **bool** | Enables or disables fast I/O operations with UDP writes to tun/tap (Experimental).&lt;br&gt; | [optional] 
**exit_notify** | **str** | The number of times this client will attempt to send an exit notifications.&lt;br&gt; | [optional] [default to 'none']
**sndrcvbuf** | **int** | The send and receive buffer size for OpenVPN. Set to null to use the system default.&lt;br&gt; | [optional] 
**create_gw** | **str** | The gateway type(s) that will be created when a virtual interface is assigned to this OpenVPN server&lt;br&gt; | [optional] [default to 'both']
**verbosity_level** | **int** | The OpenVPN logging verbosity level.&lt;br&gt; | [optional] [default to 1]

## Example

```python
from pfsense_api_client.models.post_vpn_open_vpn_client_endpoint_request import PostVPNOpenVPNClientEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostVPNOpenVPNClientEndpointRequest from a JSON string
post_vpn_open_vpn_client_endpoint_request_instance = PostVPNOpenVPNClientEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostVPNOpenVPNClientEndpointRequest.to_json())

# convert the object into a dict
post_vpn_open_vpn_client_endpoint_request_dict = post_vpn_open_vpn_client_endpoint_request_instance.to_dict()
# create an instance of PostVPNOpenVPNClientEndpointRequest from a dict
post_vpn_open_vpn_client_endpoint_request_from_dict = PostVPNOpenVPNClientEndpointRequest.from_dict(post_vpn_open_vpn_client_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


