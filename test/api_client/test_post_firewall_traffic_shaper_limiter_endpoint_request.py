# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.post_firewall_traffic_shaper_limiter_endpoint_request import PostFirewallTrafficShaperLimiterEndpointRequest

class TestPostFirewallTrafficShaperLimiterEndpointRequest(unittest.TestCase):
    """PostFirewallTrafficShaperLimiterEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostFirewallTrafficShaperLimiterEndpointRequest:
        """Test PostFirewallTrafficShaperLimiterEndpointRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostFirewallTrafficShaperLimiterEndpointRequest`
        """
        model = PostFirewallTrafficShaperLimiterEndpointRequest()
        if include_optional:
            return PostFirewallTrafficShaperLimiterEndpointRequest(
                name = '',
                number = 0,
                enabled = True,
                mask = 'none',
                maskbits = 1,
                maskbitsv6 = 1,
                qlimit = 1,
                ecn = True,
                description = '',
                aqm = 'droptail',
                sched = 'wf2q+',
                param_codel_target = 0,
                param_codel_interval = 0,
                param_pie_target = 0,
                param_pie_tupdate = 0,
                param_pie_alpha = 0,
                param_pie_beta = 0,
                param_pie_max_burst = 0,
                param_pie_max_ecnth = 0,
                pie_onoff = True,
                pie_capdrop = True,
                pie_qdelay = True,
                pie_pderand = True,
                param_red_w_q = 0,
                param_red_min_th = 0,
                param_red_max_th = 0,
                param_red_max_p = 0,
                param_gred_w_q = 0,
                param_gred_min_th = 0,
                param_gred_max_th = 0,
                param_gred_max_p = 0,
                param_fq_codel_target = 0,
                param_fq_codel_interval = 0,
                param_fq_codel_quantum = 0,
                param_fq_codel_limit = 0,
                param_fq_codel_flows = 0,
                param_fq_pie_target = 0,
                param_fq_pie_tupdate = 0,
                param_fq_pie_alpha = 0,
                param_fq_pie_beta = 0,
                param_fq_pie_max_burst = 0,
                param_fq_pie_max_ecnth = 0,
                param_fq_pie_quantum = 0,
                param_fq_pie_limit = 0,
                param_fq_pie_flows = 0,
                delay = 0,
                plr = 0,
                buckets = 16,
                bandwidth = [
                    null
                    ],
                queue = [
                    null
                    ]
            )
        else:
            return PostFirewallTrafficShaperLimiterEndpointRequest(
                name = '',
                aqm = 'droptail',
                sched = 'wf2q+',
        )
        """

    def testPostFirewallTrafficShaperLimiterEndpointRequest(self):
        """Test PostFirewallTrafficShaperLimiterEndpointRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
