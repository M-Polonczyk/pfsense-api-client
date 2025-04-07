# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.i_psec_sa_status_child_sas_inner import IPsecSAStatusChildSasInner

class TestIPsecSAStatusChildSasInner(unittest.TestCase):
    """IPsecSAStatusChildSasInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IPsecSAStatusChildSasInner:
        """Test IPsecSAStatusChildSasInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IPsecSAStatusChildSasInner`
        """
        model = IPsecSAStatusChildSasInner()
        if include_optional:
            return IPsecSAStatusChildSasInner(
                name = '',
                uniqueid = 0,
                reqid = 0,
                state = '',
                mode = '',
                protocol = '',
                encap = True,
                spi_in = '',
                spi_out = '',
                encr_alg = '',
                encr_keysize = 0,
                integ_alg = '',
                dh_group = '',
                bytes_in = 0,
                bytes_out = 0,
                packets_in = 0,
                packets_out = 0,
                use_in = 0,
                use_out = 0,
                rekey_time = 0,
                life_time = 0,
                install_time = 0,
                local_ts = [
                    ''
                    ],
                remote_ts = [
                    ''
                    ]
            )
        else:
            return IPsecSAStatusChildSasInner(
        )
        """

    def testIPsecSAStatusChildSasInner(self):
        """Test IPsecSAStatusChildSasInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
