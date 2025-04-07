# HAProxyBackendACL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this backend ACL.&lt;br&gt; | [optional] 
**expression** | **str** | The expression to use to determine the match for this ACL.&lt;br&gt; | [optional] 
**value** | **str** | The value which indicates a match for this ACL.&lt;br&gt; | [optional] 
**casesensitive** | **bool** | Enables or disables case-sensitive matching for this ACL.&lt;br&gt; | [optional] 
**var_not** | **bool** | Enables or disables inverting the context of this ACL.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.ha_proxy_backend_acl import HAProxyBackendACL

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxyBackendACL from a JSON string
ha_proxy_backend_acl_instance = HAProxyBackendACL.from_json(json)
# print the JSON string representation of the object
print(HAProxyBackendACL.to_json())

# convert the object into a dict
ha_proxy_backend_acl_dict = ha_proxy_backend_acl_instance.to_dict()
# create an instance of HAProxyBackendACL from a dict
ha_proxy_backend_acl_from_dict = HAProxyBackendACL.from_dict(ha_proxy_backend_acl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


