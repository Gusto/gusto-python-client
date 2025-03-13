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


class PutV1EmployeesRequestBodyTypedDict(TypedDict):
    r"""Update an employee."""

    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""
    first_name: NotRequired[str]
    middle_initial: NotRequired[str]
    last_name: NotRequired[str]
    preferred_first_name: NotRequired[str]
    date_of_birth: NotRequired[str]
    email: NotRequired[str]
    r"""The employee's personal email address."""
    ssn: NotRequired[str]
    two_percent_shareholder: NotRequired[bool]
    r"""Whether the employee is a two percent shareholder of the company. This field only applies to companies with an S-Corp entity type."""


class PutV1EmployeesRequestBody(BaseModel):
    r"""Update an employee."""

    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""

    first_name: Optional[str] = None

    middle_initial: Optional[str] = None

    last_name: Optional[str] = None

    preferred_first_name: Optional[str] = None

    date_of_birth: Optional[str] = None

    email: Optional[str] = None
    r"""The employee's personal email address."""

    ssn: Optional[str] = None

    two_percent_shareholder: Optional[bool] = None
    r"""Whether the employee is a two percent shareholder of the company. This field only applies to companies with an S-Corp entity type."""


class PutV1EmployeesRequestTypedDict(TypedDict):
    employee_id: str
    r"""The UUID of the employee"""
    request_body: PutV1EmployeesRequestBodyTypedDict
    r"""Update an employee."""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1EmployeesRequest(BaseModel):
    employee_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the employee"""

    request_body: Annotated[
        PutV1EmployeesRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""Update an employee."""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
