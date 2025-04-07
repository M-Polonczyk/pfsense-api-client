# PatchFirewallScheduleTimeRangeEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **List[int]** | The day of the week this schedule should be active for. Use &#x60;1&#x60; for every Monday, &#x60;2&#x60; for every Tuesday, &#x60;3&#x60; for every Wednesday, &#x60;4&#x60; for every Thursday, &#x60;5&#x60; for every Friday, &#x60;6&#x60; for every Saturday, or &#x60;7&#x60; for every Sunday. If this field has a value specified, the &#x60;month&#x60; and &#x60;day&#x60; fields will be unavailable.&lt;br&gt; | [optional] 
**month** | **List[int]** | The month for each specified &#x60;day&#x60; value. Each value specified must correspond with a &#x60;day&#x60; field value and must match the order exactly. For example, a &#x60;month&#x60; value of &#x60;[3, 6]&#x60; and a &#x60;day&#x60; value of &#x60;[2, 17]&#x60; would evaluate to March 2nd and June 17th respectively.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;position&#x60; must be equal to &#x60;NULL&#x60;&lt;br&gt; | [optional] 
**day** | **List[int]** | The day for each specified &#x60;month&#x60; value. Each value specified must correspond with a &#x60;month&#x60; field value and must match the order exactly. For example, a &#x60;month&#x60; value of &#x60;[3, 6]&#x60; and a &#x60;day&#x60; value of &#x60;[2, 17]&#x60; would evaluate to March 2nd and June 17th respectively.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;position&#x60; must be equal to &#x60;NULL&#x60;&lt;br&gt; | [optional] 
**hour** | **str** | The start time and end time for this time range in 24-hour format (i.e. HH:MM-HH:MM).&lt;br&gt; | [optional] 
**rangedescr** | **str** | A description detailing this firewall schedule time range&#39;s purpose.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_firewall_schedule_time_range_endpoint_request import PatchFirewallScheduleTimeRangeEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFirewallScheduleTimeRangeEndpointRequest from a JSON string
patch_firewall_schedule_time_range_endpoint_request_instance = PatchFirewallScheduleTimeRangeEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchFirewallScheduleTimeRangeEndpointRequest.to_json())

# convert the object into a dict
patch_firewall_schedule_time_range_endpoint_request_dict = patch_firewall_schedule_time_range_endpoint_request_instance.to_dict()
# create an instance of PatchFirewallScheduleTimeRangeEndpointRequest from a dict
patch_firewall_schedule_time_range_endpoint_request_from_dict = PatchFirewallScheduleTimeRangeEndpointRequest.from_dict(patch_firewall_schedule_time_range_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


