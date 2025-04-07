# DHCPRelay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enables or disables the DHCP relay.&lt;br&gt; | [optional] 
**interface** | **List[str]** | The downstream interfaces to listen on for DHCP requests.&lt;br&gt; | [optional] 
**agentoption** | **bool** | Enables or disables appending the circuit ID (interface number) and the agent ID to the DHCP request.&lt;br&gt; | [optional] 
**carpstatusvip** | **str** | DHCP Relay will be stopped when the chosen VIP is in BACKUP status, and started in MASTER status.&lt;br&gt; | [optional] [default to 'none']
**server** | **List[str]** | The IPv4 addresses of the DHCP server to relay requests to.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.dhcp_relay import DHCPRelay

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPRelay from a JSON string
dhcp_relay_instance = DHCPRelay.from_json(json)
# print the JSON string representation of the object
print(DHCPRelay.to_json())

# convert the object into a dict
dhcp_relay_dict = dhcp_relay_instance.to_dict()
# create an instance of DHCPRelay from a dict
dhcp_relay_from_dict = DHCPRelay.from_dict(dhcp_relay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


