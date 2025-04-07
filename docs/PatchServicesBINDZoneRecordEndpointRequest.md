# PatchServicesBINDZoneRecordEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The domain name for this record.&lt;br&gt; | [optional] 
**type** | **str** | The type of record.&lt;br&gt; | [optional] 
**rdata** | **str** | The data for this record. This can be an IP address, domain name, or other data depending on the record type.&lt;br&gt; | [optional] 
**priority** | **int** | The priority for this record.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be one of [ MX, SRV ]&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_services_bind_zone_record_endpoint_request import PatchServicesBINDZoneRecordEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServicesBINDZoneRecordEndpointRequest from a JSON string
patch_services_bind_zone_record_endpoint_request_instance = PatchServicesBINDZoneRecordEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchServicesBINDZoneRecordEndpointRequest.to_json())

# convert the object into a dict
patch_services_bind_zone_record_endpoint_request_dict = patch_services_bind_zone_record_endpoint_request_instance.to_dict()
# create an instance of PatchServicesBINDZoneRecordEndpointRequest from a dict
patch_services_bind_zone_record_endpoint_request_from_dict = PatchServicesBINDZoneRecordEndpointRequest.from_dict(patch_services_bind_zone_record_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


