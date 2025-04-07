# PostServicesBINDViewEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the view.&lt;br&gt; | 
**descr** | **str** | A description for the view.&lt;br&gt; | [optional] 
**recursion** | **bool** | Enables or disables recursion for the view.&lt;br&gt; | [optional] 
**match_clients** | **List[str]** | The access lists to match clients against.&lt;br&gt; | [optional] 
**allow_recursion** | **List[str]** | The access lists to allow recursion for.&lt;br&gt; | [optional] 
**bind_custom_options** | **str** | Custom BIND options for the view.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_services_bind_view_endpoint_request import PostServicesBINDViewEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesBINDViewEndpointRequest from a JSON string
post_services_bind_view_endpoint_request_instance = PostServicesBINDViewEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesBINDViewEndpointRequest.to_json())

# convert the object into a dict
post_services_bind_view_endpoint_request_dict = post_services_bind_view_endpoint_request_instance.to_dict()
# create an instance of PostServicesBINDViewEndpointRequest from a dict
post_services_bind_view_endpoint_request_from_dict = PostServicesBINDViewEndpointRequest.from_dict(post_services_bind_view_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


