# IPsecSAStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**con_id** | **str** | The connection ID of the tunnel.&lt;br&gt; | [optional] [readonly] 
**uniqueid** | **int** | The unique ID of the tunnel.&lt;br&gt; | [optional] [readonly] 
**version** | **int** | The IKE version used by the tunnel.&lt;br&gt; | [optional] [readonly] 
**state** | **str** | The current state of the tunnel.&lt;br&gt; | [optional] [readonly] 
**local_host** | **str** | The local host for the tunnel.&lt;br&gt; | [optional] [readonly] 
**local_port** | **str** | The local port for the tunnel. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [readonly] 
**local_id** | **str** | The local ID for the tunnel.&lt;br&gt; | [optional] [readonly] 
**remote_host** | **str** | The remote host for the tunnel.&lt;br&gt; | [optional] [readonly] 
**remote_port** | **str** | The remote port for the tunnel. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [readonly] 
**remote_id** | **str** | The remote ID for the tunnel.&lt;br&gt; | [optional] [readonly] 
**initiator_spi** | **str** | The initiator SPI for the tunnel.&lt;br&gt; | [optional] [readonly] 
**responder_spi** | **str** | The responder SPI for the tunnel.&lt;br&gt; | [optional] [readonly] 
**nat_remote** | **bool** | Whether the remote host is behind NAT.&lt;br&gt; | [optional] [readonly] 
**nat_any** | **bool** | Whether the remote host is behind any NAT.&lt;br&gt; | [optional] [readonly] 
**encr_alg** | **str** | The encryption algorithm used by the tunnel.&lt;br&gt; | [optional] [readonly] 
**encr_keysize** | **int** | The encryption key size used by the tunnel.&lt;br&gt; | [optional] [readonly] 
**integ_alg** | **str** | The integrity algorithm used by the tunnel.&lt;br&gt; | [optional] [readonly] 
**prf_alg** | **str** | The pseudo-random function algorithm used by the tunnel.&lt;br&gt; | [optional] [readonly] 
**dh_group** | **str** | The Diffie-Hellman group used by the tunnel.&lt;br&gt; | [optional] [readonly] 
**established** | **int** | The amount of time the tunnel has been established.&lt;br&gt; | [optional] [readonly] 
**rekey_time** | **int** | The amount of time until the tunnel rekeys.&lt;br&gt; | [optional] [readonly] 
**child_sas** | [**List[IPsecSAStatusChildSasInner]**](IPsecSAStatusChildSasInner.md) | The child SAs of the tunnel.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.i_psec_sa_status import IPsecSAStatus

# TODO update the JSON string below
json = "{}"
# create an instance of IPsecSAStatus from a JSON string
i_psec_sa_status_instance = IPsecSAStatus.from_json(json)
# print the JSON string representation of the object
print(IPsecSAStatus.to_json())

# convert the object into a dict
i_psec_sa_status_dict = i_psec_sa_status_instance.to_dict()
# create an instance of IPsecSAStatus from a dict
i_psec_sa_status_from_dict = IPsecSAStatus.from_dict(i_psec_sa_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


