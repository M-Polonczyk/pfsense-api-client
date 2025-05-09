# PostSystemCRLEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refid** | **str** | The unique ID for this CRL. This is automatically generated by the system and cannot be changed.&lt;br&gt; | [optional] [readonly] [default to '67ed081a76f44']
**caref** | **str** | The unique ID of the CA that this CRL is associated with.&lt;br&gt; | 
**descr** | **str** | The unique name/description for this CRL.&lt;br&gt; | 
**method** | **str** | The method used to generate this CRL.&lt;br&gt; | 
**lifetime** | **int** | The lifetime of this CRL in days.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;method&#x60; must be equal to &#x60;&#39;internal&#39;&#x60;&lt;br&gt; | [optional] [default to 730]
**serial** | **int** | The serial number of the CRL.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;method&#x60; must be equal to &#x60;&#39;internal&#39;&#x60;&lt;br&gt; | [optional] 
**text** | **str** | The raw x509 CRL data.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;method&#x60; must be equal to &#x60;&#39;existing&#39;&#x60;&lt;br&gt; | 
**cert** | [**List[CertificateRevocationListCertInner]**](CertificateRevocationListCertInner.md) | The list of revoked certificates in this CRL.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;method&#x60; must be equal to &#x60;&#39;internal&#39;&#x60;&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_system_crl_endpoint_request import PostSystemCRLEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSystemCRLEndpointRequest from a JSON string
post_system_crl_endpoint_request_instance = PostSystemCRLEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostSystemCRLEndpointRequest.to_json())

# convert the object into a dict
post_system_crl_endpoint_request_dict = post_system_crl_endpoint_request_instance.to_dict()
# create an instance of PostSystemCRLEndpointRequest from a dict
post_system_crl_endpoint_request_from_dict = PostSystemCRLEndpointRequest.from_dict(post_system_crl_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


