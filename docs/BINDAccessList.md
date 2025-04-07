# BINDAccessList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the access list.&lt;br&gt; | [optional] 
**description** | **str** | A description for the access list.&lt;br&gt; | [optional] 
**entries** | [**List[BINDAccessListEntriesInner]**](BINDAccessListEntriesInner.md) | The network entries for this access list.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.bind_access_list import BINDAccessList

# TODO update the JSON string below
json = "{}"
# create an instance of BINDAccessList from a JSON string
bind_access_list_instance = BINDAccessList.from_json(json)
# print the JSON string representation of the object
print(BINDAccessList.to_json())

# convert the object into a dict
bind_access_list_dict = bind_access_list_instance.to_dict()
# create an instance of BINDAccessList from a dict
bind_access_list_from_dict = BINDAccessList.from_dict(bind_access_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


