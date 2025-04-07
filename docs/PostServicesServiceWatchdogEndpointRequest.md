# PostServicesServiceWatchdogEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the service to be watched.&lt;br&gt; | 
**description** | **str** | The description for the service being watched.&lt;br&gt; | [optional] [readonly] 
**notify** | **bool** | Enable or disable notifications being sent when Service Watchdogs finds this service stopped.&lt;br&gt; | [optional] 
**enabled** | **bool** | Indicates if this Service Watchdog is enabled or disabled. This value is unused.&lt;br&gt; | [optional] [readonly] [default to True]

## Example

```python
from pfsense_api_client.models.post_services_service_watchdog_endpoint_request import PostServicesServiceWatchdogEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesServiceWatchdogEndpointRequest from a JSON string
post_services_service_watchdog_endpoint_request_instance = PostServicesServiceWatchdogEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesServiceWatchdogEndpointRequest.to_json())

# convert the object into a dict
post_services_service_watchdog_endpoint_request_dict = post_services_service_watchdog_endpoint_request_instance.to_dict()
# create an instance of PostServicesServiceWatchdogEndpointRequest from a dict
post_services_service_watchdog_endpoint_request_from_dict = PostServicesServiceWatchdogEndpointRequest.from_dict(post_services_service_watchdog_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


