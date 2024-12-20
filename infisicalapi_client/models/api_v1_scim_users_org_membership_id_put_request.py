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


from typing import List
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictStr
from infisicalapi_client.models.api_v1_scim_users_get200_response_resources_inner_name import ApiV1ScimUsersGet200ResponseResourcesInnerName
from typing_extensions import Annotated

class ApiV1ScimUsersOrgMembershipIdPutRequest(BaseModel):
    """
    ApiV1ScimUsersOrgMembershipIdPutRequest
    """
    schemas: Annotated[List[StrictStr], Field()] = Field(...)
    id: StrictStr = Field(...)
    user_name: StrictStr = Field(default=..., alias="userName")
    name: ApiV1ScimUsersGet200ResponseResourcesInnerName = Field(...)
    display_name: StrictStr = Field(default=..., alias="displayName")
    active: StrictBool = Field(...)
    __properties = ["schemas", "id", "userName", "name", "displayName", "active"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1ScimUsersOrgMembershipIdPutRequest:
        """Create an instance of ApiV1ScimUsersOrgMembershipIdPutRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1ScimUsersOrgMembershipIdPutRequest:
        """Create an instance of ApiV1ScimUsersOrgMembershipIdPutRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1ScimUsersOrgMembershipIdPutRequest.parse_obj(obj)

        _obj = ApiV1ScimUsersOrgMembershipIdPutRequest.parse_obj({
            "schemas": obj.get("schemas"),
            "id": obj.get("id"),
            "user_name": obj.get("userName"),
            "name": ApiV1ScimUsersGet200ResponseResourcesInnerName.from_dict(obj.get("name")) if obj.get("name") is not None else None,
            "display_name": obj.get("displayName"),
            "active": obj.get("active")
        })
        return _obj


