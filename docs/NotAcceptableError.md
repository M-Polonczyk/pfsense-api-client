# NotAcceptableError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | The HTTP status code that corresponds with the API response. | [optional] [default to 406]
**status** | **str** | The HTTP status message that corresponds with the HTTP status code. | [optional] [default to 'not acceptable']
**response_id** | **str** | The unique response ID that corresponds with the result of the APIcall. In most situations, this will contain an error code. | [optional] 
**message** | **str** | The descriptive message detailing the results of the API call. | [optional] 
**data** | [**AuthenticationErrorData**](AuthenticationErrorData.md) |  | [optional] 
**links** | **object** | An array of links to resources that are related to this API response. | [optional] 

## Example

```python
from pfsense_api_client.models.not_acceptable_error import NotAcceptableError

# TODO update the JSON string below
json = "{}"
# create an instance of NotAcceptableError from a JSON string
not_acceptable_error_instance = NotAcceptableError.from_json(json)
# print the JSON string representation of the object
print(NotAcceptableError.to_json())

# convert the object into a dict
not_acceptable_error_dict = not_acceptable_error_instance.to_dict()
# create an instance of NotAcceptableError from a dict
not_acceptable_error_from_dict = NotAcceptableError.from_dict(not_acceptable_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


