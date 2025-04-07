# PostVPNIPsecApplyEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Displays &#x60;true&#x60; when all IPsec changes are applied and there are no pending changes left.Displays &#x60;false&#x60; when there are pending IPsec changes that have not been applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.post_vpni_psec_apply_endpoint_request import PostVPNIPsecApplyEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostVPNIPsecApplyEndpointRequest from a JSON string
post_vpni_psec_apply_endpoint_request_instance = PostVPNIPsecApplyEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostVPNIPsecApplyEndpointRequest.to_json())

# convert the object into a dict
post_vpni_psec_apply_endpoint_request_dict = post_vpni_psec_apply_endpoint_request_instance.to_dict()
# create an instance of PostVPNIPsecApplyEndpointRequest from a dict
post_vpni_psec_apply_endpoint_request_from_dict = PostVPNIPsecApplyEndpointRequest.from_dict(post_vpni_psec_apply_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


