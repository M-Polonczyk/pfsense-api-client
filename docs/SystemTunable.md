# SystemTunable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tunable** | **str** | The name of the tunable to set.&lt;br&gt; | [optional] 
**value** | **str** | The value to assign this tunable.&lt;br&gt; | [optional] 
**descr** | **str** | A description for this tunable.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.system_tunable import SystemTunable

# TODO update the JSON string below
json = "{}"
# create an instance of SystemTunable from a JSON string
system_tunable_instance = SystemTunable.from_json(json)
# print the JSON string representation of the object
print(SystemTunable.to_json())

# convert the object into a dict
system_tunable_dict = system_tunable_instance.to_dict()
# create an instance of SystemTunable from a dict
system_tunable_from_dict = SystemTunable.from_dict(system_tunable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


