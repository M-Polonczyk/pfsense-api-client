# HAProxyFrontendACL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this frontend ACL.&lt;br&gt; | [optional] 
**expression** | **str** | The expression to use to determine the match for this ACL.&lt;br&gt; | [optional] 
**value** | **str** | The value which indicates a match for this ACL.&lt;br&gt; | [optional] 
**casesensitive** | **bool** | Enables or disables case-sensitive matching for this ACL.&lt;br&gt; | [optional] 
**var_not** | **bool** | Enables or disables inverting the context of this ACL.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.ha_proxy_frontend_acl import HAProxyFrontendACL

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxyFrontendACL from a JSON string
ha_proxy_frontend_acl_instance = HAProxyFrontendACL.from_json(json)
# print the JSON string representation of the object
print(HAProxyFrontendACL.to_json())

# convert the object into a dict
ha_proxy_frontend_acl_dict = ha_proxy_frontend_acl_instance.to_dict()
# create an instance of HAProxyFrontendACL from a dict
ha_proxy_frontend_acl_from_dict = HAProxyFrontendACL.from_dict(ha_proxy_frontend_acl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


