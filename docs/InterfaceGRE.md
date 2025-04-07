# InterfaceGRE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_if** | **str** | The pfSense interface interface serving as the local address to be used for the GRE tunnel.&lt;br&gt; | [optional] 
**greif** | **str** | The real interface name for this GRE interface.&lt;br&gt; | [optional] [readonly] 
**descr** | **str** | A description for this GRE interface.&lt;br&gt; | [optional] 
**add_static_route** | **bool** | Whether to add an explicit static route for the remote inner tunnel address/subnet via the local tunnel address.&lt;br&gt; | [optional] 
**remote_addr** | **str** | The remote address to use for the GRE tunnel.&lt;br&gt; | [optional] 
**tunnel_local_addr** | **str** | The local IPv4 address to use for the GRE tunnel.&lt;br&gt; | [optional] 
**tunnel_remote_addr** | **str** | The remote IPv4 address to use for the GRE tunnel.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;tunnel_local_addr&#x60; must not be equal to &#x60;NULL&#x60;&lt;br&gt; | [optional] 
**tunnel_remote_net** | **int** | The remote IPv4 subnet bitmask to use for the GRE tunnel.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;tunnel_local_addr&#x60; must not be equal to &#x60;NULL&#x60;&lt;br&gt; | [optional] [default to 32]
**tunnel_local_addr6** | **str** | The local IPv6 address to use for the GRE tunnel.&lt;br&gt; | [optional] 
**tunnel_remote_addr6** | **str** | The remote IPv6 address to use for the GRE tunnel.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;tunnel_local_addr6&#x60; must not be equal to &#x60;NULL&#x60;&lt;br&gt; | [optional] 
**tunnel_remote_net6** | **int** | The remote IPv6 subnet bitmask to use for the GRE tunnel.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;tunnel_local_addr6&#x60; must not be equal to &#x60;NULL&#x60;&lt;br&gt; | [optional] [default to 128]

## Example

```python
from pfsense_api_client.models.interface_gre import InterfaceGRE

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceGRE from a JSON string
interface_gre_instance = InterfaceGRE.from_json(json)
# print the JSON string representation of the object
print(InterfaceGRE.to_json())

# convert the object into a dict
interface_gre_dict = interface_gre_instance.to_dict()
# create an instance of InterfaceGRE from a dict
interface_gre_from_dict = InterfaceGRE.from_dict(interface_gre_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


