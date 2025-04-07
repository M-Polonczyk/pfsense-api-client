# OpenVPNServerStatusRoutesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | The common name of the OpenVPN server connection.&lt;br&gt; | [optional] [readonly] 
**remote_host** | **str** | The remote host of the OpenVPN server connection.&lt;br&gt; | [optional] [readonly] 
**virtual_addr** | **str** | The virtual address of the OpenVPN server connection.&lt;br&gt; | [optional] [readonly] 
**last_time** | **str** | The last time of the route was used.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.open_vpn_server_status_routes_inner import OpenVPNServerStatusRoutesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OpenVPNServerStatusRoutesInner from a JSON string
open_vpn_server_status_routes_inner_instance = OpenVPNServerStatusRoutesInner.from_json(json)
# print the JSON string representation of the object
print(OpenVPNServerStatusRoutesInner.to_json())

# convert the object into a dict
open_vpn_server_status_routes_inner_dict = open_vpn_server_status_routes_inner_instance.to_dict()
# create an instance of OpenVPNServerStatusRoutesInner from a dict
open_vpn_server_status_routes_inner_from_dict = OpenVPNServerStatusRoutesInner.from_dict(open_vpn_server_status_routes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


