# CARP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enables or disables CARP on this system.&lt;br&gt; | [optional] 
**maintenance_mode** | **bool** | Enables or disables CARP maintenance mode on this system.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.carp import CARP

# TODO update the JSON string below
json = "{}"
# create an instance of CARP from a JSON string
carp_instance = CARP.from_json(json)
# print the JSON string representation of the object
print(CARP.to_json())

# convert the object into a dict
carp_dict = carp_instance.to_dict()
# create an instance of CARP from a dict
carp_from_dict = CARP.from_dict(carp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


