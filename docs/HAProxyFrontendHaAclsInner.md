# HAProxyFrontendHaAclsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this frontend ACL.&lt;br&gt; | 
**expression** | **str** | The expression to use to determine the match for this ACL.&lt;br&gt; | 
**value** | **str** | The value which indicates a match for this ACL.&lt;br&gt; | 
**casesensitive** | **bool** | Enables or disables case-sensitive matching for this ACL.&lt;br&gt; | [optional] 
**var_not** | **bool** | Enables or disables inverting the context of this ACL.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.ha_proxy_frontend_ha_acls_inner import HAProxyFrontendHaAclsInner

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxyFrontendHaAclsInner from a JSON string
ha_proxy_frontend_ha_acls_inner_instance = HAProxyFrontendHaAclsInner.from_json(json)
# print the JSON string representation of the object
print(HAProxyFrontendHaAclsInner.to_json())

# convert the object into a dict
ha_proxy_frontend_ha_acls_inner_dict = ha_proxy_frontend_ha_acls_inner_instance.to_dict()
# create an instance of HAProxyFrontendHaAclsInner from a dict
ha_proxy_frontend_ha_acls_inner_from_dict = HAProxyFrontendHaAclsInner.from_dict(ha_proxy_frontend_ha_acls_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


