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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pfsense_api_client.models.dns_forwarder_host_override_aliases_inner import DNSForwarderHostOverrideAliasesInner
from typing import Optional, Set
from typing_extensions import Self

class PatchServicesDNSForwarderHostOverrideEndpointRequest(BaseModel):
    """
    PatchServicesDNSForwarderHostOverrideEndpointRequest
    """ # noqa: E501
    host: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The hostname of this override.<br>")
    domain: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The domain of this override.<br>")
    ip: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The IP address of this override.<br>")
    descr: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The description for this override.<br>")
    aliases: Optional[Annotated[List[DNSForwarderHostOverrideAliasesInner], Field(min_length=0, max_length=65535)]] = Field(default=None, description="The aliases for this override.<br>")
    id: StrictInt = Field(description="The ID of the object or resource to interact with.")
    __properties: ClassVar[List[str]] = ["host", "domain", "ip", "descr", "aliases", "id"]

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
        """Create an instance of PatchServicesDNSForwarderHostOverrideEndpointRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in aliases (list)
        _items = []
        if self.aliases:
            for _item_aliases in self.aliases:
                if _item_aliases:
                    _items.append(_item_aliases.to_dict())
            _dict['aliases'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchServicesDNSForwarderHostOverrideEndpointRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "host": obj.get("host"),
            "domain": obj.get("domain"),
            "ip": obj.get("ip"),
            "descr": obj.get("descr"),
            "aliases": [DNSForwarderHostOverrideAliasesInner.from_dict(_item) for _item in obj["aliases"]] if obj.get("aliases") is not None else None,
            "id": obj.get("id")
        })
        return _obj


