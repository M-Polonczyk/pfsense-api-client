# FirewallSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedlabel** | **str** | A unique ID for this schedule used internally by the system.&lt;br&gt; | [optional] [readonly] [default to '67ed0819d095f']
**name** | **str** | The unique name to assign this schedule.&lt;br&gt; | [optional] 
**descr** | **str** | A description of this schedules purpose.&lt;br&gt; | [optional] 
**active** | **bool** | Displays whether the schedule is currently active or not.&lt;br&gt; | [optional] [readonly] 
**timerange** | [**List[FirewallScheduleTimerangeInner]**](FirewallScheduleTimerangeInner.md) | The date/times this firewall schedule will be active.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.firewall_schedule import FirewallSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallSchedule from a JSON string
firewall_schedule_instance = FirewallSchedule.from_json(json)
# print the JSON string representation of the object
print(FirewallSchedule.to_json())

# convert the object into a dict
firewall_schedule_dict = firewall_schedule_instance.to_dict()
# create an instance of FirewallSchedule from a dict
firewall_schedule_from_dict = FirewallSchedule.from_dict(firewall_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


