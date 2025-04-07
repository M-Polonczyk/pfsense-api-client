# PatchRoutingGatewayDefaultEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultgw4** | **str** | The gateway to assigns as the default IPv4 gateway for this system. Leave blank to automatically determine the default gateway, or set to &#x60;-&#x60; to assign no gateway.&lt;br&gt; | [optional] 
**defaultgw6** | **str** | The gateway to assigns as the default IPv6 gateway for this system. Leave blank to automatically determine the default gateway, or set to &#x60;-&#x60; to assign no gateway.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.patch_routing_gateway_default_endpoint_request import PatchRoutingGatewayDefaultEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchRoutingGatewayDefaultEndpointRequest from a JSON string
patch_routing_gateway_default_endpoint_request_instance = PatchRoutingGatewayDefaultEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchRoutingGatewayDefaultEndpointRequest.to_json())

# convert the object into a dict
patch_routing_gateway_default_endpoint_request_dict = patch_routing_gateway_default_endpoint_request_instance.to_dict()
# create an instance of PatchRoutingGatewayDefaultEndpointRequest from a dict
patch_routing_gateway_default_endpoint_request_from_dict = PatchRoutingGatewayDefaultEndpointRequest.from_dict(patch_routing_gateway_default_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


