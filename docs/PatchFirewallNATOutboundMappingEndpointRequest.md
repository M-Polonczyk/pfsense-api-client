# PatchFirewallNATOutboundMappingEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | The interface on which traffic is matched as it exits the firewall. In most cases this is a WAN-type or another externally-connected interface.&lt;br&gt; | [optional] 
**protocol** | **str** | The protocol this rule should match. Use &#x60;null&#x60; for any protocol.&lt;br&gt; | [optional] 
**disabled** | **bool** | Disable this outbound NAT rule.&lt;br&gt; | [optional] 
**nonat** | **bool** | Do not NAT traffic matching this rule.&lt;br&gt; | [optional] 
**nosync** | **bool** | Do not sync this rule to HA peers.&lt;br&gt; | [optional] 
**source** | **str** | The source network this rule should match. Valid value options are: an existing interface, a subnet CIDR, an existing alias, &#x60;any&#x60;, &#x60;(self)&#x60;, &#x60;pppoe&#x60;. The context of this address can be inverted by prefixing the value with &#x60;!&#x60;. For interface values, the &#x60;:ip&#x60;  modifier can be appended to the value to use the interface&#39;s IP address instead of its entire subnet.&lt;br&gt; | [optional] 
**source_port** | **str** | The source port this rule should match. Valid options are: a TCP/UDP port number, a TCP/UDP port range separated by &#x60;:&#x60;, an existing port type firewall alias&lt;br&gt; | [optional] 
**destination** | **str** | The destination network this rule should match. Valid value options are: an existing interface, a subnet CIDR, an existing alias, &#x60;any&#x60;, &#x60;pppoe&#x60;. The context of this address can be inverted by prefixing the value with &#x60;!&#x60;. For interface values, the &#x60;:ip&#x60;  modifier can be appended to the value to use the interface&#39;s IP address instead of its entire subnet.&lt;br&gt; | [optional] 
**destination_port** | **str** | The destination port this rule should match. Valid options are: a TCP/UDP port number, a TCP/UDP port range separated by &#x60;:&#x60;, an existing port type firewall alias&lt;br&gt; | [optional] 
**target** | **str** | The target network traffic matching this rule should be translated to. Valid value options are: an IP address, an existing alias. For interface values, the &#x60;:ip&#x60;  modifier can be appended to the value to use the interface&#39;s IP address instead of its entire subnet.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;nonat&#x60; must be equal to &#x60;false&#x60;&lt;br&gt; | [optional] 
**target_subnet** | **int** | The subnet bits for the assigned &#x60;target&#x60;. This field is only applicable if &#x60;target&#x60; is set to an IP address. This has no affect for alias or interface &#x60;targets&#x60;.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;nonat&#x60; must be equal to &#x60;false&#x60;&lt;br&gt; | [optional] [default to 128]
**nat_port** | **str** | The external source port or port range used for rewriting the original source port on connections matching the rule. Valid options are: a TCP/UDP port number, a TCP/UDP port range separated by &#x60;:&#x60;&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;static_nat_port&#x60; must be equal to &#x60;false&#x60;&lt;br&gt;- &#x60;nonat&#x60; must be equal to &#x60;false&#x60;&lt;br&gt; | [optional] 
**static_nat_port** | **bool** | Do not rewrite source port for traffic matching this rule.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;nonat&#x60; must be equal to &#x60;false&#x60;&lt;br&gt; | [optional] 
**poolopts** | **str** | The pool option used to load balance external IP mapping when &#x60;target&#x60; is set to a subnet or alias of many addresses. Set to &#x60;null&#x60; to revert to the system default.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;nonat&#x60; must be equal to &#x60;false&#x60;&lt;br&gt; | [optional] 
**source_hash_key** | **str** | The key that is fed to the hashing algorithm in hex format. This must be a 16 byte (32 character) hex string prefixed with &#x60;0x&#x60;. If a value is not provided, one will automatically be generated&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;poolopts&#x60; must be equal to &#x60;&#39;source-hash&#39;&#x60;&lt;br&gt;- &#x60;nonat&#x60; must be equal to &#x60;false&#x60;&lt;br&gt; | [optional] [default to '0x3971d34cd39dfa892480e6beb923e0bd']
**descr** | **str** | A description for the outbound NAT mapping.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_firewall_nat_outbound_mapping_endpoint_request import PatchFirewallNATOutboundMappingEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFirewallNATOutboundMappingEndpointRequest from a JSON string
patch_firewall_nat_outbound_mapping_endpoint_request_instance = PatchFirewallNATOutboundMappingEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchFirewallNATOutboundMappingEndpointRequest.to_json())

# convert the object into a dict
patch_firewall_nat_outbound_mapping_endpoint_request_dict = patch_firewall_nat_outbound_mapping_endpoint_request_instance.to_dict()
# create an instance of PatchFirewallNATOutboundMappingEndpointRequest from a dict
patch_firewall_nat_outbound_mapping_endpoint_request_from_dict = PatchFirewallNATOutboundMappingEndpointRequest.from_dict(patch_firewall_nat_outbound_mapping_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


