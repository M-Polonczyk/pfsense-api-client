# PatchFirewallNATOneToOneMappingEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | The interface this 1:1 NAT mapping applies to.&lt;br&gt; | [optional] 
**disabled** | **bool** | Disables this 1:1 NAT mapping.&lt;br&gt; | [optional] 
**nobinat** | **bool** | Exclude traffic matching this mapping from a later, more general, mapping.&lt;br&gt; | [optional] 
**natreflection** | **str** | Enables or disables NAT reflection for traffic matching this mapping. Set to &#x60;null&#x60; to use the system default.&lt;br&gt; | [optional] 
**ipprotocol** | **str** | The IP version this mapping applies to.&lt;br&gt; | [optional] [default to 'inet']
**external** | **str** | The external IP address or interface for the 1:1 mapping. Valid value options are: an IP address. For interface values, the &#x60;:ip&#x60;  modifier can be appended to the value to use the interface&#39;s IP address instead of its entire subnet.&lt;br&gt; | [optional] 
**source** | **str** | The source IP address or subnet that traffic must match to apply this mapping. Valid value options are: an existing interface, an IP address, a subnet CIDR, &#x60;any&#x60;, &#x60;l2tp&#x60;, &#x60;pppoe&#x60;. The context of this address can be inverted by prefixing the value with &#x60;!&#x60;. For interface values, the &#x60;:ip&#x60;  modifier can be appended to the value to use the interface&#39;s IP address instead of its entire subnet.&lt;br&gt; | [optional] 
**destination** | **str** | The destination IP address or subnet that traffic must match to apply this mapping. Valid value options are: an existing interface, an IP address, a subnet CIDR, an existing alias, &#x60;any&#x60;, &#x60;l2tp&#x60;, &#x60;pppoe&#x60;. The context of this address can be inverted by prefixing the value with &#x60;!&#x60;. For interface values, the &#x60;:ip&#x60;  modifier can be appended to the value to use the interface&#39;s IP address instead of its entire subnet.&lt;br&gt; | [optional] 
**descr** | **str** | A description for this 1:1 NAT mapping&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_firewall_nat_one_to_one_mapping_endpoint_request import PatchFirewallNATOneToOneMappingEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFirewallNATOneToOneMappingEndpointRequest from a JSON string
patch_firewall_nat_one_to_one_mapping_endpoint_request_instance = PatchFirewallNATOneToOneMappingEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchFirewallNATOneToOneMappingEndpointRequest.to_json())

# convert the object into a dict
patch_firewall_nat_one_to_one_mapping_endpoint_request_dict = patch_firewall_nat_one_to_one_mapping_endpoint_request_instance.to_dict()
# create an instance of PatchFirewallNATOneToOneMappingEndpointRequest from a dict
patch_firewall_nat_one_to_one_mapping_endpoint_request_from_dict = PatchFirewallNATOneToOneMappingEndpointRequest.from_dict(patch_firewall_nat_one_to_one_mapping_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


