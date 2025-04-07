# HAProxyApply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Indicates whether all HAProxy configuration changes have been applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.ha_proxy_apply import HAProxyApply

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxyApply from a JSON string
ha_proxy_apply_instance = HAProxyApply.from_json(json)
# print the JSON string representation of the object
print(HAProxyApply.to_json())

# convert the object into a dict
ha_proxy_apply_dict = ha_proxy_apply_instance.to_dict()
# create an instance of HAProxyApply from a dict
ha_proxy_apply_from_dict = HAProxyApply.from_dict(ha_proxy_apply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


