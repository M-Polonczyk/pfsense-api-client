# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.certificate_revocation_list_revoked_certificate import CertificateRevocationListRevokedCertificate

class TestCertificateRevocationListRevokedCertificate(unittest.TestCase):
    """CertificateRevocationListRevokedCertificate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificateRevocationListRevokedCertificate:
        """Test CertificateRevocationListRevokedCertificate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificateRevocationListRevokedCertificate`
        """
        model = CertificateRevocationListRevokedCertificate()
        if include_optional:
            return CertificateRevocationListRevokedCertificate(
                certref = '',
                serial = '',
                reason = -1,
                revoke_time = 0,
                caref = '',
                descr = '',
                type = '',
                crt = '',
                prv = ''
            )
        else:
            return CertificateRevocationListRevokedCertificate(
        )
        """

    def testCertificateRevocationListRevokedCertificate(self):
        """Test CertificateRevocationListRevokedCertificate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
