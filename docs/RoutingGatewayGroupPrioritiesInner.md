# RoutingGatewayGroupPrioritiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** | The name of the gateway to prioritize in this gateway group.&lt;br&gt; | 
**tier** | **int** | The priority of this gateway in the group. Lower numbered tiers are higher priority.&lt;br&gt; | 
**virtual_ip** | **str** | The virtual IP to use for this gateway group. Use &#x60;address&#x60; to use the interface&#39;s current IP.&lt;br&gt; | [optional] [default to 'address']

## Example

```python
from pfsense_api_client.models.routing_gateway_group_priorities_inner import RoutingGatewayGroupPrioritiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingGatewayGroupPrioritiesInner from a JSON string
routing_gateway_group_priorities_inner_instance = RoutingGatewayGroupPrioritiesInner.from_json(json)
# print the JSON string representation of the object
print(RoutingGatewayGroupPrioritiesInner.to_json())

# convert the object into a dict
routing_gateway_group_priorities_inner_dict = routing_gateway_group_priorities_inner_instance.to_dict()
# create an instance of RoutingGatewayGroupPrioritiesInner from a dict
routing_gateway_group_priorities_inner_from_dict = RoutingGatewayGroupPrioritiesInner.from_dict(routing_gateway_group_priorities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


