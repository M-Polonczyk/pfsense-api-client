# WireGuardSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enables or disables WireGuard on this system. WireGuard cannot be disabled when one or more tunnels is assigned to a pfSense interface.&lt;br&gt; | [optional] 
**keep_conf** | **bool** | Enables or disables keeping the WireGuard configuration when the package is uninstalled/reinstalled.&lt;br&gt; | [optional] [default to True]
**resolve_interval_track** | **bool** | Enables or disables tracking the &#39;Aliases Hostnames Resolve Interval&#39; value as the &#x60;resolve_internal&#x60; value instead of specifying a value directly.&lt;br&gt; | [optional] 
**resolve_interval** | **int** | The interval (in seconds) for re-resolving endpoint host/domain names.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;resolve_interval_track&#x60; must be equal to &#x60;false&#x60;&lt;br&gt; | [optional] [default to 300]
**interface_group** | **str** | Configures which WireGuard tunnels are members of the WireGuard interface group.&lt;br&gt; | [optional] [default to 'all']
**hide_secrets** | **bool** | Enables or disables hiding all secrets (private and pre-shared keys) in the user interface.&lt;br&gt; | [optional] 
**hide_peers** | **bool** | Enables or disables initially hiding all peers in the user interface.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.wire_guard_settings import WireGuardSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WireGuardSettings from a JSON string
wire_guard_settings_instance = WireGuardSettings.from_json(json)
# print the JSON string representation of the object
print(WireGuardSettings.to_json())

# convert the object into a dict
wire_guard_settings_dict = wire_guard_settings_instance.to_dict()
# create an instance of WireGuardSettings from a dict
wire_guard_settings_from_dict = WireGuardSettings.from_dict(wire_guard_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


