# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.post_vpni_psec_phase1_endpoint_request import PostVPNIPsecPhase1EndpointRequest

class TestPostVPNIPsecPhase1EndpointRequest(unittest.TestCase):
    """PostVPNIPsecPhase1EndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostVPNIPsecPhase1EndpointRequest:
        """Test PostVPNIPsecPhase1EndpointRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostVPNIPsecPhase1EndpointRequest`
        """
        model = PostVPNIPsecPhase1EndpointRequest()
        if include_optional:
            return PostVPNIPsecPhase1EndpointRequest(
                ikeid = 0,
                descr = '',
                disabled = True,
                iketype = 'ikev1',
                mode = 'main',
                protocol = 'inet',
                interface = '',
                remote_gateway = '',
                authentication_method = 'pre_shared_key',
                myid_type = 'myaddress',
                myid_data = '',
                peerid_type = 'any',
                peerid_data = '',
                pre_shared_key = '',
                certref = '',
                caref = '',
                rekey_time = 0,
                reauth_time = 0,
                rand_time = 0,
                lifetime = 0,
                startaction = '',
                closeaction = '',
                nat_traversal = 'on',
                gw_duplicates = True,
                mobike = True,
                splitconn = True,
                prfselect_enable = True,
                ikeport = '500',
                nattport = '4500',
                dpd_delay = 0,
                dpd_maxfail = 0,
                encryption = [
                    null
                    ]
            )
        else:
            return PostVPNIPsecPhase1EndpointRequest(
                iketype = 'ikev1',
                mode = 'main',
                protocol = 'inet',
                interface = '',
                remote_gateway = '',
                authentication_method = 'pre_shared_key',
                myid_type = 'myaddress',
                myid_data = '',
                peerid_type = 'any',
                peerid_data = '',
                pre_shared_key = '',
                certref = '',
                caref = '',
                encryption = [
                    null
                    ],
        )
        """

    def testPostVPNIPsecPhase1EndpointRequest(self):
        """Test PostVPNIPsecPhase1EndpointRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
