# PostDiagnosticsCommandPromptEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | The command to be executed.&lt;br&gt; | 
**output** | **str** | The output of the executed command.&lt;br&gt; | [optional] [readonly] 
**result_code** | **int** | The result code of the executed command.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.post_diagnostics_command_prompt_endpoint_request import PostDiagnosticsCommandPromptEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDiagnosticsCommandPromptEndpointRequest from a JSON string
post_diagnostics_command_prompt_endpoint_request_instance = PostDiagnosticsCommandPromptEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostDiagnosticsCommandPromptEndpointRequest.to_json())

# convert the object into a dict
post_diagnostics_command_prompt_endpoint_request_dict = post_diagnostics_command_prompt_endpoint_request_instance.to_dict()
# create an instance of PostDiagnosticsCommandPromptEndpointRequest from a dict
post_diagnostics_command_prompt_endpoint_request_from_dict = PostDiagnosticsCommandPromptEndpointRequest.from_dict(post_diagnostics_command_prompt_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


