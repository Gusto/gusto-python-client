"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto_embedded.types import BaseModel
from gusto_embedded.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PutAddPeopleToDepartmentEmployeesTypedDict(TypedDict):
    uuid: NotRequired[str]


class PutAddPeopleToDepartmentEmployees(BaseModel):
    uuid: Optional[str] = None


class PutAddPeopleToDepartmentContractorsTypedDict(TypedDict):
    uuid: NotRequired[str]


class PutAddPeopleToDepartmentContractors(BaseModel):
    uuid: Optional[str] = None


class PutAddPeopleToDepartmentRequestBodyTypedDict(TypedDict):
    version: NotRequired[str]
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""
    employees: NotRequired[List[PutAddPeopleToDepartmentEmployeesTypedDict]]
    r"""Array of employees to add to the department"""
    contractors: NotRequired[List[PutAddPeopleToDepartmentContractorsTypedDict]]
    r"""Array of contractors to add to the department"""


class PutAddPeopleToDepartmentRequestBody(BaseModel):
    version: Optional[str] = None
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""

    employees: Optional[List[PutAddPeopleToDepartmentEmployees]] = None
    r"""Array of employees to add to the department"""

    contractors: Optional[List[PutAddPeopleToDepartmentContractors]] = None
    r"""Array of contractors to add to the department"""


class PutAddPeopleToDepartmentRequestTypedDict(TypedDict):
    department_uuid: str
    r"""The UUID of the department"""
    request_body: PutAddPeopleToDepartmentRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutAddPeopleToDepartmentRequest(BaseModel):
    department_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the department"""

    request_body: Annotated[
        PutAddPeopleToDepartmentRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
