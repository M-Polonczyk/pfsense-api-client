# FirewallAdvancedSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliasesresolveinterval** | **int** | The interval (in seconds) at which to resolve hostnames in aliases.&lt;br&gt; | [optional] [default to 999999999]
**checkaliasesurlcert** | **bool** | Check the certificate of URLs used in aliases.&lt;br&gt; | [optional] [default to True]

## Example

```python
from pfsense_api_client.models.firewall_advanced_settings import FirewallAdvancedSettings

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallAdvancedSettings from a JSON string
firewall_advanced_settings_instance = FirewallAdvancedSettings.from_json(json)
# print the JSON string representation of the object
print(FirewallAdvancedSettings.to_json())

# convert the object into a dict
firewall_advanced_settings_dict = firewall_advanced_settings_instance.to_dict()
# create an instance of FirewallAdvancedSettings from a dict
firewall_advanced_settings_from_dict = FirewallAdvancedSettings.from_dict(firewall_advanced_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


