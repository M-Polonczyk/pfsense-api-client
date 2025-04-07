# GetServicesBINDAccessListsEndpoint200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | The HTTP status code that corresponds with the API response. | [optional] [default to 200]
**status** | **str** | The HTTP status message that corresponds with the HTTP status code. | [optional] [default to 'ok']
**response_id** | **str** | The unique response ID that corresponds with the result of the APIcall. In most situations, this will contain an error code. | [optional] 
**message** | **str** | The descriptive message detailing the results of the API call. | [optional] 
**data** | [**List[BINDAccessList]**](BINDAccessList.md) |  | [optional] 
**links** | **object** | An array of links to resources that are related to this API response. | [optional] 

## Example

```python
from pfsense_api_client.models.get_services_bind_access_lists_endpoint200_response import GetServicesBINDAccessListsEndpoint200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServicesBINDAccessListsEndpoint200Response from a JSON string
get_services_bind_access_lists_endpoint200_response_instance = GetServicesBINDAccessListsEndpoint200Response.from_json(json)
# print the JSON string representation of the object
print(GetServicesBINDAccessListsEndpoint200Response.to_json())

# convert the object into a dict
get_services_bind_access_lists_endpoint200_response_dict = get_services_bind_access_lists_endpoint200_response_instance.to_dict()
# create an instance of GetServicesBINDAccessListsEndpoint200Response from a dict
get_services_bind_access_lists_endpoint200_response_from_dict = GetServicesBINDAccessListsEndpoint200Response.from_dict(get_services_bind_access_lists_endpoint200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


