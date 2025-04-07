# PostServicesDHCPServerApplyEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; if all DHCP server changes are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending DHCP server changes that have not been applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.post_services_dhcp_server_apply_endpoint_request import PostServicesDHCPServerApplyEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesDHCPServerApplyEndpointRequest from a JSON string
post_services_dhcp_server_apply_endpoint_request_instance = PostServicesDHCPServerApplyEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesDHCPServerApplyEndpointRequest.to_json())

# convert the object into a dict
post_services_dhcp_server_apply_endpoint_request_dict = post_services_dhcp_server_apply_endpoint_request_instance.to_dict()
# create an instance of PostServicesDHCPServerApplyEndpointRequest from a dict
post_services_dhcp_server_apply_endpoint_request_from_dict = PostServicesDHCPServerApplyEndpointRequest.from_dict(post_services_dhcp_server_apply_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


