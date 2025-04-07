# SystemStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** | The verbose name of this system&#39;s platform.&lt;br&gt; | [optional] [readonly] 
**serial** | **str** | The system&#39;s unique serial number/ID.&lt;br&gt; | [optional] [readonly] 
**netgate_id** | **str** | The unique ID issued for this pfSense instance by Netgate.&lt;br&gt; | [optional] [readonly] 
**uptime** | **str** | The amount of time this system has been up since the last reboot.&lt;br&gt; | [optional] [readonly] 
**bios_vendor** | **str** | The name of the BIOS vendor.&lt;br&gt; | [optional] [readonly] 
**bios_version** | **str** | The BIOS version installed on this system.&lt;br&gt; | [optional] [readonly] 
**bios_date** | **str** | The build date of the BIOS version.&lt;br&gt; | [optional] [readonly] 
**kernel_pti** | **bool** | Indicates whether kernel PTI is enabled or not.&lt;br&gt; | [optional] [readonly] 
**mds_mitigation** | **str** | Indicates whether MDS mitigation is enabled or not.&lt;br&gt; | [optional] [readonly] 
**temp_c** | **float** | The current system temperature in celsius.&lt;br&gt; | [optional] [readonly] 
**temp_f** | **float** | The current system temperature in fahrenheit.&lt;br&gt; | [optional] [readonly] 
**cpu_model** | **str** | The model of CPU installed in this system and other CPU info.&lt;br&gt; | [optional] [readonly] 
**cpu_load_avg** | **List[float]** | The CPU load averages. The first value represents the load average for the last minute, the second value represents the load average for the last 5 minutes, and the third value represents the load average for the last 15 minutes.&lt;br&gt; | [optional] [readonly] 
**cpu_count** | **int** | The total number of CPUs cores available on this system.&lt;br&gt; | [optional] [readonly] 
**cpu_usage** | **float** | The current CPU usage as a whole percentage. Note: This is an approximate usage based on the last minute load average and total number of CPU cores. This may not represent exact CPU usage.&lt;br&gt; | [optional] [readonly] 
**mbuf_usage** | **float** | The current MBUF usage as a whole percentage.&lt;br&gt; | [optional] [readonly] 
**mem_usage** | **float** | The current memory usage as a whole percentage.&lt;br&gt; | [optional] [readonly] 
**swap_usage** | **float** | The current swap usage as a whole percentage.&lt;br&gt; | [optional] [readonly] 
**disk_usage** | **float** | The current disk usage as a whole percentage.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.system_status import SystemStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SystemStatus from a JSON string
system_status_instance = SystemStatus.from_json(json)
# print the JSON string representation of the object
print(SystemStatus.to_json())

# convert the object into a dict
system_status_dict = system_status_instance.to_dict()
# create an instance of SystemStatus from a dict
system_status_from_dict = SystemStatus.from_dict(system_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


