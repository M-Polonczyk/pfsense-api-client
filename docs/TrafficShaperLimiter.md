# TrafficShaperLimiter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this limiter.&lt;br&gt; | [optional] 
**number** | **int** | A unique number auto-assigned to this limiter. This is only used internally by the system and cannot be manually set or changed.&lt;br&gt; | [optional] [readonly] [default to 1]
**enabled** | **bool** | Enables or disables this limiter and its child queues.&lt;br&gt; | [optional] 
**mask** | **str** | If &#x60;source&#x60; or &#x60;destination&#x60; slots is chosen a dynamic pipe with the bandwidth, delay, packet loss and queue size given above will be created for each source/destination IP address encountered, respectively. This makes it possible to easily specify bandwidth limits per host or subnet.&lt;br&gt; | [optional] [default to 'none']
**maskbits** | **int** | The IPv4 mask bits to use when determine the scope of the dynamic pipe for IPv4 traffic.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mask&#x60; must be one of [ srcaddress, dstaddress ]&lt;br&gt; | [optional] [default to 32]
**maskbitsv6** | **int** | The IPv6 mask bits to use when determine the scope of the dynamic pipe for IPv4 traffic.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mask&#x60; must be one of [ srcaddress, dstaddress ]&lt;br&gt; | [optional] [default to 128]
**qlimit** | **int** | The length of the limiter&#39;s queue which the scheduler and AQM are responsible for. Set to &#x60;null&#x60; to assume default.&lt;br&gt; | [optional] 
**ecn** | **bool** | Enable or disable ECN. ECN sets a reserved TCP flag when the queue is nearing or exceeding capacity. Not all AQMs or schedulers support this.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;aqm&#x60; must be one of [ codel, pie, red, gred ]&lt;br&gt;- &#x60;sched&#x60; must be one of [ fq_codel, fq_pie ]&lt;br&gt; | [optional] 
**description** | **str** | The verbose description for this limiter.&lt;br&gt; | [optional] 
**aqm** | **str** | The Active Queue Management (AQM) algorithm to use for this limiter. AQM is the intelligent drop of network packets inside the limiter, when it becomes full or gets close to becoming full, with the goal of reducing network congestion.&lt;br&gt; | [optional] 
**sched** | **str** | The scheduler to use for this limiter. The scheduler manages the sequence of network packets in the limiter&#39;s queue.&lt;br&gt; | [optional] 
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
**param_fq_codel_target** | **int** | The value for the FQ CoDel target parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;sched&#x60; must be equal to &#x60;&#39;fq_codel&#39;&#x60;&lt;br&gt; | [optional] 
**param_fq_codel_interval** | **int** | The value for the FQ CoDel interval parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;sched&#x60; must be equal to &#x60;&#39;fq_codel&#39;&#x60;&lt;br&gt; | [optional] 
**param_fq_codel_quantum** | **int** | The value for the FQ CoDel quantum parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;sched&#x60; must be equal to &#x60;&#39;fq_codel&#39;&#x60;&lt;br&gt; | [optional] 
**param_fq_codel_limit** | **int** | The value for the FQ CoDel limit parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;sched&#x60; must be equal to &#x60;&#39;fq_codel&#39;&#x60;&lt;br&gt; | [optional] 
**param_fq_codel_flows** | **int** | The value for the FQ CoDel flows parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;sched&#x60; must be equal to &#x60;&#39;fq_codel&#39;&#x60;&lt;br&gt; | [optional] 
**param_fq_pie_target** | **int** | The value for the FQ PIE target parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;sched&#x60; must be equal to &#x60;&#39;fq_pie&#39;&#x60;&lt;br&gt; | [optional] 
**param_fq_pie_tupdate** | **int** | The value for the FQ PIE tupdate parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;sched&#x60; must be equal to &#x60;&#39;fq_pie&#39;&#x60;&lt;br&gt; | [optional] 
**param_fq_pie_alpha** | **int** | The value for the FQ PIE alpha parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;sched&#x60; must be equal to &#x60;&#39;fq_pie&#39;&#x60;&lt;br&gt; | [optional] 
**param_fq_pie_beta** | **int** | The value for the FQ PIE beta parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;sched&#x60; must be equal to &#x60;&#39;fq_pie&#39;&#x60;&lt;br&gt; | [optional] 
**param_fq_pie_max_burst** | **int** | The value for the FQ PIE max_burst parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;sched&#x60; must be equal to &#x60;&#39;fq_pie&#39;&#x60;&lt;br&gt; | [optional] 
**param_fq_pie_max_ecnth** | **int** | The value for the FQ PIE ecnth parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;sched&#x60; must be equal to &#x60;&#39;fq_pie&#39;&#x60;&lt;br&gt; | [optional] 
**param_fq_pie_quantum** | **int** | The value for the FQ PIE quantum parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;sched&#x60; must be equal to &#x60;&#39;fq_pie&#39;&#x60;&lt;br&gt; | [optional] 
**param_fq_pie_limit** | **int** | The value for the FQ PIE limit parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;sched&#x60; must be equal to &#x60;&#39;fq_pie&#39;&#x60;&lt;br&gt; | [optional] 
**param_fq_pie_flows** | **int** | The value for the FQ PIE flows parameter.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;sched&#x60; must be equal to &#x60;&#39;fq_pie&#39;&#x60;&lt;br&gt; | [optional] 
**delay** | **int** | The amount of delay (in milliseconds) added to traffic passing through this limiter.&lt;br&gt; | [optional] 
**plr** | **float** | The amount of packet loss (in percentage) added to traffic passing through the limiter.&lt;br&gt; | [optional] 
**buckets** | **int** | The limiter&#39;s bucket size (slots).&lt;br&gt; | [optional] 
**bandwidth** | [**List[TrafficShaperLimiterBandwidthInner]**](TrafficShaperLimiterBandwidthInner.md) | The bandwidth profiles for this limiter.&lt;br&gt; | [optional] 
**queue** | [**List[TrafficShaperLimiterQueueInner]**](TrafficShaperLimiterQueueInner.md) | The child queues for this limiter.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.traffic_shaper_limiter import TrafficShaperLimiter

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficShaperLimiter from a JSON string
traffic_shaper_limiter_instance = TrafficShaperLimiter.from_json(json)
# print the JSON string representation of the object
print(TrafficShaperLimiter.to_json())

# convert the object into a dict
traffic_shaper_limiter_dict = traffic_shaper_limiter_instance.to_dict()
# create an instance of TrafficShaperLimiter from a dict
traffic_shaper_limiter_from_dict = TrafficShaperLimiter.from_dict(traffic_shaper_limiter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


