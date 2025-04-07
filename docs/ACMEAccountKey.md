# ACMEAccountKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the ACME account key.&lt;br&gt; | [optional] 
**descr** | **str** | A description of the ACME account key.&lt;br&gt; | [optional] 
**email** | **str** | The email address associated with the ACME account key.&lt;br&gt; | [optional] 
**acmeserver** | **str** | The ACME server this account key will belong to.&lt;br&gt; | [optional] 
**accountkey** | **str** | The RSA private key for the ACME account key.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.acme_account_key import ACMEAccountKey

# TODO update the JSON string below
json = "{}"
# create an instance of ACMEAccountKey from a JSON string
acme_account_key_instance = ACMEAccountKey.from_json(json)
# print the JSON string representation of the object
print(ACMEAccountKey.to_json())

# convert the object into a dict
acme_account_key_dict = acme_account_key_instance.to_dict()
# create an instance of ACMEAccountKey from a dict
acme_account_key_from_dict = ACMEAccountKey.from_dict(acme_account_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


