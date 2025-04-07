# PatchSystemCRLRevokedCertificateEndpointRequest


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
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_system_crl_revoked_certificate_endpoint_request import PatchSystemCRLRevokedCertificateEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSystemCRLRevokedCertificateEndpointRequest from a JSON string
patch_system_crl_revoked_certificate_endpoint_request_instance = PatchSystemCRLRevokedCertificateEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchSystemCRLRevokedCertificateEndpointRequest.to_json())

# convert the object into a dict
patch_system_crl_revoked_certificate_endpoint_request_dict = patch_system_crl_revoked_certificate_endpoint_request_instance.to_dict()
# create an instance of PatchSystemCRLRevokedCertificateEndpointRequest from a dict
patch_system_crl_revoked_certificate_endpoint_request_from_dict = PatchSystemCRLRevokedCertificateEndpointRequest.from_dict(patch_system_crl_revoked_certificate_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


