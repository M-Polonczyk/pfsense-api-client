# BINDSyncSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**synconchanges** | **str** | The sync mode to use.&lt;br&gt; | [optional] 
**synctimeout** | **int** | The timeout for the sync process.&lt;br&gt; | [optional] [default to 30]
**masterip** | **str** | The IP address of the master BIND server.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.bind_sync_settings import BINDSyncSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BINDSyncSettings from a JSON string
bind_sync_settings_instance = BINDSyncSettings.from_json(json)
# print the JSON string representation of the object
print(BINDSyncSettings.to_json())

# convert the object into a dict
bind_sync_settings_dict = bind_sync_settings_instance.to_dict()
# create an instance of BINDSyncSettings from a dict
bind_sync_settings_from_dict = BINDSyncSettings.from_dict(bind_sync_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


