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


class PutCompaniesCompanyUUIDHolidayPayPolicyAddEmployeesTypedDict(TypedDict):
    uuid: NotRequired[str]


class PutCompaniesCompanyUUIDHolidayPayPolicyAddEmployees(BaseModel):
    uuid: Optional[str] = None


class PutCompaniesCompanyUUIDHolidayPayPolicyAddRequestBodyTypedDict(TypedDict):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""
    employees: NotRequired[
        List[PutCompaniesCompanyUUIDHolidayPayPolicyAddEmployeesTypedDict]
    ]
    r"""An array of employee objects, each containing an employee_uuid."""


class PutCompaniesCompanyUUIDHolidayPayPolicyAddRequestBody(BaseModel):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""

    employees: Optional[List[PutCompaniesCompanyUUIDHolidayPayPolicyAddEmployees]] = (
        None
    )
    r"""An array of employee objects, each containing an employee_uuid."""


class PutCompaniesCompanyUUIDHolidayPayPolicyAddRequestTypedDict(TypedDict):
    company_uuid: str
    r"""The UUID of the company"""
    request_body: PutCompaniesCompanyUUIDHolidayPayPolicyAddRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutCompaniesCompanyUUIDHolidayPayPolicyAddRequest(BaseModel):
    company_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PutCompaniesCompanyUUIDHolidayPayPolicyAddRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
