# PostFirewallScheduleEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedlabel** | **str** | A unique ID for this schedule used internally by the system.&lt;br&gt; | [optional] [readonly] [default to '67ed0819d095f']
**name** | **str** | The unique name to assign this schedule.&lt;br&gt; | 
**descr** | **str** | A description of this schedules purpose.&lt;br&gt; | [optional] 
**active** | **bool** | Displays whether the schedule is currently active or not.&lt;br&gt; | [optional] [readonly] 
**timerange** | [**List[FirewallScheduleTimerangeInner]**](FirewallScheduleTimerangeInner.md) | The date/times this firewall schedule will be active.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.post_firewall_schedule_endpoint_request import PostFirewallScheduleEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFirewallScheduleEndpointRequest from a JSON string
post_firewall_schedule_endpoint_request_instance = PostFirewallScheduleEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostFirewallScheduleEndpointRequest.to_json())

# convert the object into a dict
post_firewall_schedule_endpoint_request_dict = post_firewall_schedule_endpoint_request_instance.to_dict()
# create an instance of PostFirewallScheduleEndpointRequest from a dict
post_firewall_schedule_endpoint_request_from_dict = PostFirewallScheduleEndpointRequest.from_dict(post_firewall_schedule_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


