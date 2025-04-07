# PatchServicesHAProxyBackendErrorFileEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorcode** | **int** | The HTTP status code that will trigger this error file to be used.&lt;br&gt; | [optional] 
**errorfile** | **str** | The HAProxy error file object that should be used for the assigned HTTP status code.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_ha_proxy_backend_error_file_endpoint_request import PatchServicesHAProxyBackendErrorFileEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesHAProxyBackendErrorFileEndpointRequest from a JSON string
patch_services_ha_proxy_backend_error_file_endpoint_request_instance = PatchServicesHAProxyBackendErrorFileEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesHAProxyBackendErrorFileEndpointRequest.to_json())

# convert the object into a dict
patch_services_ha_proxy_backend_error_file_endpoint_request_dict = patch_services_ha_proxy_backend_error_file_endpoint_request_instance.to_dict()
# create an instance of PatchServicesHAProxyBackendErrorFileEndpointRequest from a dict
patch_services_ha_proxy_backend_error_file_endpoint_request_from_dict = PatchServicesHAProxyBackendErrorFileEndpointRequest.from_dict(patch_services_ha_proxy_backend_error_file_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


