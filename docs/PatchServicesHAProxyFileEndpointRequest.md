# PatchServicesHAProxyFileEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this file.&lt;br&gt; | [optional] 
**type** | **str** | The type of file. Use &#x60;null&#x60; to assume an Errorfile.&lt;br&gt; | [optional] 
**content** | **str** | The content of this file.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_ha_proxy_file_endpoint_request import PatchServicesHAProxyFileEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesHAProxyFileEndpointRequest from a JSON string
patch_services_ha_proxy_file_endpoint_request_instance = PatchServicesHAProxyFileEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesHAProxyFileEndpointRequest.to_json())

# convert the object into a dict
patch_services_ha_proxy_file_endpoint_request_dict = patch_services_ha_proxy_file_endpoint_request_instance.to_dict()
# create an instance of PatchServicesHAProxyFileEndpointRequest from a dict
patch_services_ha_proxy_file_endpoint_request_from_dict = PatchServicesHAProxyFileEndpointRequest.from_dict(patch_services_ha_proxy_file_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


