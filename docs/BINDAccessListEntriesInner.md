# BINDAccessListEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The network CIDR to allow.&lt;br&gt; | 
**description** | **str** | A description of the access list entry.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.bind_access_list_entries_inner import BINDAccessListEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BINDAccessListEntriesInner from a JSON string
bind_access_list_entries_inner_instance = BINDAccessListEntriesInner.from_json(json)
# print the JSON string representation of the object
print(BINDAccessListEntriesInner.to_json())

# convert the object into a dict
bind_access_list_entries_inner_dict = bind_access_list_entries_inner_instance.to_dict()
# create an instance of BINDAccessListEntriesInner from a dict
bind_access_list_entries_inner_from_dict = BINDAccessListEntriesInner.from_dict(bind_access_list_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


