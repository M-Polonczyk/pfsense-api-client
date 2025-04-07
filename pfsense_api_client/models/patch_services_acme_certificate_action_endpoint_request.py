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

class PatchServicesACMECertificateActionEndpointRequest(BaseModel):
    """
    PatchServicesACMECertificateActionEndpointRequest
    """ # noqa: E501
    status: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default='active', description="The activation status of the ACME certificate.<br>")
    command: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The command to execute on the ACME certificate.<br>")
    method: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="The action method that should be used to run the command.<br>")
    parent_id: StrictInt = Field(description="The ID of the parent this object is nested under.")
    id: StrictInt = Field(description="The ID of the object or resource to interact with.")
    __properties: ClassVar[List[str]] = ["status", "command", "method", "parent_id", "id"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['active', 'disabled']):
            raise ValueError("must be one of enum values ('active', 'disabled')")
        return value

    @field_validator('method')
    def method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['shellcommand', 'php_command', 'servicerestart', 'xmlrpcservicerestart']):
            raise ValueError("must be one of enum values ('shellcommand', 'php_command', 'servicerestart', 'xmlrpcservicerestart')")
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
        """Create an instance of PatchServicesACMECertificateActionEndpointRequest from a JSON string"""
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
        """Create an instance of PatchServicesACMECertificateActionEndpointRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status") if obj.get("status") is not None else 'active',
            "command": obj.get("command"),
            "method": obj.get("method"),
            "parent_id": obj.get("parent_id"),
            "id": obj.get("id")
        })
        return _obj


