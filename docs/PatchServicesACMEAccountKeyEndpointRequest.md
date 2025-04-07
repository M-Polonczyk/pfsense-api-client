# PatchServicesACMEAccountKeyEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the ACME account key.&lt;br&gt; | [optional] 
**descr** | **str** | A description of the ACME account key.&lt;br&gt; | [optional] 
**email** | **str** | The email address associated with the ACME account key.&lt;br&gt; | [optional] 
**acmeserver** | **str** | The ACME server this account key will belong to.&lt;br&gt; | [optional] 
**accountkey** | **str** | The RSA private key for the ACME account key.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_acme_account_key_endpoint_request import PatchServicesACMEAccountKeyEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesACMEAccountKeyEndpointRequest from a JSON string
patch_services_acme_account_key_endpoint_request_instance = PatchServicesACMEAccountKeyEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesACMEAccountKeyEndpointRequest.to_json())

# convert the object into a dict
patch_services_acme_account_key_endpoint_request_dict = patch_services_acme_account_key_endpoint_request_instance.to_dict()
# create an instance of PatchServicesACMEAccountKeyEndpointRequest from a dict
patch_services_acme_account_key_endpoint_request_from_dict = PatchServicesACMEAccountKeyEndpointRequest.from_dict(patch_services_acme_account_key_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


