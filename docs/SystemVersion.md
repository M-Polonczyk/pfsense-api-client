# SystemVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The official pfSense version release name. (e.g. X.X.X-RELEASE)&lt;br&gt; | [optional] [readonly] 
**base** | **str** | The base pfSense version. For pfSense CE, this will be the major and minor version but not the patch. For pfSense Plus, this will be the version year and month but not the patch.&lt;br&gt; | [optional] [readonly] 
**patch** | **str** | The pfSense build&#39;s patch version.&lt;br&gt; | [optional] [readonly] 
**buildtime** | **str** | The datetime string of when the pfSense version was initially built.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.system_version import SystemVersion

# TODO update the JSON string below
json = "{}"
# create an instance of SystemVersion from a JSON string
system_version_instance = SystemVersion.from_json(json)
# print the JSON string representation of the object
print(SystemVersion.to_json())

# convert the object into a dict
system_version_dict = system_version_instance.to_dict()
# create an instance of SystemVersion from a dict
system_version_from_dict = SystemVersion.from_dict(system_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


