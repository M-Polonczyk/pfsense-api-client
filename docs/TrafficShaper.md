# TrafficShaper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enables or disables this traffic shaper.&lt;br&gt; | [optional] [default to True]
**interface** | **str** | The interface this traffic shaper will be applied to.&lt;br&gt; | [optional] 
**name** | **str** | The name of this traffic shaper. This value is automatically set by the system and cannot be changed.&lt;br&gt; | [optional] [readonly] 
**scheduler** | **str** | The scheduler type to use for this traffic shaper. Changing this value will automatically update any child queues assigned to this traffic shaper.&lt;br&gt; | [optional] 
**bandwidthtype** | **str** | The scale type of the &#x60;bandwidth&#x60; field&#39;s value.&lt;br&gt; | [optional] 
**bandwidth** | **int** | The total bandwidth amount allowed by this traffic shaper.&lt;br&gt; | [optional] 
**qlimit** | **int** | The number of packets that can be held in a queue waiting to be transmitted by the shaper.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;scheduler&#x60; must not be one of [ CODELQ ]&lt;br&gt; | [optional] [default to 50]
**tbrconfig** | **int** | The size, in bytes, of the token bucket regulator. If &#x60;null&#x60;, heuristics based on the interface bandwidth are used to determine the size.&lt;br&gt; | [optional] 
**queue** | [**List[TrafficShaperQueueInner]**](TrafficShaperQueueInner.md) | The child queues assigned to this traffic shaper.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.traffic_shaper import TrafficShaper

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficShaper from a JSON string
traffic_shaper_instance = TrafficShaper.from_json(json)
# print the JSON string representation of the object
print(TrafficShaper.to_json())

# convert the object into a dict
traffic_shaper_dict = traffic_shaper_instance.to_dict()
# create an instance of TrafficShaper from a dict
traffic_shaper_from_dict = TrafficShaper.from_dict(traffic_shaper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


