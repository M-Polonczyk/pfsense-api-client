# PatchSystemWebGUISettingsEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | The protocol to use for the web GUI.&lt;br&gt; | [optional] [default to 'https']
**port** | **str** | The port on which the web GUI listens. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '443']
**sslcertref** | **str** | The SSL/TLS certificate to use for the web GUI.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.patch_system_web_gui_settings_endpoint_request import PatchSystemWebGUISettingsEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSystemWebGUISettingsEndpointRequest from a JSON string
patch_system_web_gui_settings_endpoint_request_instance = PatchSystemWebGUISettingsEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchSystemWebGUISettingsEndpointRequest.to_json())

# convert the object into a dict
patch_system_web_gui_settings_endpoint_request_dict = patch_system_web_gui_settings_endpoint_request_instance.to_dict()
# create an instance of PatchSystemWebGUISettingsEndpointRequest from a dict
patch_system_web_gui_settings_endpoint_request_from_dict = PatchSystemWebGUISettingsEndpointRequest.from_dict(patch_system_web_gui_settings_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


