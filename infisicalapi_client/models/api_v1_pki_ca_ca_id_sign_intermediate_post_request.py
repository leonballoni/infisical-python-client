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


from typing import Optional, Union
from pydantic import StringConstraints, ConfigDict, BaseModel, Field, StrictStr
from typing_extensions import Annotated

class ApiV1PkiCaCaIdSignIntermediatePostRequest(BaseModel):
    """
    ApiV1PkiCaCaIdSignIntermediatePostRequest
    """
    csr: Annotated[str, StringConstraints(strict=True, min_length=1)] = Field(default=..., description="The pem-encoded CSR to sign with the CA")
    not_before: Optional[StrictStr] = Field(default=None, alias="notBefore", description="The date and time when the intermediate CA becomes valid in YYYY-MM-DDTHH:mm:ss.sssZ format")
    not_after: StrictStr = Field(default=..., alias="notAfter", description="The date and time when the intermediate CA expires in YYYY-MM-DDTHH:mm:ss.sssZ format")
    max_path_length: Optional[Union[Annotated[float, Field(ge=-1, strict=True)], Annotated[int, Field(ge=-1, strict=True)]]] = Field(default=-1, alias="maxPathLength", description="The maximum number of intermediate CAs that may follow this CA in the certificate / CA chain. A maxPathLength of -1 implies no path limit on the chain.")
    __properties = ["csr", "notBefore", "notAfter", "maxPathLength"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1PkiCaCaIdSignIntermediatePostRequest:
        """Create an instance of ApiV1PkiCaCaIdSignIntermediatePostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1PkiCaCaIdSignIntermediatePostRequest:
        """Create an instance of ApiV1PkiCaCaIdSignIntermediatePostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1PkiCaCaIdSignIntermediatePostRequest.parse_obj(obj)

        _obj = ApiV1PkiCaCaIdSignIntermediatePostRequest.parse_obj({
            "csr": obj.get("csr"),
            "not_before": obj.get("notBefore"),
            "not_after": obj.get("notAfter"),
            "max_path_length": obj.get("maxPathLength") if obj.get("maxPathLength") is not None else -1
        })
        return _obj


