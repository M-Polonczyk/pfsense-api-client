# PostServicesHAProxyFileEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this file.&lt;br&gt; | 
**type** | **str** | The type of file. Use &#x60;null&#x60; to assume an Errorfile.&lt;br&gt; | [optional] 
**content** | **str** | The content of this file.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.post_services_ha_proxy_file_endpoint_request import PostServicesHAProxyFileEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesHAProxyFileEndpointRequest from a JSON string
post_services_ha_proxy_file_endpoint_request_instance = PostServicesHAProxyFileEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesHAProxyFileEndpointRequest.to_json())

# convert the object into a dict
post_services_ha_proxy_file_endpoint_request_dict = post_services_ha_proxy_file_endpoint_request_instance.to_dict()
# create an instance of PostServicesHAProxyFileEndpointRequest from a dict
post_services_ha_proxy_file_endpoint_request_from_dict = PostServicesHAProxyFileEndpointRequest.from_dict(post_services_ha_proxy_file_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


