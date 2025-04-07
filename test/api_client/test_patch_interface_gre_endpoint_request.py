# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.patch_interface_gre_endpoint_request import PatchInterfaceGREEndpointRequest

class TestPatchInterfaceGREEndpointRequest(unittest.TestCase):
    """PatchInterfaceGREEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchInterfaceGREEndpointRequest:
        """Test PatchInterfaceGREEndpointRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchInterfaceGREEndpointRequest`
        """
        model = PatchInterfaceGREEndpointRequest()
        if include_optional:
            return PatchInterfaceGREEndpointRequest(
                var_if = '',
                greif = '',
                descr = '',
                add_static_route = True,
                remote_addr = '',
                tunnel_local_addr = '',
                tunnel_remote_addr = '',
                tunnel_remote_net = 1,
                tunnel_local_addr6 = '',
                tunnel_remote_addr6 = '',
                tunnel_remote_net6 = 1,
                id = 56
            )
        else:
            return PatchInterfaceGREEndpointRequest(
                id = 56,
        )
        """

    def testPatchInterfaceGREEndpointRequest(self):
        """Test PatchInterfaceGREEndpointRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
