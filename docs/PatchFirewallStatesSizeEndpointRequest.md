# PatchFirewallStatesSizeEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximumstates** | **int** | The maximum number of firewall state entries allowed by this firewall.&lt;br&gt; | [optional] [default to 198000]
**defaultmaximumstates** | **int** | The default number of firewall state entries allowed by this firewall.&lt;br&gt; | [optional] [readonly] 
**currentstates** | **int** | The number of firewall state entries currently registered in the states table.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.patch_firewall_states_size_endpoint_request import PatchFirewallStatesSizeEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFirewallStatesSizeEndpointRequest from a JSON string
patch_firewall_states_size_endpoint_request_instance = PatchFirewallStatesSizeEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchFirewallStatesSizeEndpointRequest.to_json())

# convert the object into a dict
patch_firewall_states_size_endpoint_request_dict = patch_firewall_states_size_endpoint_request_instance.to_dict()
# create an instance of PatchFirewallStatesSizeEndpointRequest from a dict
patch_firewall_states_size_endpoint_request_from_dict = PatchFirewallStatesSizeEndpointRequest.from_dict(patch_firewall_states_size_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


