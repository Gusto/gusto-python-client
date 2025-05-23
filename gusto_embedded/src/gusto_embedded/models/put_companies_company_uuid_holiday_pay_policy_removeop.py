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


class PutCompaniesCompanyUUIDHolidayPayPolicyRemoveEmployeesTypedDict(TypedDict):
    uuid: NotRequired[str]


class PutCompaniesCompanyUUIDHolidayPayPolicyRemoveEmployees(BaseModel):
    uuid: Optional[str] = None


class PutCompaniesCompanyUUIDHolidayPayPolicyRemoveRequestBodyTypedDict(TypedDict):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""
    employees: NotRequired[
        List[PutCompaniesCompanyUUIDHolidayPayPolicyRemoveEmployeesTypedDict]
    ]
    r"""An array of employee objects, each containing an employee_uuid."""


class PutCompaniesCompanyUUIDHolidayPayPolicyRemoveRequestBody(BaseModel):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""

    employees: Optional[
        List[PutCompaniesCompanyUUIDHolidayPayPolicyRemoveEmployees]
    ] = None
    r"""An array of employee objects, each containing an employee_uuid."""


class PutCompaniesCompanyUUIDHolidayPayPolicyRemoveRequestTypedDict(TypedDict):
    company_uuid: str
    r"""The UUID of the company"""
    request_body: PutCompaniesCompanyUUIDHolidayPayPolicyRemoveRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutCompaniesCompanyUUIDHolidayPayPolicyRemoveRequest(BaseModel):
    company_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PutCompaniesCompanyUUIDHolidayPayPolicyRemoveRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
