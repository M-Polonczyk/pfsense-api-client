# RoutingGatewayGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the gateway group.&lt;br&gt; | [optional] 
**trigger** | **str** | The trigger that will cause a gateway to be excluded from the group.&lt;br&gt; | [optional] [default to 'down']
**descr** | **str** | A description of the gateway group.&lt;br&gt; | [optional] 
**ipprotocol** | **str** | The assumed IP protocol of the gateways in this group.&lt;br&gt; | [optional] [readonly] [default to 'unknown']
**priorities** | [**List[RoutingGatewayGroupPrioritiesInner]**](RoutingGatewayGroupPrioritiesInner.md) | The priorities of the gateways in this group.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.routing_gateway_group import RoutingGatewayGroup

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingGatewayGroup from a JSON string
routing_gateway_group_instance = RoutingGatewayGroup.from_json(json)
# print the JSON string representation of the object
print(RoutingGatewayGroup.to_json())

# convert the object into a dict
routing_gateway_group_dict = routing_gateway_group_instance.to_dict()
# create an instance of RoutingGatewayGroup from a dict
routing_gateway_group_from_dict = RoutingGatewayGroup.from_dict(routing_gateway_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


