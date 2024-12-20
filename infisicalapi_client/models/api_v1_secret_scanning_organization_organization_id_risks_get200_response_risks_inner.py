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
from typing import List, Optional
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictStr
from typing_extensions import Annotated

class ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner(BaseModel):
    """
    ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner
    """
    id: StrictStr = Field(...)
    description: Optional[StrictStr] = None
    start_line: Optional[StrictStr] = Field(default=None, alias="startLine")
    end_line: Optional[StrictStr] = Field(default=None, alias="endLine")
    start_column: Optional[StrictStr] = Field(default=None, alias="startColumn")
    end_column: Optional[StrictStr] = Field(default=None, alias="endColumn")
    file: Optional[StrictStr] = None
    symlink_file: Optional[StrictStr] = Field(default=None, alias="symlinkFile")
    commit: Optional[StrictStr] = None
    entropy: Optional[StrictStr] = None
    author: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    var_date: Optional[StrictStr] = Field(default=None, alias="date")
    message: Optional[StrictStr] = None
    tags: Optional[Annotated[List[StrictStr], Field()]] = None
    rule_id: Optional[StrictStr] = Field(default=None, alias="ruleID")
    fingerprint: Optional[StrictStr] = None
    finger_print_without_commit_id: Optional[StrictStr] = Field(default=None, alias="fingerPrintWithoutCommitId")
    is_false_positive: Optional[StrictBool] = Field(default=False, alias="isFalsePositive")
    is_resolved: Optional[StrictBool] = Field(default=False, alias="isResolved")
    risk_owner: Optional[StrictStr] = Field(default=None, alias="riskOwner")
    installation_id: StrictStr = Field(default=..., alias="installationId")
    repository_id: Optional[StrictStr] = Field(default=None, alias="repositoryId")
    repository_link: Optional[StrictStr] = Field(default=None, alias="repositoryLink")
    repository_full_name: Optional[StrictStr] = Field(default=None, alias="repositoryFullName")
    pusher_name: Optional[StrictStr] = Field(default=None, alias="pusherName")
    pusher_email: Optional[StrictStr] = Field(default=None, alias="pusherEmail")
    status: Optional[StrictStr] = None
    org_id: StrictStr = Field(default=..., alias="orgId")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    __properties = ["id", "description", "startLine", "endLine", "startColumn", "endColumn", "file", "symlinkFile", "commit", "entropy", "author", "email", "date", "message", "tags", "ruleID", "fingerprint", "fingerPrintWithoutCommitId", "isFalsePositive", "isResolved", "riskOwner", "installationId", "repositoryId", "repositoryLink", "repositoryFullName", "pusherName", "pusherEmail", "status", "orgId", "createdAt", "updatedAt"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner:
        """Create an instance of ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if start_line (nullable) is None
        # and __fields_set__ contains the field
        if self.start_line is None and "start_line" in self.__fields_set__:
            _dict['startLine'] = None

        # set to None if end_line (nullable) is None
        # and __fields_set__ contains the field
        if self.end_line is None and "end_line" in self.__fields_set__:
            _dict['endLine'] = None

        # set to None if start_column (nullable) is None
        # and __fields_set__ contains the field
        if self.start_column is None and "start_column" in self.__fields_set__:
            _dict['startColumn'] = None

        # set to None if end_column (nullable) is None
        # and __fields_set__ contains the field
        if self.end_column is None and "end_column" in self.__fields_set__:
            _dict['endColumn'] = None

        # set to None if file (nullable) is None
        # and __fields_set__ contains the field
        if self.file is None and "file" in self.__fields_set__:
            _dict['file'] = None

        # set to None if symlink_file (nullable) is None
        # and __fields_set__ contains the field
        if self.symlink_file is None and "symlink_file" in self.__fields_set__:
            _dict['symlinkFile'] = None

        # set to None if commit (nullable) is None
        # and __fields_set__ contains the field
        if self.commit is None and "commit" in self.__fields_set__:
            _dict['commit'] = None

        # set to None if entropy (nullable) is None
        # and __fields_set__ contains the field
        if self.entropy is None and "entropy" in self.__fields_set__:
            _dict['entropy'] = None

        # set to None if author (nullable) is None
        # and __fields_set__ contains the field
        if self.author is None and "author" in self.__fields_set__:
            _dict['author'] = None

        # set to None if email (nullable) is None
        # and __fields_set__ contains the field
        if self.email is None and "email" in self.__fields_set__:
            _dict['email'] = None

        # set to None if var_date (nullable) is None
        # and __fields_set__ contains the field
        if self.var_date is None and "var_date" in self.__fields_set__:
            _dict['date'] = None

        # set to None if message (nullable) is None
        # and __fields_set__ contains the field
        if self.message is None and "message" in self.__fields_set__:
            _dict['message'] = None

        # set to None if tags (nullable) is None
        # and __fields_set__ contains the field
        if self.tags is None and "tags" in self.__fields_set__:
            _dict['tags'] = None

        # set to None if rule_id (nullable) is None
        # and __fields_set__ contains the field
        if self.rule_id is None and "rule_id" in self.__fields_set__:
            _dict['ruleID'] = None

        # set to None if fingerprint (nullable) is None
        # and __fields_set__ contains the field
        if self.fingerprint is None and "fingerprint" in self.__fields_set__:
            _dict['fingerprint'] = None

        # set to None if finger_print_without_commit_id (nullable) is None
        # and __fields_set__ contains the field
        if self.finger_print_without_commit_id is None and "finger_print_without_commit_id" in self.__fields_set__:
            _dict['fingerPrintWithoutCommitId'] = None

        # set to None if is_false_positive (nullable) is None
        # and __fields_set__ contains the field
        if self.is_false_positive is None and "is_false_positive" in self.__fields_set__:
            _dict['isFalsePositive'] = None

        # set to None if is_resolved (nullable) is None
        # and __fields_set__ contains the field
        if self.is_resolved is None and "is_resolved" in self.__fields_set__:
            _dict['isResolved'] = None

        # set to None if risk_owner (nullable) is None
        # and __fields_set__ contains the field
        if self.risk_owner is None and "risk_owner" in self.__fields_set__:
            _dict['riskOwner'] = None

        # set to None if repository_id (nullable) is None
        # and __fields_set__ contains the field
        if self.repository_id is None and "repository_id" in self.__fields_set__:
            _dict['repositoryId'] = None

        # set to None if repository_link (nullable) is None
        # and __fields_set__ contains the field
        if self.repository_link is None and "repository_link" in self.__fields_set__:
            _dict['repositoryLink'] = None

        # set to None if repository_full_name (nullable) is None
        # and __fields_set__ contains the field
        if self.repository_full_name is None and "repository_full_name" in self.__fields_set__:
            _dict['repositoryFullName'] = None

        # set to None if pusher_name (nullable) is None
        # and __fields_set__ contains the field
        if self.pusher_name is None and "pusher_name" in self.__fields_set__:
            _dict['pusherName'] = None

        # set to None if pusher_email (nullable) is None
        # and __fields_set__ contains the field
        if self.pusher_email is None and "pusher_email" in self.__fields_set__:
            _dict['pusherEmail'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner:
        """Create an instance of ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner.parse_obj(obj)

        _obj = ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner.parse_obj({
            "id": obj.get("id"),
            "description": obj.get("description"),
            "start_line": obj.get("startLine"),
            "end_line": obj.get("endLine"),
            "start_column": obj.get("startColumn"),
            "end_column": obj.get("endColumn"),
            "file": obj.get("file"),
            "symlink_file": obj.get("symlinkFile"),
            "commit": obj.get("commit"),
            "entropy": obj.get("entropy"),
            "author": obj.get("author"),
            "email": obj.get("email"),
            "var_date": obj.get("date"),
            "message": obj.get("message"),
            "tags": obj.get("tags"),
            "rule_id": obj.get("ruleID"),
            "fingerprint": obj.get("fingerprint"),
            "finger_print_without_commit_id": obj.get("fingerPrintWithoutCommitId"),
            "is_false_positive": obj.get("isFalsePositive") if obj.get("isFalsePositive") is not None else False,
            "is_resolved": obj.get("isResolved") if obj.get("isResolved") is not None else False,
            "risk_owner": obj.get("riskOwner"),
            "installation_id": obj.get("installationId"),
            "repository_id": obj.get("repositoryId"),
            "repository_link": obj.get("repositoryLink"),
            "repository_full_name": obj.get("repositoryFullName"),
            "pusher_name": obj.get("pusherName"),
            "pusher_email": obj.get("pusherEmail"),
            "status": obj.get("status"),
            "org_id": obj.get("orgId"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj


