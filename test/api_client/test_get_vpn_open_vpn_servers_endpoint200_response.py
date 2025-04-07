# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.get_vpn_open_vpn_servers_endpoint200_response import GetVPNOpenVPNServersEndpoint200Response

class TestGetVPNOpenVPNServersEndpoint200Response(unittest.TestCase):
    """GetVPNOpenVPNServersEndpoint200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetVPNOpenVPNServersEndpoint200Response:
        """Test GetVPNOpenVPNServersEndpoint200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetVPNOpenVPNServersEndpoint200Response`
        """
        model = GetVPNOpenVPNServersEndpoint200Response()
        if include_optional:
            return GetVPNOpenVPNServersEndpoint200Response(
                code = 56,
                status = 'ok',
                response_id = '',
                message = '',
                data = [
                    openapi_client.models.open_vpn_server.OpenVPNServer(
                        vpnid = 0, 
                        vpnif = '', 
                        description = '', 
                        disable = True, 
                        mode = 'p2p_tls', 
                        authmode = [
                            ''
                            ], 
                        dev_mode = 'tun', 
                        protocol = 'UDP4', 
                        interface = '', 
                        local_port = '1194', 
                        use_tls = True, 
                        tls = '', 
                        tls_type = 'auth', 
                        tlsauth_keydir = 'default', 
                        caref = '', 
                        certref = '', 
                        cert_depth = 1, 
                        dh_length = '', 
                        ecdh_curve = '', 
                        data_ciphers = [
                            ''
                            ], 
                        data_ciphers_fallback = '', 
                        digest = '', 
                        strictusercn = True, 
                        remote_cert_tls = True, 
                        tunnel_network = '', 
                        tunnel_networkv6 = '', 
                        serverbridge_dhcp = True, 
                        serverbridge_interface = '', 
                        serverbridge_routegateway = True, 
                        serverbridge_dhcp_start = '', 
                        serverbridge_dhcp_end = '', 
                        gwredir = True, 
                        gwredir6 = True, 
                        local_network = [
                            ''
                            ], 
                        local_networkv6 = [
                            ''
                            ], 
                        remote_network = [
                            ''
                            ], 
                        remote_networkv6 = [
                            ''
                            ], 
                        maxclients = 0, 
                        allow_compression = 'no', 
                        passtos = True, 
                        client2client = True, 
                        duplicate_cn = True, 
                        connlimit = 0, 
                        dynamic_ip = True, 
                        topology = 'subnet', 
                        inactive_seconds = 0, 
                        ping_method = 'keepalive', 
                        keepalive_interval = 0, 
                        keepalive_timeout = 0, 
                        ping_seconds = 0, 
                        ping_push = True, 
                        ping_action = 'ping_restart', 
                        ping_action_seconds = 0, 
                        ping_action_push = True, 
                        dns_domain = '', 
                        dns_server1 = '', 
                        dns_server2 = '', 
                        dns_server3 = '', 
                        dns_server4 = '', 
                        push_blockoutsidedns = True, 
                        push_register_dns = True, 
                        ntp_server1 = '', 
                        ntp_server2 = '', 
                        netbios_enable = True, 
                        netbios_ntype = 0, 
                        netbios_scope = '', 
                        wins_server1 = '', 
                        wins_server2 = '', 
                        custom_options = [
                            ''
                            ], 
                        username_as_common_name = True, 
                        sndrcvbuf = 65536, 
                        create_gw = 'both', 
                        verbosity_level = 0, )
                    ],
                links = openapi_client.models._links._links()
            )
        else:
            return GetVPNOpenVPNServersEndpoint200Response(
        )
        """

    def testGetVPNOpenVPNServersEndpoint200Response(self):
        """Test GetVPNOpenVPNServersEndpoint200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
