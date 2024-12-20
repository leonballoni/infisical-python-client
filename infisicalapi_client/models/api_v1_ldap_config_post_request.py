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
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictStr

class ApiV1LdapConfigPostRequest(BaseModel):
    """
    ApiV1LdapConfigPostRequest
    """
    organization_id: StrictStr = Field(default=..., alias="organizationId")
    is_active: StrictBool = Field(default=..., alias="isActive")
    url: StrictStr = Field(...)
    bind_dn: StrictStr = Field(default=..., alias="bindDN")
    bind_pass: StrictStr = Field(default=..., alias="bindPass")
    unique_user_attribute: Optional[StrictStr] = Field(default='uidNumber', alias="uniqueUserAttribute")
    search_base: StrictStr = Field(default=..., alias="searchBase")
    search_filter: Optional[StrictStr] = Field(default='(uid={{username}})', alias="searchFilter")
    group_search_base: StrictStr = Field(default=..., alias="groupSearchBase")
    group_search_filter: Optional[StrictStr] = Field(default='(|(memberUid={{.Username}})(member={{.UserDN}})(uniqueMember={{.UserDN}}))', alias="groupSearchFilter")
    ca_cert: Optional[StrictStr] = Field(default='', alias="caCert")
    __properties = ["organizationId", "isActive", "url", "bindDN", "bindPass", "uniqueUserAttribute", "searchBase", "searchFilter", "groupSearchBase", "groupSearchFilter", "caCert"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1LdapConfigPostRequest:
        """Create an instance of ApiV1LdapConfigPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1LdapConfigPostRequest:
        """Create an instance of ApiV1LdapConfigPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1LdapConfigPostRequest.parse_obj(obj)

        _obj = ApiV1LdapConfigPostRequest.parse_obj({
            "organization_id": obj.get("organizationId"),
            "is_active": obj.get("isActive"),
            "url": obj.get("url"),
            "bind_dn": obj.get("bindDN"),
            "bind_pass": obj.get("bindPass"),
            "unique_user_attribute": obj.get("uniqueUserAttribute") if obj.get("uniqueUserAttribute") is not None else 'uidNumber',
            "search_base": obj.get("searchBase"),
            "search_filter": obj.get("searchFilter") if obj.get("searchFilter") is not None else '(uid={{username}})',
            "group_search_base": obj.get("groupSearchBase"),
            "group_search_filter": obj.get("groupSearchFilter") if obj.get("groupSearchFilter") is not None else '(|(memberUid={{.Username}})(member={{.UserDN}})(uniqueMember={{.UserDN}}))',
            "ca_cert": obj.get("caCert") if obj.get("caCert") is not None else ''
        })
        return _obj


