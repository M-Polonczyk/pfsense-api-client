# StaticRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | Sets the destination network for this static route in CIDR notation.&lt;br&gt; | [optional] 
**gateway** | **str** | Sets which gateway this route applies to.&lt;br&gt; | [optional] 
**descr** | **str** | Sets a description for administrative reference.&lt;br&gt; | [optional] 
**disabled** | **bool** | Disable this static route.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.static_route import StaticRoute

# TODO update the JSON string below
json = "{}"
# create an instance of StaticRoute from a JSON string
static_route_instance = StaticRoute.from_json(json)
# print the JSON string representation of the object
print(StaticRoute.to_json())

# convert the object into a dict
static_route_dict = static_route_instance.to_dict()
# create an instance of StaticRoute from a dict
static_route_from_dict = StaticRoute.from_dict(static_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


