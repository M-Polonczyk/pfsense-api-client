# PostServicesACMEAccountKeyEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the ACME account key.&lt;br&gt; | 
**descr** | **str** | A description of the ACME account key.&lt;br&gt; | [optional] 
**email** | **str** | The email address associated with the ACME account key.&lt;br&gt; | [optional] 
**acmeserver** | **str** | The ACME server this account key will belong to.&lt;br&gt; | 
**accountkey** | **str** | The RSA private key for the ACME account key.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_services_acme_account_key_endpoint_request import PostServicesACMEAccountKeyEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesACMEAccountKeyEndpointRequest from a JSON string
post_services_acme_account_key_endpoint_request_instance = PostServicesACMEAccountKeyEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesACMEAccountKeyEndpointRequest.to_json())

# convert the object into a dict
post_services_acme_account_key_endpoint_request_dict = post_services_acme_account_key_endpoint_request_instance.to_dict()
# create an instance of PostServicesACMEAccountKeyEndpointRequest from a dict
post_services_acme_account_key_endpoint_request_from_dict = PostServicesACMEAccountKeyEndpointRequest.from_dict(post_services_acme_account_key_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


