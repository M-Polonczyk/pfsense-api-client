# PatchSystemNotificationsEmailSettingsEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable** | **bool** | Disables SMTP notifications.&lt;br&gt; | [optional] 
**ipaddress** | **str** | The IP address or hostname of the SMTP server.&lt;br&gt; | [optional] 
**port** | **str** | The port number of the SMTP server. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '25']
**timeout** | **int** | The timeout (in seconds) for the SMTP connection.&lt;br&gt; | [optional] [default to 20]
**ssl** | **bool** | Enables or disables SSL/TLS for the SMTP connection.&lt;br&gt; | [optional] 
**sslvalidate** | **bool** | Enables or disables SSL/TLS certificate validation for the SMTP connection.&lt;br&gt; | [optional] [default to True]
**fromaddress** | **str** | The email address to use as the \&quot;From\&quot; address in notifications.&lt;br&gt; | [optional] 
**notifyemailaddress** | **str** | The email address to send notifications to.&lt;br&gt; | [optional] 
**authentication_mechanism** | **str** | The authentication mechanism to use for the SMTP connection.&lt;br&gt; | [optional] [default to 'PLAIN']
**username** | **str** | The username to use for SMTP authentication.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;authentication_mechanism&#x60; must be equal to &#x60;&#39;LOGIN&#39;&#x60;&lt;br&gt; | 
**password** | **str** | The password to use for SMTP authentication.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;authentication_mechanism&#x60; must be equal to &#x60;&#39;LOGIN&#39;&#x60;&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.patch_system_notifications_email_settings_endpoint_request import PatchSystemNotificationsEmailSettingsEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSystemNotificationsEmailSettingsEndpointRequest from a JSON string
patch_system_notifications_email_settings_endpoint_request_instance = PatchSystemNotificationsEmailSettingsEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchSystemNotificationsEmailSettingsEndpointRequest.to_json())

# convert the object into a dict
patch_system_notifications_email_settings_endpoint_request_dict = patch_system_notifications_email_settings_endpoint_request_instance.to_dict()
# create an instance of PatchSystemNotificationsEmailSettingsEndpointRequest from a dict
patch_system_notifications_email_settings_endpoint_request_from_dict = PatchSystemNotificationsEmailSettingsEndpointRequest.from_dict(patch_system_notifications_email_settings_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


