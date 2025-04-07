# BINDView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the view.&lt;br&gt; | [optional] 
**descr** | **str** | A description for the view.&lt;br&gt; | [optional] 
**recursion** | **bool** | Enables or disables recursion for the view.&lt;br&gt; | [optional] 
**match_clients** | **List[str]** | The access lists to match clients against.&lt;br&gt; | [optional] 
**allow_recursion** | **List[str]** | The access lists to allow recursion for.&lt;br&gt; | [optional] 
**bind_custom_options** | **str** | Custom BIND options for the view.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.bind_view import BINDView

# TODO update the JSON string below
json = "{}"
# create an instance of BINDView from a JSON string
bind_view_instance = BINDView.from_json(json)
# print the JSON string representation of the object
print(BINDView.to_json())

# convert the object into a dict
bind_view_dict = bind_view_instance.to_dict()
# create an instance of BINDView from a dict
bind_view_from_dict = BINDView.from_dict(bind_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


