# PatchUserGroupEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for this user group.&lt;br&gt; | [optional] 
**gid** | **int** | The GID of this user group. This value is automatically assigned and cannot be changed.&lt;br&gt; | [optional] [readonly] [default to 2000]
**scope** | **str** | The scope of this user group. Use &#x60;local&#x60; for user groups that only apply to this system. use &#x60;remote&#x60; for groups that also apply to remote authentication servers.&lt;br&gt; | [optional] [default to 'local']
**description** | **str** | The description to assign to this user group.&lt;br&gt; | [optional] 
**member** | **List[str]** | The local user names to assign to this user group.&lt;br&gt; | [optional] 
**priv** | **List[str]** | The privileges to assign to this user group.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_user_group_endpoint_request import PatchUserGroupEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchUserGroupEndpointRequest from a JSON string
patch_user_group_endpoint_request_instance = PatchUserGroupEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchUserGroupEndpointRequest.to_json())

# convert the object into a dict
patch_user_group_endpoint_request_dict = patch_user_group_endpoint_request_instance.to_dict()
# create an instance of PatchUserGroupEndpointRequest from a dict
patch_user_group_endpoint_request_from_dict = PatchUserGroupEndpointRequest.from_dict(patch_user_group_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


