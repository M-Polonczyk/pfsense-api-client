# PostServicesHAProxySettingsEmailMailerEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The descriptive name for this mail server.&lt;br&gt; | 
**mailserver** | **str** | The IP or hostname of the mail server.&lt;br&gt; | 
**mailserverport** | **str** | The port used by this mail server. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '53']

## Example

```python
from pfsense_api_client.models.post_services_ha_proxy_settings_email_mailer_endpoint_request import PostServicesHAProxySettingsEmailMailerEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesHAProxySettingsEmailMailerEndpointRequest from a JSON string
post_services_ha_proxy_settings_email_mailer_endpoint_request_instance = PostServicesHAProxySettingsEmailMailerEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesHAProxySettingsEmailMailerEndpointRequest.to_json())

# convert the object into a dict
post_services_ha_proxy_settings_email_mailer_endpoint_request_dict = post_services_ha_proxy_settings_email_mailer_endpoint_request_instance.to_dict()
# create an instance of PostServicesHAProxySettingsEmailMailerEndpointRequest from a dict
post_services_ha_proxy_settings_email_mailer_endpoint_request_from_dict = PostServicesHAProxySettingsEmailMailerEndpointRequest.from_dict(post_services_ha_proxy_settings_email_mailer_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


