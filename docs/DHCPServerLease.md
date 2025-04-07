# DHCPServerLease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | The IP address of the lease.&lt;br&gt; | [optional] 
**mac** | **str** | The MAC address of the lease.&lt;br&gt; | [optional] 
**hostname** | **str** | The hostname of the lease.&lt;br&gt; | [optional] 
**var_if** | **str** | The interface the lease was registered on.&lt;br&gt; | [optional] 
**starts** | **str** | The start time of the lease.&lt;br&gt; | [optional] 
**ends** | **str** | The end time of the lease.&lt;br&gt; | [optional] 
**active_status** | **str** | The active status of the lease.&lt;br&gt; | [optional] 
**online_status** | **str** | The online status of the lease.&lt;br&gt; | [optional] 
**descr** | **str** | The description of the lease.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.dhcp_server_lease import DHCPServerLease

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPServerLease from a JSON string
dhcp_server_lease_instance = DHCPServerLease.from_json(json)
# print the JSON string representation of the object
print(DHCPServerLease.to_json())

# convert the object into a dict
dhcp_server_lease_dict = dhcp_server_lease_instance.to_dict()
# create an instance of DHCPServerLease from a dict
dhcp_server_lease_from_dict = DHCPServerLease.from_dict(dhcp_server_lease_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


