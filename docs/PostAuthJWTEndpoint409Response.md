# PostAuthJWTEndpoint409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | The HTTP status code that corresponds with the API response. | [optional] [default to 409]
**status** | **str** | The HTTP status message that corresponds with the HTTP status code. | [optional] [default to 'conflict']
**response_id** | **str** | The unique response ID that corresponds with the result of the APIcall. In most situations, this will contain an error code. | [optional] 
**message** | **str** | The descriptive message detailing the results of the API call. | [optional] 
**data** | [**PostAuthJWTEndpoint401ResponseAllOfData**](PostAuthJWTEndpoint401ResponseAllOfData.md) |  | [optional] 
**links** | **object** | An array of links to resources that are related to this API response. | [optional] 

## Example

```python
from pfsense_api_client.models.post_auth_jwt_endpoint409_response import PostAuthJWTEndpoint409Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthJWTEndpoint409Response from a JSON string
post_auth_jwt_endpoint409_response_instance = PostAuthJWTEndpoint409Response.from_json(json)
# print the JSON string representation of the object
print(PostAuthJWTEndpoint409Response.to_json())

# convert the object into a dict
post_auth_jwt_endpoint409_response_dict = post_auth_jwt_endpoint409_response_instance.to_dict()
# create an instance of PostAuthJWTEndpoint409Response from a dict
post_auth_jwt_endpoint409_response_from_dict = PostAuthJWTEndpoint409Response.from_dict(post_auth_jwt_endpoint409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


