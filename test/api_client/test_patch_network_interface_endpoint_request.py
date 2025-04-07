# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.patch_network_interface_endpoint_request import PatchNetworkInterfaceEndpointRequest

class TestPatchNetworkInterfaceEndpointRequest(unittest.TestCase):
    """PatchNetworkInterfaceEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchNetworkInterfaceEndpointRequest:
        """Test PatchNetworkInterfaceEndpointRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchNetworkInterfaceEndpointRequest`
        """
        model = PatchNetworkInterfaceEndpointRequest()
        if include_optional:
            return PatchNetworkInterfaceEndpointRequest(
                var_if = '',
                enable = True,
                descr = '',
                spoofmac = '',
                mtu = 1280,
                mss = 576,
                media = '',
                mediaopt = '',
                blockpriv = True,
                blockbogons = True,
                typev4 = 'static',
                ipaddr = '',
                subnet = 1,
                gateway = '',
                dhcphostname = '',
                alias_address = '',
                alias_subnet = 0,
                dhcprejectfrom = [
                    ''
                    ],
                adv_dhcp_config_advanced = True,
                adv_dhcp_pt_values = 'SavedCfg',
                adv_dhcp_pt_timeout = 1,
                adv_dhcp_pt_retry = 1,
                adv_dhcp_pt_select_timeout = 0,
                adv_dhcp_pt_reboot = 1,
                adv_dhcp_pt_backoff_cutoff = 1,
                adv_dhcp_pt_initial_interval = 1,
                adv_dhcp_send_options = '',
                adv_dhcp_request_options = '',
                adv_dhcp_required_options = '',
                adv_dhcp_option_modifiers = '',
                adv_dhcp_config_file_override = True,
                adv_dhcp_config_file_override_path = '',
                typev6 = 'staticv6',
                ipaddrv6 = '',
                subnetv6 = 1,
                gatewayv6 = '',
                ipv6usev4iface = True,
                slaacusev4iface = True,
                prefix_6rd = '',
                gateway_6rd = '',
                prefix_6rd_v4plen = 0,
                track6_interface = '',
                track6_prefix_id_hex = '',
                id = 56
            )
        else:
            return PatchNetworkInterfaceEndpointRequest(
                id = 56,
        )
        """

    def testPatchNetworkInterfaceEndpointRequest(self):
        """Test PatchNetworkInterfaceEndpointRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
