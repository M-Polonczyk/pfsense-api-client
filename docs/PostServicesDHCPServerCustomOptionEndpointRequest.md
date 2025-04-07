# PostServicesDHCPServerCustomOptionEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | The DHCP option number to configure.&lt;br&gt; | 
**type** | **str** | The type of value to configure for the option.&lt;br&gt; | 
**value** | **str** | The value to configure for the option.&lt;br&gt; | 
**parent_id** | **int** | The ID of the parent this object is nested under. | 

## Example

```python
from pfsense_api_client.models.post_services_dhcp_server_custom_option_endpoint_request import PostServicesDHCPServerCustomOptionEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesDHCPServerCustomOptionEndpointRequest from a JSON string
post_services_dhcp_server_custom_option_endpoint_request_instance = PostServicesDHCPServerCustomOptionEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesDHCPServerCustomOptionEndpointRequest.to_json())

# convert the object into a dict
post_services_dhcp_server_custom_option_endpoint_request_dict = post_services_dhcp_server_custom_option_endpoint_request_instance.to_dict()
# create an instance of PostServicesDHCPServerCustomOptionEndpointRequest from a dict
post_services_dhcp_server_custom_option_endpoint_request_from_dict = PostServicesDHCPServerCustomOptionEndpointRequest.from_dict(post_services_dhcp_server_custom_option_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


