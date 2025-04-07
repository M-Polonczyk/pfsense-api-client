# SSH


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable the SSH server on this system.&lt;br&gt; | [optional] 
**port** | **str** | The TCP port the SSH server will listen on. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '22']
**sshdkeyonly** | **str** | The SSH authentication mode to use. Use &#x60;enabled&#x60; to require public key authentication, use both to require both a public key AND a password, or use &#x60;null&#x60; to allow a password OR a public key.&lt;br&gt; | [optional] 
**sshdagentforwarding** | **bool** | Enable support for ssh-agent forwarding.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.ssh import SSH

# TODO update the JSON string below
json = "{}"
# create an instance of SSH from a JSON string
ssh_instance = SSH.from_json(json)
# print the JSON string representation of the object
print(SSH.to_json())

# convert the object into a dict
ssh_dict = ssh_instance.to_dict()
# create an instance of SSH from a dict
ssh_from_dict = SSH.from_dict(ssh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


