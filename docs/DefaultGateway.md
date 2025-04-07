# DefaultGateway


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultgw4** | **str** | The gateway to assigns as the default IPv4 gateway for this system. Leave blank to automatically determine the default gateway, or set to &#x60;-&#x60; to assign no gateway.&lt;br&gt; | [optional] 
**defaultgw6** | **str** | The gateway to assigns as the default IPv6 gateway for this system. Leave blank to automatically determine the default gateway, or set to &#x60;-&#x60; to assign no gateway.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.default_gateway import DefaultGateway

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultGateway from a JSON string
default_gateway_instance = DefaultGateway.from_json(json)
# print the JSON string representation of the object
print(DefaultGateway.to_json())

# convert the object into a dict
default_gateway_dict = default_gateway_instance.to_dict()
# create an instance of DefaultGateway from a dict
default_gateway_from_dict = DefaultGateway.from_dict(default_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


