# PostRoutingStaticRouteEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | Sets the destination network for this static route in CIDR notation.&lt;br&gt; | 
**gateway** | **str** | Sets which gateway this route applies to.&lt;br&gt; | 
**descr** | **str** | Sets a description for administrative reference.&lt;br&gt; | [optional] 
**disabled** | **bool** | Disable this static route.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_routing_static_route_endpoint_request import PostRoutingStaticRouteEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRoutingStaticRouteEndpointRequest from a JSON string
post_routing_static_route_endpoint_request_instance = PostRoutingStaticRouteEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostRoutingStaticRouteEndpointRequest.to_json())

# convert the object into a dict
post_routing_static_route_endpoint_request_dict = post_routing_static_route_endpoint_request_instance.to_dict()
# create an instance of PostRoutingStaticRouteEndpointRequest from a dict
post_routing_static_route_endpoint_request_from_dict = PostRoutingStaticRouteEndpointRequest.from_dict(post_routing_static_route_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


