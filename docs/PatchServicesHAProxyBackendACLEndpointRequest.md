# PatchServicesHAProxyBackendACLEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this backend ACL.&lt;br&gt; | [optional] 
**expression** | **str** | The expression to use to determine the match for this ACL.&lt;br&gt; | [optional] 
**value** | **str** | The value which indicates a match for this ACL.&lt;br&gt; | [optional] 
**casesensitive** | **bool** | Enables or disables case-sensitive matching for this ACL.&lt;br&gt; | [optional] 
**var_not** | **bool** | Enables or disables inverting the context of this ACL.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_ha_proxy_backend_acl_endpoint_request import PatchServicesHAProxyBackendACLEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesHAProxyBackendACLEndpointRequest from a JSON string
patch_services_ha_proxy_backend_acl_endpoint_request_instance = PatchServicesHAProxyBackendACLEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesHAProxyBackendACLEndpointRequest.to_json())

# convert the object into a dict
patch_services_ha_proxy_backend_acl_endpoint_request_dict = patch_services_ha_proxy_backend_acl_endpoint_request_instance.to_dict()
# create an instance of PatchServicesHAProxyBackendACLEndpointRequest from a dict
patch_services_ha_proxy_backend_acl_endpoint_request_from_dict = PatchServicesHAProxyBackendACLEndpointRequest.from_dict(patch_services_ha_proxy_backend_acl_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


