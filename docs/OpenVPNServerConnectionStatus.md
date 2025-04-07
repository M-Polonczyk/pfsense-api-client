# OpenVPNServerConnectionStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | The common name of the OpenVPN server connection.&lt;br&gt; | [optional] [readonly] 
**remote_host** | **str** | The remote host of the OpenVPN server connection.&lt;br&gt; | [optional] [readonly] 
**virtual_addr** | **str** | The virtual address of the OpenVPN server connection.&lt;br&gt; | [optional] [readonly] 
**virtual_addr6** | **str** | The virtual IPv6 address of the OpenVPN server connection.&lt;br&gt; | [optional] [readonly] 
**bytes_recv** | **int** | The number of bytes received by the OpenVPN server connection.&lt;br&gt; | [optional] [readonly] 
**bytes_sent** | **int** | The number of bytes sent by the OpenVPN server connection.&lt;br&gt; | [optional] [readonly] 
**connect_time** | **str** | The connection time of the OpenVPN server connection.&lt;br&gt; | [optional] [readonly] 
**connect_time_unix** | **int** | The connection time of the OpenVPN server connection in Unix time.&lt;br&gt; | [optional] [readonly] 
**user_name** | **str** | The user name of the OpenVPN server connection.&lt;br&gt; | [optional] [readonly] 
**client_id** | **int** | The client ID of the OpenVPN server connection.&lt;br&gt; | [optional] [readonly] 
**peer_id** | **int** | The peer ID of the OpenVPN server connection.&lt;br&gt; | [optional] [readonly] 
**cipher** | **str** | The cipher of the OpenVPN server connection.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.open_vpn_server_connection_status import OpenVPNServerConnectionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OpenVPNServerConnectionStatus from a JSON string
open_vpn_server_connection_status_instance = OpenVPNServerConnectionStatus.from_json(json)
# print the JSON string representation of the object
print(OpenVPNServerConnectionStatus.to_json())

# convert the object into a dict
open_vpn_server_connection_status_dict = open_vpn_server_connection_status_instance.to_dict()
# create an instance of OpenVPNServerConnectionStatus from a dict
open_vpn_server_connection_status_from_dict = OpenVPNServerConnectionStatus.from_dict(open_vpn_server_connection_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


