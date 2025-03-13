"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto_app_integration.types import BaseModel
from gusto_app_integration.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PostV1EmployeesRequestBodyTypedDict(TypedDict):
    r"""Create an employee."""

    first_name: str
    last_name: str
    middle_initial: NotRequired[str]
    preferred_first_name: NotRequired[str]
    date_of_birth: NotRequired[str]
    email: NotRequired[str]
    r"""The employee's personal email address."""
    ssn: NotRequired[str]
    self_onboarding: NotRequired[bool]
    r"""If true, employee is expected to self-onboard. If false, payroll admin is expected to enter in the employee's onboarding information"""


class PostV1EmployeesRequestBody(BaseModel):
    r"""Create an employee."""

    first_name: str

    last_name: str

    middle_initial: Optional[str] = None

    preferred_first_name: Optional[str] = None

    date_of_birth: Optional[str] = None

    email: Optional[str] = None
    r"""The employee's personal email address."""

    ssn: Optional[str] = None

    self_onboarding: Optional[bool] = None
    r"""If true, employee is expected to self-onboard. If false, payroll admin is expected to enter in the employee's onboarding information"""


class PostV1EmployeesRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    request_body: PostV1EmployeesRequestBodyTypedDict
    r"""Create an employee."""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1EmployeesRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PostV1EmployeesRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""Create an employee."""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
