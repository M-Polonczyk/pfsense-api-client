# RESTAPIJWT


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The generated JWT that can be used for JWT authentication.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.restapijwt import RESTAPIJWT

# TODO update the JSON string below
json = "{}"
# create an instance of RESTAPIJWT from a JSON string
restapijwt_instance = RESTAPIJWT.from_json(json)
# print the JSON string representation of the object
print(RESTAPIJWT.to_json())

# convert the object into a dict
restapijwt_dict = restapijwt_instance.to_dict()
# create an instance of RESTAPIJWT from a dict
restapijwt_from_dict = RESTAPIJWT.from_dict(restapijwt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


