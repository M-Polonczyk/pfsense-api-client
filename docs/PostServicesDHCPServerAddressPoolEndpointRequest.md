# PostServicesDHCPServerAddressPoolEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range_from** | **str** | The starting IP address for this address pool. This address must be less than or equal to the &#x60;range_to&#x60; field.&lt;br&gt; | 
**range_to** | **str** | The ending IP address for the this address pool. This address must be greater than or equal to the &#x60;range_to&#x60; field.&lt;br&gt; | 
**domain** | **str** | The domain to be assigned via DHCP.&lt;br&gt; | [optional] 
**mac_allow** | **List[str]** | MAC addresses this DHCP server is allowed to provide leases for.&lt;br&gt; | [optional] 
**mac_deny** | **List[str]** | MAC addresses this DHCP server is not allowed to provide leases for.&lt;br&gt; | [optional] 
**domainsearchlist** | **List[str]** | The domain search list to provide via DHCP.&lt;br&gt; | [optional] 
**defaultleasetime** | **int** | The default DHCP lease validity period (in seconds). This is used for clients that do not ask for a specific expiration time.&lt;br&gt; | [optional] [default to 7200]
**maxleasetime** | **int** | The maximum DHCP lease validity period (in seconds) a client can request.&lt;br&gt; | [optional] [default to 86400]
**gateway** | **str** | The gateway IPv4 address to provide via DHCP. This is only necessary if you are not using the interface&#39;s IP as the gateway. Specify &#x60;none&#x60; for no gateway assignment.&lt;br&gt; | [optional] 
**dnsserver** | **List[str]** | The DNS servers to provide via DHCP. Leave empty to default to system nameservers.&lt;br&gt; | [optional] 
**winsserver** | **List[str]** | The WINS servers to provide via DHCP.&lt;br&gt; | [optional] 
**ntpserver** | **List[str]** | The NTP servers to provide via DHCP.&lt;br&gt; | [optional] 
**ignorebootp** | **bool** | Force this DHCP server to ignore BOOTP queries.&lt;br&gt; | [optional] 
**ignoreclientuids** | **bool** | Prevent recording a unique identifier (UID) in client lease data if present in the client DHCP request. This option may be useful when a client can dual boot using different client identifiers but the same hardware (MAC) address. Note that the resulting server behavior violates the official DHCP specification.&lt;br&gt; | [optional] 
**denyunknown** | **str** | Define how to handle unknown clients requesting DHCP leases. When set to &#x60;null&#x60;, any DHCP client will get an IP address within this scope/range on this interface. If set to &#x60;enabled&#x60;, any DHCP client with a MAC address listed in a static mapping on any scope(s)/interface(s) will get an IP address. If set to &#x60;class&#x60;, only MAC addresses listed in static mappings on this interface will get an IP address within this scope/range.&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 

## Example

```python
from pfsense_api_client.models.post_services_dhcp_server_address_pool_endpoint_request import PostServicesDHCPServerAddressPoolEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesDHCPServerAddressPoolEndpointRequest from a JSON string
post_services_dhcp_server_address_pool_endpoint_request_instance = PostServicesDHCPServerAddressPoolEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesDHCPServerAddressPoolEndpointRequest.to_json())

# convert the object into a dict
post_services_dhcp_server_address_pool_endpoint_request_dict = post_services_dhcp_server_address_pool_endpoint_request_instance.to_dict()
# create an instance of PostServicesDHCPServerAddressPoolEndpointRequest from a dict
post_services_dhcp_server_address_pool_endpoint_request_from_dict = PostServicesDHCPServerAddressPoolEndpointRequest.from_dict(post_services_dhcp_server_address_pool_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


