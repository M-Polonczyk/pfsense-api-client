# PostServicesDNSResolverDomainOverrideEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain to override.&lt;br&gt; | 
**ip** | **str** | The IP address to which the domain should resolve.&lt;br&gt; | 
**descr** | **str** | The description for this domain override.&lt;br&gt; | [optional] 
**forward_tls_upstream** | **bool** | Enables or disables forwarding DNS queries to the upstream DNS server using TLS.&lt;br&gt; | [optional] 
**tls_hostname** | **str** | The hostname to use for the TLS connection to the upstream DNS server.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;forward_tls_upstream&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_services_dns_resolver_domain_override_endpoint_request import PostServicesDNSResolverDomainOverrideEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesDNSResolverDomainOverrideEndpointRequest from a JSON string
post_services_dns_resolver_domain_override_endpoint_request_instance = PostServicesDNSResolverDomainOverrideEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesDNSResolverDomainOverrideEndpointRequest.to_json())

# convert the object into a dict
post_services_dns_resolver_domain_override_endpoint_request_dict = post_services_dns_resolver_domain_override_endpoint_request_instance.to_dict()
# create an instance of PostServicesDNSResolverDomainOverrideEndpointRequest from a dict
post_services_dns_resolver_domain_override_endpoint_request_from_dict = PostServicesDNSResolverDomainOverrideEndpointRequest.from_dict(post_services_dns_resolver_domain_override_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


