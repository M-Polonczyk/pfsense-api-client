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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class FirewallAlias(BaseModel):
    """
    FirewallAlias
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=31)]] = Field(default=None, description="Sets the name for the alias. This name must be unique from all other aliases.<br>")
    type: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="Sets the type of alias this object will be. This directly impacts what values can be                 specified in the `address` field.<br>")
    descr: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="Sets a description to help specify the purpose or contents of the alias.<br>")
    address: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]], Field(min_length=0, max_length=128)]] = Field(default=None, description="Sets the host, network or port entries for the alias. When `type` is set to `host`, each                 entry must be a valid IP address or FQDN. When `type` is set to `network`, each entry must be a valid                 network CIDR or FQDN. When `type` is set to `port`, each entry must be a valid port or port range. You                 may also specify an existing alias's `name` as an entry to created nested aliases.<br>")
    detail: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]], Field(min_length=0, max_length=128)]] = Field(default=None, description="Sets descriptions for each alias `address`. Values must match the order of the `address`                  value it relates to. For example, the first value specified here is the description for the first                 value specified in the `address` field. This value cannot contain <br>")
    __properties: ClassVar[List[str]] = ["name", "type", "descr", "address", "detail"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['host', 'network', 'port']):
            raise ValueError("must be one of enum values ('host', 'network', 'port')")
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
        """Create an instance of FirewallAlias from a JSON string"""
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
        """Create an instance of FirewallAlias from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "descr": obj.get("descr"),
            "address": obj.get("address"),
            "detail": obj.get("detail")
        })
        return _obj


