# PatchFirewallNATOutboundModeEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | The outbound NAT mode to assign this system. Set to &#x60;automatic&#x60; to have this system automatically generate NAT rules this firewall, &#x60;hybrid&#x60; to automatically generate NAT rules AND allow manual outbound NAT mappings to be assigned, &#x60;manual&#x60; to prevent the system from automatically generating NAT rules and only allow manual outbound NAT mappings, or &#x60;disabled&#x60; to disable outbound NAT on this system entirely.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.patch_firewall_nat_outbound_mode_endpoint_request import PatchFirewallNATOutboundModeEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFirewallNATOutboundModeEndpointRequest from a JSON string
patch_firewall_nat_outbound_mode_endpoint_request_instance = PatchFirewallNATOutboundModeEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchFirewallNATOutboundModeEndpointRequest.to_json())

# convert the object into a dict
patch_firewall_nat_outbound_mode_endpoint_request_dict = patch_firewall_nat_outbound_mode_endpoint_request_instance.to_dict()
# create an instance of PatchFirewallNATOutboundModeEndpointRequest from a dict
patch_firewall_nat_outbound_mode_endpoint_request_from_dict = PatchFirewallNATOutboundModeEndpointRequest.from_dict(patch_firewall_nat_outbound_mode_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


