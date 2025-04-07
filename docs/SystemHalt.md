# SystemHalt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | Run through the call but don&#39;t actually initiate a shutdown.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.system_halt import SystemHalt

# TODO update the JSON string below
json = "{}"
# create an instance of SystemHalt from a JSON string
system_halt_instance = SystemHalt.from_json(json)
# print the JSON string representation of the object
print(SystemHalt.to_json())

# convert the object into a dict
system_halt_dict = system_halt_instance.to_dict()
# create an instance of SystemHalt from a dict
system_halt_from_dict = SystemHalt.from_dict(system_halt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


