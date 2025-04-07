# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.get_firewall_nat_outbound_mapping_endpoint200_response import GetFirewallNATOutboundMappingEndpoint200Response

class TestGetFirewallNATOutboundMappingEndpoint200Response(unittest.TestCase):
    """GetFirewallNATOutboundMappingEndpoint200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetFirewallNATOutboundMappingEndpoint200Response:
        """Test GetFirewallNATOutboundMappingEndpoint200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetFirewallNATOutboundMappingEndpoint200Response`
        """
        model = GetFirewallNATOutboundMappingEndpoint200Response()
        if include_optional:
            return GetFirewallNATOutboundMappingEndpoint200Response(
                code = 56,
                status = 'ok',
                response_id = '',
                message = '',
                data = openapi_client.models.outbound_nat_mapping.OutboundNATMapping(
                    interface = '', 
                    protocol = 'tcp', 
                    disabled = True, 
                    nonat = True, 
                    nosync = True, 
                    source = '', 
                    source_port = '', 
                    destination = '', 
                    destination_port = '', 
                    target = '', 
                    target_subnet = 1, 
                    nat_port = '', 
                    static_nat_port = True, 
                    poolopts = 'round-robin', 
                    source_hash_key = '0x3971d34cd39dfa892480e6beb923e0bd', 
                    descr = '', ),
                links = openapi_client.models._links._links()
            )
        else:
            return GetFirewallNATOutboundMappingEndpoint200Response(
        )
        """

    def testGetFirewallNATOutboundMappingEndpoint200Response(self):
        """Test GetFirewallNATOutboundMappingEndpoint200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
