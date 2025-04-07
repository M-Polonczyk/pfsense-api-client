# PostSystemCertificatePKCS12ExportEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certref** | **str** | The Certificate to export as a PKCS12 file.&lt;br&gt; | 
**encryption** | **str** | The level of encryption to use when exporting the PKCS#12 archive.&lt;br&gt; | [optional] [default to 'high']
**passphrase** | **str** | The passphrase to use when exporting the PKCS#12 archive. Leave empty for no passphrase.&lt;br&gt; | [optional] 
**filename** | **str** | The filename used when exporting the PKCS#12 archive. This value cannot be changed and will always be certificate refid with the .p12 extension.&lt;br&gt; | [optional] [readonly] 
**binary_data** | **str** | The PKCS#12 archive binary data. This value cannot be changed.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.post_system_certificate_pkcs12_export_endpoint_request import PostSystemCertificatePKCS12ExportEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSystemCertificatePKCS12ExportEndpointRequest from a JSON string
post_system_certificate_pkcs12_export_endpoint_request_instance = PostSystemCertificatePKCS12ExportEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostSystemCertificatePKCS12ExportEndpointRequest.to_json())

# convert the object into a dict
post_system_certificate_pkcs12_export_endpoint_request_dict = post_system_certificate_pkcs12_export_endpoint_request_instance.to_dict()
# create an instance of PostSystemCertificatePKCS12ExportEndpointRequest from a dict
post_system_certificate_pkcs12_export_endpoint_request_from_dict = PostSystemCertificatePKCS12ExportEndpointRequest.from_dict(post_system_certificate_pkcs12_export_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


