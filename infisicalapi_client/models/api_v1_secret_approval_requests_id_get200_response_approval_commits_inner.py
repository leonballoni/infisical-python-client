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
from typing import Any, List, Optional, Union
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from infisicalapi_client.models.api_v1_secret_approval_requests_id_get200_response_approval_commits_inner_secret import ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret
from infisicalapi_client.models.api_v1_secret_approval_requests_id_get200_response_approval_commits_inner_secret_version import ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecretVersion
from infisicalapi_client.models.api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_secret_versions_inner_tags_inner import ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInnerTagsInner
from typing_extensions import Annotated

class ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner(BaseModel):
    """
    ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner
    """
    id: StrictStr = Field(...)
    secret_key: StrictStr = Field(default=..., alias="secretKey")
    secret_value: StrictStr = Field(default=..., alias="secretValue")
    secret_comment: StrictStr = Field(default=..., alias="secretComment")
    secret_reminder_note: Optional[StrictStr] = Field(default=None, alias="secretReminderNote")
    secret_reminder_repeat_days: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="secretReminderRepeatDays")
    skip_multiline_encoding: Optional[StrictBool] = Field(default=False, alias="skipMultilineEncoding")
    metadata: Optional[Any] = None
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    op: StrictStr = Field(...)
    tags: Optional[Annotated[List[ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInnerTagsInner], Field()]] = None
    secret: Optional[ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret] = None
    secret_version: Optional[ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecretVersion] = Field(default=None, alias="secretVersion")
    __properties = ["id", "secretKey", "secretValue", "secretComment", "secretReminderNote", "secretReminderRepeatDays", "skipMultilineEncoding", "metadata", "createdAt", "updatedAt", "op", "tags", "secret", "secretVersion"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner:
        """Create an instance of ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of secret
        if self.secret:
            _dict['secret'] = self.secret.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secret_version
        if self.secret_version:
            _dict['secretVersion'] = self.secret_version.to_dict()
        # set to None if secret_reminder_note (nullable) is None
        # and __fields_set__ contains the field
        if self.secret_reminder_note is None and "secret_reminder_note" in self.__fields_set__:
            _dict['secretReminderNote'] = None

        # set to None if secret_reminder_repeat_days (nullable) is None
        # and __fields_set__ contains the field
        if self.secret_reminder_repeat_days is None and "secret_reminder_repeat_days" in self.__fields_set__:
            _dict['secretReminderRepeatDays'] = None

        # set to None if skip_multiline_encoding (nullable) is None
        # and __fields_set__ contains the field
        if self.skip_multiline_encoding is None and "skip_multiline_encoding" in self.__fields_set__:
            _dict['skipMultilineEncoding'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if secret (nullable) is None
        # and __fields_set__ contains the field
        if self.secret is None and "secret" in self.__fields_set__:
            _dict['secret'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner:
        """Create an instance of ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner.parse_obj(obj)

        _obj = ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner.parse_obj({
            "id": obj.get("id"),
            "secret_key": obj.get("secretKey"),
            "secret_value": obj.get("secretValue"),
            "secret_comment": obj.get("secretComment"),
            "secret_reminder_note": obj.get("secretReminderNote"),
            "secret_reminder_repeat_days": obj.get("secretReminderRepeatDays"),
            "skip_multiline_encoding": obj.get("skipMultilineEncoding") if obj.get("skipMultilineEncoding") is not None else False,
            "metadata": obj.get("metadata"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "op": obj.get("op"),
            "tags": [ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInnerTagsInner.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None,
            "secret": ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret.from_dict(obj.get("secret")) if obj.get("secret") is not None else None,
            "secret_version": ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecretVersion.from_dict(obj.get("secretVersion")) if obj.get("secretVersion") is not None else None
        })
        return _obj


