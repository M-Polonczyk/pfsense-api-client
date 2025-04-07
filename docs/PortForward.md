# PortForward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | The interface this port forward rule applies to.&lt;br&gt; | [optional] 
**ipprotocol** | **str** | The IP protocol this port forward rule should match.&lt;br&gt; | [optional] [default to 'inet']
**protocol** | **str** | The IP/transport protocol this port forward rule should match.&lt;br&gt; | [optional] 
**source** | **str** | The source address this port forward rule applies to. Valid value options are: an existing interface, an IP address, a subnet CIDR, an existing alias, &#x60;any&#x60;, &#x60;(self)&#x60;, &#x60;l2tp&#x60;, &#x60;pppoe&#x60;. The context of this address can be inverted by prefixing the value with &#x60;!&#x60;. For interface values, the &#x60;:ip&#x60;  modifier can be appended to the value to use the interface&#39;s IP address instead of its entire subnet.&lt;br&gt; | [optional] 
**source_port** | **str** | The source port this port forward rule applies to. Set to &#x60;null&#x60; to allow any source port. Valid options are: a TCP/UDP port number, a TCP/UDP port range separated by &#x60;:&#x60;, an existing port type firewall alias&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;protocol&#x60; must be one of [ tcp, udp, tcp/udp ]&lt;br&gt; | [optional] 
**destination** | **str** | The destination address this rule applies to. Valid value options are: an existing interface, an IP address, a subnet CIDR, an existing alias, &#x60;any&#x60;, &#x60;(self)&#x60;, &#x60;l2tp&#x60;, &#x60;pppoe&#x60;. The context of this address can be inverted by prefixing the value with &#x60;!&#x60;. For interface values, the &#x60;:ip&#x60;  modifier can be appended to the value to use the interface&#39;s IP address instead of its entire subnet.&lt;br&gt; | [optional] 
**destination_port** | **str** | The destination port this port forward rule applies to. Set to &#x60;null&#x60; to allow any destination port. Valid options are: a TCP/UDP port number, a TCP/UDP port range separated by &#x60;:&#x60;, an existing port type firewall alias&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;protocol&#x60; must be one of [ tcp, udp, tcp/udp ]&lt;br&gt; | [optional] 
**target** | **str** | The IP address or alias of the internal host to forward matching traffic to.&lt;br&gt; | [optional] 
**local_port** | **str** | The port on the internal host to forward matching traffic to. In most cases, this must match the &#x60;destination_port&#x60; value. In the event that the &#x60;desintation_port&#x60; is a range, this value should be the first value in that range. Valid options are: a TCP/UDP port number, an existing port type firewall alias&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;protocol&#x60; must be one of [ tcp, udp, tcp/udp ]&lt;br&gt; | [optional] 
**disabled** | **bool** | Disables this port forward rule.&lt;br&gt; | [optional] 
**nordr** | **bool** | Disables redirection for traffic matching this rule.&lt;br&gt; | [optional] 
**nosync** | **bool** | Prevents this port forward rule from being synced to non-primary CARP members.&lt;br&gt; | [optional] 
**descr** | **str** | A description for this port forward rule.&lt;br&gt; | [optional] 
**natreflection** | **str** | The NAT reflection mode to use for traffic matching this port forward rule. Set to &#x60;null&#x60; to use the system default.&lt;br&gt; | [optional] 
**associated_rule_id** | **str** | The associated firewall rule mode. Use an empty string to require a separate firewall rule to be created to pass traffic matching this port forward rule. Use &#x60;new&#x60; to create a new associated firewall rule to pass traffic matching this port forward rule. Use &#x60;pass&#x60; to automatically pass traffic matching this port forward rule without the need for a firewall rule.   Otherwise, you can specify the &#x60;associated_rule_id&#x60; of an existing firewall rule to associate with this port forward rule.&lt;br&gt; | [optional] 
**created_time** | **int** | The unix timestamp of when this port forward rule was original created.&lt;br&gt; | [optional] [readonly] 
**created_by** | **str** | The username and IP of the user who originally created this port forward rule.&lt;br&gt; | [optional] [readonly] [default to '@unknown IP (API)']
**updated_time** | **int** | The unix timestamp of when this port forward rule was original created.&lt;br&gt; | [optional] [readonly] 
**updated_by** | **str** | The username and IP of the user who last updated this port forward rule.&lt;br&gt; | [optional] [readonly] [default to '@unknown IP (API)']

## Example

```python
from pfsense_api_client.models.port_forward import PortForward

# TODO update the JSON string below
json = "{}"
# create an instance of PortForward from a JSON string
port_forward_instance = PortForward.from_json(json)
# print the JSON string representation of the object
print(PortForward.to_json())

# convert the object into a dict
port_forward_dict = port_forward_instance.to_dict()
# create an instance of PortForward from a dict
port_forward_from_dict = PortForward.from_dict(port_forward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


