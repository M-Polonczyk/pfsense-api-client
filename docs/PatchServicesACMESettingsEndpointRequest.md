# PatchServicesACMESettingsEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enables or disables the ACME renewal job.&lt;br&gt; | [optional] 
**writecerts** | **bool** | Enables or disables the writing of certificates to /conf/acme/ in various formats for use by other scripts or daemons which do not integrate with the pfSense certificate manager.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.patch_services_acme_settings_endpoint_request import PatchServicesACMESettingsEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesACMESettingsEndpointRequest from a JSON string
patch_services_acme_settings_endpoint_request_instance = PatchServicesACMESettingsEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesACMESettingsEndpointRequest.to_json())

# convert the object into a dict
patch_services_acme_settings_endpoint_request_dict = patch_services_acme_settings_endpoint_request_instance.to_dict()
# create an instance of PatchServicesACMESettingsEndpointRequest from a dict
patch_services_acme_settings_endpoint_request_from_dict = PatchServicesACMESettingsEndpointRequest.from_dict(patch_services_acme_settings_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


