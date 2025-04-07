# PatchFirewallAliasEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sets the name for the alias. This name must be unique from all other aliases.&lt;br&gt; | [optional] 
**type** | **str** | Sets the type of alias this object will be. This directly impacts what values can be                 specified in the &#x60;address&#x60; field.&lt;br&gt; | [optional] 
**descr** | **str** | Sets a description to help specify the purpose or contents of the alias.&lt;br&gt; | [optional] 
**address** | **List[str]** | Sets the host, network or port entries for the alias. When &#x60;type&#x60; is set to &#x60;host&#x60;, each                 entry must be a valid IP address or FQDN. When &#x60;type&#x60; is set to &#x60;network&#x60;, each entry must be a valid                 network CIDR or FQDN. When &#x60;type&#x60; is set to &#x60;port&#x60;, each entry must be a valid port or port range. You                 may also specify an existing alias&#39;s &#x60;name&#x60; as an entry to created nested aliases.&lt;br&gt; | [optional] 
**detail** | **List[str]** | Sets descriptions for each alias &#x60;address&#x60;. Values must match the order of the &#x60;address&#x60;                  value it relates to. For example, the first value specified here is the description for the first                 value specified in the &#x60;address&#x60; field. This value cannot contain &lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_firewall_alias_endpoint_request import PatchFirewallAliasEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFirewallAliasEndpointRequest from a JSON string
patch_firewall_alias_endpoint_request_instance = PatchFirewallAliasEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchFirewallAliasEndpointRequest.to_json())

# convert the object into a dict
patch_firewall_alias_endpoint_request_dict = patch_firewall_alias_endpoint_request_instance.to_dict()
# create an instance of PatchFirewallAliasEndpointRequest from a dict
patch_firewall_alias_endpoint_request_from_dict = PatchFirewallAliasEndpointRequest.from_dict(patch_firewall_alias_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


