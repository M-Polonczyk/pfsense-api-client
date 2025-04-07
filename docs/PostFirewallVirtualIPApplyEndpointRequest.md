# PostFirewallVirtualIPApplyEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; when all virtual IP changes are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending virtual IP changes that have not been applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.post_firewall_virtual_ip_apply_endpoint_request import PostFirewallVirtualIPApplyEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFirewallVirtualIPApplyEndpointRequest from a JSON string
post_firewall_virtual_ip_apply_endpoint_request_instance = PostFirewallVirtualIPApplyEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostFirewallVirtualIPApplyEndpointRequest.to_json())

# convert the object into a dict
post_firewall_virtual_ip_apply_endpoint_request_dict = post_firewall_virtual_ip_apply_endpoint_request_instance.to_dict()
# create an instance of PostFirewallVirtualIPApplyEndpointRequest from a dict
post_firewall_virtual_ip_apply_endpoint_request_from_dict = PostFirewallVirtualIPApplyEndpointRequest.from_dict(post_firewall_virtual_ip_apply_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


