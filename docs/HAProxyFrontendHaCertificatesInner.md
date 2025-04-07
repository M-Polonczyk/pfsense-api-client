# HAProxyFrontendHaCertificatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssl_certificate** | **str** | The SSL/TLS certificate refid to add to this frontend.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.ha_proxy_frontend_ha_certificates_inner import HAProxyFrontendHaCertificatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxyFrontendHaCertificatesInner from a JSON string
ha_proxy_frontend_ha_certificates_inner_instance = HAProxyFrontendHaCertificatesInner.from_json(json)
# print the JSON string representation of the object
print(HAProxyFrontendHaCertificatesInner.to_json())

# convert the object into a dict
ha_proxy_frontend_ha_certificates_inner_dict = ha_proxy_frontend_ha_certificates_inner_instance.to_dict()
# create an instance of HAProxyFrontendHaCertificatesInner from a dict
ha_proxy_frontend_ha_certificates_inner_from_dict = HAProxyFrontendHaCertificatesInner.from_dict(ha_proxy_frontend_ha_certificates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


