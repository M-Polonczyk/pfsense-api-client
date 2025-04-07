# FirewallStatesSize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximumstates** | **int** | The maximum number of firewall state entries allowed by this firewall.&lt;br&gt; | [optional] [default to 198000]
**defaultmaximumstates** | **int** | The default number of firewall state entries allowed by this firewall.&lt;br&gt; | [optional] [readonly] 
**currentstates** | **int** | The number of firewall state entries currently registered in the states table.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.firewall_states_size import FirewallStatesSize

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallStatesSize from a JSON string
firewall_states_size_instance = FirewallStatesSize.from_json(json)
# print the JSON string representation of the object
print(FirewallStatesSize.to_json())

# convert the object into a dict
firewall_states_size_dict = firewall_states_size_instance.to_dict()
# create an instance of FirewallStatesSize from a dict
firewall_states_size_from_dict = FirewallStatesSize.from_dict(firewall_states_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


