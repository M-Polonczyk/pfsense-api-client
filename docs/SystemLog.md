# SystemLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The raw text of the system log entry.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.system_log import SystemLog

# TODO update the JSON string below
json = "{}"
# create an instance of SystemLog from a JSON string
system_log_instance = SystemLog.from_json(json)
# print the JSON string representation of the object
print(SystemLog.to_json())

# convert the object into a dict
system_log_dict = system_log_instance.to_dict()
# create an instance of SystemLog from a dict
system_log_from_dict = SystemLog.from_dict(system_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


