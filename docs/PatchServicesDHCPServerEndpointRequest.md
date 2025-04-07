# PatchServicesDHCPServerEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | The interface to configure the DHCP server for. This field is only necessary when you wantto change the interface (ID) of an existing DHCP server, or you are replacing all DHCP server objects with a new configuration. Note that specifying an interface in this field will update the ID of the DHCP server to match the interface specified here. Leaving this field empty will retain the existing interface.&lt;br&gt; | [optional] 
**enable** | **bool** | Enable the DHCP server for this interface.&lt;br&gt; | [optional] 
**range_from** | **str** | The starting IP address for the primary DHCP pool. This address must be less than or equal to the &#x60;range_to&#x60; field.&lt;br&gt; | [optional] 
**range_to** | **str** | The ending IP address for the primary DHCP pool. This address must be greater than or equal to the &#x60;range_to&#x60; field.&lt;br&gt; | [optional] 
**domain** | **str** | The domain to be assigned via DHCP.&lt;br&gt; | [optional] 
**failover_peerip** | **str** | The interface IP address of the other firewall (failover peer) in this subnet. Leave empty to disable failover peering.&lt;br&gt; | [optional] 
**mac_allow** | **List[str]** | MAC addresses this DHCP server is allowed to provide leases for.&lt;br&gt; | [optional] 
**mac_deny** | **List[str]** | MAC addresses this DHCP server is not allowed to provide leases for.&lt;br&gt; | [optional] 
**domainsearchlist** | **List[str]** | The domain search list to provide via DHCP.&lt;br&gt; | [optional] 
**defaultleasetime** | **int** | The default DHCP lease validity period (in seconds). This is used for clients that do not ask for a specific expiration time.&lt;br&gt; | [optional] [default to 7200]
**maxleasetime** | **int** | The maximum DHCP lease validity period (in seconds) a client can request.&lt;br&gt; | [optional] [default to 86400]
**gateway** | **str** | The gateway IPv4 address to provide via DHCP. This is only necessary if you are not using the interface&#39;s IP as the gateway. Specify &#x60;none&#x60; for no gateway assignment.&lt;br&gt; | [optional] 
**dnsserver** | **List[str]** | The DNS servers to provide via DHCP. Leave empty to default to system nameservers.&lt;br&gt; | [optional] 
**winsserver** | **List[str]** | The WINS servers to provide via DHCP.&lt;br&gt; | [optional] 
**ntpserver** | **List[str]** | The NTP servers to provide via DHCP.&lt;br&gt; | [optional] 
**staticarp** | **bool** | Assign static ARP entries for DHCP leases provided by this server.&lt;br&gt; | [optional] 
**ignorebootp** | **bool** | Force this DHCP server to ignore BOOTP queries.&lt;br&gt; | [optional] 
**ignoreclientuids** | **bool** | Prevent recording a unique identifier (UID) in client lease data if present in the client DHCP request. This option may be useful when a client can dual boot using different client identifiers but the same hardware (MAC) address. Note that the resulting server behavior violates the official DHCP specification.&lt;br&gt; | [optional] 
**nonak** | **bool** | Ignore denied clients rather than reject. This option is not compatible with failover and cannot be enabled when a Failover Peer IP address is configured.&lt;br&gt; | [optional] 
**disablepingcheck** | **bool** | Prevent the DHCP server from sending a ping to the address being assigned, where if no response has been heard, it assigns the address.&lt;br&gt; | [optional] 
**dhcpleaseinlocaltime** | **bool** | Display the DHCP lease times in local time instead of UTC.&lt;br&gt; | [optional] 
**statsgraph** | **bool** | Enable adding DHCP lease statistics to the pfSense Monitoring graphs.&lt;br&gt; | [optional] 
**denyunknown** | **str** | Define how to handle unknown clients requesting DHCP leases. When set to &#x60;null&#x60;, any DHCP client will get an IP address within this scope/range on this interface. If set to &#x60;enabled&#x60;, any DHCP client with a MAC address listed in a static mapping on any scope(s)/interface(s) will get an IP address. If set to &#x60;class&#x60;, only MAC addresses listed in static mappings on this interface will get an IP address within this scope/range.&lt;br&gt; | [optional] 
**pool** | [**List[DHCPServerPoolInner]**](DHCPServerPoolInner.md) | Additional address pools applied to this DHCP server.&lt;br&gt; | [optional] 
**numberoptions** | [**List[DHCPServerNumberoptionsInner]**](DHCPServerNumberoptionsInner.md) | The custom DHCP options to apply to this DHCP server.&lt;br&gt; | [optional] 
**staticmap** | [**List[DHCPServerStaticmapInner]**](DHCPServerStaticmapInner.md) | Static mappings applied to this DHCP server.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_dhcp_server_endpoint_request import PatchServicesDHCPServerEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesDHCPServerEndpointRequest from a JSON string
patch_services_dhcp_server_endpoint_request_instance = PatchServicesDHCPServerEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesDHCPServerEndpointRequest.to_json())

# convert the object into a dict
patch_services_dhcp_server_endpoint_request_dict = patch_services_dhcp_server_endpoint_request_instance.to_dict()
# create an instance of PatchServicesDHCPServerEndpointRequest from a dict
patch_services_dhcp_server_endpoint_request_from_dict = PatchServicesDHCPServerEndpointRequest.from_dict(patch_services_dhcp_server_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


