# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.get_vpn_open_vpncsos_endpoint200_response import GetVPNOpenVPNCSOsEndpoint200Response

class TestGetVPNOpenVPNCSOsEndpoint200Response(unittest.TestCase):
    """GetVPNOpenVPNCSOsEndpoint200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetVPNOpenVPNCSOsEndpoint200Response:
        """Test GetVPNOpenVPNCSOsEndpoint200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetVPNOpenVPNCSOsEndpoint200Response`
        """
        model = GetVPNOpenVPNCSOsEndpoint200Response()
        if include_optional:
            return GetVPNOpenVPNCSOsEndpoint200Response(
                code = 56,
                status = 'ok',
                response_id = '',
                message = '',
                data = [
                    openapi_client.models.open_vpn_client_specific_override.OpenVPNClientSpecificOverride(
                        common_name = '', 
                        disable = True, 
                        block = True, 
                        description = '', 
                        server_list = [
                            ''
                            ], 
                        tunnel_network = '', 
                        tunnel_networkv6 = '', 
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
                        gwredir = True, 
                        push_reset = True, 
                        remove_route = True, 
                        dns_domain = '', 
                        dns_server1 = '', 
                        dns_server2 = '', 
                        dns_server3 = '', 
                        dns_server4 = '', 
                        ntp_server1 = '', 
                        ntp_server2 = '', 
                        netbios_enable = True, 
                        netbios_ntype = 0, 
                        netbios_scope = '', 
                        wins_server1 = '', 
                        wins_server2 = '', 
                        custom_options = [
                            ''
                            ], )
                    ],
                links = openapi_client.models._links._links()
            )
        else:
            return GetVPNOpenVPNCSOsEndpoint200Response(
        )
        """

    def testGetVPNOpenVPNCSOsEndpoint200Response(self):
        """Test GetVPNOpenVPNCSOsEndpoint200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
