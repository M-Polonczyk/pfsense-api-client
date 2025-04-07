# PostServicesNTPTimeServerEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeserver** | **str** | The IP or hostname of the remote NTP time server, pool or peer.&lt;br&gt; | 
**type** | **str** | The type of this timeserver. Use &#x60;server&#x60; is &#x60;timeserver&#x60; is a standalone NTP server, use &#x60;pool&#x60; if &#x60;timeserver&#x60; represents an NTP pool, or &#x60;peer&#x60; if &#x60;timeserver&#x60; is an NTP peer. Note: If the &#x60;timeserver&#x60; value ends with the &#x60;pool.ntp.org&#x60; suffix, this field will be forced to use &#x60;pool&#x60;.&lt;br&gt; | [optional] [default to 'server']
**prefer** | **bool** | Enable NTP favoring the use of this server more than all others.&lt;br&gt; | [optional] 
**noselect** | **bool** | Prevent NTP from using this timeserver, but continue collecting stats.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;type&#x60; must not be equal to &#x60;&#39;pool&#39;&#x60;&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.post_services_ntp_time_server_endpoint_request import PostServicesNTPTimeServerEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostServicesNTPTimeServerEndpointRequest from a JSON string
post_services_ntp_time_server_endpoint_request_instance = PostServicesNTPTimeServerEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PostServicesNTPTimeServerEndpointRequest.to_json())

# convert the object into a dict
post_services_ntp_time_server_endpoint_request_dict = post_services_ntp_time_server_endpoint_request_instance.to_dict()
# create an instance of PostServicesNTPTimeServerEndpointRequest from a dict
post_services_ntp_time_server_endpoint_request_from_dict = PostServicesNTPTimeServerEndpointRequest.from_dict(post_services_ntp_time_server_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


