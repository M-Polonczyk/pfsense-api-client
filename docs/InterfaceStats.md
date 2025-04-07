# InterfaceStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the interface.&lt;br&gt; | [optional] 
**descr** | **str** | The description of the interface.&lt;br&gt; | [optional] 
**hwif** | **str** | The hardware interface name of the interface.&lt;br&gt; | [optional] 
**macaddr** | **str** | The MAC address of the interface.&lt;br&gt; | [optional] 
**mtu** | **str** | The MTU of the interface.&lt;br&gt; | [optional] 
**enable** | **bool** | Whether the interface is enabled.&lt;br&gt; | [optional] 
**status** | **str** | The status of the interface.&lt;br&gt; | [optional] 
**ipaddr** | **str** | The IPv4 address of the interface.&lt;br&gt; | [optional] 
**subnet** | **str** | The IPv4 subnet of the interface.&lt;br&gt; | [optional] 
**linklocal** | **str** | The IPv6 link-local address of the interface.&lt;br&gt; | [optional] 
**ipaddrv6** | **str** | The IPv6 address of the interface.&lt;br&gt; | [optional] 
**subnetv6** | **str** | The IPv6 subnet of the interface.&lt;br&gt; | [optional] 
**inerrs** | **int** | The number of inbound errors on the interface.&lt;br&gt; | [optional] 
**outerrs** | **int** | The number of outbound errors on the interface.&lt;br&gt; | [optional] 
**collisions** | **int** | The number of collisions on the interface.&lt;br&gt; | [optional] 
**inbytes** | **int** | The number of inbound bytes on the interface.&lt;br&gt; | [optional] 
**inbytespass** | **int** | The number of inbound bytes passed on the interface.&lt;br&gt; | [optional] 
**outbytes** | **int** | The number of outbound bytes on the interface.&lt;br&gt; | [optional] 
**outbytespass** | **int** | The number of outbound bytes passed on the interface.&lt;br&gt; | [optional] 
**inpkts** | **int** | The number of inbound packets on the interface.&lt;br&gt; | [optional] 
**inpktspass** | **int** | The number of inbound packets passed on the interface.&lt;br&gt; | [optional] 
**outpkts** | **int** | The number of outbound packets on the interface.&lt;br&gt; | [optional] 
**outpktspass** | **int** | The number of outbound packets passed on the interface.&lt;br&gt; | [optional] 
**dhcplink** | **str** | The DHCP link status of the interface.&lt;br&gt; | [optional] 
**media** | **str** | The speed/duplex of the interface.&lt;br&gt; | [optional] 
**gateway** | **str** | The IPv4 gateway of the interface.&lt;br&gt; | [optional] 
**gatewayv6** | **str** | The IPv6 gateway of the interface.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.interface_stats import InterfaceStats

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceStats from a JSON string
interface_stats_instance = InterfaceStats.from_json(json)
# print the JSON string representation of the object
print(InterfaceStats.to_json())

# convert the object into a dict
interface_stats_dict = interface_stats_instance.to_dict()
# create an instance of InterfaceStats from a dict
interface_stats_from_dict = InterfaceStats.from_dict(interface_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


