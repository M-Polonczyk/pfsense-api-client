# IPsecPhase2EncryptionAlgorithmOptionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the encryption algorithm to use for this P2 encryption item.&lt;br&gt; | 
**keylen** | **int** | The key length for the encryption algorithm.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;name&#x60; must be one of [ aes, aes128gcm, aes192gcm, aes256gcm ]&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.i_psec_phase2_encryption_algorithm_option_inner import IPsecPhase2EncryptionAlgorithmOptionInner

# TODO update the JSON string below
json = "{}"
# create an instance of IPsecPhase2EncryptionAlgorithmOptionInner from a JSON string
i_psec_phase2_encryption_algorithm_option_inner_instance = IPsecPhase2EncryptionAlgorithmOptionInner.from_json(json)
# print the JSON string representation of the object
print(IPsecPhase2EncryptionAlgorithmOptionInner.to_json())

# convert the object into a dict
i_psec_phase2_encryption_algorithm_option_inner_dict = i_psec_phase2_encryption_algorithm_option_inner_instance.to_dict()
# create an instance of IPsecPhase2EncryptionAlgorithmOptionInner from a dict
i_psec_phase2_encryption_algorithm_option_inner_from_dict = IPsecPhase2EncryptionAlgorithmOptionInner.from_dict(i_psec_phase2_encryption_algorithm_option_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


