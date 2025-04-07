# PatchSystemConsoleEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passwd_protect_console** | **bool** | Enables or disables password protecting the console.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.patch_system_console_endpoint_request import PatchSystemConsoleEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSystemConsoleEndpointRequest from a JSON string
patch_system_console_endpoint_request_instance = PatchSystemConsoleEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchSystemConsoleEndpointRequest.to_json())

# convert the object into a dict
patch_system_console_endpoint_request_dict = patch_system_console_endpoint_request_instance.to_dict()
# create an instance of PatchSystemConsoleEndpointRequest from a dict
patch_system_console_endpoint_request_from_dict = PatchSystemConsoleEndpointRequest.from_dict(patch_system_console_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


