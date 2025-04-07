# RESTAPISettingsSync


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_data** | **str** | The serialized REST API settings data to be synced.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.restapi_settings_sync import RESTAPISettingsSync

# TODO update the JSON string below
json = "{}"
# create an instance of RESTAPISettingsSync from a JSON string
restapi_settings_sync_instance = RESTAPISettingsSync.from_json(json)
# print the JSON string representation of the object
print(RESTAPISettingsSync.to_json())

# convert the object into a dict
restapi_settings_sync_dict = restapi_settings_sync_instance.to_dict()
# create an instance of RESTAPISettingsSync from a dict
restapi_settings_sync_from_dict = RESTAPISettingsSync.from_dict(restapi_settings_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


