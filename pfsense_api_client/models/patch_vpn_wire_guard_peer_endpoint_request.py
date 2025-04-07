# coding: utf-8

"""
    pfSense REST API Documentation

    ### Getting Started<br>- [Authentication and Authorization](https://pfrest.org/AUTHENTICATION_AND_AUTHORIZATION/)<br>- [Working with Object IDs](https://pfrest.org/WORKING_WITH_OBJECT_IDS/)<br>- [Queries, Filters, and Sorting](https://pfrest.org/QUERIES_FILTERS_AND_SORTING/)<br>- [Common Control Parameters](https://pfrest.org/COMMON_CONTROL_PARAMETERS/)<br>- [Working with HATEOAS](https://pfrest.org/WORKING_WITH_HATEOAS/)<br>

    The version of the OpenAPI document: v2.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pfsense_api_client.models.wire_guard_peer_allowedips_inner import WireGuardPeerAllowedipsInner
from typing import Optional, Set
from typing_extensions import Self

class PatchVPNWireGuardPeerEndpointRequest(BaseModel):
    """
    PatchVPNWireGuardPeerEndpointRequest
    """ # noqa: E501
    enabled: Optional[StrictBool] = Field(default=None, description="Enables or disables this WireGuard peer.<br>")
    tun: Optional[StrictStr] = Field(default='unassigned', description="The WireGuard tunnel for this peer.<br>")
    endpoint: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The IP address or hostname of the remote peer. Set to `null` to make this a dynamic endpoint.<br>")
    port: Optional[StrictStr] = Field(default='51820', description="The port used by the remote peer. Valid options are: a TCP/UDP port number<br><br>This field is only available when the following conditions are met:<br>- `endpoint` must not be equal to `NULL`<br>")
    descr: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The description for this peer.<br>")
    persistentkeepalive: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=None, description="The interval (in seconds) for Keep Alive packets sent to this peer. Set to `null` to disable.<br>")
    publickey: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The public key for this peer.<br>")
    presharedkey: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The pre-shared key for this tunnel.<br>")
    allowedips: Optional[Annotated[List[WireGuardPeerAllowedipsInner], Field(min_length=0, max_length=65535)]] = Field(default=None, description="The allowed IP/subnets for this WireGuard peer.<br>")
    id: StrictInt = Field(description="The ID of the object or resource to interact with.")
    __properties: ClassVar[List[str]] = ["enabled", "tun", "endpoint", "port", "descr", "persistentkeepalive", "publickey", "presharedkey", "allowedips", "id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PatchVPNWireGuardPeerEndpointRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in allowedips (list)
        _items = []
        if self.allowedips:
            for _item_allowedips in self.allowedips:
                if _item_allowedips:
                    _items.append(_item_allowedips.to_dict())
            _dict['allowedips'] = _items
        # set to None if endpoint (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint is None and "endpoint" in self.model_fields_set:
            _dict['endpoint'] = None

        # set to None if persistentkeepalive (nullable) is None
        # and model_fields_set contains the field
        if self.persistentkeepalive is None and "persistentkeepalive" in self.model_fields_set:
            _dict['persistentkeepalive'] = None

        # set to None if presharedkey (nullable) is None
        # and model_fields_set contains the field
        if self.presharedkey is None and "presharedkey" in self.model_fields_set:
            _dict['presharedkey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchVPNWireGuardPeerEndpointRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enabled": obj.get("enabled"),
            "tun": obj.get("tun") if obj.get("tun") is not None else 'unassigned',
            "endpoint": obj.get("endpoint"),
            "port": obj.get("port") if obj.get("port") is not None else '51820',
            "descr": obj.get("descr"),
            "persistentkeepalive": obj.get("persistentkeepalive"),
            "publickey": obj.get("publickey"),
            "presharedkey": obj.get("presharedkey"),
            "allowedips": [WireGuardPeerAllowedipsInner.from_dict(_item) for _item in obj["allowedips"]] if obj.get("allowedips") is not None else None,
            "id": obj.get("id")
        })
        return _obj


