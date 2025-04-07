# CertificateRenew


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certref** | **str** | The &#x60;refid&#x60; of the Certificate to renew.&lt;br&gt; | [optional] 
**reusekey** | **bool** | Reuses the existing private key when renewing the certificate.&lt;br&gt; | [optional] [default to True]
**reuseserial** | **bool** | Reuses the existing serial number when renewing the certificate.&lt;br&gt; | [optional] [default to True]
**strictsecurity** | **bool** | Enforces strict security measures when renewing the certificate.&lt;br&gt; | [optional] 
**oldserial** | **str** | The old serial number of the Certificate before the renewal.&lt;br&gt; | [optional] [readonly] 
**newserial** | **str** | The new serial number of the Certificate after the renewal.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.certificate_renew import CertificateRenew

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateRenew from a JSON string
certificate_renew_instance = CertificateRenew.from_json(json)
# print the JSON string representation of the object
print(CertificateRenew.to_json())

# convert the object into a dict
certificate_renew_dict = certificate_renew_instance.to_dict()
# create an instance of CertificateRenew from a dict
certificate_renew_from_dict = CertificateRenew.from_dict(certificate_renew_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


