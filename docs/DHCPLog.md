# DHCPLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The raw text of the DHCP log entry.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.dhcp_log import DHCPLog

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPLog from a JSON string
dhcp_log_instance = DHCPLog.from_json(json)
# print the JSON string representation of the object
print(DHCPLog.to_json())

# convert the object into a dict
dhcp_log_dict = dhcp_log_instance.to_dict()
# create an instance of DHCPLog from a dict
dhcp_log_from_dict = DHCPLog.from_dict(dhcp_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


