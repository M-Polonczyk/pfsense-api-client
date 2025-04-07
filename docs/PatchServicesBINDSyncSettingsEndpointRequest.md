# PatchServicesBINDSyncSettingsEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**synconchanges** | **str** | The sync mode to use.&lt;br&gt; | 
**synctimeout** | **int** | The timeout for the sync process.&lt;br&gt; | [optional] [default to 30]
**masterip** | **str** | The IP address of the master BIND server.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.patch_services_bind_sync_settings_endpoint_request import PatchServicesBINDSyncSettingsEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesBINDSyncSettingsEndpointRequest from a JSON string
patch_services_bind_sync_settings_endpoint_request_instance = PatchServicesBINDSyncSettingsEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesBINDSyncSettingsEndpointRequest.to_json())

# convert the object into a dict
patch_services_bind_sync_settings_endpoint_request_dict = patch_services_bind_sync_settings_endpoint_request_instance.to_dict()
# create an instance of PatchServicesBINDSyncSettingsEndpointRequest from a dict
patch_services_bind_sync_settings_endpoint_request_from_dict = PatchServicesBINDSyncSettingsEndpointRequest.from_dict(patch_services_bind_sync_settings_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


