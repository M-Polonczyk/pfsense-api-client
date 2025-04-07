# PostSystemTunableEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tunable** | **str** | The name of the tunable to set.&lt;br&gt; | 
**value** | **str** | The value to assign this tunable.&lt;br&gt; | 
**descr** | **str** | A description for this tunable.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_system_tunable_endpoint_request import PostSystemTunableEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSystemTunableEndpointRequest from a JSON string
post_system_tunable_endpoint_request_instance = PostSystemTunableEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostSystemTunableEndpointRequest.to_json())

# convert the object into a dict
post_system_tunable_endpoint_request_dict = post_system_tunable_endpoint_request_instance.to_dict()
# create an instance of PostSystemTunableEndpointRequest from a dict
post_system_tunable_endpoint_request_from_dict = PostSystemTunableEndpointRequest.from_dict(post_system_tunable_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


