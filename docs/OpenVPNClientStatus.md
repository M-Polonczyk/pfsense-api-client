# OpenVPNClientStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the OpenVPN client.&lt;br&gt; | [optional] [readonly] 
**port** | **str** | The port number of the OpenVPN client. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [readonly] 
**vpnid** | **int** | The VPN ID of the OpenVPN client this status corresponds to.&lt;br&gt; | [optional] [readonly] 
**mgmt** | **str** | The management interface of the OpenVPN client.&lt;br&gt; | [optional] [readonly] 
**status** | **str** | The current status of the OpenVPN client.&lt;br&gt; | [optional] [readonly] 
**state** | **str** | The current state of the OpenVPN client.&lt;br&gt; | [optional] [readonly] 
**state_detail** | **str** | The details for the current state of the OpenVPN client.&lt;br&gt; | [optional] [readonly] 
**connect_time** | **str** | The connection time of the OpenVPN client.&lt;br&gt; | [optional] [readonly] 
**virtual_addr** | **str** | The virtual address of the OpenVPN client.&lt;br&gt; | [optional] [readonly] 
**virtual_addr6** | **str** | The virtual address 6 of the OpenVPN client.&lt;br&gt; | [optional] [readonly] 
**remote_host** | **str** | The remote host of the OpenVPN client.&lt;br&gt; | [optional] [readonly] 
**remote_port** | **str** | The remote port of the OpenVPN client. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [readonly] 
**local_host** | **str** | The local host of the OpenVPN client.&lt;br&gt; | [optional] [readonly] 
**local_port** | **str** | The local port of the OpenVPN client. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.open_vpn_client_status import OpenVPNClientStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OpenVPNClientStatus from a JSON string
open_vpn_client_status_instance = OpenVPNClientStatus.from_json(json)
# print the JSON string representation of the object
print(OpenVPNClientStatus.to_json())

# convert the object into a dict
open_vpn_client_status_dict = open_vpn_client_status_instance.to_dict()
# create an instance of OpenVPNClientStatus from a dict
open_vpn_client_status_from_dict = OpenVPNClientStatus.from_dict(open_vpn_client_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


