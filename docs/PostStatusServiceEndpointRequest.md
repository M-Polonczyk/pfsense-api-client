# PostStatusServiceEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The internal name of the service.&lt;br&gt; | [optional] [readonly] 
**action** | **str** | The action to perform against this service.&lt;br&gt; | [optional] 
**description** | **str** | The full descriptive name of the service.&lt;br&gt; | [optional] [readonly] 
**enabled** | **bool** | Indicates if the service is enabled.&lt;br&gt; | [optional] [readonly] 
**status** | **bool** | Indicates if the service is actively running.&lt;br&gt; | [optional] [readonly] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.post_status_service_endpoint_request import PostStatusServiceEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostStatusServiceEndpointRequest from a JSON string
post_status_service_endpoint_request_instance = PostStatusServiceEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostStatusServiceEndpointRequest.to_json())

# convert the object into a dict
post_status_service_endpoint_request_dict = post_status_service_endpoint_request_instance.to_dict()
# create an instance of PostStatusServiceEndpointRequest from a dict
post_status_service_endpoint_request_from_dict = PostStatusServiceEndpointRequest.from_dict(post_status_service_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


