# PatchRoutingGatewayGroupPriorityEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** | The name of the gateway to prioritize in this gateway group.&lt;br&gt; | [optional] 
**tier** | **int** | The priority of this gateway in the group. Lower numbered tiers are higher priority.&lt;br&gt; | [optional] 
**virtual_ip** | **str** | The virtual IP to use for this gateway group. Use &#x60;address&#x60; to use the interface&#39;s current IP.&lt;br&gt; | [optional] [default to 'address']
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_routing_gateway_group_priority_endpoint_request import PatchRoutingGatewayGroupPriorityEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchRoutingGatewayGroupPriorityEndpointRequest from a JSON string
patch_routing_gateway_group_priority_endpoint_request_instance = PatchRoutingGatewayGroupPriorityEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchRoutingGatewayGroupPriorityEndpointRequest.to_json())

# convert the object into a dict
patch_routing_gateway_group_priority_endpoint_request_dict = patch_routing_gateway_group_priority_endpoint_request_instance.to_dict()
# create an instance of PatchRoutingGatewayGroupPriorityEndpointRequest from a dict
patch_routing_gateway_group_priority_endpoint_request_from_dict = PatchRoutingGatewayGroupPriorityEndpointRequest.from_dict(patch_routing_gateway_group_priority_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


