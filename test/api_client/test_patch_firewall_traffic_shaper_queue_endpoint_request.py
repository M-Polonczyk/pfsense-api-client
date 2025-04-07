# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.patch_firewall_traffic_shaper_queue_endpoint_request import PatchFirewallTrafficShaperQueueEndpointRequest

class TestPatchFirewallTrafficShaperQueueEndpointRequest(unittest.TestCase):
    """PatchFirewallTrafficShaperQueueEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchFirewallTrafficShaperQueueEndpointRequest:
        """Test PatchFirewallTrafficShaperQueueEndpointRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchFirewallTrafficShaperQueueEndpointRequest`
        """
        model = PatchFirewallTrafficShaperQueueEndpointRequest()
        if include_optional:
            return PatchFirewallTrafficShaperQueueEndpointRequest(
                interface = '',
                enabled = True,
                name = '',
                priority = 0,
                qlimit = 1,
                description = '',
                default = True,
                red = True,
                rio = True,
                ecn = True,
                codel = True,
                bandwidthtype = 'Mb',
                bandwidth = 1,
                buckets = 0,
                hogs = 0,
                borrow = True,
                upperlimit = True,
                upperlimit_m1 = '',
                upperlimit_d = 1,
                upperlimit_m2 = '',
                realtime = True,
                realtime_m1 = '',
                realtime_d = 1,
                realtime_m2 = '',
                linkshare = True,
                linkshare_m1 = '',
                linkshare_d = 1,
                linkshare_m2 = '',
                parent_id = 56,
                id = 56
            )
        else:
            return PatchFirewallTrafficShaperQueueEndpointRequest(
                parent_id = 56,
                id = 56,
        )
        """

    def testPatchFirewallTrafficShaperQueueEndpointRequest(self):
        """Test PatchFirewallTrafficShaperQueueEndpointRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
