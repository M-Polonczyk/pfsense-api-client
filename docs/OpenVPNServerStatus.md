# OpenVPNServerStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the OpenVPN server.&lt;br&gt; | [optional] [readonly] 
**mode** | **str** | The mode of the OpenVPN server.&lt;br&gt; | [optional] [readonly] 
**port** | **str** | The port number of the OpenVPN server. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [readonly] 
**vpnid** | **int** | The VPN ID of the OpenVPN server this status corresponds to.&lt;br&gt; | [optional] [readonly] 
**mgmt** | **str** | The management interface of the OpenVPN server.&lt;br&gt; | [optional] [readonly] 
**conns** | [**List[OpenVPNServerStatusConnsInner]**](OpenVPNServerStatusConnsInner.md) | The current connections to the OpenVPN server.&lt;br&gt; | [optional] [readonly] 
**routes** | [**List[OpenVPNServerStatusRoutesInner]**](OpenVPNServerStatusRoutesInner.md) | The current routes of the OpenVPN server.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.open_vpn_server_status import OpenVPNServerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OpenVPNServerStatus from a JSON string
open_vpn_server_status_instance = OpenVPNServerStatus.from_json(json)
# print the JSON string representation of the object
print(OpenVPNServerStatus.to_json())

# convert the object into a dict
open_vpn_server_status_dict = open_vpn_server_status_instance.to_dict()
# create an instance of OpenVPNServerStatus from a dict
open_vpn_server_status_from_dict = OpenVPNServerStatus.from_dict(open_vpn_server_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


