# PatchServicesACMECertificateEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the ACME certificate.&lt;br&gt; | [optional] 
**descr** | **str** | A description of the ACME certificate.&lt;br&gt; | [optional] 
**status** | **str** | The activation status of the ACME certificate.&lt;br&gt; | [optional] [default to 'active']
**acmeaccount** | **str** | The ACME account key to use for the ACME certificate.&lt;br&gt; | [optional] 
**keylength** | **str** | The length of the private key to use for the ACME certificate.&lt;br&gt; | [optional] [default to '2048']
**keypaste** | **str** | The custom private key to use for the ACME certificate.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;keylength&#x60; must be equal to &#x60;&#39;custom&#39;&#x60;&lt;br&gt; | [optional] 
**preferredchain** | **str** | The preferred certificate chain to use for the ACME certificate.&lt;br&gt; | [optional] 
**oscpstaple** | **bool** | Whether to enable OCSP Stapling for the ACME certificate.&lt;br&gt; | [optional] 
**dnssleep** | **int** | The number of seconds to wait for DNS propagation before requesting verification.&lt;br&gt; | [optional] 
**renewafter** | **int** | The number of days before expiration to renew the ACME certificate.&lt;br&gt; | [optional] [default to 60]
**a_domainlist** | [**List[ACMECertificateADomainlistInner]**](ACMECertificateADomainlistInner.md) | The list of domain verifications  to include in the ACME certificate.&lt;br&gt; | [optional] 
**a_actionlist** | [**List[ACMECertificateAActionlistInner]**](ACMECertificateAActionlistInner.md) | The list of actions to perform on the ACME certificate after being issued/renewed.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_acme_certificate_endpoint_request import PatchServicesACMECertificateEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesACMECertificateEndpointRequest from a JSON string
patch_services_acme_certificate_endpoint_request_instance = PatchServicesACMECertificateEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesACMECertificateEndpointRequest.to_json())

# convert the object into a dict
patch_services_acme_certificate_endpoint_request_dict = patch_services_acme_certificate_endpoint_request_instance.to_dict()
# create an instance of PatchServicesACMECertificateEndpointRequest from a dict
patch_services_acme_certificate_endpoint_request_from_dict = PatchServicesACMECertificateEndpointRequest.from_dict(patch_services_acme_certificate_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


