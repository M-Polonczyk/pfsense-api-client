# ACMECertificateRenew


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | The name of the ACME certificate to be renewed.&lt;br&gt; | [optional] 
**status** | **str** | The status of the ACME certificate renew process. This will show &#39;pending&#39; if the renew process is still running or &#39;completed&#39; if the renew process has finished. This status only indicates whether the renew process has completed, not whether it was successful. You will needto refer to the result log for that information. Note: This log is only populated when the renew process is initiated via REST API, not when it is initiated via the pfSense webConfigurator or auto-renewals.&lt;br&gt; | [optional] [readonly] [default to 'pending']
**last_updated** | **int** | The unix timestamp of when the ACME certificate renew status last changed. Note: This timestamp is only updated when the renew process is initiated via REST API, not when it is initiated via the pfSense webConfigurator or auto-renewals.&lt;br&gt; | [optional] [readonly] 
**result_log** | **str** | The output result of the acme.sh renew command. Note: This log is only populated when the renew process is initiated via REST API, not when it is initiated via the pfSense webConfigurator or auto-renewals.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.acme_certificate_renew import ACMECertificateRenew

# TODO update the JSON string below
json = "{}"
# create an instance of ACMECertificateRenew from a JSON string
acme_certificate_renew_instance = ACMECertificateRenew.from_json(json)
# print the JSON string representation of the object
print(ACMECertificateRenew.to_json())

# convert the object into a dict
acme_certificate_renew_dict = acme_certificate_renew_instance.to_dict()
# create an instance of ACMECertificateRenew from a dict
acme_certificate_renew_from_dict = ACMECertificateRenew.from_dict(acme_certificate_renew_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


