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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PatchServicesDHCPServerAddressPoolEndpointRequest(BaseModel):
    """
    PatchServicesDHCPServerAddressPoolEndpointRequest
    """ # noqa: E501
    range_from: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=15)]] = Field(default=None, description="The starting IP address for this address pool. This address must be less than or equal to the `range_to` field.<br>")
    range_to: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=15)]] = Field(default=None, description="The ending IP address for the this address pool. This address must be greater than or equal to the `range_to` field.<br>")
    domain: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The domain to be assigned via DHCP.<br>")
    mac_allow: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=17)]], Field(min_length=0, max_length=128)]] = Field(default=None, description="MAC addresses this DHCP server is allowed to provide leases for.<br>")
    mac_deny: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=17)]], Field(min_length=0, max_length=128)]] = Field(default=None, description="MAC addresses this DHCP server is not allowed to provide leases for.<br>")
    domainsearchlist: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=255)]], Field(min_length=0, max_length=128)]] = Field(default=None, description="The domain search list to provide via DHCP.<br>")
    defaultleasetime: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=60)]] = Field(default=7200, description="The default DHCP lease validity period (in seconds). This is used for clients that do not ask for a specific expiration time.<br>")
    maxleasetime: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=60)]] = Field(default=86400, description="The maximum DHCP lease validity period (in seconds) a client can request.<br>")
    gateway: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=15)]] = Field(default=None, description="The gateway IPv4 address to provide via DHCP. This is only necessary if you are not using the interface's IP as the gateway. Specify `none` for no gateway assignment.<br>")
    dnsserver: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=15)]], Field(min_length=0, max_length=4)]] = Field(default=None, description="The DNS servers to provide via DHCP. Leave empty to default to system nameservers.<br>")
    winsserver: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=15)]], Field(min_length=0, max_length=2)]] = Field(default=None, description="The WINS servers to provide via DHCP.<br>")
    ntpserver: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=256)]], Field(min_length=0, max_length=4)]] = Field(default=None, description="The NTP servers to provide via DHCP.<br>")
    ignorebootp: Optional[StrictBool] = Field(default=None, description="Force this DHCP server to ignore BOOTP queries.<br>")
    ignoreclientuids: Optional[StrictBool] = Field(default=None, description="Prevent recording a unique identifier (UID) in client lease data if present in the client DHCP request. This option may be useful when a client can dual boot using different client identifiers but the same hardware (MAC) address. Note that the resulting server behavior violates the official DHCP specification.<br>")
    denyunknown: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="Define how to handle unknown clients requesting DHCP leases. When set to `null`, any DHCP client will get an IP address within this scope/range on this interface. If set to `enabled`, any DHCP client with a MAC address listed in a static mapping on any scope(s)/interface(s) will get an IP address. If set to `class`, only MAC addresses listed in static mappings on this interface will get an IP address within this scope/range.<br>")
    parent_id: StrictInt = Field(description="The ID of the parent this object is nested under.")
    id: StrictInt = Field(description="The ID of the object or resource to interact with.")
    __properties: ClassVar[List[str]] = ["range_from", "range_to", "domain", "mac_allow", "mac_deny", "domainsearchlist", "defaultleasetime", "maxleasetime", "gateway", "dnsserver", "winsserver", "ntpserver", "ignorebootp", "ignoreclientuids", "denyunknown", "parent_id", "id"]

    @field_validator('denyunknown')
    def denyunknown_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['enabled', 'class']):
            raise ValueError("must be one of enum values ('enabled', 'class')")
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
        """Create an instance of PatchServicesDHCPServerAddressPoolEndpointRequest from a JSON string"""
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
        # set to None if defaultleasetime (nullable) is None
        # and model_fields_set contains the field
        if self.defaultleasetime is None and "defaultleasetime" in self.model_fields_set:
            _dict['defaultleasetime'] = None

        # set to None if maxleasetime (nullable) is None
        # and model_fields_set contains the field
        if self.maxleasetime is None and "maxleasetime" in self.model_fields_set:
            _dict['maxleasetime'] = None

        # set to None if denyunknown (nullable) is None
        # and model_fields_set contains the field
        if self.denyunknown is None and "denyunknown" in self.model_fields_set:
            _dict['denyunknown'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchServicesDHCPServerAddressPoolEndpointRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "range_from": obj.get("range_from"),
            "range_to": obj.get("range_to"),
            "domain": obj.get("domain"),
            "mac_allow": obj.get("mac_allow"),
            "mac_deny": obj.get("mac_deny"),
            "domainsearchlist": obj.get("domainsearchlist"),
            "defaultleasetime": obj.get("defaultleasetime") if obj.get("defaultleasetime") is not None else 7200,
            "maxleasetime": obj.get("maxleasetime") if obj.get("maxleasetime") is not None else 86400,
            "gateway": obj.get("gateway"),
            "dnsserver": obj.get("dnsserver"),
            "winsserver": obj.get("winsserver"),
            "ntpserver": obj.get("ntpserver"),
            "ignorebootp": obj.get("ignorebootp"),
            "ignoreclientuids": obj.get("ignoreclientuids"),
            "denyunknown": obj.get("denyunknown"),
            "parent_id": obj.get("parent_id"),
            "id": obj.get("id")
        })
        return _obj


