# PatchFirewallTrafficShaperLimiterBandwidthEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bw** | **int** | The amount of bandwidth this profile allows.&lt;br&gt; | [optional] 
**bwscale** | **str** | The scale factor of the &#x60;bw&#x60; fields value.&lt;br&gt; | [optional] 
**bwsched** | **str** | The schedule to assign this bandwidth profile. When this firewall schedule is active, this bandwidth profile will be used.&lt;br&gt; | [optional] [default to 'none']
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_request import PatchFirewallTrafficShaperLimiterBandwidthEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFirewallTrafficShaperLimiterBandwidthEndpointRequest from a JSON string
patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_request_instance = PatchFirewallTrafficShaperLimiterBandwidthEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchFirewallTrafficShaperLimiterBandwidthEndpointRequest.to_json())

# convert the object into a dict
patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_request_dict = patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_request_instance.to_dict()
# create an instance of PatchFirewallTrafficShaperLimiterBandwidthEndpointRequest from a dict
patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_request_from_dict = PatchFirewallTrafficShaperLimiterBandwidthEndpointRequest.from_dict(patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


