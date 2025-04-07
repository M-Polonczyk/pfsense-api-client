# PatchRoutingStaticRouteEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | Sets the destination network for this static route in CIDR notation.&lt;br&gt; | [optional] 
**gateway** | **str** | Sets which gateway this route applies to.&lt;br&gt; | [optional] 
**descr** | **str** | Sets a description for administrative reference.&lt;br&gt; | [optional] 
**disabled** | **bool** | Disable this static route.&lt;br&gt; | [optional] 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_routing_static_route_endpoint_request import PatchRoutingStaticRouteEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchRoutingStaticRouteEndpointRequest from a JSON string
patch_routing_static_route_endpoint_request_instance = PatchRoutingStaticRouteEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchRoutingStaticRouteEndpointRequest.to_json())

# convert the object into a dict
patch_routing_static_route_endpoint_request_dict = patch_routing_static_route_endpoint_request_instance.to_dict()
# create an instance of PatchRoutingStaticRouteEndpointRequest from a dict
patch_routing_static_route_endpoint_request_from_dict = PatchRoutingStaticRouteEndpointRequest.from_dict(patch_routing_static_route_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


