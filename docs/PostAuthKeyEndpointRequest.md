# PostAuthKeyEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descr** | **str** | Sets a description for this API key. This is used to identify the key&#39;s purpose and cannot be changed once created.&lt;br&gt; | [optional] 
**username** | **str** | The username this API key is issued to.&lt;br&gt; | [optional] [readonly] 
**hash_algo** | **str** | The hash algorithm used for this API key. It is recommended to increase the strength of the algorithm for keys assigned to privileged users.&lt;br&gt; | [optional] [default to 'sha256']
**length_bytes** | **int** | The length of the API key (in bytes). Greater key lengths provide greater security, but also increase the number of characters used in the key string.&lt;br&gt; | [optional] [default to 24]
**hash** | **str** | The hash of the generated API key&lt;br&gt; | [optional] 
**key** | **str** | The real API key. This value is not stored internally and cannot be recovered if lost.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_auth_key_endpoint_request import PostAuthKeyEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthKeyEndpointRequest from a JSON string
post_auth_key_endpoint_request_instance = PostAuthKeyEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostAuthKeyEndpointRequest.to_json())

# convert the object into a dict
post_auth_key_endpoint_request_dict = post_auth_key_endpoint_request_instance.to_dict()
# create an instance of PostAuthKeyEndpointRequest from a dict
post_auth_key_endpoint_request_from_dict = PostAuthKeyEndpointRequest.from_dict(post_auth_key_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


