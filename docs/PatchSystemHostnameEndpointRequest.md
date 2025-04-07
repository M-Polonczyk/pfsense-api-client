# PatchSystemHostnameEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | The hostname portion of the FQDN to assign to this system.&lt;br&gt; | 
**domain** | **str** | The domain portion of the FQDN to assign to this system.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.patch_system_hostname_endpoint_request import PatchSystemHostnameEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSystemHostnameEndpointRequest from a JSON string
patch_system_hostname_endpoint_request_instance = PatchSystemHostnameEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchSystemHostnameEndpointRequest.to_json())

# convert the object into a dict
patch_system_hostname_endpoint_request_dict = patch_system_hostname_endpoint_request_instance.to_dict()
# create an instance of PatchSystemHostnameEndpointRequest from a dict
patch_system_hostname_endpoint_request_from_dict = PatchSystemHostnameEndpointRequest.from_dict(patch_system_hostname_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


