# PostVPNWireGuardApplyEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; when all WireGuard changes are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending WireGuard changes that have not been applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.post_vpn_wire_guard_apply_endpoint_request import PostVPNWireGuardApplyEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostVPNWireGuardApplyEndpointRequest from a JSON string
post_vpn_wire_guard_apply_endpoint_request_instance = PostVPNWireGuardApplyEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostVPNWireGuardApplyEndpointRequest.to_json())

# convert the object into a dict
post_vpn_wire_guard_apply_endpoint_request_dict = post_vpn_wire_guard_apply_endpoint_request_instance.to_dict()
# create an instance of PostVPNWireGuardApplyEndpointRequest from a dict
post_vpn_wire_guard_apply_endpoint_request_from_dict = PostVPNWireGuardApplyEndpointRequest.from_dict(post_vpn_wire_guard_apply_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


