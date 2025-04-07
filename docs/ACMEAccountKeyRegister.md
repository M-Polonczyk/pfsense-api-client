# ACMEAccountKeyRegister


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the ACME account key to register.&lt;br&gt; | [optional] 
**status** | **str** | The registration status of the ACME account key. This will show &#39;pending&#39; if the registration process is still running, &#39;registered&#39; if the registration was successful, &#39;failed&#39; if the registration failed, and &#39;unknown&#39; if the registration status is not known. Note: This status can only be determined for registrations initiated through the REST API.&lt;br&gt; | [optional] [readonly] [default to 'unknown']

## Example

```python
from pfsense_api_client.models.acme_account_key_register import ACMEAccountKeyRegister

# TODO update the JSON string below
json = "{}"
# create an instance of ACMEAccountKeyRegister from a JSON string
acme_account_key_register_instance = ACMEAccountKeyRegister.from_json(json)
# print the JSON string representation of the object
print(ACMEAccountKeyRegister.to_json())

# convert the object into a dict
acme_account_key_register_dict = acme_account_key_register_instance.to_dict()
# create an instance of ACMEAccountKeyRegister from a dict
acme_account_key_register_from_dict = ACMEAccountKeyRegister.from_dict(acme_account_key_register_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


