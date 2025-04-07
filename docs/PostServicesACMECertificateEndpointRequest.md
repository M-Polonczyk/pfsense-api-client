# PostServicesACMECertificateEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the ACME certificate.&lt;br&gt; | 
**descr** | **str** | A description of the ACME certificate.&lt;br&gt; | [optional] 
**status** | **str** | The activation status of the ACME certificate.&lt;br&gt; | [optional] [default to 'active']
**acmeaccount** | **str** | The ACME account key to use for the ACME certificate.&lt;br&gt; | 
**keylength** | **str** | The length of the private key to use for the ACME certificate.&lt;br&gt; | [optional] [default to '2048']
**keypaste** | **str** | The custom private key to use for the ACME certificate.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;keylength&#x60; must be equal to &#x60;&#39;custom&#39;&#x60;&lt;br&gt; | 
**preferredchain** | **str** | The preferred certificate chain to use for the ACME certificate.&lt;br&gt; | [optional] 
**oscpstaple** | **bool** | Whether to enable OCSP Stapling for the ACME certificate.&lt;br&gt; | [optional] 
**dnssleep** | **int** | The number of seconds to wait for DNS propagation before requesting verification.&lt;br&gt; | [optional] 
**renewafter** | **int** | The number of days before expiration to renew the ACME certificate.&lt;br&gt; | [optional] [default to 60]
**a_domainlist** | [**List[ACMECertificateADomainlistInner]**](ACMECertificateADomainlistInner.md) | The list of domain verifications  to include in the ACME certificate.&lt;br&gt; | 
**a_actionlist** | [**List[ACMECertificateAActionlistInner]**](ACMECertificateAActionlistInner.md) | The list of actions to perform on the ACME certificate after being issued/renewed.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_services_acme_certificate_endpoint_request import PostServicesACMECertificateEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesACMECertificateEndpointRequest from a JSON string
post_services_acme_certificate_endpoint_request_instance = PostServicesACMECertificateEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesACMECertificateEndpointRequest.to_json())

# convert the object into a dict
post_services_acme_certificate_endpoint_request_dict = post_services_acme_certificate_endpoint_request_instance.to_dict()
# create an instance of PostServicesACMECertificateEndpointRequest from a dict
post_services_acme_certificate_endpoint_request_from_dict = PostServicesACMECertificateEndpointRequest.from_dict(post_services_acme_certificate_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


