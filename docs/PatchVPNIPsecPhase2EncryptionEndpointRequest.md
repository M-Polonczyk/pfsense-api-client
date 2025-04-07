# PatchVPNIPsecPhase2EncryptionEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the encryption algorithm to use for this P2 encryption item.&lt;br&gt; | [optional] 
**keylen** | **int** | The key length for the encryption algorithm.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;name&#x60; must be one of [ aes, aes128gcm, aes192gcm, aes256gcm ]&lt;br&gt; | [optional] 
**parent_id** | **int** | The ID of the parent this object is nested under. | 
**id** | **int** | The ID of the object or resource to interact with. | 

## Example

```python
from pfsense_api_client.models.patch_vpni_psec_phase2_encryption_endpoint_request import PatchVPNIPsecPhase2EncryptionEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchVPNIPsecPhase2EncryptionEndpointRequest from a JSON string
patch_vpni_psec_phase2_encryption_endpoint_request_instance = PatchVPNIPsecPhase2EncryptionEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchVPNIPsecPhase2EncryptionEndpointRequest.to_json())

# convert the object into a dict
patch_vpni_psec_phase2_encryption_endpoint_request_dict = patch_vpni_psec_phase2_encryption_endpoint_request_instance.to_dict()
# create an instance of PatchVPNIPsecPhase2EncryptionEndpointRequest from a dict
patch_vpni_psec_phase2_encryption_endpoint_request_from_dict = PatchVPNIPsecPhase2EncryptionEndpointRequest.from_dict(patch_vpni_psec_phase2_encryption_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


