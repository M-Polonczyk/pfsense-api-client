# PostVPNWireGuardTunnelAddressEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IPv4 or IPv6 address for this WireGuard tunnel.&lt;br&gt; | 
**mask** | **int** | The subnet mask for this WireGuard tunnel.&lt;br&gt; | 
**descr** | **str** | A description for this WireGuard tunnel address entry.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 

## Example

```python
from pfsense_api_client.models.post_vpn_wire_guard_tunnel_address_endpoint_request import PostVPNWireGuardTunnelAddressEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostVPNWireGuardTunnelAddressEndpointRequest from a JSON string
post_vpn_wire_guard_tunnel_address_endpoint_request_instance = PostVPNWireGuardTunnelAddressEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostVPNWireGuardTunnelAddressEndpointRequest.to_json())

# convert the object into a dict
post_vpn_wire_guard_tunnel_address_endpoint_request_dict = post_vpn_wire_guard_tunnel_address_endpoint_request_instance.to_dict()
# create an instance of PostVPNWireGuardTunnelAddressEndpointRequest from a dict
post_vpn_wire_guard_tunnel_address_endpoint_request_from_dict = PostVPNWireGuardTunnelAddressEndpointRequest.from_dict(post_vpn_wire_guard_tunnel_address_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


