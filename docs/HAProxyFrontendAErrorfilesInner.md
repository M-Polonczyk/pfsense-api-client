# HAProxyFrontendAErrorfilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorcode** | **int** | The HTTP status code that will trigger this error file to be used.&lt;br&gt; | 
**errorfile** | **str** | The HAProxy error file object that should be used for the assigned HTTP status code.&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.ha_proxy_frontend_a_errorfiles_inner import HAProxyFrontendAErrorfilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxyFrontendAErrorfilesInner from a JSON string
ha_proxy_frontend_a_errorfiles_inner_instance = HAProxyFrontendAErrorfilesInner.from_json(json)
# print the JSON string representation of the object
print(HAProxyFrontendAErrorfilesInner.to_json())

# convert the object into a dict
ha_proxy_frontend_a_errorfiles_inner_dict = ha_proxy_frontend_a_errorfiles_inner_instance.to_dict()
# create an instance of HAProxyFrontendAErrorfilesInner from a dict
ha_proxy_frontend_a_errorfiles_inner_from_dict = HAProxyFrontendAErrorfilesInner.from_dict(ha_proxy_frontend_a_errorfiles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


