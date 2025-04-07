# SystemConsole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passwd_protect_console** | **bool** | Enables or disables password protecting the console.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.system_console import SystemConsole

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConsole from a JSON string
system_console_instance = SystemConsole.from_json(json)
# print the JSON string representation of the object
print(SystemConsole.to_json())

# convert the object into a dict
system_console_dict = system_console_instance.to_dict()
# create an instance of SystemConsole from a dict
system_console_from_dict = SystemConsole.from_dict(system_console_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


