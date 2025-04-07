# PostDiagnosticsHaltSystemEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | Run through the call but don&#39;t actually initiate a shutdown.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_diagnostics_halt_system_endpoint_request import PostDiagnosticsHaltSystemEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDiagnosticsHaltSystemEndpointRequest from a JSON string
post_diagnostics_halt_system_endpoint_request_instance = PostDiagnosticsHaltSystemEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostDiagnosticsHaltSystemEndpointRequest.to_json())

# convert the object into a dict
post_diagnostics_halt_system_endpoint_request_dict = post_diagnostics_halt_system_endpoint_request_instance.to_dict()
# create an instance of PostDiagnosticsHaltSystemEndpointRequest from a dict
post_diagnostics_halt_system_endpoint_request_from_dict = PostDiagnosticsHaltSystemEndpointRequest.from_dict(post_diagnostics_halt_system_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


