# PatchServicesHAProxyBackendActionEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to take when an ACL match is found.&lt;br&gt; | [optional] 
**acl** | **str** | The name of the backend ACL this action is associated with.&lt;br&gt; | [optional] 
**server** | **str** | The backend server to use when an ACL match is found.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;action&#x60; must be equal to &#x60;&#39;use_server&#39;&#x60;&lt;br&gt; | [optional] 
**customaction** | **str** | The custom action to take when an ACL match is found.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;action&#x60; must be equal to &#x60;&#39;custom&#39;&#x60;&lt;br&gt; | [optional] 
**deny_status** | **str** | The deny status to use when an ACL match is found.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;action&#x60; must be one of [ http-request_deny, http-request_tarpit ]&lt;br&gt; | [optional] 
**realm** | **str** | The authentication realm to use when an ACL match is found.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;action&#x60; must be equal to &#x60;&#39;http-request_auth&#39;&#x60;&lt;br&gt; | [optional] 
**rule** | **str** | The redirect rule to use when an ACL match is found.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;action&#x60; must be equal to &#x60;&#39;http-request_redirect&#39;&#x60;&lt;br&gt; | [optional] 
**lua_function** | **str** | The Lua function to use when an ACL match is found.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;action&#x60; must be one of [ http-request_lua, http-request_use-service, http-response_lua, tcp-request_content_lua, tcp-request_content_use-service, tcp-response_content_lua ]&lt;br&gt; | [optional] 
**name** | **str** | The name to use when an ACL match is found.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;action&#x60; must be one of [ http-request_add-header, http-request_set-header, http-request_del-header, http-request_replace-header, http-request_replace-value, http-response_add-header, http-response_set-header, http-response_del-header, http-response_replace-header, http-response_replace-value, http-after-response_add-header, http-after-response_set-header, http-after-response_del-header, http-after-response_replace-header, http-after-response_replace-value ]&lt;br&gt; | [optional] 
**fmt** | **str** | The fmt value to use when an ACL match is found.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;action&#x60; must be one of [ http-request_add-header, http-request_set-header, http-request_set-method, http-request_set-path, http-request_set-query, http-request_set-uri, http-response_add-header, http-response_set-header, http-after-response_add-header, http-after-response_set-header ]&lt;br&gt; | [optional] 
**find** | **str** | The value to find when an ACL match is found.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;action&#x60; must be one of [ http-request_replace-header, http-request_replace-value, http-response_replace-header, http-request_replace-path, http-response_replace-value, http-after-response_replace-header, http-after-response_replace-value ]&lt;br&gt; | [optional] 
**replace** | **str** | The value to replace with when an ACL match is found.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;action&#x60; must be one of [ http-request_replace-header, http-request_replace-value, http-request_replace-path, http-response_replace-header, http-response_replace-value, http-after-response_replace-header, http-after-response_replace-value ]&lt;br&gt; | [optional] 
**path** | **str** | The path to use when an ACL match is found.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;action&#x60; must be equal to &#x60;&#39;http-request_replace-path&#39;&#x60;&lt;br&gt; | [optional] 
**status** | **str** | The status to use when an ACL match is found.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;action&#x60; must be one of [ http-response_set-status, http-after-response_set-status ]&lt;br&gt; | [optional] 
**reason** | **str** | The status reason to use when an ACL match is found.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;action&#x60; must be one of [ http-response_set-status, http-after-response_set-status ]&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_ha_proxy_backend_action_endpoint_request import PatchServicesHAProxyBackendActionEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesHAProxyBackendActionEndpointRequest from a JSON string
patch_services_ha_proxy_backend_action_endpoint_request_instance = PatchServicesHAProxyBackendActionEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesHAProxyBackendActionEndpointRequest.to_json())

# convert the object into a dict
patch_services_ha_proxy_backend_action_endpoint_request_dict = patch_services_ha_proxy_backend_action_endpoint_request_instance.to_dict()
# create an instance of PatchServicesHAProxyBackendActionEndpointRequest from a dict
patch_services_ha_proxy_backend_action_endpoint_request_from_dict = PatchServicesHAProxyBackendActionEndpointRequest.from_dict(patch_services_ha_proxy_backend_action_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


