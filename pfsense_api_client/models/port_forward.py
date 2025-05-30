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

class PortForward(BaseModel):
    """
    PortForward
    """ # noqa: E501
    interface: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The interface this port forward rule applies to.<br>")
    ipprotocol: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='inet', description="The IP protocol this port forward rule should match.<br>")
    protocol: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The IP/transport protocol this port forward rule should match.<br>")
    source: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The source address this port forward rule applies to. Valid value options are: an existing interface, an IP address, a subnet CIDR, an existing alias, `any`, `(self)`, `l2tp`, `pppoe`. The context of this address can be inverted by prefixing the value with `!`. For interface values, the `:ip`  modifier can be appended to the value to use the interface's IP address instead of its entire subnet.<br>")
    source_port: Optional[StrictStr] = Field(default=None, description="The source port this port forward rule applies to. Set to `null` to allow any source port. Valid options are: a TCP/UDP port number, a TCP/UDP port range separated by `:`, an existing port type firewall alias<br><br>This field is only available when the following conditions are met:<br>- `protocol` must be one of [ tcp, udp, tcp/udp ]<br>")
    destination: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The destination address this rule applies to. Valid value options are: an existing interface, an IP address, a subnet CIDR, an existing alias, `any`, `(self)`, `l2tp`, `pppoe`. The context of this address can be inverted by prefixing the value with `!`. For interface values, the `:ip`  modifier can be appended to the value to use the interface's IP address instead of its entire subnet.<br>")
    destination_port: Optional[StrictStr] = Field(default=None, description="The destination port this port forward rule applies to. Set to `null` to allow any destination port. Valid options are: a TCP/UDP port number, a TCP/UDP port range separated by `:`, an existing port type firewall alias<br><br>This field is only available when the following conditions are met:<br>- `protocol` must be one of [ tcp, udp, tcp/udp ]<br>")
    target: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The IP address or alias of the internal host to forward matching traffic to.<br>")
    local_port: Optional[StrictStr] = Field(default=None, description="The port on the internal host to forward matching traffic to. In most cases, this must match the `destination_port` value. In the event that the `desintation_port` is a range, this value should be the first value in that range. Valid options are: a TCP/UDP port number, an existing port type firewall alias<br><br>This field is only available when the following conditions are met:<br>- `protocol` must be one of [ tcp, udp, tcp/udp ]<br>")
    disabled: Optional[StrictBool] = Field(default=None, description="Disables this port forward rule.<br>")
    nordr: Optional[StrictBool] = Field(default=None, description="Disables redirection for traffic matching this rule.<br>")
    nosync: Optional[StrictBool] = Field(default=None, description="Prevents this port forward rule from being synced to non-primary CARP members.<br>")
    descr: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="A description for this port forward rule.<br>")
    natreflection: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The NAT reflection mode to use for traffic matching this port forward rule. Set to `null` to use the system default.<br>")
    associated_rule_id: Optional[StrictStr] = Field(default=None, description="The associated firewall rule mode. Use an empty string to require a separate firewall rule to be created to pass traffic matching this port forward rule. Use `new` to create a new associated firewall rule to pass traffic matching this port forward rule. Use `pass` to automatically pass traffic matching this port forward rule without the need for a firewall rule.   Otherwise, you can specify the `associated_rule_id` of an existing firewall rule to associate with this port forward rule.<br>")
    created_time: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=None, description="The unix timestamp of when this port forward rule was original created.<br>")
    created_by: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='@unknown IP (API)', description="The username and IP of the user who originally created this port forward rule.<br>")
    updated_time: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=None, description="The unix timestamp of when this port forward rule was original created.<br>")
    updated_by: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='@unknown IP (API)', description="The username and IP of the user who last updated this port forward rule.<br>")
    __properties: ClassVar[List[str]] = ["interface", "ipprotocol", "protocol", "source", "source_port", "destination", "destination_port", "target", "local_port", "disabled", "nordr", "nosync", "descr", "natreflection", "associated_rule_id", "created_time", "created_by", "updated_time", "updated_by"]

    @field_validator('ipprotocol')
    def ipprotocol_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['inet', 'inet6', 'inet46']):
            raise ValueError("must be one of enum values ('inet', 'inet6', 'inet46')")
        return value

    @field_validator('protocol')
    def protocol_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['tcp', 'udp', 'tcp/udp', 'icmp', 'esp', 'ah', 'gre', 'ipv6', 'igmp', 'pim', 'ospf']):
            raise ValueError("must be one of enum values ('tcp', 'udp', 'tcp/udp', 'icmp', 'esp', 'ah', 'gre', 'ipv6', 'igmp', 'pim', 'ospf')")
        return value

    @field_validator('natreflection')
    def natreflection_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['enable', 'disable', 'purenat']):
            raise ValueError("must be one of enum values ('enable', 'disable', 'purenat')")
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
        """Create an instance of PortForward from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "created_by",
            "updated_time",
            "updated_by",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if source_port (nullable) is None
        # and model_fields_set contains the field
        if self.source_port is None and "source_port" in self.model_fields_set:
            _dict['source_port'] = None

        # set to None if destination_port (nullable) is None
        # and model_fields_set contains the field
        if self.destination_port is None and "destination_port" in self.model_fields_set:
            _dict['destination_port'] = None

        # set to None if natreflection (nullable) is None
        # and model_fields_set contains the field
        if self.natreflection is None and "natreflection" in self.model_fields_set:
            _dict['natreflection'] = None

        # set to None if created_time (nullable) is None
        # and model_fields_set contains the field
        if self.created_time is None and "created_time" in self.model_fields_set:
            _dict['created_time'] = None

        # set to None if created_by (nullable) is None
        # and model_fields_set contains the field
        if self.created_by is None and "created_by" in self.model_fields_set:
            _dict['created_by'] = None

        # set to None if updated_time (nullable) is None
        # and model_fields_set contains the field
        if self.updated_time is None and "updated_time" in self.model_fields_set:
            _dict['updated_time'] = None

        # set to None if updated_by (nullable) is None
        # and model_fields_set contains the field
        if self.updated_by is None and "updated_by" in self.model_fields_set:
            _dict['updated_by'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PortForward from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "interface": obj.get("interface"),
            "ipprotocol": obj.get("ipprotocol") if obj.get("ipprotocol") is not None else 'inet',
            "protocol": obj.get("protocol"),
            "source": obj.get("source"),
            "source_port": obj.get("source_port"),
            "destination": obj.get("destination"),
            "destination_port": obj.get("destination_port"),
            "target": obj.get("target"),
            "local_port": obj.get("local_port"),
            "disabled": obj.get("disabled"),
            "nordr": obj.get("nordr"),
            "nosync": obj.get("nosync"),
            "descr": obj.get("descr"),
            "natreflection": obj.get("natreflection"),
            "associated_rule_id": obj.get("associated_rule_id"),
            "created_time": obj.get("created_time"),
            "created_by": obj.get("created_by") if obj.get("created_by") is not None else '@unknown IP (API)',
            "updated_time": obj.get("updated_time"),
            "updated_by": obj.get("updated_by") if obj.get("updated_by") is not None else '@unknown IP (API)'
        })
        return _obj


