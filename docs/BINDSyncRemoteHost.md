# BINDSyncRemoteHost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**syncdestinenable** | **bool** | Enable this remote host for syncing.&lt;br&gt; | [optional] 
**syncprotocol** | **str** | The protocol to use for syncing.&lt;br&gt; | [optional] 
**ipaddress** | **str** | The IP address/hostname of the remote host.&lt;br&gt; | [optional] 
**syncport** | **str** | The remote host port to use for syncing. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] 
**username** | **str** | The username to use to authenticate when syncing.&lt;br&gt; | [optional] 
**password** | **str** | The password to use to authenticate when syncing.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.bind_sync_remote_host import BINDSyncRemoteHost

# TODO update the JSON string below
json = "{}"
# create an instance of BINDSyncRemoteHost from a JSON string
bind_sync_remote_host_instance = BINDSyncRemoteHost.from_json(json)
# print the JSON string representation of the object
print(BINDSyncRemoteHost.to_json())

# convert the object into a dict
bind_sync_remote_host_dict = bind_sync_remote_host_instance.to_dict()
# create an instance of BINDSyncRemoteHost from a dict
bind_sync_remote_host_from_dict = BINDSyncRemoteHost.from_dict(bind_sync_remote_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


