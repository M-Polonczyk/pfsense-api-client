# PostRoutingApplyEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; when all routing changes are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending routing changes that have not been applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.post_routing_apply_endpoint_request import PostRoutingApplyEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRoutingApplyEndpointRequest from a JSON string
post_routing_apply_endpoint_request_instance = PostRoutingApplyEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostRoutingApplyEndpointRequest.to_json())

# convert the object into a dict
post_routing_apply_endpoint_request_dict = post_routing_apply_endpoint_request_instance.to_dict()
# create an instance of PostRoutingApplyEndpointRequest from a dict
post_routing_apply_endpoint_request_from_dict = PostRoutingApplyEndpointRequest.from_dict(post_routing_apply_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


