# BINDZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Disable this BIND zone.&lt;br&gt; | [optional] 
**name** | **str** | The name of this BIND zone.&lt;br&gt; | [optional] 
**description** | **str** | A description for this BIND zone.&lt;br&gt; | [optional] 
**type** | **str** | The type of this BIND zone.&lt;br&gt; | [optional] [default to 'master']
**view** | **List[str]** | The views this BIND zone belongs to.&lt;br&gt; | [optional] 
**reversev4** | **bool** | Enable reverse DNS for this BIND zone.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be one of [ master, slave ]&lt;br&gt; | [optional] 
**reversev6** | **bool** | Enable reverse IPv6 DNS for this BIND zone.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be one of [ master, slave ]&lt;br&gt; | [optional] 
**rpz** | **bool** | Enable this zone as part of a response policy.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be one of [ master, slave ]&lt;br&gt; | [optional] 
**custom** | **str** | Custom BIND options for this BIND zone.&lt;br&gt; | [optional] 
**dnssec** | **bool** | Enable DNSSEC for this BIND zone.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be one of [ master, slave ]&lt;br&gt; | [optional] 
**backupkeys** | **bool** | Enable backing up DNSSEC keys in the XML configuration for this BIND zone.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;dnssec&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**slaveip** | **str** | The IP address of the slave server for this BIND zone.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;slave&#39;&#x60;&lt;br&gt; | [optional] 
**forwarders** | **List[str]** | The forwarders for this BIND zone.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;forward&#39;&#x60;&lt;br&gt; | [optional] 
**ttl** | **int** | The default TTL interval (in seconds) for records within this BIND zone without a specific TTL.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;master&#39;&#x60;&lt;br&gt; | [optional] 
**baseip** | **str** | The IP address of the base domain for this zone. This sets an A record for the base domain.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;master&#39;&#x60;&lt;br&gt; | [optional] 
**nameserver** | **str** | The SOA nameserver for this zone.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be one of [ master, redirect ]&lt;br&gt; | [optional] 
**mail** | **str** | The SOA email address (RNAME) for this zone. This must be in an FQDN format.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be one of [ master, redirect ]&lt;br&gt; | [optional] 
**serial** | **int** | The SOA serial number for this zone.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be one of [ master, redirect ]&lt;br&gt; | [optional] 
**refresh** | **str** | The SOA refresh interval for this zone. TTL-style time-unit suffixes are supported (e.g. 1h, 1d, 1w), otherwise time in seconds is assumed.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be one of [ master, redirect ]&lt;br&gt; | [optional] 
**retry** | **str** | The SOA retry interval for this zone. TTL-style time-unit suffixes are supported (e.g. 1h, 1d, 1w), otherwise time in seconds is assumed.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be one of [ master, redirect ]&lt;br&gt; | [optional] 
**expire** | **str** | The SOA expiry interval for this zone. TTL-style time-unit suffixes are supported (e.g. 1h, 1d, 1w), otherwise time in seconds is assumed.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be one of [ master, redirect ]&lt;br&gt; | [optional] 
**minimum** | **str** | The SOA minimum TTL interval (in seconds) for this zone. This is also referred to as the negative TTL. TTL-style time-unit suffixes are supported (e.g. 1h, 1d, 1w), otherwise time in seconds is assumed.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be one of [ master, redirect ]&lt;br&gt; | [optional] 
**enable_updatepolicy** | **bool** | Enable a specific dynamic update policy for this BIND zone.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;master&#39;&#x60;&lt;br&gt; | [optional] 
**updatepolicy** | **str** | The update policy for this BIND zone.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;master&#39;&#x60;&lt;br&gt;- &#x60;enable_updatepolicy&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**allowupdate** | **List[str]** | The access lists that are allowed to submit dynamic updates for &#39;master&#39; zones (e.g. dynamic DNS).&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;master&#39;&#x60;&lt;br&gt;- &#x60;enable_updatepolicy&#x60; must be equal to &#x60;false&#x60;&lt;br&gt; | [optional] 
**allowtransfer** | **List[str]** | The access lists that are allowed to transfer this BIND zone.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;master&#39;&#x60;&lt;br&gt; | [optional] 
**allowquery** | **List[str]** | The access lists that are allowed to query this BIND zone.&lt;br&gt; | [optional] 
**regdhcpstatic** | **bool** | Register DHCP static mappings as records in this BIND zone.&lt;br&gt; | [optional] 
**customzonerecords** | **str** | Custom records for this BIND zone.&lt;br&gt; | [optional] 
**records** | [**List[BINDZoneRecordsInner]**](BINDZoneRecordsInner.md) | The records for this BIND zone.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.bind_zone import BINDZone

# TODO update the JSON string below
json = "{}"
# create an instance of BINDZone from a JSON string
bind_zone_instance = BINDZone.from_json(json)
# print the JSON string representation of the object
print(BINDZone.to_json())

# convert the object into a dict
bind_zone_dict = bind_zone_instance.to_dict()
# create an instance of BINDZone from a dict
bind_zone_from_dict = BINDZone.from_dict(bind_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


