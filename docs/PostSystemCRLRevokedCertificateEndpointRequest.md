# PostSystemCRLRevokedCertificateEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certref** | **str** | The reference ID of the certificate to be revoked&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;serial&#x60; must be equal to &#x60;NULL&#x60;&lt;br&gt; | 
**serial** | **str** | The serial number of the certificate to be revoked.&lt;br&gt; | [optional] 
**reason** | **int** | The CRL reason for revocation code.&lt;br&gt; | [optional] 
**revoke_time** | **int** | The unix timestamp of when the certificate was revoked.&lt;br&gt; | 
**caref** | **str** | The unique ID of the CA that signed the revoked certificate.&lt;br&gt; | [optional] 
**descr** | **str** | The unique name/description for this CRL.&lt;br&gt; | [optional] 
**type** | **str** | The type of the certificate to be revoked.&lt;br&gt; | [optional] 
**crt** | **str** | The X509 certificate string.&lt;br&gt; | [optional] 
**prv** | **str** | The X509 private key string.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 

## Example

```python
from pfsense_api_client.models.post_system_crl_revoked_certificate_endpoint_request import PostSystemCRLRevokedCertificateEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSystemCRLRevokedCertificateEndpointRequest from a JSON string
post_system_crl_revoked_certificate_endpoint_request_instance = PostSystemCRLRevokedCertificateEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostSystemCRLRevokedCertificateEndpointRequest.to_json())

# convert the object into a dict
post_system_crl_revoked_certificate_endpoint_request_dict = post_system_crl_revoked_certificate_endpoint_request_instance.to_dict()
# create an instance of PostSystemCRLRevokedCertificateEndpointRequest from a dict
post_system_crl_revoked_certificate_endpoint_request_from_dict = PostSystemCRLRevokedCertificateEndpointRequest.from_dict(post_system_crl_revoked_certificate_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


