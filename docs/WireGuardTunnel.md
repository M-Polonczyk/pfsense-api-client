# WireGuardTunnel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the WireGuard interface. This value is automatically assigned by the system and cannot be changed.&lt;br&gt; | [optional] [readonly] 
**enabled** | **bool** | Enables or disables this tunnels and any associated peers.&lt;br&gt; | [optional] [default to True]
**listenport** | **str** | The port WireGuard will listen on for this tunnel. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '51820']
**publickey** | **str** | The public key for this tunnel. This value is automatically derived from the &#x60;privatekey&#x60; value and cannot be set manually.&lt;br&gt; | [optional] [readonly] 
**privatekey** | **str** | The private key for this tunnel.&lt;br&gt; | [optional] 
**mtu** | **int** | The MTU for this WireGuard tunnel interface. This value is ignored if this tunnel is assigned as a pfSense interface.&lt;br&gt; | [optional] [default to 1420]
**addresses** | [**List[WireGuardTunnelAddressesInner]**](WireGuardTunnelAddressesInner.md) | The IPv4 or IPv6 addresses to assign this WireGuard tunnel interface. This field is ignored if this tunnel interface is assigned to an existing pfSense interface object.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.wire_guard_tunnel import WireGuardTunnel

# TODO update the JSON string below
json = "{}"
# create an instance of WireGuardTunnel from a JSON string
wire_guard_tunnel_instance = WireGuardTunnel.from_json(json)
# print the JSON string representation of the object
print(WireGuardTunnel.to_json())

# convert the object into a dict
wire_guard_tunnel_dict = wire_guard_tunnel_instance.to_dict()
# create an instance of WireGuardTunnel from a dict
wire_guard_tunnel_from_dict = WireGuardTunnel.from_dict(wire_guard_tunnel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


