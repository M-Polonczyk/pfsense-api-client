# IPsecPhase2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uniqid** | **str** | A unique ID used to identify this IPsec phase2 entry internally. This value is automatically set by the system and cannot be changed.&lt;br&gt; | [optional] [readonly] [default to '67ed081abfaf0']
**reqid** | **int** | A unique ID used to identify this IPsec phase2 entry internally. This value is automatically set by the system and cannot be changed.&lt;br&gt; | [optional] [readonly] [default to 1]
**ikeid** | **int** | The &#x60;ikeid&#x60; of the parent IPsec phase 1 entry this IPsec phase 2 entry belongs to.&lt;br&gt; | [optional] 
**descr** | **str** | A description for this IPsec phase 2 entry.&lt;br&gt; | [optional] 
**disabled** | **bool** | Disables this IPsec phase 2 entry.&lt;br&gt; | [optional] 
**mode** | **str** | The IPsec phase 2 mode this entry will use.&lt;br&gt; | [optional] 
**localid_type** | **str** | The local ID type to use for this phase 2 entry. Valid value options are: an existing interface, &#x60;address&#x60;, &#x60;network&#x60;. For interface values, the &#x60;:ip&#x60;  modifier can be appended to the value to use the interface&#39;s IP address instead of its entire subnet.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must not be equal to &#x60;&#39;transport&#39;&#x60;&lt;br&gt; | [optional] 
**localid_address** | **str** | The local network IP component of this IPsec security association.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;localid_type&#x60; must be one of [ address, network ]&lt;br&gt; | [optional] 
**localid_netbits** | **int** | The subnet bits of the &#x60;localid_address&#x60; network.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;localid_type&#x60; must be equal to &#x60;&#39;network&#39;&#x60;&lt;br&gt; | [optional] 
**natlocalid_type** | **str** | The NAT/BINAT translation type for this IPsec phase 2 entry. Leave as &#x60;null&#x60; if NAT/BINAT is not needed. Valid value options are: an existing interface, &#x60;address&#x60;, &#x60;network&#x60;. For interface values, the &#x60;:ip&#x60;  modifier can be appended to the value to use the interface&#39;s IP address instead of its entire subnet.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must not be one of [ transport, vti ]&lt;br&gt; | [optional] 
**natlocalid_address** | **str** | The NAT/BINAT local network IP component of this IPsec security association.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;natlocalid_type&#x60; must be one of [ address, network ]&lt;br&gt; | [optional] 
**natlocalid_netbits** | **int** | The subnet bits of the &#x60;natlocalid_address&#x60; network.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;natlocalid_type&#x60; must be equal to &#x60;&#39;network&#39;&#x60;&lt;br&gt; | [optional] 
**remoteid_type** | **str** | The remote ID type to use for this phase 2 entry. Valid value options are: &#x60;address&#x60;, &#x60;network&#x60;. For interface values, the &#x60;:ip&#x60;  modifier can be appended to the value to use the interface&#39;s IP address instead of its entire subnet.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;mode&#x60; must not be equal to &#x60;&#39;transport&#39;&#x60;&lt;br&gt; | [optional] 
**remoteid_address** | **str** | The remote network IP component of this IPsec security association.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;remoteid_type&#x60; must be one of [ address, network ]&lt;br&gt; | [optional] 
**remoteid_netbits** | **int** | The subnet bits of the &#x60;remoteid_address&#x60; network.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;remoteid_type&#x60; must be equal to &#x60;&#39;network&#39;&#x60;&lt;br&gt; | [optional] 
**protocol** | **str** | the IPsec phase 2 proposal protocol for this entry. Encapsulating Security Payload (&#x60;esp&#x60;) performs encryption and authentication, Authentication Header (&#x60;ah&#x60;) is authentication only.&lt;br&gt; | [optional] [default to 'esp']
**encryption_algorithm_option** | [**List[IPsecPhase2EncryptionAlgorithmOptionInner]**](IPsecPhase2EncryptionAlgorithmOptionInner.md) | The encryption algorithms to be used by this phase 2 entry.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;protocol&#x60; must be equal to &#x60;&#39;esp&#39;&#x60;&lt;br&gt; | [optional] 
**hash_algorithm_option** | **List[str]** | The hashing algorithms used by this IPsec phase 2 entry. Note: Hash is ignored with GCM algorithms. SHA1 provides weak security and should be avoided.&lt;br&gt; | [optional] 
**pfsgroup** | **int** | The PFS key group this IPsec phase 2 entry should use. Note: Groups 1, 2, 5, 22, 23, and 24 provide weak security and should be avoided.&lt;br&gt; | [optional] [default to 14]
**rekey_time** | **int** | The amount of time (in seconds) before an IKE SA establishes new keys.&lt;br&gt; | [optional] [default to 3240]
**rand_time** | **int** | A random value up to this amount will be subtracted from the &#x60;rekey_time&#x60; and &#x60;reauth_time&#x60; to avoid simultaneous renegotiation.&lt;br&gt; | [optional] [default to 360]
**lifetime** | **int** | The hard IKE SA lifetime (in seconds) after which the IKE SA will be expired.&lt;br&gt; | [optional] [default to 3600]
**pinghost** | **str** | The IP address to send an ICMP echo request to inside the tunnel. Can trigger initiation of a tunnel mode P2, but does not trigger initiation of a VTI mode P2.&lt;br&gt; | [optional] 
**keepalive** | **bool** | Enables or disables checking this P2 and initiating if disconnected; does not send traffic inside the tunnel. This check ignores the P1 option &#39;Child SA Start Action&#39; and works for both VTI and tunnel mode P2s. For IKEv2 without split connections, this only needs to be enabled on one P2.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.i_psec_phase2 import IPsecPhase2

# TODO update the JSON string below
json = "{}"
# create an instance of IPsecPhase2 from a JSON string
i_psec_phase2_instance = IPsecPhase2.from_json(json)
# print the JSON string representation of the object
print(IPsecPhase2.to_json())

# convert the object into a dict
i_psec_phase2_dict = i_psec_phase2_instance.to_dict()
# create an instance of IPsecPhase2 from a dict
i_psec_phase2_from_dict = IPsecPhase2.from_dict(i_psec_phase2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


