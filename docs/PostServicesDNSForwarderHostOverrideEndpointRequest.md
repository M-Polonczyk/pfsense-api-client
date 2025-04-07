# PostServicesDNSForwarderHostOverrideEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The hostname of this override.&lt;br&gt; | 
**domain** | **str** | The domain of this override.&lt;br&gt; | 
**ip** | **str** | The IP address of this override.&lt;br&gt; | 
**descr** | **str** | The description for this override.&lt;br&gt; | [optional] 
**aliases** | [**List[DNSForwarderHostOverrideAliasesInner]**](DNSForwarderHostOverrideAliasesInner.md) | The aliases for this override.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_services_dns_forwarder_host_override_endpoint_request import PostServicesDNSForwarderHostOverrideEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesDNSForwarderHostOverrideEndpointRequest from a JSON string
post_services_dns_forwarder_host_override_endpoint_request_instance = PostServicesDNSForwarderHostOverrideEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesDNSForwarderHostOverrideEndpointRequest.to_json())

# convert the object into a dict
post_services_dns_forwarder_host_override_endpoint_request_dict = post_services_dns_forwarder_host_override_endpoint_request_instance.to_dict()
# create an instance of PostServicesDNSForwarderHostOverrideEndpointRequest from a dict
post_services_dns_forwarder_host_override_endpoint_request_from_dict = PostServicesDNSForwarderHostOverrideEndpointRequest.from_dict(post_services_dns_forwarder_host_override_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


