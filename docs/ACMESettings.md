# ACMESettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enables or disables the ACME renewal job.&lt;br&gt; | [optional] 
**writecerts** | **bool** | Enables or disables the writing of certificates to /conf/acme/ in various formats for use by other scripts or daemons which do not integrate with the pfSense certificate manager.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.acme_settings import ACMESettings

# TODO update the JSON string below
json = "{}"
# create an instance of ACMESettings from a JSON string
acme_settings_instance = ACMESettings.from_json(json)
# print the JSON string representation of the object
print(ACMESettings.to_json())

# convert the object into a dict
acme_settings_dict = acme_settings_instance.to_dict()
# create an instance of ACMESettings from a dict
acme_settings_from_dict = ACMESettings.from_dict(acme_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


