# DHCPServerBackend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcpbackend** | **str** | The backend DHCP server service to use. ISC DHCP is deprecate and will be removed in a future version of pfSense.&lt;br&gt; | [optional] [default to 'isc']

## Example

```python
from pfsense_api_client.models.dhcp_server_backend import DHCPServerBackend

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPServerBackend from a JSON string
dhcp_server_backend_instance = DHCPServerBackend.from_json(json)
# print the JSON string representation of the object
print(DHCPServerBackend.to_json())

# convert the object into a dict
dhcp_server_backend_dict = dhcp_server_backend_instance.to_dict()
# create an instance of DHCPServerBackend from a dict
dhcp_server_backend_from_dict = DHCPServerBackend.from_dict(dhcp_server_backend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


