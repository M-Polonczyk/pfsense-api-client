# HAProxyFrontendCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssl_certificate** | **str** | The SSL/TLS certificate refid to add to this frontend.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.ha_proxy_frontend_certificate import HAProxyFrontendCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxyFrontendCertificate from a JSON string
ha_proxy_frontend_certificate_instance = HAProxyFrontendCertificate.from_json(json)
# print the JSON string representation of the object
print(HAProxyFrontendCertificate.to_json())

# convert the object into a dict
ha_proxy_frontend_certificate_dict = ha_proxy_frontend_certificate_instance.to_dict()
# create an instance of HAProxyFrontendCertificate from a dict
ha_proxy_frontend_certificate_from_dict = HAProxyFrontendCertificate.from_dict(ha_proxy_frontend_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


