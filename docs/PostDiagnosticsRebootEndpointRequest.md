# PostDiagnosticsRebootEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | Run through the call but don&#39;t actually initiate a reboot.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_diagnostics_reboot_endpoint_request import PostDiagnosticsRebootEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDiagnosticsRebootEndpointRequest from a JSON string
post_diagnostics_reboot_endpoint_request_instance = PostDiagnosticsRebootEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostDiagnosticsRebootEndpointRequest.to_json())

# convert the object into a dict
post_diagnostics_reboot_endpoint_request_dict = post_diagnostics_reboot_endpoint_request_instance.to_dict()
# create an instance of PostDiagnosticsRebootEndpointRequest from a dict
post_diagnostics_reboot_endpoint_request_from_dict = PostDiagnosticsRebootEndpointRequest.from_dict(post_diagnostics_reboot_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


