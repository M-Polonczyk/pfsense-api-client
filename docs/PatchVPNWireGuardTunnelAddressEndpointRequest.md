# PatchVPNWireGuardTunnelAddressEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IPv4 or IPv6 address for this WireGuard tunnel.&lt;br&gt; | [optional] 
**mask** | **int** | The subnet mask for this WireGuard tunnel.&lt;br&gt; | [optional] 
**descr** | **str** | A description for this WireGuard tunnel address entry.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_vpn_wire_guard_tunnel_address_endpoint_request import PatchVPNWireGuardTunnelAddressEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchVPNWireGuardTunnelAddressEndpointRequest from a JSON string
patch_vpn_wire_guard_tunnel_address_endpoint_request_instance = PatchVPNWireGuardTunnelAddressEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchVPNWireGuardTunnelAddressEndpointRequest.to_json())

# convert the object into a dict
patch_vpn_wire_guard_tunnel_address_endpoint_request_dict = patch_vpn_wire_guard_tunnel_address_endpoint_request_instance.to_dict()
# create an instance of PatchVPNWireGuardTunnelAddressEndpointRequest from a dict
patch_vpn_wire_guard_tunnel_address_endpoint_request_from_dict = PatchVPNWireGuardTunnelAddressEndpointRequest.from_dict(patch_vpn_wire_guard_tunnel_address_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


