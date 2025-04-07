# PostUserAuthServerEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refid** | **str** | The unique reference ID for this authentication server. This value is only used internally and cannot be manually set or changed.&lt;br&gt; | [optional] [readonly] [default to '67ed081aa92b7']
**type** | **str** | The type of this authentication server.&lt;br&gt; | 
**name** | **str** | The descriptive name for this authentication server.&lt;br&gt; | 
**host** | **str** | The remote IP address or hostname of the authentication server.&lt;br&gt; | 
**ldap_port** | **str** | The LDAP port to connect to on this LDAP authentication server. Valid options are: a TCP/UDP port number&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | 
**ldap_urltype** | **str** | The encryption mode to use when connecting to this authentication server. Use &#x60;Standard TCP&#x60; for unencrypted LDAP connections, use &#x60;STARTTLS Encrypt&#x60; to start an encrypted connection via STARTTLS if it&#39;s available, or &#x60;SSL/TLS Encrypted&#x60; to only use LDAPS encrypted connections.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | 
**ldap_protver** | **int** | The LDAP protocol version to use for connections to this LDAP authentication server.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | [optional] [default to 3]
**ldap_timeout** | **int** | The timeout (in seconds) for connections to the LDAP authentication server.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | [optional] [default to 25]
**ldap_caref** | **str** | The certificate authority used to validate the LDAP server certificate.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;ldap_urltype&#x60; must be one of [ starttls, encrypted ]&lt;br&gt; | [optional] [default to 'global']
**ldap_scope** | **str** | The LDAP search scope. Use &#x60;one&#x60; to limit the scope to a single level, or &#x60;subtree&#x60; to allow the entire subtree to be searched.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | 
**ldap_basedn** | **str** | The root for LDAP searches on this authentication server.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | [optional] 
**ldap_authcn** | **str** | The LDAP authentication container.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | [optional] 
**ldap_extended_enabled** | **bool** | Enable LDAP extended queries.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | [optional] 
**ldap_extended_query** | **str** | The extended LDAP query to make during LDAP searches.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt;- &#x60;ldap_extended_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**ldap_binddn** | **str** | The DN to use when binding to this authentication server. Set to &#x60;null&#x60; to bind anonymously.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | [optional] 
**ldap_bindpw** | **str** | The password to use when binding to this authentication server.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt;- &#x60;ldap_binddn&#x60; must not be equal to &#x60;NULL&#x60;&lt;br&gt; | 
**ldap_attr_user** | **str** | The LDAP user attribute.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | [optional] [default to 'cn']
**ldap_attr_group** | **str** | The LDAP group attribute.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | [optional] [default to 'cn']
**ldap_attr_member** | **str** | The LDAP member attribute.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | [optional] [default to 'member']
**ldap_rfc2307** | **bool** | Enables or disable RFC2307 LDAP options.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | [optional] 
**ldap_rfc2307_userdn** | **bool** | Enables or disable the use of DNs for username searches.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt;- &#x60;ldap_rfc2307&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**ldap_attr_groupobj** | **str** | The group object class for groups in RFC2307 mode.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt;- &#x60;ldap_rfc2307&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] [default to 'posixGroup']
**ldap_pam_groupdn** | **str** | The group DN to use for shell authentication. Users must be a member of this group and have valid posixAccount attributes to sign in.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | [optional] 
**ldap_utf8** | **bool** | Enables or disables UTF-8 encoding LDAP parameters before sending them to this authentication server&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | [optional] 
**ldap_nostrip_at** | **bool** | Do not strip away parts of the username after the @ symbol.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | [optional] 
**ldap_allow_unauthenticated** | **bool** | Enables or disables unauthenticated binding. Unauthenticated binds are bind with an existing login but with an empty password. Some LDAP servers (Microsoft AD) allow this type of bind without any possibility to disable it.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;ldap&#39;&#x60;&lt;br&gt; | [optional] [default to True]
**radius_secret** | **str** | The shared secret to use when authenticating to this RADIUS server.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;radius&#39;&#x60;&lt;br&gt; | 
**radius_auth_port** | **str** | The port used by RADIUS for authentication. Set to &#x60;null&#x60; to disable use of authentication services. Valid options are: a TCP/UDP port number&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;radius&#39;&#x60;&lt;br&gt; | [optional] [default to '1812']
**radius_acct_port** | **str** | The port used by RADIUS for accounting. Set to &#x60;null&#x60; to disable use of accounting services. Valid options are: a TCP/UDP port number&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;radius&#39;&#x60;&lt;br&gt; | [optional] [default to '1813']
**radius_protocol** | **str** | The RADIUS protocol to use when authenticating.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;radius&#39;&#x60;&lt;br&gt; | [optional] [default to 'MSCHAPv2']
**radius_timeout** | **int** | The timeout (in seconds) for connections to this RADIUS authentication server.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;radius&#39;&#x60;&lt;br&gt; | [optional] [default to 5]
**radius_nasip_attribute** | **str** | The interface whose IP will be used as the &#39;NAS-IP-Address&#39; attribute during RADIUS Access-Requests. This choice will not change the interface used for contacting the RADIUS server.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must be equal to &#x60;&#39;radius&#39;&#x60;&lt;br&gt; | 

## Example

```python
from pfsense_api_client.models.post_user_auth_server_endpoint_request import PostUserAuthServerEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostUserAuthServerEndpointRequest from a JSON string
post_user_auth_server_endpoint_request_instance = PostUserAuthServerEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostUserAuthServerEndpointRequest.to_json())

# convert the object into a dict
post_user_auth_server_endpoint_request_dict = post_user_auth_server_endpoint_request_instance.to_dict()
# create an instance of PostUserAuthServerEndpointRequest from a dict
post_user_auth_server_endpoint_request_from_dict = PostUserAuthServerEndpointRequest.from_dict(post_user_auth_server_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


