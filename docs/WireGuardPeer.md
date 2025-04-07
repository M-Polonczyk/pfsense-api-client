# WireGuardPeer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enables or disables this WireGuard peer.&lt;br&gt; | [optional] 
**tun** | **str** | The WireGuard tunnel for this peer.&lt;br&gt; | [optional] [default to 'unassigned']
**endpoint** | **str** | The IP address or hostname of the remote peer. Set to &#x60;null&#x60; to make this a dynamic endpoint.&lt;br&gt; | [optional] 
**port** | **str** | The port used by the remote peer. Valid options are: a TCP/UDP port number&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;endpoint&#x60; must not be equal to &#x60;NULL&#x60;&lt;br&gt; | [optional] [default to '51820']
**descr** | **str** | The description for this peer.&lt;br&gt; | [optional] 
**persistentkeepalive** | **int** | The interval (in seconds) for Keep Alive packets sent to this peer. Set to &#x60;null&#x60; to disable.&lt;br&gt; | [optional] 
**publickey** | **str** | The public key for this peer.&lt;br&gt; | [optional] 
**presharedkey** | **str** | The pre-shared key for this tunnel.&lt;br&gt; | [optional] 
**allowedips** | [**List[WireGuardPeerAllowedipsInner]**](WireGuardPeerAllowedipsInner.md) | The allowed IP/subnets for this WireGuard peer.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.wire_guard_peer import WireGuardPeer

# TODO update the JSON string below
json = "{}"
# create an instance of WireGuardPeer from a JSON string
wire_guard_peer_instance = WireGuardPeer.from_json(json)
# print the JSON string representation of the object
print(WireGuardPeer.to_json())

# convert the object into a dict
wire_guard_peer_dict = wire_guard_peer_instance.to_dict()
# create an instance of WireGuardPeer from a dict
wire_guard_peer_from_dict = WireGuardPeer.from_dict(wire_guard_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


