# NTPSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enables or disabled the NTP server.&lt;br&gt; | [optional] [default to True]
**interface** | **List[str]** | The interfaces the NTP server will listen on.&lt;br&gt; | [optional] 
**ntpmaxpeers** | **int** | The maximum number of candidate peers in the NTP pool.&lt;br&gt; | [optional] [default to 5]
**orphan** | **int** | The orphan mode stratum to set. Orphan mode allows the system clock to be used when no other clocks are available. The number here specifies the stratum reported during orphan mode and should normally be set to a number high enough to ensure that any other servers available to clients are preferred over this server&lt;br&gt; | [optional] [default to 12]
**ntpminpoll** | **str** | The minimum poll interval for NTP messages. Use empty string to assume system default, and &#x60;omit&#x60; to not set this value.&lt;br&gt; | [optional] 
**ntpmaxpoll** | **str** | The maximum poll interval for NTP messages. Use empty string to assume system default, and &#x60;omit&#x60; to not set this value. This value must be greater than the &#x60;ntpminpoll&#x60;.&lt;br&gt; | [optional] 
**dnsresolv** | **str** | The IP protocol peers are forced to use for DNS resolution.&lt;br&gt; | [optional] [default to 'auto']
**logpeer** | **bool** | Enable or disable logging peer messages.&lt;br&gt; | [optional] 
**logsys** | **bool** | Enable or disable logging system messages.&lt;br&gt; | [optional] 
**clockstats** | **bool** | Enable or disable logging reference clock statistics.&lt;br&gt; | [optional] 
**loopstats** | **bool** | Enable or disable logging clock discipline statistics.&lt;br&gt; | [optional] 
**peerstats** | **bool** | Enable or disable logging peer statistics.&lt;br&gt; | [optional] 
**statsgraph** | **bool** | Enable or disable RRD graphs for NTP statistics.&lt;br&gt; | [optional] 
**leapsec** | **str** | The Leap second configuration as text.&lt;br&gt; | [optional] 
**serverauth** | **bool** | Enable or disable NTPv3 server authentication. (RFC 1305)&lt;br&gt; | [optional] 
**serverauthkey** | **str** | The NTP server authentication key.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;serverauth&#x60; must be equal to &#x60;true&#x60;&lt;br&gt; | [optional] 
**serverauthalgo** | **str** | The digest algorithm for the server authentication key.&lt;br&gt; | [optional] [default to 'md5']

## Example

```python
from pfsense_api_client.models.ntp_settings import NTPSettings

# TODO update the JSON string below
json = "{}"
# create an instance of NTPSettings from a JSON string
ntp_settings_instance = NTPSettings.from_json(json)
# print the JSON string representation of the object
print(NTPSettings.to_json())

# convert the object into a dict
ntp_settings_dict = ntp_settings_instance.to_dict()
# create an instance of NTPSettings from a dict
ntp_settings_from_dict = NTPSettings.from_dict(ntp_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


