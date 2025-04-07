# PatchFirewallAdvancedSettingsEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliasesresolveinterval** | **int** | The interval (in seconds) at which to resolve hostnames in aliases.&lt;br&gt; | [optional] [default to 999999999]
**checkaliasesurlcert** | **bool** | Check the certificate of URLs used in aliases.&lt;br&gt; | [optional] [default to True]

## Example

```python
from pfsense_api_client.models.patch_firewall_advanced_settings_endpoint_request import PatchFirewallAdvancedSettingsEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFirewallAdvancedSettingsEndpointRequest from a JSON string
patch_firewall_advanced_settings_endpoint_request_instance = PatchFirewallAdvancedSettingsEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchFirewallAdvancedSettingsEndpointRequest.to_json())

# convert the object into a dict
patch_firewall_advanced_settings_endpoint_request_dict = patch_firewall_advanced_settings_endpoint_request_instance.to_dict()
# create an instance of PatchFirewallAdvancedSettingsEndpointRequest from a dict
patch_firewall_advanced_settings_endpoint_request_from_dict = PatchFirewallAdvancedSettingsEndpointRequest.from_dict(patch_firewall_advanced_settings_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


