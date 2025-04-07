# HAProxyBackend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this backend.&lt;br&gt; | [optional] 
**servers** | [**List[HAProxyBackendServersInner]**](HAProxyBackendServersInner.md) | The pool of servers this backend will use.&lt;br&gt; | [optional] 
**balance** | **str** | The load balancing option to use for servers assigned to this backend.&lt;br&gt; | [optional] 
**balance_urilen** | **int** | The number of URI characters the algorithm should consider when hashing.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;balance&#x60; must be equal to &#x60;&#39;uri&#39;&#x60;&lt;br&gt; | [optional] 
**balance_uridepth** | **int** | The maximum directory depth to be used to compute the hash. One level is counted for each slash in the request.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;balance&#x60; must be equal to &#x60;&#39;uri&#39;&#x60;&lt;br&gt; | [optional] 
**balance_uriwhole** | **bool** | Enables or disables allowing the use of whole URIs, including URL parameters.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;balance&#x60; must be equal to &#x60;&#39;uri&#39;&#x60;&lt;br&gt; | [optional] 
**acls** | [**List[HAProxyBackendAclsInner]**](HAProxyBackendAclsInner.md) | The ACLs to apply to this backend.&lt;br&gt; | [optional] 
**actions** | [**List[HAProxyBackendActionsInner]**](HAProxyBackendActionsInner.md) | The actions to apply to this backend.&lt;br&gt; | [optional] 
**connection_timeout** | **int** | The amount of time (in milliseconds) to wait before giving up on connections.&lt;br&gt; | [optional] [default to 30000]
**server_timeout** | **int** | The amount of time (in milliseconds) to wait for data transferred to or from the server.&lt;br&gt; | [optional] [default to 30000]
**retries** | **int** | The number of retry attempts to allow after a connection failure to the server.&lt;br&gt; | [optional] 
**check_type** | **str** | The health check method to use when checking the health of backend servers.&lt;br&gt; | [optional] [default to 'none']
**checkinter** | **int** | The interval (in milliseconds) in which health checks will be performed.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;check_type&#x60; must not be equal to &#x60;&#39;none&#39;&#x60;&lt;br&gt; | [optional] 
**log_health_checks** | **bool** | Enables or disables logging changes to the health check status&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;check_type&#x60; must not be equal to &#x60;&#39;none&#39;&#x60;&lt;br&gt; | [optional] 
**httpcheck_method** | **str** | The HTTP method to use for HTTP health checks.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;check_type&#x60; must be equal to &#x60;&#39;HTTP&#39;&#x60;&lt;br&gt; | [optional] [default to 'OPTIONS']
**monitor_uri** | **str** | The URL to use for HTTP health checks.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;check_type&#x60; must be equal to &#x60;&#39;HTTP&#39;&#x60;&lt;br&gt; | [optional] [default to '/']
**monitor_httpversion** | **str** | The HTTP version to use for HTTP health checks.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;check_type&#x60; must be equal to &#x60;&#39;HTTP&#39;&#x60;&lt;br&gt; | [optional] [default to 'HTTP/1.0']
**monitor_username** | **str** | The username to use for MySQL or PostgreSQL health checks.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;check_type&#x60; must be one of [ MySQL, PostgreSQL ]&lt;br&gt; | [optional] 
**monitor_domain** | **str** | The domain to use for SMTP or ESMTP health checks.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;check_type&#x60; must be one of [ SMTP, ESMTP ]&lt;br&gt; | [optional] 
**agent_checks** | **bool** | Enables or disables using a TCP connection to read an ASCII string of the form.&lt;br&gt; | [optional] 
**agent_port** | **str** |  Valid options are: a TCP/UDP port number&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;agent_checks&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**agent_inter** | **int** | The interval (in milliseconds) between agent checks.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;agent_checks&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] [default to 2000]
**persist_cookie_enabled** | **bool** | Enables or disables cookie based persistence.&lt;br&gt; | [optional] 
**persist_cookie_name** | **str** | The string name to track in Set-Cookie and Cookie HTTP headers.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;persist_cookie_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**persist_cookie_mode** | **str** | The mode HAProxy uses to insert/prefix/replace or examine cookie and set-cookie headers.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;persist_cookie_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] [default to 'passive']
**persist_cookie_cachable** | **bool** | Enables or disables allowing shared caches to cache the server response.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;persist_cookie_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**persist_cookie_postonly** | **bool** | Enables or disables only inserting cookies on POST requests.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;persist_cookie_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**persist_cookie_httponly** | **bool** | Enables or disables preventing the use of cookies with non-HTTP components.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;persist_cookie_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**persist_cookie_secure** | **bool** | Enables or disables prevention of cookie usage over non-secure channels.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;persist_cookie_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**haproxy_cookie_maxidle** | **int** | The max-idle time to allow. This option only applies to insert mode cookies.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;persist_cookie_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**haproxy_cookie_maxlife** | **int** | The max-life time to allow. This option only applies to insert mode cookies.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;persist_cookie_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**haproxy_cookie_domains** | **List[str]** | The domains to set the cookies for.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;persist_cookie_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**haproxy_cookie_dynamic_cookie_key** | **str** | The dynamic cookie secret key. This is will be used to generate dynamic cookies for this backend.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;persist_cookie_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**persist_sticky_type** | **str** | The sticky table mode to use for this backend. These options are used to make sure subsequent requests from a single client go to the same backend.&lt;br&gt; | [optional] [default to 'none']
**persist_stick_expire** | **str** | The maximum duration of an entry in the stick-table since it was last created, refreshed or matched.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;persist_sticky_type&#x60; must not be equal to &#x60;&#39;none&#39;&#x60;&lt;br&gt; | [optional] 
**persist_stick_tablesize** | **str** | The maximum number of entries allowed in the table. This value directly impacts memory usage.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;persist_sticky_type&#x60; must not be equal to &#x60;&#39;none&#39;&#x60;&lt;br&gt; | [optional] 
**persist_stick_cookiename** | **str** | The cookie name to use for stick table.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;persist_sticky_type&#x60; must be one of [ stick_cookie_value, stick_rdp_cookie ]&lt;br&gt; | [optional] 
**persist_stick_length** | **int** | The maximum number of characters allowed in a string type stick table&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;persist_sticky_type&#x60; must be one of [ stick_cookie_value, stick_rdp_cookie ]&lt;br&gt; | [optional] 
**email_level** | **str** | The maximum log level to send emails for. Leave empty to disable sending email alerts. If left empty, the value set in the global settings will be used.&lt;br&gt; | [optional] 
**email_to** | **str** | The email address to send emails to. If left empty, the value set in the global settings will be used.&lt;br&gt; | [optional] 
**stats_enabled** | **bool** | Enables or disables the HAProxy statistics page for this backend.&lt;br&gt; | [optional] 
**stats_uri** | **str** | The statistics URL for this backend.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;stats_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**stats_scope** | **List[str]** | The frontends and backends stats to be shown, leave empty to show all.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;stats_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**stats_realm** | **str** | The realm that is shown when authentication is requested by HAProxy.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;stats_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**stats_username** | **str** | The stats page username&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;stats_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**stats_password** | **str** | The stats page password.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;stats_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**stats_admin** | **str** | The admin to make use of the options disable/enable/softstop/softstart/killsessions from the stats page.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;stats_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**stats_node** | **str** | The short name displayed in stats and helps differentiate which server in the cluster is actually serving clients.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;stats_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**stats_desc** | **str** | The verbose description for this node.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;stats_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**stats_refresh** | **int** | The interval (in seconds) in which the stats page is refreshed.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;stats_enabled&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] [default to 10]
**strict_transport_security** | **int** | The HSTS validity period for this backend. Leave empty to disable HSTS.&lt;br&gt; | [optional] 
**errorfiles** | [**List[HAProxyBackendErrorfilesInner]**](HAProxyBackendErrorfilesInner.md) | The HAProxy error file mappings to use for this backend.&lt;br&gt; | [optional] 
**cookie_attribute_secure** | **bool** | Enables or disables assigning the secure attributes on cookies for this backend.&lt;br&gt; | [optional] 
**advanced** | **str** | The per server pass thru to apply to each server line.&lt;br&gt; | [optional] 
**advanced_backend** | **str** | The backend pass thru to apply to the backend section.&lt;br&gt; | [optional] 
**transparent_clientip** | **bool** | Enables or disables using the client-IP to connect to backend servers.&lt;br&gt; | [optional] 
**transparent_interface** | **str** | The interface that will connect to the backend server.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;transparent_clientip&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.ha_proxy_backend import HAProxyBackend

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxyBackend from a JSON string
ha_proxy_backend_instance = HAProxyBackend.from_json(json)
# print the JSON string representation of the object
print(HAProxyBackend.to_json())

# convert the object into a dict
ha_proxy_backend_dict = ha_proxy_backend_instance.to_dict()
# create an instance of HAProxyBackend from a dict
ha_proxy_backend_from_dict = HAProxyBackend.from_dict(ha_proxy_backend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


