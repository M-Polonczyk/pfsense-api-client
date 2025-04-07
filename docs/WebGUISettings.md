# WebGUISettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | The protocol to use for the web GUI.&lt;br&gt; | [optional] [default to 'https']
**port** | **str** | The port on which the web GUI listens. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '443']
**sslcertref** | **str** | The SSL/TLS certificate to use for the web GUI.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.web_gui_settings import WebGUISettings

# TODO update the JSON string below
json = "{}"
# create an instance of WebGUISettings from a JSON string
web_gui_settings_instance = WebGUISettings.from_json(json)
# print the JSON string representation of the object
print(WebGUISettings.to_json())

# convert the object into a dict
web_gui_settings_dict = web_gui_settings_instance.to_dict()
# create an instance of WebGUISettings from a dict
web_gui_settings_from_dict = WebGUISettings.from_dict(web_gui_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


