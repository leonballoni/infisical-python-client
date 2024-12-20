# coding: utf-8

"""
    Infisical API

    List of all available APIs that can be consumed

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import StringConstraints, ConfigDict, BaseModel, Field, StrictStr
from typing_extensions import Annotated

class ApiV1OrganizationOrganizationIdRolesPostRequest(BaseModel):
    """
    ApiV1OrganizationOrganizationIdRolesPostRequest
    """
    slug: Annotated[str, StringConstraints(strict=True, min_length=1)] = Field(...)
    name: StrictStr = Field(...)
    description: Optional[StrictStr] = None
    permissions: Annotated[List[StrictStr], Field()] = Field(...)
    __properties = ["slug", "name", "description", "permissions"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1OrganizationOrganizationIdRolesPostRequest:
        """Create an instance of ApiV1OrganizationOrganizationIdRolesPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1OrganizationOrganizationIdRolesPostRequest:
        """Create an instance of ApiV1OrganizationOrganizationIdRolesPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1OrganizationOrganizationIdRolesPostRequest.parse_obj(obj)

        _obj = ApiV1OrganizationOrganizationIdRolesPostRequest.parse_obj({
            "slug": obj.get("slug"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "permissions": obj.get("permissions")
        })
        return _obj


