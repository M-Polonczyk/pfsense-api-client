# IPsecPhase1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ikeid** | **int** | The unique IKE ID for this phase 1 entry. This value is dynamically set and cannot be set or changed by users.&lt;br&gt; | [optional] [readonly] [default to 1]
**descr** | **str** | A description for this IPsec phase 1 entry.&lt;br&gt; | [optional] 
**disabled** | **bool** | Disables this IPsec phase 1 entry.&lt;br&gt; | [optional] 
**iketype** | **str** | The IKE protocol version this phase 1 entry will use.&lt;br&gt; | [optional] 
**mode** | **str** | The IKEv1 negotiation mode this phase 1 entry will use.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;iketype&#x60; must be one of [ ikev1, auto ]&lt;br&gt; | [optional] 
**protocol** | **str** | The IP version this phase 1 entry will use.&lt;br&gt; | [optional] 
**interface** | **str** | The interface for the local endpoint of this phase 1 entry. This should be an interface that is reachable by the remote peer.&lt;br&gt; | [optional] 
**remote_gateway** | **str** | The IP address or hostname of the remote gateway.&lt;br&gt; | [optional] 
**authentication_method** | **str** | The IPsec authentication method this tunnel will use.&lt;br&gt; | [optional] 
**myid_type** | **str** | The identifier type used by the local end of the tunnel.&lt;br&gt; | [optional] 
**myid_data** | **str** | The identifier value used by the local end of the tunnel. This must be a value that corresponds with the current &#x60;myid_type&#x60; value.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;myid_type&#x60; must not be equal to &#x60;&#39;myaddress&#39;&#x60;&lt;br&gt; | [optional] 
**peerid_type** | **str** | The identifier type used by the remote end of the tunnel.&lt;br&gt; | [optional] 
**peerid_data** | **str** | The identifier value used by the remote end of the tunnel. This must be a value that corresponds with the current &#x60;peerid_type&#x60; value.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;peerid_type&#x60; must not be one of [ any, peeraddress ]&lt;br&gt; | [optional] 
**pre_shared_key** | **str** | The Pre-Shared Key (PSK) value. This key must match on both peers and should be long and random to protect the tunnel and its contents. A weak Pre-Shared Key can lead to a tunnel compromise.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;authentication_method&#x60; must be equal to &#x60;&#39;pre_shared_key&#39;&#x60;&lt;br&gt; | [optional] 
**certref** | **str** | The certificate which identifies this system. The certificate must have at least one non-wildcard SAN.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;authentication_method&#x60; must be equal to &#x60;&#39;cert&#39;&#x60;&lt;br&gt; | [optional] 
**caref** | **str** | The certificate authority to use when validating the peer certificate.&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;authentication_method&#x60; must be equal to &#x60;&#39;cert&#39;&#x60;&lt;br&gt; | [optional] 
**rekey_time** | **int** | The amount of time (in seconds) before an child SA establishes new keys.&lt;br&gt; | [optional] [default to 25920]
**reauth_time** | **int** | The amount of time (in seconds) before an child SA is torn down and recreated from scratch, including authentication.&lt;br&gt; | [optional] 
**rand_time** | **int** | A random value up to this amount will be subtracted from the &#x60;rekey_time&#x60; to avoid simultaneous renegotiation.&lt;br&gt; | [optional] [default to 2880]
**lifetime** | **int** | The hard child SA lifetime (in seconds) after which the child SA will be expired.&lt;br&gt; | [optional] [default to 28800]
**startaction** | **str** | The option used to force specific initiation/responder behavior for child SA (P2) entries.&lt;br&gt; | [optional] 
**closeaction** | **str** | The option used to control the behavior when the remote peer unexpectedly closes a child SA (P2)&lt;br&gt; | [optional] 
**nat_traversal** | **str** | The option used to enable the use of NAT-T (i.e. the encapsulation of ESP in UDP packets) if needed, which can help with clients that are behind restrictive firewalls.&lt;br&gt; | [optional] [default to 'on']
**gw_duplicates** | **bool** | Enables or disables the allowance of multiple phase 1 configurations with the same remote gateway endpoint.&lt;br&gt; | [optional] 
**mobike** | **bool** | Enables or disables the use of MOBIKE for this tunnel.&lt;br&gt; | [optional] 
**splitconn** | **bool** | Enables or disables the use split connection entries with multiple phase 2 configurations. Required for remote endpoints that support only a single traffic selector per child SA.&lt;br&gt; | [optional] 
**prfselect_enable** | **bool** | Enables or disables manual Pseudo-Random Function (PRF) selection.&lt;br&gt; | [optional] 
**ikeport** | **str** | The UDP port for IKE on the remote gateway. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '500']
**nattport** | **str** | The UDP port for NAT-T on the remote gateway. Valid options are: a TCP/UDP port number&lt;br&gt; | [optional] [default to '4500']
**dpd_delay** | **int** | The delay (in seconds) between sending peer acknowledgement messages.&lt;br&gt; | [optional] [default to 10]
**dpd_maxfail** | **int** | The number of consecutive failures allowed before disconnecting.&lt;br&gt; | [optional] [default to 5]
**encryption** | [**List[IPsecPhase1EncryptionInner]**](IPsecPhase1EncryptionInner.md) | The encryption algorithms supported by this P1 encryption.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.i_psec_phase1 import IPsecPhase1

# TODO update the JSON string below
json = "{}"
# create an instance of IPsecPhase1 from a JSON string
i_psec_phase1_instance = IPsecPhase1.from_json(json)
# print the JSON string representation of the object
print(IPsecPhase1.to_json())

# convert the object into a dict
i_psec_phase1_dict = i_psec_phase1_instance.to_dict()
# create an instance of IPsecPhase1 from a dict
i_psec_phase1_from_dict = IPsecPhase1.from_dict(i_psec_phase1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


