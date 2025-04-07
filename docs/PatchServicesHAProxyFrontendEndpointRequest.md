# PatchServicesHAProxyFrontendEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this HAProxy frontend.&lt;br&gt; | [optional] 
**descr** | **str** | The description for this HAProxy frontend.&lt;br&gt; | [optional] 
**status** | **str** | The activation status for this HAProxy frontend.&lt;br&gt; | [optional] [default to 'active']
**a_extaddr** | [**List[HAProxyFrontendAExtaddrInner]**](HAProxyFrontendAExtaddrInner.md) | The external addresses assigned to this frontend.&lt;br&gt; | [optional] 
**max_connections** | **int** | The maximum number of connections allowed by this frontend.&lt;br&gt; | [optional] 
**type** | **str** | The processing type for this frontend.&lt;br&gt; | [optional] 
**ha_acls** | [**List[HAProxyFrontendHaAclsInner]**](HAProxyFrontendHaAclsInner.md) | The ACLs to apply to this frontend.&lt;br&gt; | [optional] 
**a_actionitems** | [**List[HAProxyFrontendAActionitemsInner]**](HAProxyFrontendAActionitemsInner.md) | The actions to take when an ACL match is found.&lt;br&gt; | [optional] 
**backend_serverpool** | **str** | The default backend to use for this frontend.&lt;br&gt; | [optional] 
**socket_stats** | **bool** | Enables or disables collecting and providing separate statistics for each socket.&lt;br&gt; | [optional] 
**dontlognull** | **bool** | Enables or disables logging connections with no data transferred.&lt;br&gt; | [optional] 
**dontlog_normal** | **bool** | Enables or disables only logging anomalous (not normal) connection.&lt;br&gt; | [optional] 
**log_separate_errors** | **bool** | Enables or disables changing the log level from info to err on potentially interesting info.&lt;br&gt; | [optional] 
**log_detailed** | **bool** | Enables or disables more detailed logging.&lt;br&gt; | [optional] 
**a_errorfiles** | [**List[HAProxyFrontendAErrorfilesInner]**](HAProxyFrontendAErrorfilesInner.md) | The custom error files to use for this frontend.&lt;br&gt; | [optional] 
**client_timeout** | **int** | The amount of time (in milliseconds) to wait for data from the client.&lt;br&gt; | [optional] [default to 30000]
**forwardfor** | **bool** | Enables or disables the HTTP X-Forwarded-For header which contains the client&#39;s IP address.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;http&#39;&#x60;&lt;br&gt; | [optional] 
**httpclose** | **str** | The &#x60;httpclose&#x60; option this frontend will operate.&lt;br&gt; | [optional] [default to 'http-keep-alive']
**advanced_bind** | **str** | Custom value to pass behind each bind option.&lt;br&gt; | [optional] 
**advanced** | **str** | Custom configuration to pass to this frontend.&lt;br&gt; | [optional] 
**ssloffloadcert** | **str** | The default SSL/TLS certificate refid to use for this frontend.&lt;br&gt; | [optional] 
**ha_certificates** | [**List[HAProxyFrontendHaCertificatesInner]**](HAProxyFrontendHaCertificatesInner.md) | The additional SSL/TLS certificates to use on this frontend.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_ha_proxy_frontend_endpoint_request import PatchServicesHAProxyFrontendEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesHAProxyFrontendEndpointRequest from a JSON string
patch_services_ha_proxy_frontend_endpoint_request_instance = PatchServicesHAProxyFrontendEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesHAProxyFrontendEndpointRequest.to_json())

# convert the object into a dict
patch_services_ha_proxy_frontend_endpoint_request_dict = patch_services_ha_proxy_frontend_endpoint_request_instance.to_dict()
# create an instance of PatchServicesHAProxyFrontendEndpointRequest from a dict
patch_services_ha_proxy_frontend_endpoint_request_from_dict = PatchServicesHAProxyFrontendEndpointRequest.from_dict(patch_services_ha_proxy_frontend_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


