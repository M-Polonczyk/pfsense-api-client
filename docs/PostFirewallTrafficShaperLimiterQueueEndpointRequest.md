# PostFirewallTrafficShaperLimiterQueueEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this limiter queue.&lt;br&gt; | 
**number** | **int** | A unique number auto-assigned to this limiter. This is only used internally by the system and cannot be manually set or changed.&lt;br&gt; | [optional] [readonly] [default to 1]
**enabled** | **bool** | Enables or disables this limiter queue.&lt;br&gt; | [optional] 
**mask** | **str** | If &#x60;source&#x60; or &#x60;destination&#x60; slots is chosen a dynamic pipe with the bandwidth, delay, packet loss and queue size given above will be created for each source/destination IP address encountered, respectively. This makes it possible to easily specify bandwidth limits per host or subnet.&lt;br&gt; | [optional] [default to 'none']
**maskbits** | **int** | The IPv4 mask bits to use when determine the scope of the dynamic pipe for IPv4 traffic.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mask&#x60; must be one of [ srcaddress, dstaddress ]&lt;br&gt; | [optional] [default to 32]
**maskbitsv6** | **int** | The IPv6 mask bits to use when determine the scope of the dynamic pipe for IPv4 traffic.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mask&#x60; must be one of [ srcaddress, dstaddress ]&lt;br&gt; | [optional] [default to 128]
**qlimit** | **int** | The length of the limiter&#39;s queue which the scheduler and AQM are responsible for. Set to &#x60;null&#x60; to assume default.&lt;br&gt; | [optional] 
**ecn** | **bool** | Enable or disable ECN. ECN sets a reserved TCP flag when the queue is nearing or exceeding capacity. Not all AQMs or schedulers support this.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be one of [ codel, pie, red, gred ]&lt;br&gt;- &#x60;sched&#x60; must be one of [ fq_codel, fq_pie ]&lt;br&gt; | [optional] 
**description** | **str** | The verbose description for this limiter queue.&lt;br&gt; | [optional] 
**aqm** | **str** | The Active Queue Management (AQM) algorithm to use for this queue. AQM is the intelligent drop of network packets inside the queue, when it becomes full or gets close to becoming full, with the goal of reducing network congestion.&lt;br&gt; | 
**param_codel_target** | **int** | The value for the CoDel target parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;codel&#39;&#x60;&lt;br&gt; | [optional] 
**param_codel_interval** | **int** | The value for the CoDel interval parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;codel&#39;&#x60;&lt;br&gt; | [optional] 
**param_pie_target** | **int** | The value for the PIE target parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;pie&#39;&#x60;&lt;br&gt; | [optional] 
**param_pie_tupdate** | **int** | The value for the PIE tupdate parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;pie&#39;&#x60;&lt;br&gt; | [optional] 
**param_pie_alpha** | **int** | The value for the PIE alpha parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;pie&#39;&#x60;&lt;br&gt; | [optional] 
**param_pie_beta** | **int** | The value for the PIE beta parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;pie&#39;&#x60;&lt;br&gt; | [optional] 
**param_pie_max_burst** | **int** | The value for the PIE max_burst parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;pie&#39;&#x60;&lt;br&gt; | [optional] 
**param_pie_max_ecnth** | **int** | The value for the PIE ecnth parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;pie&#39;&#x60;&lt;br&gt; | [optional] 
**pie_onoff** | **bool** | Enable or disable turning PIE on and off depending on queue load.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;pie&#39;&#x60;&lt;br&gt; | [optional] 
**pie_capdrop** | **bool** | Enable or disable cap drop adjustment.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;pie&#39;&#x60;&lt;br&gt; | [optional] 
**pie_qdelay** | **bool** | Set queue delay type to timestamps (true) or departure rate estimation (false).&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;pie&#39;&#x60;&lt;br&gt; | [optional] 
**pie_pderand** | **bool** | Enable or disable drop probability de-randomisation.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;pie&#39;&#x60;&lt;br&gt; | [optional] 
**param_red_w_q** | **int** | The value for the RED w_q parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;red&#39;&#x60;&lt;br&gt; | [optional] [default to 1]
**param_red_min_th** | **int** | The value for the RED min_th parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;red&#39;&#x60;&lt;br&gt; | [optional] 
**param_red_max_th** | **int** | The value for the RED max_th parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;red&#39;&#x60;&lt;br&gt; | [optional] [default to 1]
**param_red_max_p** | **int** | The value for the RED max_p parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;red&#39;&#x60;&lt;br&gt; | [optional] [default to 1]
**param_gred_w_q** | **int** | The value for the GRED w_q parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;gred&#39;&#x60;&lt;br&gt; | [optional] [default to 1]
**param_gred_min_th** | **int** | The value for the GRED min_th parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;gred&#39;&#x60;&lt;br&gt; | [optional] 
**param_gred_max_th** | **int** | The value for the GRED max_th parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;gred&#39;&#x60;&lt;br&gt; | [optional] [default to 1]
**param_gred_max_p** | **int** | The value for the GRED max_p parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be equal to &#x60;&#39;gred&#39;&#x60;&lt;br&gt; | [optional] [default to 1]
**weight** | **int** | The share of the parent limiter this queue gets.&lt;br&gt; | [optional] 
**plr** | **float** | The amount of packet loss (in percentage) added to traffic passing through this limiter queue.&lt;br&gt; | [optional] 
**buckets** | **int** | The limiter queue&#39;s bucket size (slots).&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 

## Example

```python
from pfsense_api_client.models.post_firewall_traffic_shaper_limiter_queue_endpoint_request import PostFirewallTrafficShaperLimiterQueueEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFirewallTrafficShaperLimiterQueueEndpointRequest from a JSON string
post_firewall_traffic_shaper_limiter_queue_endpoint_request_instance = PostFirewallTrafficShaperLimiterQueueEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostFirewallTrafficShaperLimiterQueueEndpointRequest.to_json())

# convert the object into a dict
post_firewall_traffic_shaper_limiter_queue_endpoint_request_dict = post_firewall_traffic_shaper_limiter_queue_endpoint_request_instance.to_dict()
# create an instance of PostFirewallTrafficShaperLimiterQueueEndpointRequest from a dict
post_firewall_traffic_shaper_limiter_queue_endpoint_request_from_dict = PostFirewallTrafficShaperLimiterQueueEndpointRequest.from_dict(post_firewall_traffic_shaper_limiter_queue_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


