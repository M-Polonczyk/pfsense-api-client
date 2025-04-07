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

class PatchServicesBINDSettingsEndpointRequest(BaseModel):
    """
    PatchServicesBINDSettingsEndpointRequest
    """ # noqa: E501
    enable_bind: Optional[StrictBool] = Field(default=None, description="Enables the BIND service.<br>")
    bind_ip_version: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The IP version to use for the BIND service. Leave empty to use both IPv4 and IPv6.<br>")
    listenon: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]], Field(min_length=0, max_length=128)]] = Field(default=None, description="The interfaces to listen on for DNS requests.<br>")
    bind_notify: Optional[StrictBool] = Field(default=None, description="Notify slave server after any update on master.<br>")
    bind_hide_version: Optional[StrictBool] = Field(default=None, description="Hide the BIND version in responses.<br>")
    bind_ram_limit: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='256M', description="The maximum amount of RAM to use for the BIND service.<br>")
    bind_logging: Optional[StrictBool] = Field(default=None, description="Enable logging for the BIND service.<br>")
    log_severity: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='critical', description="The minimum severity of events to log.<br>")
    log_options: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]], Field(min_length=0, max_length=128)]] = Field(default=None, description="The categories to log.<br>")
    rate_enabled: Optional[StrictBool] = Field(default=None, description="Enable rate limiting for the BIND service.<br>")
    rate_limit: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=15, description="The maximum number of queries per second to allow.<br><br>This field is only available when the following conditions are met:<br>- `rate_enabled` must be equal to `true`<br>")
    log_only: Optional[StrictBool] = Field(default=None, description="When rate limiting, only log that the query limit has been exceeded. If disabled, the query will be dropped instead.<br>")
    bind_forwarder: Optional[StrictBool] = Field(default=None, description="Enable forwarding queries to other DNS servers listed below rather than this server performing its own recursion.<br>")
    bind_forwarder_ips: Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]], Field(min_length=0, max_length=128)] = Field(description="The IP addresses of the DNS servers to forward queries to.<br><br>This field is only available when the following conditions are met:<br>- `bind_forwarder` must be equal to `true`<br>")
    bind_dnssec_validation: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='auto', description="Enable DNSSEC validation when BIND is acting as a recursive resolver.<br>")
    listenport: Optional[StrictStr] = Field(default='53', description="The TCP and UDP port to listen on for DNS requests. Valid options are: a TCP/UDP port number<br>")
    controlport: Optional[StrictStr] = Field(default='953', description="The TCP port to listen on for control requests (localhost only). Valid options are: a TCP/UDP port number<br>")
    bind_custom_options: Optional[StrictStr] = Field(default=None, description="Custom BIND options to include in the configuration file.<br>")
    bind_global_settings: Optional[StrictStr] = Field(default=None, description="Global BIND settings to include in the configuration file.<br>")
    __properties: ClassVar[List[str]] = ["enable_bind", "bind_ip_version", "listenon", "bind_notify", "bind_hide_version", "bind_ram_limit", "bind_logging", "log_severity", "log_options", "rate_enabled", "rate_limit", "log_only", "bind_forwarder", "bind_forwarder_ips", "bind_dnssec_validation", "listenport", "controlport", "bind_custom_options", "bind_global_settings"]

    @field_validator('bind_ip_version')
    def bind_ip_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['', '-4', '-6']):
            raise ValueError("must be one of enum values ('', '-4', '-6')")
        return value

    @field_validator('log_severity')
    def log_severity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['critical', 'error', 'warning', 'notice', 'info', 'debug 1', 'debug 3', 'debug 5', 'dynamic']):
            raise ValueError("must be one of enum values ('critical', 'error', 'warning', 'notice', 'info', 'debug 1', 'debug 3', 'debug 5', 'dynamic')")
        return value

    @field_validator('log_options')
    def log_options_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['default', 'general', 'database', 'security', 'config', 'resolver', 'xfer-in', 'xfer-out', 'notify', 'client', 'unmatched', 'queries', 'network', 'update', 'dispatch', 'dnssec', 'lame-servers']):
                raise ValueError("each list item must be one of ('default', 'general', 'database', 'security', 'config', 'resolver', 'xfer-in', 'xfer-out', 'notify', 'client', 'unmatched', 'queries', 'network', 'update', 'dispatch', 'dnssec', 'lame-servers')")
        return value

    @field_validator('bind_dnssec_validation')
    def bind_dnssec_validation_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['auto', 'on', 'off']):
            raise ValueError("must be one of enum values ('auto', 'on', 'off')")
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
        """Create an instance of PatchServicesBINDSettingsEndpointRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchServicesBINDSettingsEndpointRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enable_bind": obj.get("enable_bind"),
            "bind_ip_version": obj.get("bind_ip_version"),
            "listenon": obj.get("listenon"),
            "bind_notify": obj.get("bind_notify"),
            "bind_hide_version": obj.get("bind_hide_version"),
            "bind_ram_limit": obj.get("bind_ram_limit") if obj.get("bind_ram_limit") is not None else '256M',
            "bind_logging": obj.get("bind_logging"),
            "log_severity": obj.get("log_severity") if obj.get("log_severity") is not None else 'critical',
            "log_options": obj.get("log_options"),
            "rate_enabled": obj.get("rate_enabled"),
            "rate_limit": obj.get("rate_limit") if obj.get("rate_limit") is not None else 15,
            "log_only": obj.get("log_only"),
            "bind_forwarder": obj.get("bind_forwarder"),
            "bind_forwarder_ips": obj.get("bind_forwarder_ips"),
            "bind_dnssec_validation": obj.get("bind_dnssec_validation") if obj.get("bind_dnssec_validation") is not None else 'auto',
            "listenport": obj.get("listenport") if obj.get("listenport") is not None else '53',
            "controlport": obj.get("controlport") if obj.get("controlport") is not None else '953',
            "bind_custom_options": obj.get("bind_custom_options"),
            "bind_global_settings": obj.get("bind_global_settings")
        })
        return _obj


