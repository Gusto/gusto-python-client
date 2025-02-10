"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from datetime import date
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


class PostV1EmployeesEmployeeIDWorkAddressesRequestBodyTypedDict(TypedDict):
    location_uuid: NotRequired[str]
    r"""Reference to a company location"""
    effective_date: NotRequired[date]
    r"""Date the employee began working at the company location"""


class PostV1EmployeesEmployeeIDWorkAddressesRequestBody(BaseModel):
    location_uuid: Optional[str] = None
    r"""Reference to a company location"""

    effective_date: Optional[date] = None
    r"""Date the employee began working at the company location"""


class PostV1EmployeesEmployeeIDWorkAddressesRequestTypedDict(TypedDict):
    employee_id: str
    r"""The UUID of the employee"""
    request_body: PostV1EmployeesEmployeeIDWorkAddressesRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1EmployeesEmployeeIDWorkAddressesRequest(BaseModel):
    employee_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the employee"""

    request_body: Annotated[
        PostV1EmployeesEmployeeIDWorkAddressesRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
