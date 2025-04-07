# PostServicesBINDSyncRemoteHostEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**syncdestinenable** | **bool** | Enable this remote host for syncing.&lt;br&gt; | [optional] 
**syncprotocol** | **str** | The protocol to use for syncing.&lt;br&gt; | 
**ipaddress** | **str** | The IP address/hostname of the remote host.&lt;br&gt; | 
**syncport** | **str** | The remote host port to use for syncing. Valid options are: a TCP/UDP port number&lt;br&gt; | 
**username** | **str** | The username to use to authenticate when syncing.&lt;br&gt; | 
**password** | **str** | The password to use to authenticate when syncing.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.post_services_bind_sync_remote_host_endpoint_request import PostServicesBINDSyncRemoteHostEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesBINDSyncRemoteHostEndpointRequest from a JSON string
post_services_bind_sync_remote_host_endpoint_request_instance = PostServicesBINDSyncRemoteHostEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesBINDSyncRemoteHostEndpointRequest.to_json())

# convert the object into a dict
post_services_bind_sync_remote_host_endpoint_request_dict = post_services_bind_sync_remote_host_endpoint_request_instance.to_dict()
# create an instance of PostServicesBINDSyncRemoteHostEndpointRequest from a dict
post_services_bind_sync_remote_host_endpoint_request_from_dict = PostServicesBINDSyncRemoteHostEndpointRequest.from_dict(post_services_bind_sync_remote_host_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


