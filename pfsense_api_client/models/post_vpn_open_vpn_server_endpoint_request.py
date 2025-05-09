# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PostVPNOpenVPNServerEndpointRequest(BaseModel):
    """
    PostVPNOpenVPNServerEndpointRequest
    """ # noqa: E501
    vpnid: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=None, description="The unique ID for this OpenVPN server. This value is assigned by the system and cannot be changed.<br>")
    vpnif: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The VPN interface name for this OpenVPN server. This value is assigned by the system and cannot be changed.<br>")
    description: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The description for this OpenVPN server.<br>")
    disable: Optional[StrictBool] = Field(default=None, description="Disables this OpenVPN server.<br>")
    mode: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The OpenVPN server mode.<br>")
    authmode: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=128)]] = Field(default=None, description="The name of the authentication server to use as the authentication backend for this OpenVPN server<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    dev_mode: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The carrier mode for this OpenVPN server. `tun` mode carries IPv4 and IPv6 (layer 3) and is the most common and compatible mode across all platforms. `tap` mode is capable of carrying 802.3 (layer 2).<br>")
    protocol: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The protocol used by this OpenVPN server.<br>")
    interface: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The interface or Virtual IP address where OpenVPN will receive client connections.<br><br>This field is only available when the following conditions are met:<br>- `protocol` must not be one of [ UDP, TCP ]<br>")
    local_port: Optional[StrictStr] = Field(default='1194', description="The port used by OpenVPN to receive client connections. Valid options are: a TCP/UDP port number<br>")
    use_tls: Optional[StrictBool] = Field(default=None, description="Enables or disables the use of a TLS key for this OpenVPN server.<br>")
    tls: Optional[StrictStr] = Field(default=None, description="The TLS key this OpenVPN server will use to sign control channel packets with an HMAC signature for authentication when establishing the tunnel.<br><br>This field is only available when the following conditions are met:<br>- `use_tls` must be equal to `true`<br>")
    tls_type: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The TLS key usage type. In `auth` mode, the TLS key is used only as HMAC authentication for the control channel, protecting the peers from unauthorized connections. The `crypt` mode encrypts the control channel communication in addition to providing authentication, providing more privacy and traffic control channel obfuscation.<br><br>This field is only available when the following conditions are met:<br>- `use_tls` must be equal to `true`<br>")
    tlsauth_keydir: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='default', description="The TLS key direction. This must be set to complementary values on the client and server. For example, if the server is set to 0, the client must be set to 1. Both may be set to omit the direction, in which case the TLS Key will be used bidirectionally.<br><br>This field is only available when the following conditions are met:<br>- `use_tls` must be equal to `true`<br>")
    caref: StrictStr = Field(description="The `refid` of the CA object to assume as the peer CA.<br>")
    certref: StrictStr = Field(description="The `refid` of the certificate object to assume as the OpenVPN server certificate.<br>")
    cert_depth: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=1, description="The depth of the certificate chain to check when a certificate based client signs in. Certificates below this depth are not accepted. This is useful for denying certificates made with intermediate CAs generated from the same CA as the server. Set to null to use system default.<br>")
    dh_length: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The Diffie-Hellman (DH) parameter set used for key exchange.<br>")
    ecdh_curve: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The Elliptic Curve to use for key exchange. The curve from the server certificate is used by default when the server uses an ECDSA certificate. Otherwise, secp384r1 is used as a fallback.<br>")
    data_ciphers: Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]], Field(min_length=1, max_length=128)] = Field(description="The encryption algorithms/ciphers allowed by this OpenVPN server.<br>")
    data_ciphers_fallback: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The fallback encryption algorithm/cipher used for data channel packets when communicating with clients that do not support data encryption algorithm negotiation (e.g. Shared Key).<br>")
    digest: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The algorithm used to authenticate data channel packets, and control channel packets if a TLS Key is present.<br>")
    strictusercn: Optional[StrictBool] = Field(default=None, description="Enables or disables enforcing a match between the common name of the client certificate and the username given at login.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    remote_cert_tls: Optional[StrictBool] = Field(default=True, description="Enables or disables requiring hosts to have a client certificate to connect.<br>")
    tunnel_network: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The IPv4 virtual network used for private communications between this server and client hosts.<br>")
    tunnel_networkv6: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The IPv6 virtual network used for private communications between this server and client hosts.<br>")
    serverbridge_dhcp: Optional[StrictBool] = Field(default=None, description="Enables or disables clients on the bridge to obtain DHCP.<br><br>This field is only available when the following conditions are met:<br>- `dev_mode` must be equal to `'tap'`<br>")
    serverbridge_interface: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The interface to which this TAP instance will be bridged. This is not done automatically. This interface must be assigned and the bridge created separately. This setting controls which existing IP address and subnet mask are used by OpenVPN for the bridge.<br><br>This field is only available when the following conditions are met:<br>- `serverbridge_dhcp` must be equal to `true`<br>")
    serverbridge_routegateway: Optional[StrictBool] = Field(default=None, description="Enables or disables pushing the bridge interface's IPv4 address to connecting clients as a route gateway.<br><br>This field is only available when the following conditions are met:<br>- `serverbridge_dhcp` must be equal to `true`<br>")
    serverbridge_dhcp_start: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The bridge DHCP range's start address.<br><br>This field is only available when the following conditions are met:<br>- `serverbridge_dhcp` must be equal to `true`<br>")
    serverbridge_dhcp_end: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The bridge DHCP range's end address.<br><br>This field is only available when the following conditions are met:<br>- `serverbridge_dhcp` must be equal to `true`<br>")
    gwredir: Optional[StrictBool] = Field(default=None, description="Enable forcing all client-generated IPv4 traffic through the tunnel.<br>")
    gwredir6: Optional[StrictBool] = Field(default=None, description="Enable forcing all client-generated IPv6 traffic through the tunnel.<br>")
    local_network: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]], Field(min_length=0, max_length=10000)]] = Field(default=None, description="The IPv4 networks that will be accessible from the remote endpoint. Expressed as a list of one or more CIDR ranges or host/network type aliases. This may be left blank if not adding a route to the local network through this tunnel on the remote machine. This is generally set to the LAN network.<br><br>This field is only available when the following conditions are met:<br>- `gwredir` must be equal to `false`<br>")
    local_networkv6: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]], Field(min_length=0, max_length=128)]] = Field(default=None, description="The IPv6 networks that will be accessible from the remote endpoint. Expressed as a list of one or more CIDR ranges or host/network type aliases. This may be left blank if not adding a route to the local network through this tunnel on the remote machine. This is generally set to the LAN network.<br><br>This field is only available when the following conditions are met:<br>- `gwredir6` must be equal to `false`<br>")
    remote_network: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]], Field(min_length=0, max_length=128)]] = Field(default=None, description="IPv4 networks that will be routed through the tunnel, so that a site-to-site VPN can be established without manually changing the routing tables. Expressed as a list of one or more CIDR ranges or host/network type aliases. If this is a site-to-site VPN, enter the remote LAN/s here. May be left empty for non site-to-site VPN.<br>")
    remote_networkv6: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]], Field(min_length=0, max_length=128)]] = Field(default=None, description="IPv6 networks that will be routed through the tunnel, so that a site-to-site VPN can be established without manually changing the routing tables. Expressed as a list of one or more CIDR ranges or host/network type aliases. If this is a site-to-site VPN, enter the remote LAN/s here. May be left empty for non site-to-site VPN.<br>")
    maxclients: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=None, description="The maximum number of clients allowed to concurrently connect to this server.<br>")
    allow_compression: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='no', description="The compression mode allowed by this OpenVPN server. Compression can potentially increase throughput but may allow an attacker to extract secrets if they can control compressed plaintext traversing the VPN (e.g. HTTP)<br>")
    passtos: Optional[StrictBool] = Field(default=None, description="Enables or disables setting the TOS IP header value of tunnel packets to match the encapsulated packet value.<br>")
    client2client: Optional[StrictBool] = Field(default=None, description="Enables or disables allowing communication between clients connected to this server.<br>")
    duplicate_cn: Optional[StrictBool] = Field(default=None, description="Enables or disable allowing the same user to connect multiple times.<br>")
    connlimit: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=None, description="The number of concurrent connections a single user can have.<br><br>This field is only available when the following conditions are met:<br>- `duplicate_cn` must be equal to `true`<br>")
    dynamic_ip: Optional[StrictBool] = Field(default=None, description="Enables or disables allowing connected clients to retain their connections if their IP address changes.<br>")
    topology: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='subnet', description="The method used to supply a virtual adapter IP address to clients when using TUN mode on IPv4.<br><br>This field is only available when the following conditions are met:<br>- `dev_mode` must be equal to `'tun'`<br>")
    inactive_seconds: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=300, description="The amount of time (in seconds) until a client connection is closed for inactivity.<br>")
    ping_method: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='keepalive', description="The method used to define ping configuration.<br>")
    keepalive_interval: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=10, description="The keepalive interval parameter.<br><br>This field is only available when the following conditions are met:<br>- `ping_method` must be equal to `'keepalive'`<br>")
    keepalive_timeout: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=60, description="The keepalive timeout parameter.<br><br>This field is only available when the following conditions are met:<br>- `ping_method` must be equal to `'keepalive'`<br>")
    ping_seconds: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=10, description="The number of seconds to accept no packets before sending a ping to the remote peer over the TCP/UDP control channel.<br><br>This field is only available when the following conditions are met:<br>- `ping_method` must be equal to `'ping'`<br>")
    ping_push: Optional[StrictBool] = Field(default=None, description="Enables or disables push ping to the VPN client.<br><br>This field is only available when the following conditions are met:<br>- `ping_method` must be equal to `'ping'`<br>")
    ping_action: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='ping_restart', description="The action to take after a ping to the remote peer times-out.<br><br>This field is only available when the following conditions are met:<br>- `ping_method` must be equal to `'ping'`<br>")
    ping_action_seconds: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=60, description="The number of seconds that must elapse before the ping is considered a timeout and the configured `ping_action` is performed.<br><br>This field is only available when the following conditions are met:<br>- `ping_method` must be equal to `'ping'`<br>")
    ping_action_push: Optional[StrictBool] = Field(default=None, description="Enables or disables pushing the ping action to the VPN client.<br><br>This field is only available when the following conditions are met:<br>- `ping_method` must be equal to `'ping'`<br>")
    dns_domain: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The default domain to provide to clients.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    dns_server1: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The primary DNS server to provide to clients.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    dns_server2: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The secondary DNS server to provide to clients.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    dns_server3: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The tertiary DNS server to provide to clients.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    dns_server4: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The quaternary DNS server to provide to clients.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    push_blockoutsidedns: Optional[StrictBool] = Field(default=None, description="Enables or disables blocking Windows 10 clients' access to DNS servers except across OpenVPN while connected, forcing clients to use only VPN DNS servers.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    push_register_dns: Optional[StrictBool] = Field(default=None, description="Enables or disables running `net stop dnscache`, `net start dnscache`, `ipconfig /flushdns` and `ipconfig /registerdns` on connection initiation for Windows clients.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    ntp_server1: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The primary NTP server to provide to clients.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    ntp_server2: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The secondary NTP server to provide to clients.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    netbios_enable: Optional[StrictBool] = Field(default=None, description="Enables or disables NetBIOS over TCP/IP.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    netbios_ntype: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=None, description="The NetBIOS node type.<br><br>This field is only available when the following conditions are met:<br>- `netbios_enable` must be equal to `true`<br>")
    netbios_scope: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The NetBIOS Scope ID. This provides an extended naming service for NetBIOS over TCP/IP. The NetBIOS scope ID isolates NetBIOS traffic on a single network to only those nodes with the same NetBIOS scope ID.<br><br>This field is only available when the following conditions are met:<br>- `netbios_enable` must be equal to `true`<br>")
    wins_server1: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The primary WINS server to provide to clients.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    wins_server2: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The secondary WINS server to provide to clients.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    custom_options: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]], Field(min_length=0, max_length=128)]] = Field(default=None, description="Additional options to add to the OpenVPN server configuration.<br>")
    username_as_common_name: Optional[StrictBool] = Field(default=None, description="Enables or disable the username of the client being used in place of the certificate common name for purposes such as determining Client Specific Overrides.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>")
    sndrcvbuf: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=None, description="The send and receive buffer size for OpenVPN. Set to null to use the system default.<br>")
    create_gw: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='both', description="The gateway type(s) that will be created when a virtual interface is assigned to this OpenVPN server<br>")
    verbosity_level: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=1, description="The OpenVPN logging verbosity level.<br>")
    __properties: ClassVar[List[str]] = ["vpnid", "vpnif", "description", "disable", "mode", "authmode", "dev_mode", "protocol", "interface", "local_port", "use_tls", "tls", "tls_type", "tlsauth_keydir", "caref", "certref", "cert_depth", "dh_length", "ecdh_curve", "data_ciphers", "data_ciphers_fallback", "digest", "strictusercn", "remote_cert_tls", "tunnel_network", "tunnel_networkv6", "serverbridge_dhcp", "serverbridge_interface", "serverbridge_routegateway", "serverbridge_dhcp_start", "serverbridge_dhcp_end", "gwredir", "gwredir6", "local_network", "local_networkv6", "remote_network", "remote_networkv6", "maxclients", "allow_compression", "passtos", "client2client", "duplicate_cn", "connlimit", "dynamic_ip", "topology", "inactive_seconds", "ping_method", "keepalive_interval", "keepalive_timeout", "ping_seconds", "ping_push", "ping_action", "ping_action_seconds", "ping_action_push", "dns_domain", "dns_server1", "dns_server2", "dns_server3", "dns_server4", "push_blockoutsidedns", "push_register_dns", "ntp_server1", "ntp_server2", "netbios_enable", "netbios_ntype", "netbios_scope", "wins_server1", "wins_server2", "custom_options", "username_as_common_name", "sndrcvbuf", "create_gw", "verbosity_level"]

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['p2p_tls', 'server_tls', 'server_user', 'server_tls_user']):
            raise ValueError("must be one of enum values ('p2p_tls', 'server_tls', 'server_user', 'server_tls_user')")
        return value

    @field_validator('dev_mode')
    def dev_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['tun', 'tap']):
            raise ValueError("must be one of enum values ('tun', 'tap')")
        return value

    @field_validator('protocol')
    def protocol_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['UDP4', 'UDP6', 'UDP', 'TCP4', 'TCP6', 'TCP']):
            raise ValueError("must be one of enum values ('UDP4', 'UDP6', 'UDP', 'TCP4', 'TCP6', 'TCP')")
        return value

    @field_validator('tls_type')
    def tls_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['auth', 'crypt']):
            raise ValueError("must be one of enum values ('auth', 'crypt')")
        return value

    @field_validator('tlsauth_keydir')
    def tlsauth_keydir_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['default', '0', '1', '2']):
            raise ValueError("must be one of enum values ('default', '0', '1', '2')")
        return value

    @field_validator('cert_depth')
    def cert_depth_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([1, 2, 3, 4, 5]):
            raise ValueError("must be one of enum values (1, 2, 3, 4, 5)")
        return value

    @field_validator('allow_compression')
    def allow_compression_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['no', 'yes', 'asym']):
            raise ValueError("must be one of enum values ('no', 'yes', 'asym')")
        return value

    @field_validator('topology')
    def topology_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['subnet', 'net30']):
            raise ValueError("must be one of enum values ('subnet', 'net30')")
        return value

    @field_validator('ping_method')
    def ping_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['keepalive', 'ping']):
            raise ValueError("must be one of enum values ('keepalive', 'ping')")
        return value

    @field_validator('ping_action')
    def ping_action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ping_restart', 'ping_exit']):
            raise ValueError("must be one of enum values ('ping_restart', 'ping_exit')")
        return value

    @field_validator('netbios_ntype')
    def netbios_ntype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1, 2, 4, 8]):
            raise ValueError("must be one of enum values (0, 1, 2, 4, 8)")
        return value

    @field_validator('sndrcvbuf')
    def sndrcvbuf_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([65536, 131072, 262144, 524288, 1048576, 2097152]):
            raise ValueError("must be one of enum values (65536, 131072, 262144, 524288, 1048576, 2097152)")
        return value

    @field_validator('create_gw')
    def create_gw_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['both', 'v4only', 'v6only']):
            raise ValueError("must be one of enum values ('both', 'v4only', 'v6only')")
        return value

    @field_validator('verbosity_level')
    def verbosity_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]):
            raise ValueError("must be one of enum values (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PostVPNOpenVPNServerEndpointRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "vpnid",
            "vpnif",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if vpnid (nullable) is None
        # and model_fields_set contains the field
        if self.vpnid is None and "vpnid" in self.model_fields_set:
            _dict['vpnid'] = None

        # set to None if vpnif (nullable) is None
        # and model_fields_set contains the field
        if self.vpnif is None and "vpnif" in self.model_fields_set:
            _dict['vpnif'] = None

        # set to None if cert_depth (nullable) is None
        # and model_fields_set contains the field
        if self.cert_depth is None and "cert_depth" in self.model_fields_set:
            _dict['cert_depth'] = None

        # set to None if maxclients (nullable) is None
        # and model_fields_set contains the field
        if self.maxclients is None and "maxclients" in self.model_fields_set:
            _dict['maxclients'] = None

        # set to None if connlimit (nullable) is None
        # and model_fields_set contains the field
        if self.connlimit is None and "connlimit" in self.model_fields_set:
            _dict['connlimit'] = None

        # set to None if sndrcvbuf (nullable) is None
        # and model_fields_set contains the field
        if self.sndrcvbuf is None and "sndrcvbuf" in self.model_fields_set:
            _dict['sndrcvbuf'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostVPNOpenVPNServerEndpointRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "vpnid": obj.get("vpnid"),
            "vpnif": obj.get("vpnif"),
            "description": obj.get("description"),
            "disable": obj.get("disable"),
            "mode": obj.get("mode"),
            "authmode": obj.get("authmode"),
            "dev_mode": obj.get("dev_mode"),
            "protocol": obj.get("protocol"),
            "interface": obj.get("interface"),
            "local_port": obj.get("local_port") if obj.get("local_port") is not None else '1194',
            "use_tls": obj.get("use_tls"),
            "tls": obj.get("tls"),
            "tls_type": obj.get("tls_type"),
            "tlsauth_keydir": obj.get("tlsauth_keydir") if obj.get("tlsauth_keydir") is not None else 'default',
            "caref": obj.get("caref"),
            "certref": obj.get("certref"),
            "cert_depth": obj.get("cert_depth") if obj.get("cert_depth") is not None else 1,
            "dh_length": obj.get("dh_length"),
            "ecdh_curve": obj.get("ecdh_curve"),
            "data_ciphers": obj.get("data_ciphers"),
            "data_ciphers_fallback": obj.get("data_ciphers_fallback"),
            "digest": obj.get("digest"),
            "strictusercn": obj.get("strictusercn"),
            "remote_cert_tls": obj.get("remote_cert_tls") if obj.get("remote_cert_tls") is not None else True,
            "tunnel_network": obj.get("tunnel_network"),
            "tunnel_networkv6": obj.get("tunnel_networkv6"),
            "serverbridge_dhcp": obj.get("serverbridge_dhcp"),
            "serverbridge_interface": obj.get("serverbridge_interface"),
            "serverbridge_routegateway": obj.get("serverbridge_routegateway"),
            "serverbridge_dhcp_start": obj.get("serverbridge_dhcp_start"),
            "serverbridge_dhcp_end": obj.get("serverbridge_dhcp_end"),
            "gwredir": obj.get("gwredir"),
            "gwredir6": obj.get("gwredir6"),
            "local_network": obj.get("local_network"),
            "local_networkv6": obj.get("local_networkv6"),
            "remote_network": obj.get("remote_network"),
            "remote_networkv6": obj.get("remote_networkv6"),
            "maxclients": obj.get("maxclients"),
            "allow_compression": obj.get("allow_compression") if obj.get("allow_compression") is not None else 'no',
            "passtos": obj.get("passtos"),
            "client2client": obj.get("client2client"),
            "duplicate_cn": obj.get("duplicate_cn"),
            "connlimit": obj.get("connlimit"),
            "dynamic_ip": obj.get("dynamic_ip"),
            "topology": obj.get("topology") if obj.get("topology") is not None else 'subnet',
            "inactive_seconds": obj.get("inactive_seconds") if obj.get("inactive_seconds") is not None else 300,
            "ping_method": obj.get("ping_method") if obj.get("ping_method") is not None else 'keepalive',
            "keepalive_interval": obj.get("keepalive_interval") if obj.get("keepalive_interval") is not None else 10,
            "keepalive_timeout": obj.get("keepalive_timeout") if obj.get("keepalive_timeout") is not None else 60,
            "ping_seconds": obj.get("ping_seconds") if obj.get("ping_seconds") is not None else 10,
            "ping_push": obj.get("ping_push"),
            "ping_action": obj.get("ping_action") if obj.get("ping_action") is not None else 'ping_restart',
            "ping_action_seconds": obj.get("ping_action_seconds") if obj.get("ping_action_seconds") is not None else 60,
            "ping_action_push": obj.get("ping_action_push"),
            "dns_domain": obj.get("dns_domain"),
            "dns_server1": obj.get("dns_server1"),
            "dns_server2": obj.get("dns_server2"),
            "dns_server3": obj.get("dns_server3"),
            "dns_server4": obj.get("dns_server4"),
            "push_blockoutsidedns": obj.get("push_blockoutsidedns"),
            "push_register_dns": obj.get("push_register_dns"),
            "ntp_server1": obj.get("ntp_server1"),
            "ntp_server2": obj.get("ntp_server2"),
            "netbios_enable": obj.get("netbios_enable"),
            "netbios_ntype": obj.get("netbios_ntype"),
            "netbios_scope": obj.get("netbios_scope"),
            "wins_server1": obj.get("wins_server1"),
            "wins_server2": obj.get("wins_server2"),
            "custom_options": obj.get("custom_options"),
            "username_as_common_name": obj.get("username_as_common_name"),
            "sndrcvbuf": obj.get("sndrcvbuf"),
            "create_gw": obj.get("create_gw") if obj.get("create_gw") is not None else 'both',
            "verbosity_level": obj.get("verbosity_level") if obj.get("verbosity_level") is not None else 1
        })
        return _obj


