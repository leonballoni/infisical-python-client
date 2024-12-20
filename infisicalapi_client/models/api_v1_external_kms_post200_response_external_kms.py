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

from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictStr
from infisicalapi_client.models.api_v1_external_kms_post200_response_external_kms_external import ApiV1ExternalKmsPost200ResponseExternalKmsExternal

class ApiV1ExternalKmsPost200ResponseExternalKms(BaseModel):
    """
    ApiV1ExternalKmsPost200ResponseExternalKms
    """
    id: StrictStr = Field(...)
    description: Optional[StrictStr] = None
    is_disabled: Optional[StrictBool] = Field(default=False, alias="isDisabled")
    is_reserved: Optional[StrictBool] = Field(default=True, alias="isReserved")
    org_id: StrictStr = Field(default=..., alias="orgId")
    slug: StrictStr = Field(...)
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    external: ApiV1ExternalKmsPost200ResponseExternalKmsExternal = Field(...)
    __properties = ["id", "description", "isDisabled", "isReserved", "orgId", "slug", "createdAt", "updatedAt", "external"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1ExternalKmsPost200ResponseExternalKms:
        """Create an instance of ApiV1ExternalKmsPost200ResponseExternalKms from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of external
        if self.external:
            _dict['external'] = self.external.to_dict()
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if is_disabled (nullable) is None
        # and __fields_set__ contains the field
        if self.is_disabled is None and "is_disabled" in self.__fields_set__:
            _dict['isDisabled'] = None

        # set to None if is_reserved (nullable) is None
        # and __fields_set__ contains the field
        if self.is_reserved is None and "is_reserved" in self.__fields_set__:
            _dict['isReserved'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1ExternalKmsPost200ResponseExternalKms:
        """Create an instance of ApiV1ExternalKmsPost200ResponseExternalKms from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1ExternalKmsPost200ResponseExternalKms.parse_obj(obj)

        _obj = ApiV1ExternalKmsPost200ResponseExternalKms.parse_obj({
            "id": obj.get("id"),
            "description": obj.get("description"),
            "is_disabled": obj.get("isDisabled") if obj.get("isDisabled") is not None else False,
            "is_reserved": obj.get("isReserved") if obj.get("isReserved") is not None else True,
            "org_id": obj.get("orgId"),
            "slug": obj.get("slug"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "external": ApiV1ExternalKmsPost200ResponseExternalKmsExternal.from_dict(obj.get("external")) if obj.get("external") is not None else None
        })
        return _obj


