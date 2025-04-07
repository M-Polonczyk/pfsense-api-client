# PostServicesDHCPServerStaticMappingEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac** | **str** | The MAC address of the client this mapping is for.&lt;br&gt; | 
**ipaddr** | **str** | The IP address to assign this client via DHCP.&lt;br&gt; | [optional] 
**cid** | **str** | The client identifier of the client this mapping is for.&lt;br&gt; | [optional] 
**hostname** | **str** | The hostname to assign this client via DHCP.&lt;br&gt; | [optional] 
**domain** | **str** | The domain to be assigned via DHCP.&lt;br&gt; | [optional] 
**domainsearchlist** | **List[str]** | The domain search list to provide via DHCP.&lt;br&gt; | [optional] 
**defaultleasetime** | **int** | The default DHCP lease validity period (in seconds). This is used for clients that do not ask for a specific expiration time.&lt;br&gt; | [optional] [default to 7200]
**maxleasetime** | **int** | The maximum DHCP lease validity period (in seconds) this client can request.&lt;br&gt; | [optional] [default to 86400]
**gateway** | **str** | The gateway IPv4 address to provide via DHCP. This is only necessary if you are not using the interface&#39;s IP as the gateway. Specify &#x60;none&#x60; for no gateway assignment.&lt;br&gt; | [optional] 
**dnsserver** | **List[str]** | The DNS servers to provide via DHCP. Leave empty to default to system nameservers.&lt;br&gt; | [optional] 
**winsserver** | **List[str]** | The WINS servers to provide via DHCP.&lt;br&gt; | [optional] 
**ntpserver** | **List[str]** | The NTP servers to provide via DHCP.&lt;br&gt; | [optional] 
**arp_table_static_entry** | **bool** | Assign a static ARP entry for this static mapping.&lt;br&gt; | [optional] 
**descr** | **str** | The description of this static mapping.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 

## Example

```python
from pfsense_api_client.models.post_services_dhcp_server_static_mapping_endpoint_request import PostServicesDHCPServerStaticMappingEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesDHCPServerStaticMappingEndpointRequest from a JSON string
post_services_dhcp_server_static_mapping_endpoint_request_instance = PostServicesDHCPServerStaticMappingEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesDHCPServerStaticMappingEndpointRequest.to_json())

# convert the object into a dict
post_services_dhcp_server_static_mapping_endpoint_request_dict = post_services_dhcp_server_static_mapping_endpoint_request_instance.to_dict()
# create an instance of PostServicesDHCPServerStaticMappingEndpointRequest from a dict
post_services_dhcp_server_static_mapping_endpoint_request_from_dict = PostServicesDHCPServerStaticMappingEndpointRequest.from_dict(post_services_dhcp_server_static_mapping_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


