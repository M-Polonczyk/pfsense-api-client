# PostServicesHAProxyFrontendCertificateEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssl_certificate** | **str** | The SSL/TLS certificate refid to add to this frontend.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 

## Example

```python
from pfsense_api_client.models.post_services_ha_proxy_frontend_certificate_endpoint_request import PostServicesHAProxyFrontendCertificateEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesHAProxyFrontendCertificateEndpointRequest from a JSON string
post_services_ha_proxy_frontend_certificate_endpoint_request_instance = PostServicesHAProxyFrontendCertificateEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesHAProxyFrontendCertificateEndpointRequest.to_json())

# convert the object into a dict
post_services_ha_proxy_frontend_certificate_endpoint_request_dict = post_services_ha_proxy_frontend_certificate_endpoint_request_instance.to_dict()
# create an instance of PostServicesHAProxyFrontendCertificateEndpointRequest from a dict
post_services_ha_proxy_frontend_certificate_endpoint_request_from_dict = PostServicesHAProxyFrontendCertificateEndpointRequest.from_dict(post_services_ha_proxy_frontend_certificate_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


