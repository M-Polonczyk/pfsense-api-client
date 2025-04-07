# DHCPServerCustomOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | The DHCP option number to configure.&lt;br&gt; | [optional] 
**type** | **str** | The type of value to configure for the option.&lt;br&gt; | [optional] 
**value** | **str** | The value to configure for the option.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.dhcp_server_custom_option import DHCPServerCustomOption

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPServerCustomOption from a JSON string
dhcp_server_custom_option_instance = DHCPServerCustomOption.from_json(json)
# print the JSON string representation of the object
print(DHCPServerCustomOption.to_json())

# convert the object into a dict
dhcp_server_custom_option_dict = dhcp_server_custom_option_instance.to_dict()
# create an instance of DHCPServerCustomOption from a dict
dhcp_server_custom_option_from_dict = DHCPServerCustomOption.from_dict(dhcp_server_custom_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


