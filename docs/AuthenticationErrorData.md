# AuthenticationErrorData

The data requested from the API. In the event that many objects havebeen requested, this field will be an array of objects. Otherwise, it will only returnthe single object requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from pfsense_api_client.models.authentication_error_data import AuthenticationErrorData

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationErrorData from a JSON string
authentication_error_data_instance = AuthenticationErrorData.from_json(json)
# print the JSON string representation of the object
print(AuthenticationErrorData.to_json())

# convert the object into a dict
authentication_error_data_dict = authentication_error_data_instance.to_dict()
# create an instance of AuthenticationErrorData from a dict
authentication_error_data_from_dict = AuthenticationErrorData.from_dict(authentication_error_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


