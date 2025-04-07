# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The username of this local user.&lt;br&gt; | [optional] 
**password** | **str** | The password of this local user.&lt;br&gt; | [optional] 
**uid** | **int** | The UID of this local user. This value is automatically assigned and cannot be changed.&lt;br&gt; | [optional] [readonly] [default to 2000]
**scope** | **str** | The scope of this local user. This value is automatically assigned and cannot be changed.&lt;br&gt; | [optional] [readonly] [default to 'user']
**priv** | **List[str]** | The privileges assigned to this local user.&lt;br&gt; | [optional] 
**disabled** | **bool** | Disable this local user.&lt;br&gt; | [optional] 
**descr** | **str** | The full descriptive name for this local user.&lt;br&gt; | [optional] 
**expires** | **str** | The expiration date for this user in mm/dd/YYYY format. Use empty string for no expiration&lt;br&gt; | [optional] 
**cert** | **List[str]** | The user certificates to assign this user. Items must be existing certificate &#x60;refid&#x60;s.&lt;br&gt; | [optional] 
**authorizedkeys** | **str** | The SSH authorized keys to assign this user.&lt;br&gt; | [optional] 
**ipsecpsk** | **str** | The IPsec pre-shared key to assign this user.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


