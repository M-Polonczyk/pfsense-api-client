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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PostVPNIPsecPhase1EncryptionEndpointRequest(BaseModel):
    """
    PostVPNIPsecPhase1EncryptionEndpointRequest
    """ # noqa: E501
    encryption_algorithm_name: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The name of the encryption algorithm to use for this P1 encryption item.<br>")
    encryption_algorithm_keylen: Annotated[int, Field(le=99999999999999, strict=True, ge=0)] = Field(description="The key length for the encryption algorithm.<br><br>This field is only available when the following conditions are met:<br>- `encryption_algorithm_name` must be one of [ aes, aes128gcm, aes192gcm, aes256gcm ]<br>")
    hash_algorithm: Annotated[str, Field(min_length=0, strict=True, max_length=1024)] = Field(description="The hash algorithm to use for this P1 encryption item.<br>")
    dhgroup: Annotated[int, Field(le=99999999999999, strict=True, ge=0)] = Field(description="The Diffie-Hellman (DH) group to use for this P1 encryption item.<br>")
    prf_algorithm: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='sha256', description="The PRF algorithm to use for this P1 encryption item. This value has no affect unless the P1 entry has PRF enabled.<br>")
    parent_id: StrictInt = Field(description="The ID of the parent this object is nested under.")
    __properties: ClassVar[List[str]] = ["encryption_algorithm_name", "encryption_algorithm_keylen", "hash_algorithm", "dhgroup", "prf_algorithm", "parent_id"]

    @field_validator('encryption_algorithm_name')
    def encryption_algorithm_name_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['aes', 'aes128gcm', 'aes192gcm', 'aes256gcm', 'chacha20poly1305']):
            raise ValueError("must be one of enum values ('aes', 'aes128gcm', 'aes192gcm', 'aes256gcm', 'chacha20poly1305')")
        return value

    @field_validator('hash_algorithm')
    def hash_algorithm_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['sha1', 'sha256', 'sha384', 'sha512', 'aesxcbc']):
            raise ValueError("must be one of enum values ('sha1', 'sha256', 'sha384', 'sha512', 'aesxcbc')")
        return value

    @field_validator('dhgroup')
    def dhgroup_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set([1, 2, 5, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]):
            raise ValueError("must be one of enum values (1, 2, 5, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)")
        return value

    @field_validator('prf_algorithm')
    def prf_algorithm_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['sha1', 'sha256', 'sha384', 'sha512', 'aesxcbc']):
            raise ValueError("must be one of enum values ('sha1', 'sha256', 'sha384', 'sha512', 'aesxcbc')")
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
        """Create an instance of PostVPNIPsecPhase1EncryptionEndpointRequest from a JSON string"""
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
        """Create an instance of PostVPNIPsecPhase1EncryptionEndpointRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "encryption_algorithm_name": obj.get("encryption_algorithm_name"),
            "encryption_algorithm_keylen": obj.get("encryption_algorithm_keylen"),
            "hash_algorithm": obj.get("hash_algorithm"),
            "dhgroup": obj.get("dhgroup"),
            "prf_algorithm": obj.get("prf_algorithm") if obj.get("prf_algorithm") is not None else 'sha256',
            "parent_id": obj.get("parent_id")
        })
        return _obj


