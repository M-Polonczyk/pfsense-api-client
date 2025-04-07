# CommandPrompt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | The command to be executed.&lt;br&gt; | [optional] 
**output** | **str** | The output of the executed command.&lt;br&gt; | [optional] [readonly] 
**result_code** | **int** | The result code of the executed command.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.command_prompt import CommandPrompt

# TODO update the JSON string below
json = "{}"
# create an instance of CommandPrompt from a JSON string
command_prompt_instance = CommandPrompt.from_json(json)
# print the JSON string representation of the object
print(CommandPrompt.to_json())

# convert the object into a dict
command_prompt_dict = command_prompt_instance.to_dict()
# create an instance of CommandPrompt from a dict
command_prompt_from_dict = CommandPrompt.from_dict(command_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


