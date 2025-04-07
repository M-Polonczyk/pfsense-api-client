# CertificateRevocationListRevokedCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certref** | **str** | The reference ID of the certificate to be revoked&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;serial&#x60; must be equal to &#x60;NULL&#x60;&lt;br&gt; | [optional] 
**serial** | **str** | The serial number of the certificate to be revoked.&lt;br&gt; | [optional] 
**reason** | **int** | The CRL reason for revocation code.&lt;br&gt; | [optional] 
**revoke_time** | **int** | The unix timestamp of when the certificate was revoked.&lt;br&gt; | [optional] 
**caref** | **str** | The unique ID of the CA that signed the revoked certificate.&lt;br&gt; | [optional] 
**descr** | **str** | The unique name/description for this CRL.&lt;br&gt; | [optional] 
**type** | **str** | The type of the certificate to be revoked.&lt;br&gt; | [optional] 
**crt** | **str** | The X509 certificate string.&lt;br&gt; | [optional] 
**prv** | **str** | The X509 private key string.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.certificate_revocation_list_revoked_certificate import CertificateRevocationListRevokedCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateRevocationListRevokedCertificate from a JSON string
certificate_revocation_list_revoked_certificate_instance = CertificateRevocationListRevokedCertificate.from_json(json)
# print the JSON string representation of the object
print(CertificateRevocationListRevokedCertificate.to_json())

# convert the object into a dict
certificate_revocation_list_revoked_certificate_dict = certificate_revocation_list_revoked_certificate_instance.to_dict()
# create an instance of CertificateRevocationListRevokedCertificate from a dict
certificate_revocation_list_revoked_certificate_from_dict = CertificateRevocationListRevokedCertificate.from_dict(certificate_revocation_list_revoked_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


