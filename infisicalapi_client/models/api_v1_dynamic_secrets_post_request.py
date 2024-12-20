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


from typing import Optional
from pydantic import StringConstraints, ConfigDict, BaseModel, Field, StrictStr
from infisicalapi_client.models.api_v1_dynamic_secrets_post_request_provider import ApiV1DynamicSecretsPostRequestProvider
from typing_extensions import Annotated

class ApiV1DynamicSecretsPostRequest(BaseModel):
    """
    ApiV1DynamicSecretsPostRequest
    """
    project_slug: Annotated[str, StringConstraints(strict=True, min_length=1)] = Field(default=..., alias="projectSlug", description="The slug of the project to create dynamic secret in.")
    provider: ApiV1DynamicSecretsPostRequestProvider = Field(...)
    default_ttl: StrictStr = Field(default=..., alias="defaultTTL", description="The default TTL that will be applied for all the leases.")
    max_ttl: Optional[StrictStr] = Field(default=None, alias="maxTTL", description="The maximum limit a TTL can be leases or renewed.")
    path: Optional[StrictStr] = Field(default='/', description="The path to create the dynamic secret in.")
    environment_slug: Annotated[str, StringConstraints(strict=True, min_length=1)] = Field(default=..., alias="environmentSlug", description="The slug of the environment to create the dynamic secret in.")
    name: Annotated[str, StringConstraints(strict=True, max_length=64, min_length=1)] = Field(default=..., description="The name of the dynamic secret.")
    __properties = ["projectSlug", "provider", "defaultTTL", "maxTTL", "path", "environmentSlug", "name"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1DynamicSecretsPostRequest:
        """Create an instance of ApiV1DynamicSecretsPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of provider
        if self.provider:
            _dict['provider'] = self.provider.to_dict()
        # set to None if max_ttl (nullable) is None
        # and __fields_set__ contains the field
        if self.max_ttl is None and "max_ttl" in self.__fields_set__:
            _dict['maxTTL'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1DynamicSecretsPostRequest:
        """Create an instance of ApiV1DynamicSecretsPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1DynamicSecretsPostRequest.parse_obj(obj)

        _obj = ApiV1DynamicSecretsPostRequest.parse_obj({
            "project_slug": obj.get("projectSlug"),
            "provider": ApiV1DynamicSecretsPostRequestProvider.from_dict(obj.get("provider")) if obj.get("provider") is not None else None,
            "default_ttl": obj.get("defaultTTL"),
            "max_ttl": obj.get("maxTTL"),
            "path": obj.get("path") if obj.get("path") is not None else '/',
            "environment_slug": obj.get("environmentSlug"),
            "name": obj.get("name")
        })
        return _obj


