# WireGuardTunnelAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IPv4 or IPv6 address for this WireGuard tunnel.&lt;br&gt; | [optional] 
**mask** | **int** | The subnet mask for this WireGuard tunnel.&lt;br&gt; | [optional] 
**descr** | **str** | A description for this WireGuard tunnel address entry.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.wire_guard_tunnel_address import WireGuardTunnelAddress

# TODO update the JSON string below
json = "{}"
# create an instance of WireGuardTunnelAddress from a JSON string
wire_guard_tunnel_address_instance = WireGuardTunnelAddress.from_json(json)
# print the JSON string representation of the object
print(WireGuardTunnelAddress.to_json())

# convert the object into a dict
wire_guard_tunnel_address_dict = wire_guard_tunnel_address_instance.to_dict()
# create an instance of WireGuardTunnelAddress from a dict
wire_guard_tunnel_address_from_dict = WireGuardTunnelAddress.from_dict(wire_guard_tunnel_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


