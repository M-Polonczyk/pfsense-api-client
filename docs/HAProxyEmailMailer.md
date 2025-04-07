# HAProxyEmailMailer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The descriptive name for this mail server.&lt;br&gt; | [optional] 
**mailserver** | **str** | The IP or hostname of the mail server.&lt;br&gt; | [optional] 
**mailserverport** | **str** | The port used by this mail server. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '53']

## Example

```python
from pfsense_api_client.models.ha_proxy_email_mailer import HAProxyEmailMailer

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxyEmailMailer from a JSON string
ha_proxy_email_mailer_instance = HAProxyEmailMailer.from_json(json)
# print the JSON string representation of the object
print(HAProxyEmailMailer.to_json())

# convert the object into a dict
ha_proxy_email_mailer_dict = ha_proxy_email_mailer_instance.to_dict()
# create an instance of HAProxyEmailMailer from a dict
ha_proxy_email_mailer_from_dict = HAProxyEmailMailer.from_dict(ha_proxy_email_mailer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


