# HAProxyBackendErrorFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorcode** | **int** | The HTTP status code that will trigger this error file to be used.&lt;br&gt; | [optional] 
**errorfile** | **str** | The HAProxy error file object that should be used for the assigned HTTP status code.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.ha_proxy_backend_error_file import HAProxyBackendErrorFile

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxyBackendErrorFile from a JSON string
ha_proxy_backend_error_file_instance = HAProxyBackendErrorFile.from_json(json)
# print the JSON string representation of the object
print(HAProxyBackendErrorFile.to_json())

# convert the object into a dict
ha_proxy_backend_error_file_dict = ha_proxy_backend_error_file_instance.to_dict()
# create an instance of HAProxyBackendErrorFile from a dict
ha_proxy_backend_error_file_from_dict = HAProxyBackendErrorFile.from_dict(ha_proxy_backend_error_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


