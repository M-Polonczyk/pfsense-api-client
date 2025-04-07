# RoutingGatewayStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the gateway this status corresponds to.&lt;br&gt; | [optional] [readonly] 
**srcip** | **str** | The current source IP being used to send monitoring probes to this gateway.&lt;br&gt; | [optional] [readonly] 
**monitorip** | **str** | The current IP being monitored for this gateway.&lt;br&gt; | [optional] [readonly] 
**delay** | **float** | The current latency (in milliseconds) for this gateway.&lt;br&gt; | [optional] [readonly] 
**stddev** | **float** | The standard deviation in latency (in milliseconds) for this gateway.&lt;br&gt; | [optional] [readonly] 
**loss** | **float** | The current amount of packet loss (in percentage) for this gateway. This uses a whole percentage (0.0-100.0).&lt;br&gt; | [optional] [readonly] 
**status** | **str** | The current status of this gateway. Typically, this will indicate if the gateway is consider online or offline.&lt;br&gt; | [optional] [readonly] 
**substatus** | **str** | The current sub-status of this gateway. Typically, this provide details into problems this gateway is seeing such as latency or packet loss.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.routing_gateway_status import RoutingGatewayStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingGatewayStatus from a JSON string
routing_gateway_status_instance = RoutingGatewayStatus.from_json(json)
# print the JSON string representation of the object
print(RoutingGatewayStatus.to_json())

# convert the object into a dict
routing_gateway_status_dict = routing_gateway_status_instance.to_dict()
# create an instance of RoutingGatewayStatus from a dict
routing_gateway_status_from_dict = RoutingGatewayStatus.from_dict(routing_gateway_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


