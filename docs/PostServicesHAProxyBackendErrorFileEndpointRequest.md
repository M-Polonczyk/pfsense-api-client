# PostServicesHAProxyBackendErrorFileEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorcode** | **int** | The HTTP status code that will trigger this error file to be used.&lt;br&gt; | 
**errorfile** | **str** | The HAProxy error file object that should be used for the assigned HTTP status code.&lt;br&gt; | 
**parent_id** | **int** | The ID of the parent this object is nested under. | 

## Example

```python
from pfsense_api_client.models.post_services_ha_proxy_backend_error_file_endpoint_request import PostServicesHAProxyBackendErrorFileEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesHAProxyBackendErrorFileEndpointRequest from a JSON string
post_services_ha_proxy_backend_error_file_endpoint_request_instance = PostServicesHAProxyBackendErrorFileEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesHAProxyBackendErrorFileEndpointRequest.to_json())

# convert the object into a dict
post_services_ha_proxy_backend_error_file_endpoint_request_dict = post_services_ha_proxy_backend_error_file_endpoint_request_instance.to_dict()
# create an instance of PostServicesHAProxyBackendErrorFileEndpointRequest from a dict
post_services_ha_proxy_backend_error_file_endpoint_request_from_dict = PostServicesHAProxyBackendErrorFileEndpointRequest.from_dict(post_services_ha_proxy_backend_error_file_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


