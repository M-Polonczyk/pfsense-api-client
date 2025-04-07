# RESTAPIVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_version** | **str** | The current API version installed on this system.&lt;br&gt; | [optional] [readonly] 
**latest_version** | **str** | The latest API version available to this system.&lt;br&gt; | [optional] [readonly] 
**latest_version_release_date** | **str** | The latest API version&#39;s release date.&lt;br&gt; | [optional] [readonly] 
**update_available** | **bool** | Indicates if an API update is available for this system.&lt;br&gt; | [optional] [readonly] 
**install_version** | **str** | Set the API version to update or rollback to.&lt;br&gt; | [optional] 
**available_versions** | **List[str]** | All available versions of the REST API package for this system.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.restapi_version import RESTAPIVersion

# TODO update the JSON string below
json = "{}"
# create an instance of RESTAPIVersion from a JSON string
restapi_version_instance = RESTAPIVersion.from_json(json)
# print the JSON string representation of the object
print(RESTAPIVersion.to_json())

# convert the object into a dict
restapi_version_dict = restapi_version_instance.to_dict()
# create an instance of RESTAPIVersion from a dict
restapi_version_from_dict = RESTAPIVersion.from_dict(restapi_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


