# PostAuthJWTEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The generated JWT that can be used for JWT authentication.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.post_auth_jwt_endpoint_request import PostAuthJWTEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthJWTEndpointRequest from a JSON string
post_auth_jwt_endpoint_request_instance = PostAuthJWTEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostAuthJWTEndpointRequest.to_json())

# convert the object into a dict
post_auth_jwt_endpoint_request_dict = post_auth_jwt_endpoint_request_instance.to_dict()
# create an instance of PostAuthJWTEndpointRequest from a dict
post_auth_jwt_endpoint_request_from_dict = PostAuthJWTEndpointRequest.from_dict(post_auth_jwt_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


