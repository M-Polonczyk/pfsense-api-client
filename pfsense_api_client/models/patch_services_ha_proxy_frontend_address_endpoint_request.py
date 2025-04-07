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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PatchServicesHAProxyFrontendAddressEndpointRequest(BaseModel):
    """
    PatchServicesHAProxyFrontendAddressEndpointRequest
    """ # noqa: E501
    extaddr: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The external address to use.<br>")
    extaddr_custom: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The custom IPv4 or IPv6 address to use as the external address.<br><br>This field is only available when the following conditions are met:<br>- `extaddr` must be equal to `'custom'`<br>")
    extaddr_port: Optional[StrictStr] = Field(default=None, description="The port to bind to for this address. Valid options are: a TCP/UDP port number<br>")
    extaddr_ssl: Optional[StrictBool] = Field(default=None, description="Enables or disables using SSL/TLS for this address.<br>")
    exaddr_advanced: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The advanced configuration to apply to this address.<br>")
    parent_id: StrictInt = Field(description="The ID of the parent this object is nested under.")
    id: StrictInt = Field(description="The ID of the object or resource to interact with.")
    __properties: ClassVar[List[str]] = ["extaddr", "extaddr_custom", "extaddr_port", "extaddr_ssl", "exaddr_advanced", "parent_id", "id"]

    @field_validator('extaddr')
    def extaddr_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['custom', 'any_ipv4', 'any_ipv6', 'localhost_ipv4', 'localhost_ipv6']):
            raise ValueError("must be one of enum values ('custom', 'any_ipv4', 'any_ipv6', 'localhost_ipv4', 'localhost_ipv6')")
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
        """Create an instance of PatchServicesHAProxyFrontendAddressEndpointRequest from a JSON string"""
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
        # set to None if extaddr_port (nullable) is None
        # and model_fields_set contains the field
        if self.extaddr_port is None and "extaddr_port" in self.model_fields_set:
            _dict['extaddr_port'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchServicesHAProxyFrontendAddressEndpointRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "extaddr": obj.get("extaddr"),
            "extaddr_custom": obj.get("extaddr_custom"),
            "extaddr_port": obj.get("extaddr_port"),
            "extaddr_ssl": obj.get("extaddr_ssl"),
            "exaddr_advanced": obj.get("exaddr_advanced"),
            "parent_id": obj.get("parent_id"),
            "id": obj.get("id")
        })
        return _obj


