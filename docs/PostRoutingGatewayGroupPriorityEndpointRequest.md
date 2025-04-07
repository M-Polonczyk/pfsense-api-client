# PostRoutingGatewayGroupPriorityEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** | The name of the gateway to prioritize in this gateway group.&lt;br&gt; | 
**tier** | **int** | The priority of this gateway in the group. Lower numbered tiers are higher priority.&lt;br&gt; | 
**virtual_ip** | **str** | The virtual IP to use for this gateway group. Use &#x60;address&#x60; to use the interface&#39;s current IP.&lt;br&gt; | [optional] [default to 'address']
**parent_id** | **int** | The ID of the parent this object is nested under. | 

## Example

```python
from pfsense_api_client.models.post_routing_gateway_group_priority_endpoint_request import PostRoutingGatewayGroupPriorityEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRoutingGatewayGroupPriorityEndpointRequest from a JSON string
post_routing_gateway_group_priority_endpoint_request_instance = PostRoutingGatewayGroupPriorityEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostRoutingGatewayGroupPriorityEndpointRequest.to_json())

# convert the object into a dict
post_routing_gateway_group_priority_endpoint_request_dict = post_routing_gateway_group_priority_endpoint_request_instance.to_dict()
# create an instance of PostRoutingGatewayGroupPriorityEndpointRequest from a dict
post_routing_gateway_group_priority_endpoint_request_from_dict = PostRoutingGatewayGroupPriorityEndpointRequest.from_dict(post_routing_gateway_group_priority_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


