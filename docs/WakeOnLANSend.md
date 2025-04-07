# WakeOnLANSend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | The interface the host to be woken up is connected to.&lt;br&gt; | [optional] 
**mac_addr** | **str** | The MAC address of the host to be awoken.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.wake_on_lan_send import WakeOnLANSend

# TODO update the JSON string below
json = "{}"
# create an instance of WakeOnLANSend from a JSON string
wake_on_lan_send_instance = WakeOnLANSend.from_json(json)
# print the JSON string representation of the object
print(WakeOnLANSend.to_json())

# convert the object into a dict
wake_on_lan_send_dict = wake_on_lan_send_instance.to_dict()
# create an instance of WakeOnLANSend from a dict
wake_on_lan_send_from_dict = WakeOnLANSend.from_dict(wake_on_lan_send_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


