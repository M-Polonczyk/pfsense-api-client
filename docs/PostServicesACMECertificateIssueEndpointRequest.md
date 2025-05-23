# PostServicesACMECertificateIssueEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | The name of the ACME certificate to be issued.&lt;br&gt; | 
**status** | **str** | The status of the ACME certificate issue process. This will show &#39;pending&#39; if the issue process is still running or &#39;completed&#39; if the issue process has finished. This status only indicates whether the issue process has completed, not whether it was successful. You will needto refer to the result log for that information.&lt;br&gt; | [optional] [readonly] [default to 'pending']
**last_updated** | **int** | The unix timestamp of when the ACME certificate issue status last changed.&lt;br&gt; | [optional] [readonly] 
**result_log** | **str** | The output result of the acme.sh issue command.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.post_services_acme_certificate_issue_endpoint_request import PostServicesACMECertificateIssueEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesACMECertificateIssueEndpointRequest from a JSON string
post_services_acme_certificate_issue_endpoint_request_instance = PostServicesACMECertificateIssueEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesACMECertificateIssueEndpointRequest.to_json())

# convert the object into a dict
post_services_acme_certificate_issue_endpoint_request_dict = post_services_acme_certificate_issue_endpoint_request_instance.to_dict()
# create an instance of PostServicesACMECertificateIssueEndpointRequest from a dict
post_services_acme_certificate_issue_endpoint_request_from_dict = PostServicesACMECertificateIssueEndpointRequest.from_dict(post_services_acme_certificate_issue_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


