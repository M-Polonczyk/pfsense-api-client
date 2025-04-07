# PostServicesBINDAccessListEntryEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The network CIDR to allow.&lt;br&gt; | 
**description** | **str** | A description of the access list entry.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 

## Example

```python
from pfsense_api_client.models.post_services_bind_access_list_entry_endpoint_request import PostServicesBINDAccessListEntryEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesBINDAccessListEntryEndpointRequest from a JSON string
post_services_bind_access_list_entry_endpoint_request_instance = PostServicesBINDAccessListEntryEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesBINDAccessListEntryEndpointRequest.to_json())

# convert the object into a dict
post_services_bind_access_list_entry_endpoint_request_dict = post_services_bind_access_list_entry_endpoint_request_instance.to_dict()
# create an instance of PostServicesBINDAccessListEntryEndpointRequest from a dict
post_services_bind_access_list_entry_endpoint_request_from_dict = PostServicesBINDAccessListEntryEndpointRequest.from_dict(post_services_bind_access_list_entry_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


