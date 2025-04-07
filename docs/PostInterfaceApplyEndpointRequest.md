# PostInterfaceApplyEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; when all interfaces are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending interface changes that have not been applied.&lt;br&gt; | [optional] [readonly] 
**pending_interfaces** | **List[str]** | Displays a list of interfaces that have pending changes waiting to be applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.post_interface_apply_endpoint_request import PostInterfaceApplyEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostInterfaceApplyEndpointRequest from a JSON string
post_interface_apply_endpoint_request_instance = PostInterfaceApplyEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostInterfaceApplyEndpointRequest.to_json())

# convert the object into a dict
post_interface_apply_endpoint_request_dict = post_interface_apply_endpoint_request_instance.to_dict()
# create an instance of PostInterfaceApplyEndpointRequest from a dict
post_interface_apply_endpoint_request_from_dict = PostInterfaceApplyEndpointRequest.from_dict(post_interface_apply_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


