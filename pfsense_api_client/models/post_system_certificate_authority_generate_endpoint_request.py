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

class PostSystemCertificateAuthorityGenerateEndpointRequest(BaseModel):
    """
    PostSystemCertificateAuthorityGenerateEndpointRequest
    """ # noqa: E501
    descr: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The descriptive name for this certificate authority.<br>")
    refid: Optional[StrictStr] = Field(default='67ed081a7d9ed', description="The unique ID assigned to this certificate authority for internal system use. This value is generated by this system and cannot be changed.<br>")
    trust: Optional[StrictBool] = Field(default=None, description="Adds or removes this certificate authority from the operating system's trust stored.<br>")
    randomserial: Optional[StrictBool] = Field(default=None, description="Enables or disables the randomization of serial numbers for certificates signed by this CA.<br>")
    serial: Optional[Annotated[int, Field(le=99999999999999, strict=True, ge=0)]] = Field(default=1, description="The decimal number to be used as a sequential serial number for the next certificate to be signed by this CA. This value is ignored when Randomize Serial is checked.<br>")
    is_intermediate: Optional[StrictBool] = Field(default=None, description="Indicates if this certificate authority is an intermediate certificate authority.<br>")
    caref: StrictStr = Field(description="The certificate authority to use as the parent for this intermediate certificate authority.<br><br>This field is only available when the following conditions are met:<br>- `is_intermediate` must be equal to `true`<br>")
    keytype: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The type of key pair to generate.<br>")
    keylen: Annotated[int, Field(le=99999999999999, strict=True, ge=0)] = Field(description="The length of the RSA key pair to generate.<br><br>This field is only available when the following conditions are met:<br>- `keytype` must be equal to `'RSA'`<br>")
    ecname: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The name of the elliptic curve to use for the ECDSA key pair.<br><br>This field is only available when the following conditions are met:<br>- `keytype` must be equal to `'ECDSA'`<br>")
    digest_alg: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The digest algorithm to use when signing certificates.<br>")
    lifetime: Optional[Annotated[int, Field(le=12000, strict=True, ge=1)]] = Field(default=3650, description="The number of days the certificate authority is valid for.<br>")
    dn_commonname: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='internal-ca', description="The common name for the certificate authority.<br>")
    dn_country: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The country for the certificate authority.<br>")
    dn_state: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The state for the certificate authority.<br>")
    dn_city: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The city for the certificate authority.<br>")
    dn_organization: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The organization for the certificate authority.<br>")
    dn_organizationalunit: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The organizational unit for the certificate authority.<br>")
    crt: Optional[StrictStr] = Field(default=None, description="The X509 certificate string.<br>")
    prv: Optional[StrictStr] = Field(default=None, description="The X509 private key string.<br>")
    __properties: ClassVar[List[str]] = ["descr", "refid", "trust", "randomserial", "serial", "is_intermediate", "caref", "keytype", "keylen", "ecname", "digest_alg", "lifetime", "dn_commonname", "dn_country", "dn_state", "dn_city", "dn_organization", "dn_organizationalunit", "crt", "prv"]

    @field_validator('keytype')
    def keytype_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['RSA', 'ECDSA']):
            raise ValueError("must be one of enum values ('RSA', 'ECDSA')")
        return value

    @field_validator('keylen')
    def keylen_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set([1024, 2048, 3072, 4096, 6144, 7680, 8192, 15360, 16384]):
            raise ValueError("must be one of enum values (1024, 2048, 3072, 4096, 6144, 7680, 8192, 15360, 16384)")
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
        """Create an instance of PostSystemCertificateAuthorityGenerateEndpointRequest from a JSON string"""
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
            "refid",
            "serial",
            "crt",
            "prv",
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

        # set to None if serial (nullable) is None
        # and model_fields_set contains the field
        if self.serial is None and "serial" in self.model_fields_set:
            _dict['serial'] = None

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
        """Create an instance of PostSystemCertificateAuthorityGenerateEndpointRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "descr": obj.get("descr"),
            "refid": obj.get("refid") if obj.get("refid") is not None else '67ed081a7d9ed',
            "trust": obj.get("trust"),
            "randomserial": obj.get("randomserial"),
            "serial": obj.get("serial") if obj.get("serial") is not None else 1,
            "is_intermediate": obj.get("is_intermediate"),
            "caref": obj.get("caref"),
            "keytype": obj.get("keytype"),
            "keylen": obj.get("keylen"),
            "ecname": obj.get("ecname"),
            "digest_alg": obj.get("digest_alg"),
            "lifetime": obj.get("lifetime") if obj.get("lifetime") is not None else 3650,
            "dn_commonname": obj.get("dn_commonname") if obj.get("dn_commonname") is not None else 'internal-ca',
            "dn_country": obj.get("dn_country"),
            "dn_state": obj.get("dn_state"),
            "dn_city": obj.get("dn_city"),
            "dn_organization": obj.get("dn_organization"),
            "dn_organizationalunit": obj.get("dn_organizationalunit"),
            "crt": obj.get("crt"),
            "prv": obj.get("prv")
        })
        return _obj


