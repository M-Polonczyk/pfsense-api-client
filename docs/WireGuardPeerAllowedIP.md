# WireGuardPeerAllowedIP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IPv4 or IPv6 address for this peer IP.&lt;br&gt; | [optional] 
**mask** | **int** | The subnet mask for this peer IP.&lt;br&gt; | [optional] 
**descr** | **str** | A description for this allowed peer IP.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.wire_guard_peer_allowed_ip import WireGuardPeerAllowedIP

# TODO update the JSON string below
json = "{}"
# create an instance of WireGuardPeerAllowedIP from a JSON string
wire_guard_peer_allowed_ip_instance = WireGuardPeerAllowedIP.from_json(json)
# print the JSON string representation of the object
print(WireGuardPeerAllowedIP.to_json())

# convert the object into a dict
wire_guard_peer_allowed_ip_dict = wire_guard_peer_allowed_ip_instance.to_dict()
# create an instance of WireGuardPeerAllowedIP from a dict
wire_guard_peer_allowed_ip_from_dict = WireGuardPeerAllowedIP.from_dict(wire_guard_peer_allowed_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


