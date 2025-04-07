# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.i_psec_sa_status import IPsecSAStatus

class TestIPsecSAStatus(unittest.TestCase):
    """IPsecSAStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IPsecSAStatus:
        """Test IPsecSAStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IPsecSAStatus`
        """
        model = IPsecSAStatus()
        if include_optional:
            return IPsecSAStatus(
                con_id = '',
                uniqueid = 0,
                version = 0,
                state = '',
                local_host = '',
                local_port = '',
                local_id = '',
                remote_host = '',
                remote_port = '',
                remote_id = '',
                initiator_spi = '',
                responder_spi = '',
                nat_remote = True,
                nat_any = True,
                encr_alg = '',
                encr_keysize = 0,
                integ_alg = '',
                prf_alg = '',
                dh_group = '',
                established = 0,
                rekey_time = 0,
                child_sas = [
                    null
                    ]
            )
        else:
            return IPsecSAStatus(
        )
        """

    def testIPsecSAStatus(self):
        """Test IPsecSAStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
