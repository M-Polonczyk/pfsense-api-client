# PatchServicesACMECertificateActionEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The activation status of the ACME certificate.&lt;br&gt; | [optional] [default to 'active']
**command** | **str** | The command to execute on the ACME certificate.&lt;br&gt; | [optional] 
**method** | **str** | The action method that should be used to run the command.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_acme_certificate_action_endpoint_request import PatchServicesACMECertificateActionEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesACMECertificateActionEndpointRequest from a JSON string
patch_services_acme_certificate_action_endpoint_request_instance = PatchServicesACMECertificateActionEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesACMECertificateActionEndpointRequest.to_json())

# convert the object into a dict
patch_services_acme_certificate_action_endpoint_request_dict = patch_services_acme_certificate_action_endpoint_request_instance.to_dict()
# create an instance of PatchServicesACMECertificateActionEndpointRequest from a dict
patch_services_acme_certificate_action_endpoint_request_from_dict = PatchServicesACMECertificateActionEndpointRequest.from_dict(patch_services_acme_certificate_action_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


