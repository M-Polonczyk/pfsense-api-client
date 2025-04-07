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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PostFirewallVirtualIPEndpointRequest(BaseModel):
    """
    PostFirewallVirtualIPEndpointRequest
    """ # noqa: E501
    uniqid: Optional[StrictStr] = Field(default='67ed0819dfdaa', description="The unique ID for this virtual IP.<br>")
    mode: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The virtual IP mode to use for this virtual IP.<br>")
    interface: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The interface this virtual IP will apply to.<br>")
    type: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='single', description="The virtual IP scope type. The `network` option is only applicable to the `proxyarp` and `other` virtual IP modes.<br>")
    subnet: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The address for this virtual IP.<br>")
    subnet_bits: Annotated[int, Field(le=128, strict=True, ge=1)] = Field(description="The subnet bits for this virtual IP. For `proxyarp` and `other` virtual IPs, this value specifies a block of many IP address. For all other virtual IP modes, this specifies the subnet mask<br>")
    descr: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="A description for administrative reference<br>")
    noexpand: Optional[StrictBool] = Field(default=None, description="Disable expansion of this entry into IPs on NAT lists (e.g. 192.168.1.0/24 expands to 256 entries.)<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one of [ proxyarp, other ]<br>")
    vhid: Annotated[int, Field(le=255, strict=True, ge=1)] = Field(description="The VHID group that the machines will share.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be equal to `'carp'`<br>")
    advbase: Optional[Annotated[int, Field(le=254, strict=True, ge=1)]] = Field(default=1, description="The base frequency that this machine will advertise.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be equal to `'carp'`<br>")
    advskew: Optional[Annotated[int, Field(le=254, strict=True, ge=0)]] = Field(default=None, description="The frequency skew that this machine will advertise.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be equal to `'carp'`<br>")
    password: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The VHID group password shared by all CARP members.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be equal to `'carp'`<br>")
    carp_status: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The current CARP status of this virtual IP. This will display show whether this CARP node is the primary or backup peer.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be equal to `'carp'`<br>")
    carp_mode: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='mcast', description="The CARP mode to use for this virtual IP. Please note this field is exclusive to pfSense Plus and has no effect on CE.<br><br>This field is only available when the following conditions are met:<br>- `mode` must be equal to `'carp'`<br>")
    carp_peer: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The IP address of the CARP peer. Please note this field is exclusive to pfSense Plus and has no effect on CE.<br><br>This field is only available when the following conditions are met:<br>- `carp_mode` must be equal to `'ucast'`<br>")
    __properties: ClassVar[List[str]] = ["uniqid", "mode", "interface", "type", "subnet", "subnet_bits", "descr", "noexpand", "vhid", "advbase", "advskew", "password", "carp_status", "carp_mode", "carp_peer"]

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ipalias', 'proxyarp', 'carp', 'other']):
            raise ValueError("must be one of enum values ('ipalias', 'proxyarp', 'carp', 'other')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['single', 'network']):
            raise ValueError("must be one of enum values ('single', 'network')")
        return value

    @field_validator('carp_mode')
    def carp_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['mcast', 'ucast']):
            raise ValueError("must be one of enum values ('mcast', 'ucast')")
        return value

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
        """Create an instance of PostFirewallVirtualIPEndpointRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "uniqid",
            "carp_status",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if uniqid (nullable) is None
        # and model_fields_set contains the field
        if self.uniqid is None and "uniqid" in self.model_fields_set:
            _dict['uniqid'] = None

        # set to None if carp_status (nullable) is None
        # and model_fields_set contains the field
        if self.carp_status is None and "carp_status" in self.model_fields_set:
            _dict['carp_status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostFirewallVirtualIPEndpointRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uniqid": obj.get("uniqid") if obj.get("uniqid") is not None else '67ed0819dfdaa',
            "mode": obj.get("mode"),
            "interface": obj.get("interface"),
            "type": obj.get("type") if obj.get("type") is not None else 'single',
            "subnet": obj.get("subnet"),
            "subnet_bits": obj.get("subnet_bits"),
            "descr": obj.get("descr"),
            "noexpand": obj.get("noexpand"),
            "vhid": obj.get("vhid"),
            "advbase": obj.get("advbase") if obj.get("advbase") is not None else 1,
            "advskew": obj.get("advskew"),
            "password": obj.get("password"),
            "carp_status": obj.get("carp_status"),
            "carp_mode": obj.get("carp_mode") if obj.get("carp_mode") is not None else 'mcast',
            "carp_peer": obj.get("carp_peer")
        })
        return _obj


