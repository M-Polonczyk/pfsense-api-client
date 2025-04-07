# CertificatePKCS12Export


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certref** | **str** | The Certificate to export as a PKCS12 file.&lt;br&gt; | [optional] 
**encryption** | **str** | The level of encryption to use when exporting the PKCS#12 archive.&lt;br&gt; | [optional] [default to 'high']
**passphrase** | **str** | The passphrase to use when exporting the PKCS#12 archive. Leave empty for no passphrase.&lt;br&gt; | [optional] 
**filename** | **str** | The filename used when exporting the PKCS#12 archive. This value cannot be changed and will always be certificate refid with the .p12 extension.&lt;br&gt; | [optional] [readonly] 
**binary_data** | **str** | The PKCS#12 archive binary data. This value cannot be changed.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.certificate_pkcs12_export import CertificatePKCS12Export

# TODO update the JSON string below
json = "{}"
# create an instance of CertificatePKCS12Export from a JSON string
certificate_pkcs12_export_instance = CertificatePKCS12Export.from_json(json)
# print the JSON string representation of the object
print(CertificatePKCS12Export.to_json())

# convert the object into a dict
certificate_pkcs12_export_dict = certificate_pkcs12_export_instance.to_dict()
# create an instance of CertificatePKCS12Export from a dict
certificate_pkcs12_export_from_dict = CertificatePKCS12Export.from_dict(certificate_pkcs12_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


