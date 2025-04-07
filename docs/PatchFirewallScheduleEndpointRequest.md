# PatchFirewallScheduleEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedlabel** | **str** | A unique ID for this schedule used internally by the system.&lt;br&gt; | [optional] [readonly] [default to '67ed0819d095f']
**name** | **str** | The unique name to assign this schedule.&lt;br&gt; | [optional] 
**descr** | **str** | A description of this schedules purpose.&lt;br&gt; | [optional] 
**active** | **bool** | Displays whether the schedule is currently active or not.&lt;br&gt; | [optional] [readonly] 
**timerange** | [**List[FirewallScheduleTimerangeInner]**](FirewallScheduleTimerangeInner.md) | The date/times this firewall schedule will be active.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_firewall_schedule_endpoint_request import PatchFirewallScheduleEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFirewallScheduleEndpointRequest from a JSON string
patch_firewall_schedule_endpoint_request_instance = PatchFirewallScheduleEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchFirewallScheduleEndpointRequest.to_json())

# convert the object into a dict
patch_firewall_schedule_endpoint_request_dict = patch_firewall_schedule_endpoint_request_instance.to_dict()
# create an instance of PatchFirewallScheduleEndpointRequest from a dict
patch_firewall_schedule_endpoint_request_from_dict = PatchFirewallScheduleEndpointRequest.from_dict(patch_firewall_schedule_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


