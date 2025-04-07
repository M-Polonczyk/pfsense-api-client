# PatchRoutingGatewayEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sets a name for the gateway.&lt;br&gt; | [optional] 
**descr** | **str** | Sets a descriptions for the gateway.&lt;br&gt; | [optional] 
**disabled** | **bool** | Disable this gateway.&lt;br&gt; | [optional] 
**ipprotocol** | **str** | Sets the Internet Protocol version this gateway uses.&lt;br&gt; | [optional] 
**interface** | **str** | Sets the interface this gateway will apply to.&lt;br&gt; | [optional] 
**gateway** | **str** | Sets the IP address of the remote gateway.&lt;br&gt; | [optional] 
**monitor_disable** | **bool** | Disable gateway monitoring for this gateway.&lt;br&gt; | [optional] 
**monitor** | **str** | Sets a different IP address to use when monitoring this gateway. This is typically only                 necessary if the gateway IP does not accept ICMP probes.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;monitor_disable&#x60; must be equal to &#x60;false&#x60;&lt;br&gt; | [optional] 
**action_disable** | **bool** | Disable actions from taking place when gateway events occur. The gateway will always be                 considered up.&lt;br&gt; | [optional] 
**force_down** | **bool** | Always consider this gateway to be up.&lt;br&gt; | [optional] 
**dpinger_dont_add_static_route** | **bool** | Prevents gateway monitoring from adding a static route for this gateway&#39;s monitor IP.&lt;br&gt; | [optional] 
**gw_down_kill_states** | **str** | Controls the state killing behavior when this specific gateway goes down. Killing states for specific down gateways only affects states created by policy routing rules and reply-to. Has no effect if gateway monitoring or its action are disabled or if the gateway is forced down. May not have any effect on dynamic gateways during a link loss event.&lt;br&gt; | [optional] 
**nonlocalgateway** | **bool** | Allows or disallows gateway IPs that are not a part of the parent interface&#39;s subnet(s).&lt;br&gt; | [optional] [default to True]
**weight** | **int** | Sets the weight for this gateway when used in a Gateway Group.&lt;br&gt; | [optional] [default to 1]
**data_payload** | **int** | Sets the data payload to send in ICMP packets to gateway monitor IP.&lt;br&gt; | [optional] [default to 1]
**latencylow** | **int** | Sets the threshold to consider latency as low.&lt;br&gt; | [optional] [default to 200]
**latencyhigh** | **int** | Sets the threshold to consider latency as high. This value must be greater than &#x60;latencylow&#x60;.&lt;br&gt; | [optional] [default to 500]
**losslow** | **int** | Sets the threshold to consider packet loss as low.&lt;br&gt; | [optional] [default to 10]
**losshigh** | **int** | Sets the threshold to consider packet loss as high. This value must be greater than &#x60;losslow&#x60;.&lt;br&gt; | [optional] [default to 20]
**interval** | **int** | Sets how often ICMP probes will be sent in milliseconds.&lt;br&gt; | [optional] [default to 500]
**loss_interval** | **int** | Sets the time interval in milliseconds before packets are treated as lost.&lt;br&gt; | [optional] [default to 2000]
**time_period** | **int** | Sets the time period in milliseconds over which results are averaged.&lt;br&gt; | [optional] [default to 60000]
**alert_interval** | **int** | Sets the time interval in milliseconds between checking for an alert conditions.&lt;br&gt; | [optional] [default to 1000]
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_routing_gateway_endpoint_request import PatchRoutingGatewayEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchRoutingGatewayEndpointRequest from a JSON string
patch_routing_gateway_endpoint_request_instance = PatchRoutingGatewayEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchRoutingGatewayEndpointRequest.to_json())

# convert the object into a dict
patch_routing_gateway_endpoint_request_dict = patch_routing_gateway_endpoint_request_instance.to_dict()
# create an instance of PatchRoutingGatewayEndpointRequest from a dict
patch_routing_gateway_endpoint_request_from_dict = PatchRoutingGatewayEndpointRequest.from_dict(patch_routing_gateway_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


