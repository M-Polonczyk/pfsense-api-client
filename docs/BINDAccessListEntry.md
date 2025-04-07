# BINDAccessListEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The network CIDR to allow.&lt;br&gt; | [optional] 
**description** | **str** | A description of the access list entry.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.bind_access_list_entry import BINDAccessListEntry

# TODO update the JSON string below
json = "{}"
# create an instance of BINDAccessListEntry from a JSON string
bind_access_list_entry_instance = BINDAccessListEntry.from_json(json)
# print the JSON string representation of the object
print(BINDAccessListEntry.to_json())

# convert the object into a dict
bind_access_list_entry_dict = bind_access_list_entry_instance.to_dict()
# create an instance of BINDAccessListEntry from a dict
bind_access_list_entry_from_dict = BINDAccessListEntry.from_dict(bind_access_list_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


