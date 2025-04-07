# PostSystemCertificateRenewEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certref** | **str** | The &#x60;refid&#x60; of the Certificate to renew.&lt;br&gt; | 
**reusekey** | **bool** | Reuses the existing private key when renewing the certificate.&lt;br&gt; | [optional] [default to True]
**reuseserial** | **bool** | Reuses the existing serial number when renewing the certificate.&lt;br&gt; | [optional] [default to True]
**strictsecurity** | **bool** | Enforces strict security measures when renewing the certificate.&lt;br&gt; | [optional] 
**oldserial** | **str** | The old serial number of the Certificate before the renewal.&lt;br&gt; | [optional] [readonly] 
**newserial** | **str** | The new serial number of the Certificate after the renewal.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.post_system_certificate_renew_endpoint_request import PostSystemCertificateRenewEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSystemCertificateRenewEndpointRequest from a JSON string
post_system_certificate_renew_endpoint_request_instance = PostSystemCertificateRenewEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostSystemCertificateRenewEndpointRequest.to_json())

# convert the object into a dict
post_system_certificate_renew_endpoint_request_dict = post_system_certificate_renew_endpoint_request_instance.to_dict()
# create an instance of PostSystemCertificateRenewEndpointRequest from a dict
post_system_certificate_renew_endpoint_request_from_dict = PostSystemCertificateRenewEndpointRequest.from_dict(post_system_certificate_renew_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


