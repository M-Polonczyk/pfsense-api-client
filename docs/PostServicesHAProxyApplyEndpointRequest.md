# PostServicesHAProxyApplyEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Indicates whether all HAProxy configuration changes have been applied.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.post_services_ha_proxy_apply_endpoint_request import PostServicesHAProxyApplyEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesHAProxyApplyEndpointRequest from a JSON string
post_services_ha_proxy_apply_endpoint_request_instance = PostServicesHAProxyApplyEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesHAProxyApplyEndpointRequest.to_json())

# convert the object into a dict
post_services_ha_proxy_apply_endpoint_request_dict = post_services_ha_proxy_apply_endpoint_request_instance.to_dict()
# create an instance of PostServicesHAProxyApplyEndpointRequest from a dict
post_services_ha_proxy_apply_endpoint_request_from_dict = PostServicesHAProxyApplyEndpointRequest.from_dict(post_services_ha_proxy_apply_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


