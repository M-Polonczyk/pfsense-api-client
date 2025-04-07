# PatchServicesBINDSettingsEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_bind** | **bool** | Enables the BIND service.&lt;br&gt; | [optional] 
**bind_ip_version** | **str** | The IP version to use for the BIND service. Leave empty to use both IPv4 and IPv6.&lt;br&gt; | [optional] 
**listenon** | **List[str]** | The interfaces to listen on for DNS requests.&lt;br&gt; | [optional] [default to [All]]
**bind_notify** | **bool** | Notify slave server after any update on master.&lt;br&gt; | [optional] 
**bind_hide_version** | **bool** | Hide the BIND version in responses.&lt;br&gt; | [optional] 
**bind_ram_limit** | **str** | The maximum amount of RAM to use for the BIND service.&lt;br&gt; | [optional] [default to '256M']
**bind_logging** | **bool** | Enable logging for the BIND service.&lt;br&gt; | [optional] 
**log_severity** | **str** | The minimum severity of events to log.&lt;br&gt; | [optional] [default to 'critical']
**log_options** | **List[str]** | The categories to log.&lt;br&gt; | [optional] [default to [default]]
**rate_enabled** | **bool** | Enable rate limiting for the BIND service.&lt;br&gt; | [optional] 
**rate_limit** | **int** | The maximum number of queries per second to allow.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;rate_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] [default to 15]
**log_only** | **bool** | When rate limiting, only log that the query limit has been exceeded. If disabled, the query will be dropped instead.&lt;br&gt; | [optional] 
**bind_forwarder** | **bool** | Enable forwarding queries to other DNS servers listed below rather than this server performing its own recursion.&lt;br&gt; | [optional] 
**bind_forwarder_ips** | **List[str]** | The IP addresses of the DNS servers to forward queries to.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;bind_forwarder&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | 
**bind_dnssec_validation** | **str** | Enable DNSSEC validation when BIND is acting as a recursive resolver.&lt;br&gt; | [optional] [default to 'auto']
**listenport** | **str** | The TCP and UDP port to listen on for DNS requests. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '53']
**controlport** | **str** | The TCP port to listen on for control requests (localhost only). Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '953']
**bind_custom_options** | **str** | Custom BIND options to include in the configuration file.&lt;br&gt; | [optional] 
**bind_global_settings** | **str** | Global BIND settings to include in the configuration file.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.patch_services_bind_settings_endpoint_request import PatchServicesBINDSettingsEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesBINDSettingsEndpointRequest from a JSON string
patch_services_bind_settings_endpoint_request_instance = PatchServicesBINDSettingsEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesBINDSettingsEndpointRequest.to_json())

# convert the object into a dict
patch_services_bind_settings_endpoint_request_dict = patch_services_bind_settings_endpoint_request_instance.to_dict()
# create an instance of PatchServicesBINDSettingsEndpointRequest from a dict
patch_services_bind_settings_endpoint_request_from_dict = PatchServicesBINDSettingsEndpointRequest.from_dict(patch_services_bind_settings_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


