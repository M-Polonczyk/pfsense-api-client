# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.get_routing_gateway_groups_endpoint200_response import GetRoutingGatewayGroupsEndpoint200Response

class TestGetRoutingGatewayGroupsEndpoint200Response(unittest.TestCase):
    """GetRoutingGatewayGroupsEndpoint200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetRoutingGatewayGroupsEndpoint200Response:
        """Test GetRoutingGatewayGroupsEndpoint200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRoutingGatewayGroupsEndpoint200Response`
        """
        model = GetRoutingGatewayGroupsEndpoint200Response()
        if include_optional:
            return GetRoutingGatewayGroupsEndpoint200Response(
                code = 56,
                status = 'ok',
                response_id = '',
                message = '',
                data = [
                    openapi_client.models.routing_gateway_group.RoutingGatewayGroup(
                        name = '', 
                        trigger = 'down', 
                        descr = '', 
                        ipprotocol = 'unknown', 
                        priorities = [
                            null
                            ], )
                    ],
                links = openapi_client.models._links._links()
            )
        else:
            return GetRoutingGatewayGroupsEndpoint200Response(
        )
        """

    def testGetRoutingGatewayGroupsEndpoint200Response(self):
        """Test GetRoutingGatewayGroupsEndpoint200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
