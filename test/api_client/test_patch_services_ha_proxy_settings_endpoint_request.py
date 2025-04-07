# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.patch_services_ha_proxy_settings_endpoint_request import PatchServicesHAProxySettingsEndpointRequest

class TestPatchServicesHAProxySettingsEndpointRequest(unittest.TestCase):
    """PatchServicesHAProxySettingsEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchServicesHAProxySettingsEndpointRequest:
        """Test PatchServicesHAProxySettingsEndpointRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchServicesHAProxySettingsEndpointRequest`
        """
        model = PatchServicesHAProxySettingsEndpointRequest()
        if include_optional:
            return PatchServicesHAProxySettingsEndpointRequest(
                enable = True,
                maxconn = 0,
                nbthread = 0,
                terminate_on_reload = True,
                hard_stop_after = '15m',
                carpdev = '',
                localstatsport = '',
                localstats_refreshtime = 0,
                localstats_sticktable_refreshtime = 0,
                remotesyslog = '',
                logfacility = 'syslog',
                loglevel = 'warning',
                log_send_hostname = '',
                dns_resolvers = [
                    null
                    ],
                resolver_retries = 0,
                resolver_timeoutretry = '1s',
                resolver_holdvalid = '1s',
                email_mailers = [
                    null
                    ],
                email_level = '',
                email_myhostname = '',
                email_from = '',
                email_to = '',
                sslcompatibilitymode = 'auto',
                ssldefaultdhparam = 1024,
                advanced = '',
                enablesync = True
            )
        else:
            return PatchServicesHAProxySettingsEndpointRequest(
        )
        """

    def testPatchServicesHAProxySettingsEndpointRequest(self):
        """Test PatchServicesHAProxySettingsEndpointRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
