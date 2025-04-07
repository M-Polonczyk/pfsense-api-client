# PostVPNIPsecPhase1EncryptionEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_algorithm_name** | **str** | The name of the encryption algorithm to use for this P1 encryption item.&lt;br&gt; | 
**encryption_algorithm_keylen** | **int** | The key length for the encryption algorithm.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;encryption_algorithm_name&#x60; must be one of [ aes, aes128gcm, aes192gcm, aes256gcm ]&lt;br&gt; | 
**hash_algorithm** | **str** | The hash algorithm to use for this P1 encryption item.&lt;br&gt; | 
**dhgroup** | **int** | The Diffie-Hellman (DH) group to use for this P1 encryption item.&lt;br&gt; | 
**prf_algorithm** | **str** | The PRF algorithm to use for this P1 encryption item. This value has no affect unless the P1 entry has PRF enabled.&lt;br&gt; | [optional] [default to 'sha256']
**parent_id** | **int** | The ID of the parent this object is nested under. | 

## Example

```python
from pfsense_api_client.models.post_vpni_psec_phase1_encryption_endpoint_request import PostVPNIPsecPhase1EncryptionEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostVPNIPsecPhase1EncryptionEndpointRequest from a JSON string
post_vpni_psec_phase1_encryption_endpoint_request_instance = PostVPNIPsecPhase1EncryptionEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostVPNIPsecPhase1EncryptionEndpointRequest.to_json())

# convert the object into a dict
post_vpni_psec_phase1_encryption_endpoint_request_dict = post_vpni_psec_phase1_encryption_endpoint_request_instance.to_dict()
# create an instance of PostVPNIPsecPhase1EncryptionEndpointRequest from a dict
post_vpni_psec_phase1_encryption_endpoint_request_from_dict = PostVPNIPsecPhase1EncryptionEndpointRequest.from_dict(post_vpni_psec_phase1_encryption_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


