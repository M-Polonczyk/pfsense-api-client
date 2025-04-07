# PatchServicesHAProxySettingsEmailMailerEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The descriptive name for this mail server.&lt;br&gt; | [optional] 
**mailserver** | **str** | The IP or hostname of the mail server.&lt;br&gt; | [optional] 
**mailserverport** | **str** | The port used by this mail server. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '53']
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_ha_proxy_settings_email_mailer_endpoint_request import PatchServicesHAProxySettingsEmailMailerEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesHAProxySettingsEmailMailerEndpointRequest from a JSON string
patch_services_ha_proxy_settings_email_mailer_endpoint_request_instance = PatchServicesHAProxySettingsEmailMailerEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesHAProxySettingsEmailMailerEndpointRequest.to_json())

# convert the object into a dict
patch_services_ha_proxy_settings_email_mailer_endpoint_request_dict = patch_services_ha_proxy_settings_email_mailer_endpoint_request_instance.to_dict()
# create an instance of PatchServicesHAProxySettingsEmailMailerEndpointRequest from a dict
patch_services_ha_proxy_settings_email_mailer_endpoint_request_from_dict = PatchServicesHAProxySettingsEmailMailerEndpointRequest.from_dict(patch_services_ha_proxy_settings_email_mailer_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


