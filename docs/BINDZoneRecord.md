# BINDZoneRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The domain name for this record.&lt;br&gt; | [optional] 
**type** | **str** | The type of record.&lt;br&gt; | [optional] 
**rdata** | **str** | The data for this record. This can be an IP address, domain name, or other data depending on the record type.&lt;br&gt; | [optional] 
**priority** | **int** | The priority for this record.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be one of [ MX, SRV ]&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.bind_zone_record import BINDZoneRecord

# TODO update the JSON string below
json = "{}"
# create an instance of BINDZoneRecord from a JSON string
bind_zone_record_instance = BINDZoneRecord.from_json(json)
# print the JSON string representation of the object
print(BINDZoneRecord.to_json())

# convert the object into a dict
bind_zone_record_dict = bind_zone_record_instance.to_dict()
# create an instance of BINDZoneRecord from a dict
bind_zone_record_from_dict = BINDZoneRecord.from_dict(bind_zone_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


