# PostFirewallApplyEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; when all firewall changes are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending firewall changes that have not been applied.&lt;br&gt; | [optional] [readonly] 
**pending_subsystems** | **List[str]** | Displays the specific firewall subsystems that have pending changes.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.post_firewall_apply_endpoint_request import PostFirewallApplyEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFirewallApplyEndpointRequest from a JSON string
post_firewall_apply_endpoint_request_instance = PostFirewallApplyEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostFirewallApplyEndpointRequest.to_json())

# convert the object into a dict
post_firewall_apply_endpoint_request_dict = post_firewall_apply_endpoint_request_instance.to_dict()
# create an instance of PostFirewallApplyEndpointRequest from a dict
post_firewall_apply_endpoint_request_from_dict = PostFirewallApplyEndpointRequest.from_dict(post_firewall_apply_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


