# ARPTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | The hostname associated with the ARP entry.&lt;br&gt; | [optional] [readonly] 
**ip_address** | **str** | The IP address associated with the ARP entry.&lt;br&gt; | [optional] [readonly] 
**mac_address** | **str** | The MAC address associated with the ARP entry.&lt;br&gt; | [optional] [readonly] 
**interface** | **str** | The interface where the ARP entry was registered.&lt;br&gt; | [optional] [readonly] 
**type** | **str** | The type of connection this host utilizes.&lt;br&gt; | [optional] [readonly] 
**permanent** | **bool** | Indicates whether the ARP entry is permanent in the ARP table.&lt;br&gt; | [optional] [readonly] 
**dnsresolve** | **str** | The full DNS name associated with this ARP entry.&lt;br&gt; | [optional] [readonly] 
**expires** | **str** | The expiration time for this ARP entry.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.arp_table import ARPTable

# TODO update the JSON string below
json = "{}"
# create an instance of ARPTable from a JSON string
arp_table_instance = ARPTable.from_json(json)
# print the JSON string representation of the object
print(ARPTable.to_json())

# convert the object into a dict
arp_table_dict = arp_table_instance.to_dict()
# create an instance of ARPTable from a dict
arp_table_from_dict = ARPTable.from_dict(arp_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


