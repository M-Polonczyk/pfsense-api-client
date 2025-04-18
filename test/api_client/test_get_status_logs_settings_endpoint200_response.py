# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.get_status_logs_settings_endpoint200_response import GetStatusLogsSettingsEndpoint200Response

class TestGetStatusLogsSettingsEndpoint200Response(unittest.TestCase):
    """GetStatusLogsSettingsEndpoint200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetStatusLogsSettingsEndpoint200Response:
        """Test GetStatusLogsSettingsEndpoint200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetStatusLogsSettingsEndpoint200Response`
        """
        model = GetStatusLogsSettingsEndpoint200Response()
        if include_optional:
            return GetStatusLogsSettingsEndpoint200Response(
                code = 56,
                status = 'ok',
                response_id = '',
                message = '',
                data = openapi_client.models.log_settings.LogSettings(
                    format = 'rfc3164', 
                    reverseorder = True, 
                    nentries = 5, 
                    nologdefaultblock = True, 
                    nologdefaultpass = True, 
                    nologbogons = True, 
                    nologprivatenets = True, 
                    nolognginx = True, 
                    rawfilter = True, 
                    disablelocallogging = True, 
                    logconfigchanges = True, 
                    filterdescriptions = 0, 
                    logfilesize = 100000, 
                    rotatecount = 0, 
                    logcompressiontype = 'bzip2', 
                    enableremotelogging = True, 
                    ipprotocol = 'ipv4', 
                    sourceip = '', 
                    remoteserver = '', 
                    remoteserver2 = '', 
                    remoteserver3 = '', 
                    logall = True, 
                    filter = True, 
                    dhcp = True, 
                    auth = True, 
                    portalauth = True, 
                    vpn = True, 
                    dpinger = True, 
                    hostapd = True, 
                    system = True, 
                    resolver = True, 
                    ppp = True, 
                    routing = True, 
                    ntpd = True, ),
                links = openapi_client.models._links._links()
            )
        else:
            return GetStatusLogsSettingsEndpoint200Response(
        )
        """

    def testGetStatusLogsSettingsEndpoint200Response(self):
        """Test GetStatusLogsSettingsEndpoint200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
