# RESTAPIAccessListEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of access this entry provides. \&quot;allow\&quot; entries permit access to the REST API from the specified networks. \&quot;deny\&quot; entries block access to the REST API from the specified networks.&lt;br&gt; | [optional] [default to 'allow']
**weight** | **int** | The weight of this entry. Entries with lower weights are evaluated first. If multiple entries match a request, the entry with the lowest weight will be applied.&lt;br&gt; | [optional] [default to 1]
**network** | **str** | The network (in CIDR notation) that this entry applies to. Clients interacting with the REST API from this network will be affected by this entry.&lt;br&gt; | [optional] 
**users** | **List[str]** | The users that this entry applies to. Only users in this list will be affected by this entry.&lt;br&gt; | [optional] 
**sched** | **str** | The firewall schedule that this entry will use. This entry will only be active during the                  times specified in the schedule. Leave empty to apply this entry at all times.&lt;br&gt; | [optional] 
**descr** | **str** | A description of this access list entry. This field is optional.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.restapi_access_list_entry import RESTAPIAccessListEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RESTAPIAccessListEntry from a JSON string
restapi_access_list_entry_instance = RESTAPIAccessListEntry.from_json(json)
# print the JSON string representation of the object
print(RESTAPIAccessListEntry.to_json())

# convert the object into a dict
restapi_access_list_entry_dict = restapi_access_list_entry_instance.to_dict()
# create an instance of RESTAPIAccessListEntry from a dict
restapi_access_list_entry_from_dict = RESTAPIAccessListEntry.from_dict(restapi_access_list_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


