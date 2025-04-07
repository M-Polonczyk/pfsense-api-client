# PostInterfaceGroupEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ifname** | **str** | The name of this interface group.&lt;br&gt; | 
**members** | **List[str]** | The member interfaces to assign to this interface group.&lt;br&gt; | [optional] 
**descr** | **str** | The description for this interface group.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_interface_group_endpoint_request import PostInterfaceGroupEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostInterfaceGroupEndpointRequest from a JSON string
post_interface_group_endpoint_request_instance = PostInterfaceGroupEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostInterfaceGroupEndpointRequest.to_json())

# convert the object into a dict
post_interface_group_endpoint_request_dict = post_interface_group_endpoint_request_instance.to_dict()
# create an instance of PostInterfaceGroupEndpointRequest from a dict
post_interface_group_endpoint_request_from_dict = PostInterfaceGroupEndpointRequest.from_dict(post_interface_group_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


