# HAProxyFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this file.&lt;br&gt; | [optional] 
**type** | **str** | The type of file. Use &#x60;null&#x60; to assume an Errorfile.&lt;br&gt; | [optional] 
**content** | **str** | The content of this file.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.ha_proxy_file import HAProxyFile

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxyFile from a JSON string
ha_proxy_file_instance = HAProxyFile.from_json(json)
# print the JSON string representation of the object
print(HAProxyFile.to_json())

# convert the object into a dict
ha_proxy_file_dict = ha_proxy_file_instance.to_dict()
# create an instance of HAProxyFile from a dict
ha_proxy_file_from_dict = HAProxyFile.from_dict(ha_proxy_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


