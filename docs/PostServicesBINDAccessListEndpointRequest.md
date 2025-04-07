# PostServicesBINDAccessListEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the access list.&lt;br&gt; | 
**description** | **str** | A description for the access list.&lt;br&gt; | [optional] 
**entries** | [**List[BINDAccessListEntriesInner]**](BINDAccessListEntriesInner.md) | The network entries for this access list.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.post_services_bind_access_list_endpoint_request import PostServicesBINDAccessListEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesBINDAccessListEndpointRequest from a JSON string
post_services_bind_access_list_endpoint_request_instance = PostServicesBINDAccessListEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesBINDAccessListEndpointRequest.to_json())

# convert the object into a dict
post_services_bind_access_list_endpoint_request_dict = post_services_bind_access_list_endpoint_request_instance.to_dict()
# create an instance of PostServicesBINDAccessListEndpointRequest from a dict
post_services_bind_access_list_endpoint_request_from_dict = PostServicesBINDAccessListEndpointRequest.from_dict(post_services_bind_access_list_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


