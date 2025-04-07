# ACMECertificateAActionlistInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The activation status of the ACME certificate.&lt;br&gt; | [optional] [default to 'active']
**command** | **str** | The command to execute on the ACME certificate.&lt;br&gt; | 
**method** | **str** | The action method that should be used to run the command.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.acme_certificate_a_actionlist_inner import ACMECertificateAActionlistInner

# TODO update the JSON string below
json = "{}"
# create an instance of ACMECertificateAActionlistInner from a JSON string
acme_certificate_a_actionlist_inner_instance = ACMECertificateAActionlistInner.from_json(json)
# print the JSON string representation of the object
print(ACMECertificateAActionlistInner.to_json())

# convert the object into a dict
acme_certificate_a_actionlist_inner_dict = acme_certificate_a_actionlist_inner_instance.to_dict()
# create an instance of ACMECertificateAActionlistInner from a dict
acme_certificate_a_actionlist_inner_from_dict = ACMECertificateAActionlistInner.from_dict(acme_certificate_a_actionlist_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


