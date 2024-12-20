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



from pydantic import ConfigDict, BaseModel, Field, StrictStr

class ApiV1WorkspaceWorkspaceIdNamePostRequest(BaseModel):
    """
    ApiV1WorkspaceWorkspaceIdNamePostRequest
    """
    name: StrictStr = Field(...)
    __properties = ["name"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1WorkspaceWorkspaceIdNamePostRequest:
        """Create an instance of ApiV1WorkspaceWorkspaceIdNamePostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WorkspaceWorkspaceIdNamePostRequest:
        """Create an instance of ApiV1WorkspaceWorkspaceIdNamePostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1WorkspaceWorkspaceIdNamePostRequest.parse_obj(obj)

        _obj = ApiV1WorkspaceWorkspaceIdNamePostRequest.parse_obj({
            "name": obj.get("name")
        })
        return _obj


