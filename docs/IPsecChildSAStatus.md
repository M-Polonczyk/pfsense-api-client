# IPsecChildSAStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the connection ID for the child SA.&lt;br&gt; | [optional] [readonly] 
**uniqueid** | **int** | The unique ID of the child SA.&lt;br&gt; | [optional] [readonly] 
**reqid** | **int** | The request ID of the child SA.&lt;br&gt; | [optional] [readonly] 
**state** | **str** | The current state of the child SA.&lt;br&gt; | [optional] [readonly] 
**mode** | **str** | The mode of the child SA.&lt;br&gt; | [optional] [readonly] 
**protocol** | **str** | The protocol of the child SA.&lt;br&gt; | [optional] [readonly] 
**encap** | **bool** | Whether encapsulation is used for the child SA.&lt;br&gt; | [optional] [readonly] 
**spi_in** | **str** | The incoming SPI of the child SA.&lt;br&gt; | [optional] [readonly] 
**spi_out** | **str** | The outgoing SPI of the child SA.&lt;br&gt; | [optional] [readonly] 
**encr_alg** | **str** | The encryption algorithm used by the child SA.&lt;br&gt; | [optional] [readonly] 
**encr_keysize** | **int** | The encryption key size used by the child SA.&lt;br&gt; | [optional] [readonly] 
**integ_alg** | **str** | The integrity algorithm used by the child SA.&lt;br&gt; | [optional] [readonly] 
**dh_group** | **str** | The Diffie-Hellman group used by the child SA.&lt;br&gt; | [optional] [readonly] 
**bytes_in** | **int** | The number of bytes received by the child SA.&lt;br&gt; | [optional] [readonly] 
**bytes_out** | **int** | The number of bytes sent by the child SA.&lt;br&gt; | [optional] [readonly] 
**packets_in** | **int** | The number of packets received by the child SA.&lt;br&gt; | [optional] [readonly] 
**packets_out** | **int** | The number of packets sent by the child SA.&lt;br&gt; | [optional] [readonly] 
**use_in** | **int** | The number of times the child SA has been used to receive data.&lt;br&gt; | [optional] [readonly] 
**use_out** | **int** | The number of times the child SA has been used to send data.&lt;br&gt; | [optional] [readonly] 
**rekey_time** | **int** | The time at which the child SA will be rekeyed.&lt;br&gt; | [optional] [readonly] 
**life_time** | **int** | The time at which the child SA will expire.&lt;br&gt; | [optional] [readonly] 
**install_time** | **int** | The time at which the child SA was installed.&lt;br&gt; | [optional] [readonly] 
**local_ts** | **List[str]** | The local traffic selector of the child SA.&lt;br&gt; | [optional] [readonly] 
**remote_ts** | **List[str]** | The remote traffic selector of the child SA.&lt;br&gt; | [optional] [readonly] 

## Example

```python
from pfsense_api_client.models.i_psec_child_sa_status import IPsecChildSAStatus

# TODO update the JSON string below
json = "{}"
# create an instance of IPsecChildSAStatus from a JSON string
i_psec_child_sa_status_instance = IPsecChildSAStatus.from_json(json)
# print the JSON string representation of the object
print(IPsecChildSAStatus.to_json())

# convert the object into a dict
i_psec_child_sa_status_dict = i_psec_child_sa_status_instance.to_dict()
# create an instance of IPsecChildSAStatus from a dict
i_psec_child_sa_status_from_dict = IPsecChildSAStatus.from_dict(i_psec_child_sa_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


