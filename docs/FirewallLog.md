# FirewallLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The raw text of the firewall log entry.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.firewall_log import FirewallLog

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallLog from a JSON string
firewall_log_instance = FirewallLog.from_json(json)
# print the JSON string representation of the object
print(FirewallLog.to_json())

# convert the object into a dict
firewall_log_dict = firewall_log_instance.to_dict()
# create an instance of FirewallLog from a dict
firewall_log_from_dict = FirewallLog.from_dict(firewall_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


