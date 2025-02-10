"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from enum import Enum
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


class PutV1EmployeesEmployeeIDBankAccountsAccountType(str, Enum):
    CHECKING = "Checking"
    SAVINGS = "Savings"


class PutV1EmployeesEmployeeIDBankAccountsRequestBodyTypedDict(TypedDict):
    name: str
    routing_number: str
    account_number: str
    account_type: PutV1EmployeesEmployeeIDBankAccountsAccountType


class PutV1EmployeesEmployeeIDBankAccountsRequestBody(BaseModel):
    name: str

    routing_number: str

    account_number: str

    account_type: PutV1EmployeesEmployeeIDBankAccountsAccountType


class PutV1EmployeesEmployeeIDBankAccountsRequestTypedDict(TypedDict):
    employee_id: str
    r"""The UUID of the employee"""
    bank_account_uuid: str
    r"""The UUID of the bank account"""
    request_body: PutV1EmployeesEmployeeIDBankAccountsRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1EmployeesEmployeeIDBankAccountsRequest(BaseModel):
    employee_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the employee"""

    bank_account_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the bank account"""

    request_body: Annotated[
        PutV1EmployeesEmployeeIDBankAccountsRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
