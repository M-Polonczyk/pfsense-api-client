# PostServicesACMECertificateActionEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The activation status of the ACME certificate.&lt;br&gt; | [optional] [default to 'active']
**command** | **str** | The command to execute on the ACME certificate.&lt;br&gt; | 
**method** | **str** | The action method that should be used to run the command.&lt;br&gt; | 
**parent_id** | **int** | The ID of the parent this object is nested under. | 

## Example

```python
from pfsense_api_client.models.post_services_acme_certificate_action_endpoint_request import PostServicesACMECertificateActionEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesACMECertificateActionEndpointRequest from a JSON string
post_services_acme_certificate_action_endpoint_request_instance = PostServicesACMECertificateActionEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesACMECertificateActionEndpointRequest.to_json())

# convert the object into a dict
post_services_acme_certificate_action_endpoint_request_dict = post_services_acme_certificate_action_endpoint_request_instance.to_dict()
# create an instance of PostServicesACMECertificateActionEndpointRequest from a dict
post_services_acme_certificate_action_endpoint_request_from_dict = PostServicesACMECertificateActionEndpointRequest.from_dict(post_services_acme_certificate_action_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


