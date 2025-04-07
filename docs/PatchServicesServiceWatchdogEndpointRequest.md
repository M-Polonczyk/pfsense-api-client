# PatchServicesServiceWatchdogEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the service to be watched.&lt;br&gt; | [optional] 
**description** | **str** | The description for the service being watched.&lt;br&gt; | [optional] [readonly] 
**notify** | **bool** | Enable or disable notifications being sent when Service Watchdogs finds this service stopped.&lt;br&gt; | [optional] 
**enabled** | **bool** | Indicates if this Service Watchdog is enabled or disabled. This value is unused.&lt;br&gt; | [optional] [readonly] [default to True]
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_service_watchdog_endpoint_request import PatchServicesServiceWatchdogEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesServiceWatchdogEndpointRequest from a JSON string
patch_services_service_watchdog_endpoint_request_instance = PatchServicesServiceWatchdogEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesServiceWatchdogEndpointRequest.to_json())

# convert the object into a dict
patch_services_service_watchdog_endpoint_request_dict = patch_services_service_watchdog_endpoint_request_instance.to_dict()
# create an instance of PatchServicesServiceWatchdogEndpointRequest from a dict
patch_services_service_watchdog_endpoint_request_from_dict = PatchServicesServiceWatchdogEndpointRequest.from_dict(patch_services_service_watchdog_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


