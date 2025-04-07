# PostSystemRESTAPISettingsSyncEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_data** | **str** | The serialized REST API settings data to be synced.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.post_system_restapi_settings_sync_endpoint_request import PostSystemRESTAPISettingsSyncEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSystemRESTAPISettingsSyncEndpointRequest from a JSON string
post_system_restapi_settings_sync_endpoint_request_instance = PostSystemRESTAPISettingsSyncEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostSystemRESTAPISettingsSyncEndpointRequest.to_json())

# convert the object into a dict
post_system_restapi_settings_sync_endpoint_request_dict = post_system_restapi_settings_sync_endpoint_request_instance.to_dict()
# create an instance of PostSystemRESTAPISettingsSyncEndpointRequest from a dict
post_system_restapi_settings_sync_endpoint_request_from_dict = PostSystemRESTAPISettingsSyncEndpointRequest.from_dict(post_system_restapi_settings_sync_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


