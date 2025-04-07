# DHCPServerApply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; if all DHCP server changes are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending DHCP server changes that have not been applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.dhcp_server_apply import DHCPServerApply

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPServerApply from a JSON string
dhcp_server_apply_instance = DHCPServerApply.from_json(json)
# print the JSON string representation of the object
print(DHCPServerApply.to_json())

# convert the object into a dict
dhcp_server_apply_dict = dhcp_server_apply_instance.to_dict()
# create an instance of DHCPServerApply from a dict
dhcp_server_apply_from_dict = DHCPServerApply.from_dict(dhcp_server_apply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


