# FailedDependencyError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | The HTTP status code that corresponds with the API response. | [optional] [default to 424]
**status** | **str** | The HTTP status message that corresponds with the HTTP status code. | [optional] [default to 'failed dependency']
**response_id** | **str** | The unique response ID that corresponds with the result of the APIcall. In most situations, this will contain an error code. | [optional] 
**message** | **str** | The descriptive message detailing the results of the API call. | [optional] 
**data** | [**AuthenticationErrorData**](AuthenticationErrorData.md) |  | [optional] 
**links** | **object** | An array of links to resources that are related to this API response. | [optional] 

## Example

```python
from pfsense_api_client.models.failed_dependency_error import FailedDependencyError

# TODO update the JSON string below
json = "{}"
# create an instance of FailedDependencyError from a JSON string
failed_dependency_error_instance = FailedDependencyError.from_json(json)
# print the JSON string representation of the object
print(FailedDependencyError.to_json())

# convert the object into a dict
failed_dependency_error_dict = failed_dependency_error_instance.to_dict()
# create an instance of FailedDependencyError from a dict
failed_dependency_error_from_dict = FailedDependencyError.from_dict(failed_dependency_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


