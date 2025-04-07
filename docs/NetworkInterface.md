# NetworkInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_if** | **str** | The real interface this configuration will be applied to.&lt;br&gt; | [optional] 
**enable** | **bool** | Enable or disable this interface.&lt;br&gt; | [optional] 
**descr** | **str** | The descriptive name for this interface.&lt;br&gt; | [optional] 
**spoofmac** | **str** | Assigns (spoofs) the MAC address for this interface instead of using the interface&#39;s real MAC.&lt;br&gt; | [optional] 
**mtu** | **int** | Sets the MTU for this interface. Assumes default MTU if value is &#x60;null&#x60;.&lt;br&gt; | [optional] 
**mss** | **int** | Sets the MSS for this interface. Assumes default MSS if value is &#x60;null&#x60;.&lt;br&gt; | [optional] 
**media** | **str** | Sets the link speed for this interface. In most situations this can be left as the default.&lt;br&gt; | [optional] 
**mediaopt** | **str** | Sets the link duplex for this interface. In most situations this can be left as the default.&lt;br&gt; | [optional] 
**blockpriv** | **bool** | Enable or disable automatically blocking RFC 1918 private networks on this interface.&lt;br&gt; | [optional] 
**blockbogons** | **bool** | Enable or disable automatically blocking bogon networks on this interface.&lt;br&gt; | [optional] 
**typev4** | **str** | Selects the IPv4 address type to assign this interface.&lt;br&gt; | [optional] 
**ipaddr** | **str** | Sets the IPv4 address to assign to this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be one of [ static, dhcp ]&lt;br&gt; | [optional] 
**subnet** | **int** | Sets the subnet bit count to assign this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;static&#39;&#x60;&lt;br&gt; | [optional] 
**gateway** | **str** | Sets the upstream gateway this interface will use. This is only applicable for WAN-type interfaces.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;static&#39;&#x60;&lt;br&gt; | [optional] 
**dhcphostname** | **str** | Sets the DHCP hostname this interface will advertise via DHCP.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt; | [optional] 
**alias_address** | **str** | Sets the value used as a fixed alias IPv4 address by the DHCP client.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt; | [optional] 
**alias_subnet** | **int** | Sets the value used as the fixed alias IPv4 address&#39;s subnet bit count by the DHCP client.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt; | [optional] [default to 32]
**dhcprejectfrom** | **List[str]** | Sets a list of IPv4 DHCP server addresses to reject DHCP offers for on this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt; | [optional] 
**adv_dhcp_config_advanced** | **bool** | Enables or disables the advanced DHCP settings on this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt; | [optional] 
**adv_dhcp_pt_values** | **str** | Selects the advanced DHCP timing preset.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt;- &#x60;adv_dhcp_config_advanced&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] [default to 'SavedCfg']
**adv_dhcp_pt_timeout** | **int** | Manually sets the timeout timing value used when requested DHCP leases on this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt;- &#x60;adv_dhcp_config_advanced&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**adv_dhcp_pt_retry** | **int** | Manually sets the retry timing value used when requested DHCP leases on this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt;- &#x60;adv_dhcp_config_advanced&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**adv_dhcp_pt_select_timeout** | **int** | Manually sets the select timing value used when requested DHCP leases on this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt;- &#x60;adv_dhcp_config_advanced&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**adv_dhcp_pt_reboot** | **int** | Manually sets the reboot timing value used when requested DHCP leases on this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt;- &#x60;adv_dhcp_config_advanced&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**adv_dhcp_pt_backoff_cutoff** | **int** | Manually sets the backoff cutoff timing value used when requested DHCP leases on this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt;- &#x60;adv_dhcp_config_advanced&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**adv_dhcp_pt_initial_interval** | **int** | Manually sets the initial interval timing value used when requested DHCP leases on this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt;- &#x60;adv_dhcp_config_advanced&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**adv_dhcp_send_options** | **str** | Sets DHCP options to be sent when requesting a DHCP lease for this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt;- &#x60;adv_dhcp_config_advanced&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**adv_dhcp_request_options** | **str** | Sets DHCP option 55 values to be sent when requesting a DHCP lease for this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt;- &#x60;adv_dhcp_config_advanced&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**adv_dhcp_required_options** | **str** | Sets DHCP options required by the client when requesting a DHCP lease for this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt;- &#x60;adv_dhcp_config_advanced&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**adv_dhcp_option_modifiers** | **str** | Sets DHCP option modifiers applied to the obtained DHCP lease.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt;- &#x60;adv_dhcp_config_advanced&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**adv_dhcp_config_file_override** | **bool** | Enables or disables overriding the entire DHCP configuration file for this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt; | [optional] 
**adv_dhcp_config_file_override_path** | **str** | Sets the local file path of the custom DHCP configuration file.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev4&#x60; must be equal to &#x60;&#39;dhcp&#39;&#x60;&lt;br&gt;- &#x60;adv_dhcp_config_file_override&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**typev6** | **str** | Selects the IPv6 address type to assign this interface.&lt;br&gt; | [optional] 
**ipaddrv6** | **str** | Sets the IPv6 address to assign to this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev6&#x60; must be one of [ staticv6, dhcp6, slaac, 6rd, track6, 6to4 ]&lt;br&gt; | [optional] 
**subnetv6** | **int** | Sets the subnet bit count to assign this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev6&#x60; must be equal to &#x60;&#39;staticv6&#39;&#x60;&lt;br&gt; | [optional] 
**gatewayv6** | **str** | Sets the upstream IPv6 gateway this interface will use. This is only applicable for WAN-type interfaces.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev6&#x60; must be equal to &#x60;&#39;staticv6&#39;&#x60;&lt;br&gt; | [optional] 
**ipv6usev4iface** | **bool** | Enable or disable IPv6 using the IPv4 connectivity link (PPPoE).&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev6&#x60; must be equal to &#x60;&#39;staticv6&#39;&#x60;&lt;br&gt; | [optional] 
**slaacusev4iface** | **bool** | Enable or disable IPv6 using the IPv4 connectivity link (PPPoE).&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev6&#x60; must be equal to &#x60;&#39;slaac&#39;&#x60;&lt;br&gt; | [optional] 
**prefix_6rd** | **str** | Sets the 6RD IPv6 prefix assigned by the ISP for this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev6&#x60; must be equal to &#x60;&#39;6rd&#39;&#x60;&lt;br&gt; | [optional] 
**gateway_6rd** | **str** | Sets the 6RD IPv4 gateway address assigned by the ISP for this interface.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev6&#x60; must be equal to &#x60;&#39;6rd&#39;&#x60;&lt;br&gt; | [optional] 
**prefix_6rd_v4plen** | **int** | Sets the 6RD IPv4 prefix length. Normally specified by the ISP. A value of 0 means embed theentire IPv4 address in the 6RD prefix.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev6&#x60; must be equal to &#x60;&#39;6rd&#39;&#x60;&lt;br&gt; | [optional] 
**track6_interface** | **str** | Sets the dynamic IPv6 WAN interface to track for configuration.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev6&#x60; must be equal to &#x60;&#39;track6&#39;&#x60;&lt;br&gt; | [optional] 
**track6_prefix_id_hex** | **str** | Sets the hexadecimal IPv6 prefix ID. This determines the configurable network ID based on the dynamic IPv6 connection.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;typev6&#x60; must be equal to &#x60;&#39;track6&#39;&#x60;&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.network_interface import NetworkInterface

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInterface from a JSON string
network_interface_instance = NetworkInterface.from_json(json)
# print the JSON string representation of the object
print(NetworkInterface.to_json())

# convert the object into a dict
network_interface_dict = network_interface_instance.to_dict()
# create an instance of NetworkInterface from a dict
network_interface_from_dict = NetworkInterface.from_dict(network_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


