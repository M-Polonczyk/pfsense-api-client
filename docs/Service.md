# Service


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The internal name of the service.&lt;br&gt; | [optional] [readonly] 
**action** | **str** | The action to perform against this service.&lt;br&gt; | [optional] 
**description** | **str** | The full descriptive name of the service.&lt;br&gt; | [optional] [readonly] 
**enabled** | **bool** | Indicates if the service is enabled.&lt;br&gt; | [optional] [readonly] 
**status** | **bool** | Indicates if the service is actively running.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print(Service.to_json())

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_from_dict = Service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


