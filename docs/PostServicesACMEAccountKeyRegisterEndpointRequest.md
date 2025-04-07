# PostServicesACMEAccountKeyRegisterEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the ACME account key to register.&lt;br&gt; | 
**status** | **str** | The registration status of the ACME account key. This will show &#39;pending&#39; if the registration process is still running, &#39;registered&#39; if the registration was successful, &#39;failed&#39; if the registration failed, and &#39;unknown&#39; if the registration status is not known. Note: This status can only be determined for registrations initiated through the REST API.&lt;br&gt; | [optional] [readonly] [default to 'unknown']

## Example

```python
from pfsense_api_client.models.post_services_acme_account_key_register_endpoint_request import PostServicesACMEAccountKeyRegisterEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesACMEAccountKeyRegisterEndpointRequest from a JSON string
post_services_acme_account_key_register_endpoint_request_instance = PostServicesACMEAccountKeyRegisterEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesACMEAccountKeyRegisterEndpointRequest.to_json())

# convert the object into a dict
post_services_acme_account_key_register_endpoint_request_dict = post_services_acme_account_key_register_endpoint_request_instance.to_dict()
# create an instance of PostServicesACMEAccountKeyRegisterEndpointRequest from a dict
post_services_acme_account_key_register_endpoint_request_from_dict = PostServicesACMEAccountKeyRegisterEndpointRequest.from_dict(post_services_acme_account_key_register_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


