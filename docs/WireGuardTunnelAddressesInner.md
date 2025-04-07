# WireGuardTunnelAddressesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IPv4 or IPv6 address for this WireGuard tunnel.&lt;br&gt; | 
**mask** | **int** | The subnet mask for this WireGuard tunnel.&lt;br&gt; | 
**descr** | **str** | A description for this WireGuard tunnel address entry.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.wire_guard_tunnel_addresses_inner import WireGuardTunnelAddressesInner

# TODO update the JSON string below
json = "{}"
# create an instance of WireGuardTunnelAddressesInner from a JSON string
wire_guard_tunnel_addresses_inner_instance = WireGuardTunnelAddressesInner.from_json(json)
# print the JSON string representation of the object
print(WireGuardTunnelAddressesInner.to_json())

# convert the object into a dict
wire_guard_tunnel_addresses_inner_dict = wire_guard_tunnel_addresses_inner_instance.to_dict()
# create an instance of WireGuardTunnelAddressesInner from a dict
wire_guard_tunnel_addresses_inner_from_dict = WireGuardTunnelAddressesInner.from_dict(wire_guard_tunnel_addresses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


