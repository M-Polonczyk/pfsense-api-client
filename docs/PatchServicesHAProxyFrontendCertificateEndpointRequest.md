# PatchServicesHAProxyFrontendCertificateEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssl_certificate** | **str** | The SSL/TLS certificate refid to add to this frontend.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_ha_proxy_frontend_certificate_endpoint_request import PatchServicesHAProxyFrontendCertificateEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesHAProxyFrontendCertificateEndpointRequest from a JSON string
patch_services_ha_proxy_frontend_certificate_endpoint_request_instance = PatchServicesHAProxyFrontendCertificateEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesHAProxyFrontendCertificateEndpointRequest.to_json())

# convert the object into a dict
patch_services_ha_proxy_frontend_certificate_endpoint_request_dict = patch_services_ha_proxy_frontend_certificate_endpoint_request_instance.to_dict()
# create an instance of PatchServicesHAProxyFrontendCertificateEndpointRequest from a dict
patch_services_ha_proxy_frontend_certificate_endpoint_request_from_dict = PatchServicesHAProxyFrontendCertificateEndpointRequest.from_dict(patch_services_ha_proxy_frontend_certificate_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


