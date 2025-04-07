# HAProxyBackendServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this backend server.&lt;br&gt; | [optional] 
**status** | **str** | The eligibility status for this backend server.&lt;br&gt; | [optional] [default to 'active']
**address** | **str** | The hostname or IP address of this backend server. Hostname values are only resolved at service startup.&lt;br&gt; | [optional] 
**port** | **str** | The port to forward to for this backend server. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] 
**weight** | **int** | The weight of this backend server when load balancing.&lt;br&gt; | [optional] [default to 1]
**ssl** | **bool** | Enables or disables using SSL/TLS when forwarding to this backend server.&lt;br&gt; | [optional] 
**sslserververify** | **bool** | Enables or disables verifying the SSL/TLS certificate when forwarding to this backend server.&lt;br&gt; | [optional] 
**serverid** | **int** | The unique ID for this backend server. This value is set by the system for internal use and cannot be changed.&lt;br&gt; | [optional] [readonly] [default to 175]

## Example

```python
from pfsense_api_client.models.ha_proxy_backend_server import HAProxyBackendServer

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxyBackendServer from a JSON string
ha_proxy_backend_server_instance = HAProxyBackendServer.from_json(json)
# print the JSON string representation of the object
print(HAProxyBackendServer.to_json())

# convert the object into a dict
ha_proxy_backend_server_dict = ha_proxy_backend_server_instance.to_dict()
# create an instance of HAProxyBackendServer from a dict
ha_proxy_backend_server_from_dict = HAProxyBackendServer.from_dict(ha_proxy_backend_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


