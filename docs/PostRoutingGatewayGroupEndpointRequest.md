# PostRoutingGatewayGroupEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the gateway group.&lt;br&gt; | 
**trigger** | **str** | The trigger that will cause a gateway to be excluded from the group.&lt;br&gt; | [optional] [default to 'down']
**descr** | **str** | A description of the gateway group.&lt;br&gt; | [optional] 
**ipprotocol** | **str** | The assumed IP protocol of the gateways in this group.&lt;br&gt; | [optional] [readonly] [default to 'unknown']
**priorities** | [**List[RoutingGatewayGroupPrioritiesInner]**](RoutingGatewayGroupPrioritiesInner.md) | The priorities of the gateways in this group.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.post_routing_gateway_group_endpoint_request import PostRoutingGatewayGroupEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRoutingGatewayGroupEndpointRequest from a JSON string
post_routing_gateway_group_endpoint_request_instance = PostRoutingGatewayGroupEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostRoutingGatewayGroupEndpointRequest.to_json())

# convert the object into a dict
post_routing_gateway_group_endpoint_request_dict = post_routing_gateway_group_endpoint_request_instance.to_dict()
# create an instance of PostRoutingGatewayGroupEndpointRequest from a dict
post_routing_gateway_group_endpoint_request_from_dict = PostRoutingGatewayGroupEndpointRequest.from_dict(post_routing_gateway_group_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


