# AvailablePackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the pfSense package.&lt;br&gt; | [optional] 
**shortname** | **str** | The package&#39;s shortname.&lt;br&gt; | [optional] [readonly] 
**descr** | **str** | The package&#39;s description.&lt;br&gt; | [optional] [readonly] 
**version** | **str** | The latest version available for this package.&lt;br&gt; | [optional] [readonly] 
**installed** | **bool** | Indicates whether the package is currently installed or not.&lt;br&gt; | [optional] [readonly] 
**deps** | **List[str]** | Dependencies for this package that are also installed when this package is installed.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.available_package import AvailablePackage

# TODO update the JSON string below
json = "{}"
# create an instance of AvailablePackage from a JSON string
available_package_instance = AvailablePackage.from_json(json)
# print the JSON string representation of the object
print(AvailablePackage.to_json())

# convert the object into a dict
available_package_dict = available_package_instance.to_dict()
# create an instance of AvailablePackage from a dict
available_package_from_dict = AvailablePackage.from_dict(available_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


