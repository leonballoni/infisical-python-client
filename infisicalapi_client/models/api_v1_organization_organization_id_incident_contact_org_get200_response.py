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
from pydantic import ConfigDict, BaseModel, Field
from infisicalapi_client.models.api_v1_organization_organization_id_incident_contact_org_get200_response_incident_contacts_org_inner import ApiV1OrganizationOrganizationIdIncidentContactOrgGet200ResponseIncidentContactsOrgInner
from typing_extensions import Annotated

class ApiV1OrganizationOrganizationIdIncidentContactOrgGet200Response(BaseModel):
    """
    ApiV1OrganizationOrganizationIdIncidentContactOrgGet200Response
    """
    incident_contacts_org: Annotated[List[ApiV1OrganizationOrganizationIdIncidentContactOrgGet200ResponseIncidentContactsOrgInner], Field()] = Field(default=..., alias="incidentContactsOrg")
    __properties = ["incidentContactsOrg"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1OrganizationOrganizationIdIncidentContactOrgGet200Response:
        """Create an instance of ApiV1OrganizationOrganizationIdIncidentContactOrgGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in incident_contacts_org (list)
        _items = []
        if self.incident_contacts_org:
            for _item in self.incident_contacts_org:
                if _item:
                    _items.append(_item.to_dict())
            _dict['incidentContactsOrg'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1OrganizationOrganizationIdIncidentContactOrgGet200Response:
        """Create an instance of ApiV1OrganizationOrganizationIdIncidentContactOrgGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1OrganizationOrganizationIdIncidentContactOrgGet200Response.parse_obj(obj)

        _obj = ApiV1OrganizationOrganizationIdIncidentContactOrgGet200Response.parse_obj({
            "incident_contacts_org": [ApiV1OrganizationOrganizationIdIncidentContactOrgGet200ResponseIncidentContactsOrgInner.from_dict(_item) for _item in obj.get("incidentContactsOrg")] if obj.get("incidentContactsOrg") is not None else None
        })
        return _obj


