# HAProxySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enables or disable HAProxy on the system.&lt;br&gt; | [optional] 
**maxconn** | **int** | The maximum per-process number of concurrent connections&lt;br&gt; | [optional] 
**nbthread** | **int** | The number of threads to start per process. This setting is experimental.&lt;br&gt; | [optional] [default to 1]
**terminate_on_reload** | **bool** | Enables or disables an immediate stop of old process on reload. (closes existing connections)&lt;br&gt; | [optional] 
**hard_stop_after** | **str** | The maximum time allowed to perform a clean soft-stop. This can be represented as different time values such as 30s, 15m, 3h or 1d.&lt;br&gt; | [optional] [default to '15m']
**carpdev** | **str** | The CARP interface IP to monitor. HAProxy will only run on the firewall whose interface is MASTER.&lt;br&gt; | [optional] 
**localstatsport** | **str** | The internal port to be used for the stats tab. Set to null to disable local stats. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] 
**localstats_refreshtime** | **int** | The internal (in seconds) in which local stats will be refreshed.&lt;br&gt; | [optional] 
**localstats_sticktable_refreshtime** | **int** | The internal (in seconds) in which the sticktable stats will be refreshed.&lt;br&gt; | [optional] 
**remotesyslog** | **str** | The IP address or hostname of the remote syslog server to send logs to. Use &#x60;/var/run/log&#x60; to to log to the local pfSense system log.&lt;br&gt; | [optional] 
**logfacility** | **str** | The logging facility to log to.&lt;br&gt; | [optional] [default to 'syslog']
**loglevel** | **str** | The log level to begin logging events. Only events of this level or higher will be logged.&lt;br&gt; | [optional] [default to 'warning']
**log_send_hostname** | **str** | The hostname field to include in the syslog header. Leave empty to use the system hostname.&lt;br&gt; | [optional] 
**dns_resolvers** | [**List[PostServicesHAProxySettingsDNSResolverEndpointRequest]**](PostServicesHAProxySettingsDNSResolverEndpointRequest.md) | The DNS resolvers HAProxy will use for DNS queries.&lt;br&gt; | [optional] 
**resolver_retries** | **int** | The number of queries to send to resolve a server name before giving up.&lt;br&gt; | [optional] [default to 3]
**resolver_timeoutretry** | **str** | The time between two DNS queries, when no response have been received.&lt;br&gt; | [optional] [default to '1s']
**resolver_holdvalid** | **str** | The interval between two successive name resolution when the last answer was valid.&lt;br&gt; | [optional] [default to '1s']
**email_mailers** | [**List[PostServicesHAProxySettingsEmailMailerEndpointRequest]**](PostServicesHAProxySettingsEmailMailerEndpointRequest.md) | The email servers HAProxy will use to send SMTP alerts.&lt;br&gt; | [optional] 
**email_level** | **str** | The maximum log level to send emails for. Leave empty to disable sending email alerts.&lt;br&gt; | [optional] 
**email_myhostname** | **str** | The hostname to use as the origin of the email.&lt;br&gt; | [optional] 
**email_from** | **str** | The email address to be used as the sender of the emails.&lt;br&gt; | [optional] 
**email_to** | **str** | The email address to send emails to.&lt;br&gt; | [optional] 
**sslcompatibilitymode** | **str** | The SSL/TLS compatibility mode which determines the cipher suites and TLS versions supported.&lt;br&gt; | [optional] [default to 'auto']
**ssldefaultdhparam** | **int** | The maximum size of the Diffie-Hellman parameters used for generating the ephemeral/temporary Diffie-Hellman key in case of DHE key exchange&lt;br&gt; | [optional] [default to 1024]
**advanced** | **str** | Additional HAProxy options to include in the global settings area.&lt;br&gt; | [optional] 
**enablesync** | **bool** | Enables or disables including HAProxy configurations in HA sync if configured.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.ha_proxy_settings import HAProxySettings

# TODO update the JSON string below
json = "{}"
# create an instance of HAProxySettings from a JSON string
ha_proxy_settings_instance = HAProxySettings.from_json(json)
# print the JSON string representation of the object
print(HAProxySettings.to_json())

# convert the object into a dict
ha_proxy_settings_dict = ha_proxy_settings_instance.to_dict()
# create an instance of HAProxySettings from a dict
ha_proxy_settings_from_dict = HAProxySettings.from_dict(ha_proxy_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


