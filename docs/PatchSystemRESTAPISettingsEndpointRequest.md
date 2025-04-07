# PatchSystemRESTAPISettingsEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enables or disables the API. If set to &#x60;false&#x60;, the API will no longer respond to API requests              and can only be re-enabled via webConfigurator.&lt;br&gt; | [optional] [default to True]
**read_only** | **bool** | Enables or disables read-only API access. If enabled, the API will only respond to GET requests             and can only be disabled via webConfigurator.&lt;br&gt; | [optional] 
**keep_backup** | **bool** | Enables or disables keeping a persistent backup of the API configuration that can be used             to restore the API configuration after package and systems updates.&lt;br&gt; | [optional] [default to True]
**login_protection** | **bool** | Enables or disables Login Protection for API authentication. When enabled, Login Protection will             monitor API attempts and temporarily block clients who fail API authentication too many times within a             period of time. When disabled, Login Protection will not monitor API authentication but will continue to              monitor webConfigurator and SSH logins (if configured). Login Protection can be configured globally in             System &gt; Advanced.&lt;br&gt; | [optional] [default to True]
**log_successful_auth** | **bool** | Enables or disables logging of API authentication attempts that are successful. By default, only             failed API authentication attempts are logged to prevent flooding the authentication logs. This field is             only applicable when the API &#x60;login_protection&#x60; setting is enabled.&lt;br&gt; | [optional] 
**allow_pre_releases** | **bool** | Enables or disables displaying pre-releases in available API updates. Pre-releases contain fixes             and features that are currently under development and may not be fully stable. Use of pre-release versions             is at your own risk.&lt;br&gt; | [optional] 
**hateoas** | **bool** | Enables or disables HATEOAS. Enabling HATEOAS will allow the API to include links to related resources in API responses. This is primarily useful for frontend web applications and self-navigating client scripts that integrate with HAL standards. Enabling HATEOAS may increase API response times, especially on systems with large configurations.&lt;br&gt; | [optional] 
**expose_sensitive_fields** | **bool** | Enables or disables exposing sensitive fields in API responses. When enabled, sensitive fields such as passwords, private keys, and other sensitive data will be included in API responses.&lt;br&gt; | [optional] 
**override_sensitive_fields** | **List[str]** | Specifies a list of fields (formatted as ModelName:FieldName) that should have their sensitive attribute overridden. Fields selected here will not be considered sensitive and will be included in API responses regardless of the &#x60;expose_sensitive_fields&#x60; setting.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;expose_sensitive_fields&#x60; must be equal to &#x60;false&#x60;&lt;br&gt; | [optional] 
**allowed_interfaces** | **List[str]** | Sets the interfaces allowed to accept incoming API calls.&lt;br&gt; | [optional] 
**represent_interfaces_as** | **str** | Specifies how the API should represent interface names. Use &#x60;descr&#x60; to represent              interface objects by their description name, use &#x60;id&#x60; to represent interface objects by their             internal pfSense ID (e.g. wan, lan, opt1), or use &#x60;if&#x60; to represent interface objects by their             real interface name (e.g. em0, igb1, bxe3).&lt;br&gt; | [optional] [default to 'descr']
**auth_methods** | **List[str]** | Sets the API authentication methods allowed to authenticate API calls.&lt;br&gt; | [optional] [default to [BasicAuth]]
**jwt_exp** | **int** | Sets the amount of time (in seconds) JWTs are valid for.&lt;br&gt; | [optional] [default to 3600]
**ha_sync** | **bool** | Enables or disables syncing API settings to HA peers. When enabled, API settings from this             host will automatically be synced to any hosts defined in &#x60;ha_sync_hosts&#x60;.&lt;br&gt; | [optional] 
**ha_sync_validate_certs** | **bool** | Enables or disables certificate validation when syncing API configurations to HA sync peers. If             enabled, all hosts defined in &#x60;ha_sync_hosts&#x60; must have their webConfigurator configured with a certificate             trusted by this system. It is strongly recommended this be enabled at all times to help mitigate              Man-in-the-Middle attacks.&lt;br&gt; | [optional] [default to True]
**ha_sync_hosts** | **List[str]** | Set a list of IP addresses or hostnames to sync API settings to.&lt;br&gt; | [optional] 
**ha_sync_username** | **str** | Sets the username to use when authenticating for HA sync processes. This user must be the present             on all hosts defined in &#x60;ha_sync_hosts&#x60;.&lt;br&gt; | [optional] 
**ha_sync_password** | **str** | Sets the password to use when authenticating for HA sync processes. This must be the password             for the user defined in &#x60;ha_sync_username&#x60; and must be the same on all hosts defined in &#x60;ha_sync_hosts&#x60;.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.patch_system_restapi_settings_endpoint_request import PatchSystemRESTAPISettingsEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSystemRESTAPISettingsEndpointRequest from a JSON string
patch_system_restapi_settings_endpoint_request_instance = PatchSystemRESTAPISettingsEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchSystemRESTAPISettingsEndpointRequest.to_json())

# convert the object into a dict
patch_system_restapi_settings_endpoint_request_dict = patch_system_restapi_settings_endpoint_request_instance.to_dict()
# create an instance of PatchSystemRESTAPISettingsEndpointRequest from a dict
patch_system_restapi_settings_endpoint_request_from_dict = PatchSystemRESTAPISettingsEndpointRequest.from_dict(patch_system_restapi_settings_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


