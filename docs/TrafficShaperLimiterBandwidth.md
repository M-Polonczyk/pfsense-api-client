# TrafficShaperLimiterBandwidth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bw** | **int** | The amount of bandwidth this profile allows.&lt;br&gt; | [optional] 
**bwscale** | **str** | The scale factor of the &#x60;bw&#x60; fields value.&lt;br&gt; | [optional] 
**bwsched** | **str** | The schedule to assign this bandwidth profile. When this firewall schedule is active, this bandwidth profile will be used.&lt;br&gt; | [optional] [default to 'none']

## Example

```python
from pfsense_api_client.models.traffic_shaper_limiter_bandwidth import TrafficShaperLimiterBandwidth

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficShaperLimiterBandwidth from a JSON string
traffic_shaper_limiter_bandwidth_instance = TrafficShaperLimiterBandwidth.from_json(json)
# print the JSON string representation of the object
print(TrafficShaperLimiterBandwidth.to_json())

# convert the object into a dict
traffic_shaper_limiter_bandwidth_dict = traffic_shaper_limiter_bandwidth_instance.to_dict()
# create an instance of TrafficShaperLimiterBandwidth from a dict
traffic_shaper_limiter_bandwidth_from_dict = TrafficShaperLimiterBandwidth.from_dict(traffic_shaper_limiter_bandwidth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


