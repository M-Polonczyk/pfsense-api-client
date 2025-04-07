# MethodNotAllowedError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | The HTTP status code that corresponds with the API response. | [optional] [default to 405]
**status** | **str** | The HTTP status message that corresponds with the HTTP status code. | [optional] [default to 'method not allowed']
**response_id** | **str** | The unique response ID that corresponds with the result of the APIcall. In most situations, this will contain an error code. | [optional] 
**message** | **str** | The descriptive message detailing the results of the API call. | [optional] 
**data** | [**AuthenticationErrorData**](AuthenticationErrorData.md) |  | [optional] 
**links** | **object** | An array of links to resources that are related to this API response. | [optional] 

## Example

```python
from pfsense_api_client.models.method_not_allowed_error import MethodNotAllowedError

# TODO update the JSON string below
json = "{}"
# create an instance of MethodNotAllowedError from a JSON string
method_not_allowed_error_instance = MethodNotAllowedError.from_json(json)
# print the JSON string representation of the object
print(MethodNotAllowedError.to_json())

# convert the object into a dict
method_not_allowed_error_dict = method_not_allowed_error_instance.to_dict()
# create an instance of MethodNotAllowedError from a dict
method_not_allowed_error_from_dict = MethodNotAllowedError.from_dict(method_not_allowed_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


