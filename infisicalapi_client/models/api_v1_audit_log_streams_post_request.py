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
from pydantic import StringConstraints, ConfigDict, BaseModel, Field
from infisicalapi_client.models.api_v1_audit_log_streams_post_request_headers_inner import ApiV1AuditLogStreamsPostRequestHeadersInner
from typing_extensions import Annotated

class ApiV1AuditLogStreamsPostRequest(BaseModel):
    """
    ApiV1AuditLogStreamsPostRequest
    """
    url: Annotated[str, StringConstraints(strict=True, min_length=1)] = Field(default=..., description="The HTTP URL to push logs to.")
    headers: Optional[Annotated[List[ApiV1AuditLogStreamsPostRequestHeadersInner], Field()]] = Field(default=None, description="The HTTP headers attached for the external prrovider requests.")
    __properties = ["url", "headers"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1AuditLogStreamsPostRequest:
        """Create an instance of ApiV1AuditLogStreamsPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in headers (list)
        _items = []
        if self.headers:
            for _item in self.headers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['headers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AuditLogStreamsPostRequest:
        """Create an instance of ApiV1AuditLogStreamsPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AuditLogStreamsPostRequest.parse_obj(obj)

        _obj = ApiV1AuditLogStreamsPostRequest.parse_obj({
            "url": obj.get("url"),
            "headers": [ApiV1AuditLogStreamsPostRequestHeadersInner.from_dict(_item) for _item in obj.get("headers")] if obj.get("headers") is not None else None
        })
        return _obj


