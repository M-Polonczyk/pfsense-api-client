# ConfigHistoryRevision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **int** | The time the configuration change was made.&lt;br&gt; | [optional] 
**description** | **str** | The description of the configuration change.&lt;br&gt; | [optional] 
**version** | **str** | The configuration version associated with this change.&lt;br&gt; | [optional] 
**filesize** | **int** | The file size (in bytes) of the configuration file associated with this change.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.config_history_revision import ConfigHistoryRevision

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigHistoryRevision from a JSON string
config_history_revision_instance = ConfigHistoryRevision.from_json(json)
# print the JSON string representation of the object
print(ConfigHistoryRevision.to_json())

# convert the object into a dict
config_history_revision_dict = config_history_revision_instance.to_dict()
# create an instance of ConfigHistoryRevision from a dict
config_history_revision_from_dict = ConfigHistoryRevision.from_dict(config_history_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


