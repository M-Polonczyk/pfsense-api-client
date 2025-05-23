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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PostSystemCertificateAuthorityEndpointRequest(BaseModel):
    """
    PostSystemCertificateAuthorityEndpointRequest
    """ # noqa: E501
    descr: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The descriptive name for this certificate authority.<br>")
    refid: Optional[StrictStr] = Field(default='67ed081a7a0e9', description="The unique ID assigned to this certificate authority for internal system use. This value is generated by this system and cannot be changed.<br>")
    trust: Optional[StrictBool] = Field(default=None, description="Adds or removes this certificate authority from the operating system's trust stored.<br>")
    randomserial: Optional[StrictBool] = Field(default=None, description="Enables or disables the randomization of serial numbers for certificates signed by this CA.<br>")
    serial: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=1)]] = Field(default=1, description="The decimal number to be used as a sequential serial number for the next certificate to be signed by this CA. This value is ignored when Randomize Serial is checked.<br>")
    crt: StrictStr = Field(description="The X509 certificate string.<br>")
    prv: Optional[StrictStr] = Field(default=None, description="The X509 private key string.<br>")
    __properties: ClassVar[List[str]] = ["descr", "refid", "trust", "randomserial", "serial", "crt", "prv"]

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
        """Create an instance of PostSystemCertificateAuthorityEndpointRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "refid",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if refid (nullable) is None
        # and model_fields_set contains the field
        if self.refid is None and "refid" in self.model_fields_set:
            _dict['refid'] = None

        # set to None if prv (nullable) is None
        # and model_fields_set contains the field
        if self.prv is None and "prv" in self.model_fields_set:
            _dict['prv'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostSystemCertificateAuthorityEndpointRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "descr": obj.get("descr"),
            "refid": obj.get("refid") if obj.get("refid") is not None else '67ed081a7a0e9',
            "trust": obj.get("trust"),
            "randomserial": obj.get("randomserial"),
            "serial": obj.get("serial") if obj.get("serial") is not None else 1,
            "crt": obj.get("crt"),
            "prv": obj.get("prv")
        })
        return _obj


