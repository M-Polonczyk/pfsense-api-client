# FirewallApply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; when all firewall changes are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending firewall changes that have not been applied.&lt;br&gt; | [optional] [readonly] 
**pending_subsystems** | **List[str]** | Displays the specific firewall subsystems that have pending changes.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.firewall_apply import FirewallApply

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallApply from a JSON string
firewall_apply_instance = FirewallApply.from_json(json)
# print the JSON string representation of the object
print(FirewallApply.to_json())

# convert the object into a dict
firewall_apply_dict = firewall_apply_instance.to_dict()
# create an instance of FirewallApply from a dict
firewall_apply_from_dict = FirewallApply.from_dict(firewall_apply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


