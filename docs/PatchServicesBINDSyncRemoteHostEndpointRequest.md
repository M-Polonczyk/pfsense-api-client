# PatchServicesBINDSyncRemoteHostEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**syncdestinenable** | **bool** | Enable this remote host for syncing.&lt;br&gt; | [optional] 
**syncprotocol** | **str** | The protocol to use for syncing.&lt;br&gt; | [optional] 
**ipaddress** | **str** | The IP address/hostname of the remote host.&lt;br&gt; | [optional] 
**syncport** | **str** | The remote host port to use for syncing. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] 
**username** | **str** | The username to use to authenticate when syncing.&lt;br&gt; | [optional] 
**password** | **str** | The password to use to authenticate when syncing.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_bind_sync_remote_host_endpoint_request import PatchServicesBINDSyncRemoteHostEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesBINDSyncRemoteHostEndpointRequest from a JSON string
patch_services_bind_sync_remote_host_endpoint_request_instance = PatchServicesBINDSyncRemoteHostEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesBINDSyncRemoteHostEndpointRequest.to_json())

# convert the object into a dict
patch_services_bind_sync_remote_host_endpoint_request_dict = patch_services_bind_sync_remote_host_endpoint_request_instance.to_dict()
# create an instance of PatchServicesBINDSyncRemoteHostEndpointRequest from a dict
patch_services_bind_sync_remote_host_endpoint_request_from_dict = PatchServicesBINDSyncRemoteHostEndpointRequest.from_dict(patch_services_bind_sync_remote_host_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


