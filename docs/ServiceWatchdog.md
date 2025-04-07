# ServiceWatchdog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the service to be watched.&lt;br&gt; | [optional] 
**description** | **str** | The description for the service being watched.&lt;br&gt; | [optional] [readonly] 
**notify** | **bool** | Enable or disable notifications being sent when Service Watchdogs finds this service stopped.&lt;br&gt; | [optional] 
**enabled** | **bool** | Indicates if this Service Watchdog is enabled or disabled. This value is unused.&lt;br&gt; | [optional] [readonly] [default to True]

## Example

```python
from pfsense_api_client.models.service_watchdog import ServiceWatchdog

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceWatchdog from a JSON string
service_watchdog_instance = ServiceWatchdog.from_json(json)
# print the JSON string representation of the object
print(ServiceWatchdog.to_json())

# convert the object into a dict
service_watchdog_dict = service_watchdog_instance.to_dict()
# create an instance of ServiceWatchdog from a dict
service_watchdog_from_dict = ServiceWatchdog.from_dict(service_watchdog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


