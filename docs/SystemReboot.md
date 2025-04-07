# SystemReboot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | Run through the call but don&#39;t actually initiate a reboot.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.system_reboot import SystemReboot

# TODO update the JSON string below
json = "{}"
# create an instance of SystemReboot from a JSON string
system_reboot_instance = SystemReboot.from_json(json)
# print the JSON string representation of the object
print(SystemReboot.to_json())

# convert the object into a dict
system_reboot_dict = system_reboot_instance.to_dict()
# create an instance of SystemReboot from a dict
system_reboot_from_dict = SystemReboot.from_dict(system_reboot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


