# DHCPServerNumberoptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | The DHCP option number to configure.&lt;br&gt; | 
**type** | **str** | The type of value to configure for the option.&lt;br&gt; | 
**value** | **str** | The value to configure for the option.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.dhcp_server_numberoptions_inner import DHCPServerNumberoptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPServerNumberoptionsInner from a JSON string
dhcp_server_numberoptions_inner_instance = DHCPServerNumberoptionsInner.from_json(json)
# print the JSON string representation of the object
print(DHCPServerNumberoptionsInner.to_json())

# convert the object into a dict
dhcp_server_numberoptions_inner_dict = dhcp_server_numberoptions_inner_instance.to_dict()
# create an instance of DHCPServerNumberoptionsInner from a dict
dhcp_server_numberoptions_inner_from_dict = DHCPServerNumberoptionsInner.from_dict(dhcp_server_numberoptions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


