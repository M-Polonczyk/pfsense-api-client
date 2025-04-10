# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.open_vpn_server_status_conns_inner import OpenVPNServerStatusConnsInner

class TestOpenVPNServerStatusConnsInner(unittest.TestCase):
    """OpenVPNServerStatusConnsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenVPNServerStatusConnsInner:
        """Test OpenVPNServerStatusConnsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenVPNServerStatusConnsInner`
        """
        model = OpenVPNServerStatusConnsInner()
        if include_optional:
            return OpenVPNServerStatusConnsInner(
                common_name = '',
                remote_host = '',
                virtual_addr = '',
                virtual_addr6 = '',
                bytes_recv = 0,
                bytes_sent = 0,
                connect_time = '',
                connect_time_unix = 0,
                user_name = '',
                client_id = 0,
                peer_id = 0,
                cipher = ''
            )
        else:
            return OpenVPNServerStatusConnsInner(
        )
        """

    def testOpenVPNServerStatusConnsInner(self):
        """Test OpenVPNServerStatusConnsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
