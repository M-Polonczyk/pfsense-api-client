# UnprocessableContentError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | The HTTP status code that corresponds with the API response. | [optional] [default to 422]
**status** | **str** | The HTTP status message that corresponds with the HTTP status code. | [optional] [default to 'unprocessable entity']
**response_id** | **str** | The unique response ID that corresponds with the result of the APIcall. In most situations, this will contain an error code. | [optional] 
**message** | **str** | The descriptive message detailing the results of the API call. | [optional] 
**data** | [**AuthenticationErrorData**](AuthenticationErrorData.md) |  | [optional] 
**links** | **object** | An array of links to resources that are related to this API response. | [optional] 

## Example

```python
from pfsense_api_client.models.unprocessable_content_error import UnprocessableContentError

# TODO update the JSON string below
json = "{}"
# create an instance of UnprocessableContentError from a JSON string
unprocessable_content_error_instance = UnprocessableContentError.from_json(json)
# print the JSON string representation of the object
print(UnprocessableContentError.to_json())

# convert the object into a dict
unprocessable_content_error_dict = unprocessable_content_error_instance.to_dict()
# create an instance of UnprocessableContentError from a dict
unprocessable_content_error_from_dict = UnprocessableContentError.from_dict(unprocessable_content_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


