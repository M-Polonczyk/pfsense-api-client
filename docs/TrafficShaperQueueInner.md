# TrafficShaperQueueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | The parent interface this traffic shaper queue a child of. This value is automatically determined by the queue&#39;s parent and cannot be manually set or changed.&lt;br&gt; | [optional] [readonly] 
**enabled** | **bool** | Enables or disables the traffic shaper queue.&lt;br&gt; | [optional] 
**name** | **str** | The name to assign this traffic shaper queue.&lt;br&gt; | 
**priority** | **int** | The priority level for this traffic shaper queue.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- Parent field &#x60;scheduler&#x60; must be one of [ FAIRQ, CBQ, PRIQ ]&lt;br&gt; | [optional] [default to 1]
**qlimit** | **int** | The number of packets that can be held in a queue waiting to be transmitted by the shaper.&lt;br&gt; | 
**description** | **str** | A description for this traffic shaper queue.&lt;br&gt; | [optional] 
**default** | **bool** | Mark this traffic shaper queue as the default queue.&lt;br&gt; | [optional] 
**red** | **bool** | Use the &#39;Random Early Detection&#39; scheduler option for this traffic shaper queue.&lt;br&gt; | [optional] 
**rio** | **bool** | Use the &#39;Random Early Detection In and Out&#39; scheduler option for this traffic shaper queue.&lt;br&gt; | [optional] 
**ecn** | **bool** | Use the &#39;Explicit Congestion Notification&#39; scheduler option for this traffic shaper queue.&lt;br&gt; | [optional] 
**codel** | **bool** | Use the &#39;Codel Active Queue&#39; scheduler option for this traffic shaper queue.&lt;br&gt; | [optional] 
**bandwidthtype** | **str** | The scale type of the &#x60;bandwidth&#x60; field&#39;s value.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- Parent field &#x60;scheduler&#x60; must be one of [ FAIRQ, CBQ, HFSC ]&lt;br&gt; | [optional] [default to 'Mb']
**bandwidth** | **int** | The total bandwidth amount allowed by this traffic shaper.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- Parent field &#x60;scheduler&#x60; must be one of [ FAIRQ, CBQ, HFSC ]&lt;br&gt; | 
**buckets** | **int** | &lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- Parent field &#x60;scheduler&#x60; must be equal to &#x60;&#39;FAIRQ&#39;&#x60;&lt;br&gt; | [optional] 
**hogs** | **int** | The bandwidth limit per host.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- Parent field &#x60;scheduler&#x60; must be equal to &#x60;&#39;FAIRQ&#39;&#x60;&lt;br&gt; | [optional] 
**borrow** | **bool** | Allow this queue to borrow from other queues when available.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- Parent field &#x60;scheduler&#x60; must be equal to &#x60;&#39;CBQ&#39;&#x60;&lt;br&gt; | [optional] 
**upperlimit** | **bool** | Allow setting the maximum bandwidth allowed for the queue. Will force hard bandwidth limiting.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- Parent field &#x60;scheduler&#x60; must be equal to &#x60;&#39;HFSC&#39;&#x60;&lt;br&gt; | [optional] 
**upperlimit_m1** | **str** | The burst-able bandwidth limit for this traffic shaper queue.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;upperlimit&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**upperlimit_d** | **int** | The duration (in milliseconds) that the burst-able bandwidth limit (&#x60;upperlimit_m1&#x60; is in effect.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;upperlimit&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**upperlimit_m2** | **str** | The normal bandwidth limit for this traffic shaper queue. If &#x60;upperlimit_m1&#x60; is not defined, this limit will always be in effect. If &#x60;upperlimit_m1&#x60; is defined, this limit will take effect after the &#x60;upperlimit_d&#x60; duration has expired.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;upperlimit&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | 
**realtime** | **bool** | Allow setting the guaranteed bandwidth minimum allotted to the queue.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- Parent field &#x60;scheduler&#x60; must be equal to &#x60;&#39;HFSC&#39;&#x60;&lt;br&gt; | [optional] 
**realtime_m1** | **str** | The guaranteed minimum bandwidth limit for this traffic shaper queue during real time.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;realtime&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**realtime_d** | **int** | The duration (in milliseconds) that the guaranteed bandwidth limit (&#x60;realtime_m1&#x60;) is in effect.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;realtime&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**realtime_m2** | **str** | The maximum bandwidth this traffic shaper queue is allowed to use. Note: This value should not exceed 30% of parent queue&#39;s maximum bandwidth.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;realtime&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | 
**linkshare** | **bool** | Allow sharing bandwidth from this queue for other queues as long as the real time values have been satisfied.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- Parent field &#x60;scheduler&#x60; must be equal to &#x60;&#39;HFSC&#39;&#x60;&lt;br&gt; | [optional] 
**linkshare_m1** | **str** | The initial bandwidth limit for this traffic shaper queue when link sharing.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;linkshare&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**linkshare_d** | **int** | The duration (in milliseconds) that the initial bandwidth limit (&#x60;linkshare_m1&#x60;) is in effect.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;linkshare&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**linkshare_m2** | **str** | The maximum bandwidth this traffic shaper queue is allowed to use. Note: This behaves exactly the same as the &#x60;bandwidth&#x60; field. If this field is set, it will override whatever value is current assigned to the &#x60;bandwidth&#x60; field.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;linkshare&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.traffic_shaper_queue_inner import TrafficShaperQueueInner

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficShaperQueueInner from a JSON string
traffic_shaper_queue_inner_instance = TrafficShaperQueueInner.from_json(json)
# print the JSON string representation of the object
print(TrafficShaperQueueInner.to_json())

# convert the object into a dict
traffic_shaper_queue_inner_dict = traffic_shaper_queue_inner_instance.to_dict()
# create an instance of TrafficShaperQueueInner from a dict
traffic_shaper_queue_inner_from_dict = TrafficShaperQueueInner.from_dict(traffic_shaper_queue_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


