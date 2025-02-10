"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto.types import BaseModel
from gusto.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PutV1EmployeesEmployeeIDOnboardingDocumentsConfigRequestBodyTypedDict(TypedDict):
    i9_document: NotRequired[bool]
    r"""Whether to include Form I-9 for an employee during onboarding"""


class PutV1EmployeesEmployeeIDOnboardingDocumentsConfigRequestBody(BaseModel):
    i9_document: Optional[bool] = None
    r"""Whether to include Form I-9 for an employee during onboarding"""


class PutV1EmployeesEmployeeIDOnboardingDocumentsConfigRequestTypedDict(TypedDict):
    employee_id: str
    r"""The UUID of the employee"""
    request_body: PutV1EmployeesEmployeeIDOnboardingDocumentsConfigRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1EmployeesEmployeeIDOnboardingDocumentsConfigRequest(BaseModel):
    employee_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the employee"""

    request_body: Annotated[
        PutV1EmployeesEmployeeIDOnboardingDocumentsConfigRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
