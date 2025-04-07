# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfsense_api_client.models.system_status import SystemStatus

class TestSystemStatus(unittest.TestCase):
    """SystemStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemStatus:
        """Test SystemStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemStatus`
        """
        model = SystemStatus()
        if include_optional:
            return SystemStatus(
                platform = '',
                serial = '',
                netgate_id = '',
                uptime = '',
                bios_vendor = '',
                bios_version = '',
                bios_date = '',
                kernel_pti = True,
                mds_mitigation = '',
                temp_c = 0,
                temp_f = 0,
                cpu_model = '',
                cpu_load_avg = [
                    0
                    ],
                cpu_count = 0,
                cpu_usage = 0,
                mbuf_usage = 0,
                mem_usage = 0,
                swap_usage = 0,
                disk_usage = 0
            )
        else:
            return SystemStatus(
        )
        """

    def testSystemStatus(self):
        """Test SystemStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
