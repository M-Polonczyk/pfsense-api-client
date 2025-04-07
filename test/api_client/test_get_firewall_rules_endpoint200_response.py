# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.get_firewall_rules_endpoint200_response import GetFirewallRulesEndpoint200Response

class TestGetFirewallRulesEndpoint200Response(unittest.TestCase):
    """GetFirewallRulesEndpoint200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetFirewallRulesEndpoint200Response:
        """Test GetFirewallRulesEndpoint200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetFirewallRulesEndpoint200Response`
        """
        model = GetFirewallRulesEndpoint200Response()
        if include_optional:
            return GetFirewallRulesEndpoint200Response(
                code = 56,
                status = 'ok',
                response_id = '',
                message = '',
                data = [
                    openapi_client.models.firewall_rule.FirewallRule(
                        type = 'pass', 
                        interface = [
                            ''
                            ], 
                        ipprotocol = 'inet', 
                        protocol = 'tcp', 
                        icmptype = [
                            'any'
                            ], 
                        source = '', 
                        source_port = '', 
                        destination = '', 
                        destination_port = '', 
                        descr = '', 
                        disabled = True, 
                        log = True, 
                        tag = '', 
                        statetype = 'keep state', 
                        tcp_flags_any = True, 
                        tcp_flags_out_of = [
                            'fin'
                            ], 
                        tcp_flags_set = [
                            'fin'
                            ], 
                        gateway = '', 
                        sched = '', 
                        dnpipe = '', 
                        pdnpipe = '', 
                        defaultqueue = '', 
                        ackqueue = '', 
                        floating = True, 
                        quick = True, 
                        direction = 'any', 
                        tracker = 0, 
                        associated_rule_id = '', 
                        created_time = 0, 
                        created_by = '@unknown IP (API)', 
                        updated_time = 0, 
                        updated_by = '@unknown IP (API)', )
                    ],
                links = openapi_client.models._links._links()
            )
        else:
            return GetFirewallRulesEndpoint200Response(
        )
        """

    def testGetFirewallRulesEndpoint200Response(self):
        """Test GetFirewallRulesEndpoint200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
