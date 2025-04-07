# ACMECertificateIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | The name of the ACME certificate to be issued.&lt;br&gt; | [optional] 
**status** | **str** | The status of the ACME certificate issue process. This will show &#39;pending&#39; if the issue process is still running or &#39;completed&#39; if the issue process has finished. This status only indicates whether the issue process has completed, not whether it was successful. You will needto refer to the result log for that information.&lt;br&gt; | [optional] [readonly] [default to 'pending']
**last_updated** | **int** | The unix timestamp of when the ACME certificate issue status last changed.&lt;br&gt; | [optional] [readonly] 
**result_log** | **str** | The output result of the acme.sh issue command.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.acme_certificate_issue import ACMECertificateIssue

# TODO update the JSON string below
json = "{}"
# create an instance of ACMECertificateIssue from a JSON string
acme_certificate_issue_instance = ACMECertificateIssue.from_json(json)
# print the JSON string representation of the object
print(ACMECertificateIssue.to_json())

# convert the object into a dict
acme_certificate_issue_dict = acme_certificate_issue_instance.to_dict()
# create an instance of ACMECertificateIssue from a dict
acme_certificate_issue_from_dict = ACMECertificateIssue.from_dict(acme_certificate_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


