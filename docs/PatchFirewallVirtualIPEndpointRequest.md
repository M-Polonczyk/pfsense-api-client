# PatchFirewallVirtualIPEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uniqid** | **str** | The unique ID for this virtual IP.&lt;br&gt; | [optional] [readonly] [default to '67ed0819dfdaa']
**mode** | **str** | The virtual IP mode to use for this virtual IP.&lt;br&gt; | [optional] 
**interface** | **str** | The interface this virtual IP will apply to.&lt;br&gt; | [optional] 
**type** | **str** | The virtual IP scope type. The &#x60;network&#x60; option is only applicable to the &#x60;proxyarp&#x60; and &#x60;other&#x60; virtual IP modes.&lt;br&gt; | [optional] [default to 'single']
**subnet** | **str** | The address for this virtual IP.&lt;br&gt; | [optional] 
**subnet_bits** | **int** | The subnet bits for this virtual IP. For &#x60;proxyarp&#x60; and &#x60;other&#x60; virtual IPs, this value specifies a block of many IP address. For all other virtual IP modes, this specifies the subnet mask&lt;br&gt; | [optional] 
**descr** | **str** | A description for administrative reference&lt;br&gt; | [optional] 
**noexpand** | **bool** | Disable expansion of this entry into IPs on NAT lists (e.g. 192.168.1.0/24 expands to 256 entries.)&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be one of [ proxyarp, other ]&lt;br&gt; | [optional] 
**vhid** | **int** | The VHID group that the machines will share.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be equal to &#x60;&#39;carp&#39;&#x60;&lt;br&gt; | [optional] 
**advbase** | **int** | The base frequency that this machine will advertise.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be equal to &#x60;&#39;carp&#39;&#x60;&lt;br&gt; | [optional] [default to 1]
**advskew** | **int** | The frequency skew that this machine will advertise.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be equal to &#x60;&#39;carp&#39;&#x60;&lt;br&gt; | [optional] 
**password** | **str** | The VHID group password shared by all CARP members.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be equal to &#x60;&#39;carp&#39;&#x60;&lt;br&gt; | [optional] 
**carp_status** | **str** | The current CARP status of this virtual IP. This will display show whether this CARP node is the primary or backup peer.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be equal to &#x60;&#39;carp&#39;&#x60;&lt;br&gt; | [optional] [readonly] 
**carp_mode** | **str** | The CARP mode to use for this virtual IP. Please note this field is exclusive to pfSense Plus and has no effect on CE.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must be equal to &#x60;&#39;carp&#39;&#x60;&lt;br&gt; | [optional] [default to 'mcast']
**carp_peer** | **str** | The IP address of the CARP peer. Please note this field is exclusive to pfSense Plus and has no effect on CE.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;carp_mode&#x60; must be equal to &#x60;&#39;ucast&#39;&#x60;&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_firewall_virtual_ip_endpoint_request import PatchFirewallVirtualIPEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFirewallVirtualIPEndpointRequest from a JSON string
patch_firewall_virtual_ip_endpoint_request_instance = PatchFirewallVirtualIPEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchFirewallVirtualIPEndpointRequest.to_json())

# convert the object into a dict
patch_firewall_virtual_ip_endpoint_request_dict = patch_firewall_virtual_ip_endpoint_request_instance.to_dict()
# create an instance of PatchFirewallVirtualIPEndpointRequest from a dict
patch_firewall_virtual_ip_endpoint_request_from_dict = PatchFirewallVirtualIPEndpointRequest.from_dict(patch_firewall_virtual_ip_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


