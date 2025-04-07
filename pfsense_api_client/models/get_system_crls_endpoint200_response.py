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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pfsense_api_client.models.certificate_revocation_list import CertificateRevocationList
from typing import Optional, Set
from typing_extensions import Self

class GetSystemCRLsEndpoint200Response(BaseModel):
    """
    GetSystemCRLsEndpoint200Response
    """ # noqa: E501
    code: Optional[StrictInt] = Field(default=200, description="The HTTP status code that corresponds with the API response.")
    status: Optional[StrictStr] = Field(default='ok', description="The HTTP status message that corresponds with the HTTP status code.")
    response_id: Optional[StrictStr] = Field(default=None, description="The unique response ID that corresponds with the result of the APIcall. In most situations, this will contain an error code.")
    message: Optional[StrictStr] = Field(default=None, description="The descriptive message detailing the results of the API call.")
    data: Optional[List[CertificateRevocationList]] = None
    links: Optional[Dict[str, Any]] = Field(default=None, description="An array of links to resources that are related to this API response.", alias="_links")
    __properties: ClassVar[List[str]] = ["code", "status", "response_id", "message", "data", "_links"]

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
        """Create an instance of GetSystemCRLsEndpoint200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item_data in self.data:
                if _item_data:
                    _items.append(_item_data.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetSystemCRLsEndpoint200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code") if obj.get("code") is not None else 200,
            "status": obj.get("status") if obj.get("status") is not None else 'ok',
            "response_id": obj.get("response_id"),
            "message": obj.get("message"),
            "data": [CertificateRevocationList.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None,
            "_links": obj.get("_links")
        })
        return _obj


