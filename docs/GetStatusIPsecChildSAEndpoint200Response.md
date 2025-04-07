# GetStatusIPsecChildSAEndpoint200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | The HTTP status code that corresponds with the API response. | [optional] [default to 200]
**status** | **str** | The HTTP status message that corresponds with the HTTP status code. | [optional] [default to 'ok']
**response_id** | **str** | The unique response ID that corresponds with the result of the APIcall. In most situations, this will contain an error code. | [optional] 
**message** | **str** | The descriptive message detailing the results of the API call. | [optional] 
**data** | [**IPsecChildSAStatus**](IPsecChildSAStatus.md) |  | [optional] 
**links** | **object** | An array of links to resources that are related to this API response. | [optional] 

## Example

```python
from pfsense_api_client.models.get_status_i_psec_child_sa_endpoint200_response import GetStatusIPsecChildSAEndpoint200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusIPsecChildSAEndpoint200Response from a JSON string
get_status_i_psec_child_sa_endpoint200_response_instance = GetStatusIPsecChildSAEndpoint200Response.from_json(json)
# print the JSON string representation of the object
print(GetStatusIPsecChildSAEndpoint200Response.to_json())

# convert the object into a dict
get_status_i_psec_child_sa_endpoint200_response_dict = get_status_i_psec_child_sa_endpoint200_response_instance.to_dict()
# create an instance of GetStatusIPsecChildSAEndpoint200Response from a dict
get_status_i_psec_child_sa_endpoint200_response_from_dict = GetStatusIPsecChildSAEndpoint200Response.from_dict(get_status_i_psec_child_sa_endpoint200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


