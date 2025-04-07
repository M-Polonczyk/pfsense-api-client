# FirewallState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | The interface that initially received the traffic which registered the state.&lt;br&gt; | [optional] 
**protocol** | **str** | The protocol listed in the state.&lt;br&gt; | [optional] 
**direction** | **str** | The direction of traffic listed in the state.&lt;br&gt; | [optional] 
**source** | **str** | The source address listed in the state. Note: Depending on the &#x60;protocol&#x60;, this value may contain the source port as well.&lt;br&gt; | [optional] 
**destination** | **str** | The destination address listed in the state. Note: Depending on the &#x60;protocol&#x60;, this value may contain the destination port as well.&lt;br&gt; | [optional] 
**state** | **str** | The current status of the firewall state.&lt;br&gt; | [optional] 
**age** | **str** | The age of the firewall state in HH:MM:SS format.&lt;br&gt; | [optional] 
**expires_in** | **str** | The amount of time remaining until the state expires in HH:MM:SS format.&lt;br&gt; | [optional] 
**packets_total** | **int** | The total number of packets observed by the state.&lt;br&gt; | [optional] 
**packets_in** | **int** | The total number of inbound packets observed by the state.&lt;br&gt; | [optional] 
**packets_out** | **int** | The total number of outbound packets observed by the state.&lt;br&gt; | [optional] 
**bytes_total** | **int** | The total number of traffic (in bytes) observed by the state.&lt;br&gt; | [optional] 
**bytes_in** | **int** | The total number of inbound traffic (in bytes) observed by the state.&lt;br&gt; | [optional] 
**bytes_out** | **int** | The total number of outbound traffic (in bytes) observed by the state.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.firewall_state import FirewallState

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallState from a JSON string
firewall_state_instance = FirewallState.from_json(json)
# print the JSON string representation of the object
print(FirewallState.to_json())

# convert the object into a dict
firewall_state_dict = firewall_state_instance.to_dict()
# create an instance of FirewallState from a dict
firewall_state_from_dict = FirewallState.from_dict(firewall_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


