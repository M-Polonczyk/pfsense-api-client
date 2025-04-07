# InterfaceLAGG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**laggif** | **str** | The real name of the LAGG interface.&lt;br&gt; | [optional] [readonly] 
**descr** | **str** | A description to help document the purpose of this LAGG interface.&lt;br&gt; | [optional] 
**members** | **List[str]** | A list of member interfaces to include in the LAGG.&lt;br&gt; | [optional] 
**proto** | **str** | The LAGG protocol to use.&lt;br&gt; | [optional] 
**lacptimeout** | **str** | The LACP timeout mode to use.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;proto&#x60; must be equal to &#x60;&#39;lacp&#39;&#x60;&lt;br&gt; | [optional] [default to 'slow']
**lagghash** | **str** | The LAGG hash algorithm to use.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;proto&#x60; must be one of [ lacp, loadbalance ]&lt;br&gt; | [optional] [default to 'l2,l3,l4']
**failovermaster** | **str** | The failover master interface to use.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;proto&#x60; must be equal to &#x60;&#39;failover&#39;&#x60;&lt;br&gt; | [optional] [default to 'auto']

## Example

```python
from pfsense_api_client.models.interface_lagg import InterfaceLAGG

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceLAGG from a JSON string
interface_lagg_instance = InterfaceLAGG.from_json(json)
# print the JSON string representation of the object
print(InterfaceLAGG.to_json())

# convert the object into a dict
interface_lagg_dict = interface_lagg_instance.to_dict()
# create an instance of InterfaceLAGG from a dict
interface_lagg_from_dict = InterfaceLAGG.from_dict(interface_lagg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


