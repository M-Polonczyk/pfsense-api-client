# IPsecApply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; when all IPsec changes are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending IPsec changes that have not been applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.i_psec_apply import IPsecApply

# TODO update the JSON string below
json = "{}"
# create an instance of IPsecApply from a JSON string
i_psec_apply_instance = IPsecApply.from_json(json)
# print the JSON string representation of the object
print(IPsecApply.to_json())

# convert the object into a dict
i_psec_apply_dict = i_psec_apply_instance.to_dict()
# create an instance of IPsecApply from a dict
i_psec_apply_from_dict = IPsecApply.from_dict(i_psec_apply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


