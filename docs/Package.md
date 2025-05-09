# Package


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the pfSense package.&lt;br&gt; | [optional] 
**shortname** | **str** | The package&#39;s shortname.&lt;br&gt; | [optional] [readonly] 
**descr** | **str** | The package&#39;s description.&lt;br&gt; | [optional] [readonly] 
**installed_version** | **str** | The version of the package currently installed.&lt;br&gt; | [optional] [readonly] 
**latest_version** | **str** | The latest version available for this package.&lt;br&gt; | [optional] [readonly] 
**update_available** | **bool** | Indicates whether the installed package has an update available.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.package import Package

# TODO update the JSON string below
json = "{}"
# create an instance of Package from a JSON string
package_instance = Package.from_json(json)
# print the JSON string representation of the object
print(Package.to_json())

# convert the object into a dict
package_dict = package_instance.to_dict()
# create an instance of Package from a dict
package_from_dict = Package.from_dict(package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


