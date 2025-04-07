# PostFirewallRuleEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The action to take against traffic that matches this rule.&lt;br&gt; | 
**interface** | **List[str]** | The interface where packets must originate to match this rule.&lt;br&gt; | 
**ipprotocol** | **str** | The IP version(s) this rule applies to.&lt;br&gt; | 
**protocol** | **str** | The IP/transport protocol this rule should match.&lt;br&gt; | [optional] 
**icmptype** | **List[str]** | Th ICMP subtypes this rule applies to. This field is only applicable when &#x60;ipprotocol&#x60; is &#x60;inet&#x60; and &#x60;protocol&#x60; is &#x60;icmp&#x60;.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;protocol&#x60; must be equal to &#x60;&#39;icmp&#39;&#x60;&lt;br&gt; | [optional] [default to [any]]
**source** | **str** | The source address this rule applies to. Valid value options are: an existing interface, an IP address, a subnet CIDR, an existing alias, &#x60;any&#x60;, &#x60;(self)&#x60;, &#x60;l2tp&#x60;, &#x60;pppoe&#x60;. The context of this address can be inverted by prefixing the value with &#x60;!&#x60;. For interface values, the &#x60;:ip&#x60;  modifier can be appended to the value to use the interface&#39;s IP address instead of its entire subnet.&lt;br&gt; | 
**source_port** | **str** | The source port this rule applies to. Set to &#x60;null&#x60; to allow any source port. Valid options are: a TCP/UDP port number, a TCP/UDP port range separated by &#x60;:&#x60;, an existing port type firewall alias&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;protocol&#x60; must be one of [ tcp, udp, tcp/udp ]&lt;br&gt; | [optional] 
**destination** | **str** | The destination address this rule applies to. Valid value options are: an existing interface, an IP address, a subnet CIDR, an existing alias, &#x60;any&#x60;, &#x60;(self)&#x60;, &#x60;l2tp&#x60;, &#x60;pppoe&#x60;. The context of this address can be inverted by prefixing the value with &#x60;!&#x60;. For interface values, the &#x60;:ip&#x60;  modifier can be appended to the value to use the interface&#39;s IP address instead of its entire subnet.&lt;br&gt; | 
**destination_port** | **str** | The destination port this rule applies to. Set to &#x60;null&#x60; to allow any destination port. Valid options are: a TCP/UDP port number, a TCP/UDP port range separated by &#x60;:&#x60;, an existing port type firewall alias&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;protocol&#x60; must be one of [ tcp, udp, tcp/udp ]&lt;br&gt; | [optional] 
**descr** | **str** | A description detailing the purpose or justification of this firewall rule.&lt;br&gt; | [optional] 
**disabled** | **bool** | Enable or disable this firewall rule.&lt;br&gt; | [optional] 
**log** | **bool** | Enable or disable logging of traffic that matches this rule.&lt;br&gt; | [optional] 
**tag** | **str** | A packet matching this rule can be marked and this mark used to match on other NAT/filter rules. It is called &lt;br&gt; | [optional] 
**statetype** | **str** | The state mechanism to use for this firewall rule.&lt;br&gt; | [optional] [default to 'keep state']
**tcp_flags_any** | **bool** | Allow any TCP flags.&lt;br&gt; | [optional] 
**tcp_flags_out_of** | **List[str]** | The TCP flags that can be set for this rule to match.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;tcp_flags_any&#x60; must be equal to &#x60;false&#x60;&lt;br&gt; | [optional] 
**tcp_flags_set** | **List[str]** | The TCP flags that must be set for this rule to match.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;tcp_flags_any&#x60; must be equal to &#x60;false&#x60;&lt;br&gt; | [optional] 
**gateway** | **str** | The gateway traffic matching this rule will be routed to. Set to &#x60;null&#x60; to use default.&lt;br&gt; | [optional] 
**sched** | **str** | The name of an existing firewall schedule to assign to this firewall rule.&lt;br&gt; | [optional] 
**dnpipe** | **str** | The name of the traffic shaper limiter pipe or queue to use for incoming traffic.&lt;br&gt; | [optional] 
**pdnpipe** | **str** | The name of the traffic shaper limiter pipe or queue to use for outgoing traffic.&lt;br&gt; | [optional] 
**defaultqueue** | **str** | The name of the traffic shaper queue to assume as the default queue for traffic matching this rule.&lt;br&gt; | [optional] 
**ackqueue** | **str** | The name of the traffic shaper queue to assume as the ACK queue for ACK traffic matching this rule.&lt;br&gt; | [optional] 
**floating** | **bool** | Mark this rule as a floating firewall rule.&lt;br&gt; | [optional] 
**quick** | **bool** | Apply this action to traffic that matches this rule immediately. This field only applies to floating firewall rules.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;floating&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**direction** | **str** | The direction of traffic this firewall rule applies to. This field only applies to floating firewall rules.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;floating&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] [default to 'any']
**tracker** | **int** | The internal tracking ID for this firewall rule.&lt;br&gt; | [optional] [readonly] 
**associated_rule_id** | **str** | The internal rule ID for the NAT rule associated with this rule.&lt;br&gt; | [optional] [readonly] 
**created_time** | **int** | The unix timestamp of when this firewall rule was original created.&lt;br&gt; | [optional] [readonly] 
**created_by** | **str** | The username and IP of the user who originally created this firewall rule.&lt;br&gt; | [optional] [readonly] [default to '@unknown IP (API)']
**updated_time** | **int** | The unix timestamp of when this firewall rule was original created.&lt;br&gt; | [optional] [readonly] 
**updated_by** | **str** | The username and IP of the user who last updated this firewall rule.&lt;br&gt; | [optional] [readonly] [default to '@unknown IP (API)']

## Example

```python
from pfsense_api_client.models.post_firewall_rule_endpoint_request import PostFirewallRuleEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFirewallRuleEndpointRequest from a JSON string
post_firewall_rule_endpoint_request_instance = PostFirewallRuleEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostFirewallRuleEndpointRequest.to_json())

# convert the object into a dict
post_firewall_rule_endpoint_request_dict = post_firewall_rule_endpoint_request_instance.to_dict()
# create an instance of PostFirewallRuleEndpointRequest from a dict
post_firewall_rule_endpoint_request_from_dict = PostFirewallRuleEndpointRequest.from_dict(post_firewall_rule_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


