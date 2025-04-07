# PostSystemPackageEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the pfSense package.&lt;br&gt; | 
**shortname** | **str** | The package&#39;s shortname.&lt;br&gt; | [optional] [readonly] 
**descr** | **str** | The package&#39;s description.&lt;br&gt; | [optional] [readonly] 
**installed_version** | **str** | The version of the package currently installed.&lt;br&gt; | [optional] [readonly] 
**latest_version** | **str** | The latest version available for this package.&lt;br&gt; | [optional] [readonly] 
**update_available** | **bool** | Indicates whether the installed package has an update available.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.post_system_package_endpoint_request import PostSystemPackageEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSystemPackageEndpointRequest from a JSON string
post_system_package_endpoint_request_instance = PostSystemPackageEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostSystemPackageEndpointRequest.to_json())

# convert the object into a dict
post_system_package_endpoint_request_dict = post_system_package_endpoint_request_instance.to_dict()
# create an instance of PostSystemPackageEndpointRequest from a dict
post_system_package_endpoint_request_from_dict = PostSystemPackageEndpointRequest.from_dict(post_system_package_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


