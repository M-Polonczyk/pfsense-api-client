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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CertificateRevocationListRevokedCertificate(BaseModel):
    """
    CertificateRevocationListRevokedCertificate
    """ # noqa: E501
    certref: Optional[StrictStr] = Field(default=None, description="The reference ID of the certificate to be revoked<br><br>This field is only available when the following conditions are met:<br>- `serial` must be equal to `NULL`<br>")
    serial: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The serial number of the certificate to be revoked.<br>")
    reason: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=-1)]] = Field(default=None, description="The CRL reason for revocation code.<br>")
    revoke_time: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=None, description="The unix timestamp of when the certificate was revoked.<br>")
    caref: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The unique ID of the CA that signed the revoked certificate.<br>")
    descr: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The unique name/description for this CRL.<br>")
    type: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The type of the certificate to be revoked.<br>")
    crt: Optional[StrictStr] = Field(default=None, description="The X509 certificate string.<br>")
    prv: Optional[StrictStr] = Field(default=None, description="The X509 private key string.<br>")
    __properties: ClassVar[List[str]] = ["certref", "serial", "reason", "revoke_time", "caref", "descr", "type", "crt", "prv"]

    @field_validator('reason')
    def reason_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([-1, 0, 1, 2, 3, 4, 5, 6, 9]):
            raise ValueError("must be one of enum values (-1, 0, 1, 2, 3, 4, 5, 6, 9)")
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
        """Create an instance of CertificateRevocationListRevokedCertificate from a JSON string"""
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
        # set to None if serial (nullable) is None
        # and model_fields_set contains the field
        if self.serial is None and "serial" in self.model_fields_set:
            _dict['serial'] = None

        # set to None if caref (nullable) is None
        # and model_fields_set contains the field
        if self.caref is None and "caref" in self.model_fields_set:
            _dict['caref'] = None

        # set to None if descr (nullable) is None
        # and model_fields_set contains the field
        if self.descr is None and "descr" in self.model_fields_set:
            _dict['descr'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if crt (nullable) is None
        # and model_fields_set contains the field
        if self.crt is None and "crt" in self.model_fields_set:
            _dict['crt'] = None

        # set to None if prv (nullable) is None
        # and model_fields_set contains the field
        if self.prv is None and "prv" in self.model_fields_set:
            _dict['prv'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CertificateRevocationListRevokedCertificate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "certref": obj.get("certref"),
            "serial": obj.get("serial"),
            "reason": obj.get("reason"),
            "revoke_time": obj.get("revoke_time"),
            "caref": obj.get("caref"),
            "descr": obj.get("descr"),
            "type": obj.get("type"),
            "crt": obj.get("crt"),
            "prv": obj.get("prv")
        })
        return _obj


