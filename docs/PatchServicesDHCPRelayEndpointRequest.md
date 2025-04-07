# PatchServicesDHCPRelayEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enables or disables the DHCP relay.&lt;br&gt; | [optional] 
**interface** | **List[str]** | The downstream interfaces to listen on for DHCP requests.&lt;br&gt; | [optional] 
**agentoption** | **bool** | Enables or disables appending the circuit ID (interface number) and the agent ID to the DHCP request.&lt;br&gt; | [optional] 
**carpstatusvip** | **str** | DHCP Relay will be stopped when the chosen VIP is in BACKUP status, and started in MASTER status.&lt;br&gt; | [optional] [default to 'none']
**server** | **List[str]** | The IPv4 addresses of the DHCP server to relay requests to.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.patch_services_dhcp_relay_endpoint_request import PatchServicesDHCPRelayEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesDHCPRelayEndpointRequest from a JSON string
patch_services_dhcp_relay_endpoint_request_instance = PatchServicesDHCPRelayEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesDHCPRelayEndpointRequest.to_json())

# convert the object into a dict
patch_services_dhcp_relay_endpoint_request_dict = patch_services_dhcp_relay_endpoint_request_instance.to_dict()
# create an instance of PatchServicesDHCPRelayEndpointRequest from a dict
patch_services_dhcp_relay_endpoint_request_from_dict = PatchServicesDHCPRelayEndpointRequest.from_dict(patch_services_dhcp_relay_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


