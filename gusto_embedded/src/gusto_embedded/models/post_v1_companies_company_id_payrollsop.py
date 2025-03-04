"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from enum import Enum
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


class OffCycleReason(str, Enum):
    r"""An off cycle payroll reason. Select one from the following list."""

    BONUS = "Bonus"
    CORRECTION = "Correction"
    DISMISSED_EMPLOYEE = "Dismissed employee"
    TRANSITION_FROM_OLD_PAY_SCHEDULE = "Transition from old pay schedule"


class WithholdingPayPeriod(str, Enum):
    r"""The payment schedule tax rate the payroll is based on."""

    EVERY_WEEK = "Every week"
    EVERY_OTHER_WEEK = "Every other week"
    TWICE_PER_MONTH = "Twice per month"
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    SEMIANNUALLY = "Semiannually"
    ANNUALLY = "Annually"


class PostV1CompaniesCompanyIDPayrollsRequestBodyTypedDict(TypedDict):
    off_cycle: bool
    r"""Whether it is an off cycle payroll."""
    off_cycle_reason: OffCycleReason
    r"""An off cycle payroll reason. Select one from the following list."""
    start_date: str
    r"""Pay period start date."""
    end_date: str
    r"""Pay period end date."""
    pay_schedule_uuid: NotRequired[str]
    r"""A pay schedule is required for transition from old pay schedule payroll to identify the matching transition pay period."""
    employee_uuids: NotRequired[List[str]]
    r"""A list of employee uuids to include on the payroll."""
    check_date: NotRequired[str]
    r"""Payment date."""
    withholding_pay_period: NotRequired[WithholdingPayPeriod]
    r"""The payment schedule tax rate the payroll is based on."""
    skip_regular_deductions: NotRequired[bool]
    r"""Block regular deductions and contributions for this payroll."""
    fixed_withholding_rate: NotRequired[bool]
    r"""Enable taxes to be withheld at the IRS's required rate of 22% for federal income taxes. State income taxes will be taxed at the state's supplemental tax rate. Otherwise, we'll sum the entirety of the employee's wages and withhold taxes on the entire amount at the rate for regular wages."""


class PostV1CompaniesCompanyIDPayrollsRequestBody(BaseModel):
    off_cycle: bool
    r"""Whether it is an off cycle payroll."""

    off_cycle_reason: OffCycleReason
    r"""An off cycle payroll reason. Select one from the following list."""

    start_date: str
    r"""Pay period start date."""

    end_date: str
    r"""Pay period end date."""

    pay_schedule_uuid: Optional[str] = None
    r"""A pay schedule is required for transition from old pay schedule payroll to identify the matching transition pay period."""

    employee_uuids: Optional[List[str]] = None
    r"""A list of employee uuids to include on the payroll."""

    check_date: Optional[str] = None
    r"""Payment date."""

    withholding_pay_period: Optional[WithholdingPayPeriod] = None
    r"""The payment schedule tax rate the payroll is based on."""

    skip_regular_deductions: Optional[bool] = None
    r"""Block regular deductions and contributions for this payroll."""

    fixed_withholding_rate: Optional[bool] = None
    r"""Enable taxes to be withheld at the IRS's required rate of 22% for federal income taxes. State income taxes will be taxed at the state's supplemental tax rate. Otherwise, we'll sum the entirety of the employee's wages and withhold taxes on the entire amount at the rate for regular wages."""


class PostV1CompaniesCompanyIDPayrollsRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    request_body: PostV1CompaniesCompanyIDPayrollsRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1CompaniesCompanyIDPayrollsRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PostV1CompaniesCompanyIDPayrollsRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
