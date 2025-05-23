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


class PutV1CompaniesCompanyIDPayrollsPaymentMethod(str, Enum):
    r"""The employee's compensation payment method. Invalid values will be ignored."""

    DIRECT_DEPOSIT = "Direct Deposit"
    CHECK = "Check"


class PutV1CompaniesCompanyIDPayrollsFixedCompensationsTypedDict(TypedDict):
    r"""An array of fixed compensations for the employee. Fixed compensations include tips, bonuses, and one time reimbursements."""

    name: NotRequired[str]
    r"""The name of the compensation. This also serves as the unique, immutable identifier for this compensation."""
    amount: NotRequired[str]
    r"""The amount of the compensation for the pay period."""
    job_uuid: NotRequired[str]
    r"""The UUID of the job for the compensation."""


class PutV1CompaniesCompanyIDPayrollsFixedCompensations(BaseModel):
    r"""An array of fixed compensations for the employee. Fixed compensations include tips, bonuses, and one time reimbursements."""

    name: Optional[str] = None
    r"""The name of the compensation. This also serves as the unique, immutable identifier for this compensation."""

    amount: Optional[str] = None
    r"""The amount of the compensation for the pay period."""

    job_uuid: Optional[str] = None
    r"""The UUID of the job for the compensation."""


class PutV1CompaniesCompanyIDPayrollsHourlyCompensationsTypedDict(TypedDict):
    r"""An array of hourly compensations for the employee. Hourly compensations include regular, overtime, and double overtime hours."""

    name: NotRequired[str]
    r"""The name of the compensation. This also serves as the unique, immutable identifier for this compensation."""
    hours: NotRequired[str]
    r"""The number of hours to be compensated for this pay period."""
    job_uuid: NotRequired[str]
    r"""The UUIDs of the job for the compensation."""


class PutV1CompaniesCompanyIDPayrollsHourlyCompensations(BaseModel):
    r"""An array of hourly compensations for the employee. Hourly compensations include regular, overtime, and double overtime hours."""

    name: Optional[str] = None
    r"""The name of the compensation. This also serves as the unique, immutable identifier for this compensation."""

    hours: Optional[str] = None
    r"""The number of hours to be compensated for this pay period."""

    job_uuid: Optional[str] = None
    r"""The UUIDs of the job for the compensation."""


class PutV1CompaniesCompanyIDPayrollsPaidTimeOffTypedDict(TypedDict):
    name: NotRequired[str]
    r"""The name of the PTO. This also serves as the unique, immutable identifier for the PTO. Must pass in name or policy_uuid but not both."""
    hours: NotRequired[str]
    r"""The hours of this PTO taken during the pay period."""
    policy_uuid: NotRequired[str]
    r"""The uuid of the PTO policy. Must pass in name or policy_uuid but not both."""
    final_payout_unused_hours_input: NotRequired[str]
    r"""The outstanding hours paid upon termination. This field is only applicable for termination payrolls."""


class PutV1CompaniesCompanyIDPayrollsPaidTimeOff(BaseModel):
    name: Optional[str] = None
    r"""The name of the PTO. This also serves as the unique, immutable identifier for the PTO. Must pass in name or policy_uuid but not both."""

    hours: Optional[str] = None
    r"""The hours of this PTO taken during the pay period."""

    policy_uuid: Optional[str] = None
    r"""The uuid of the PTO policy. Must pass in name or policy_uuid but not both."""

    final_payout_unused_hours_input: Optional[str] = None
    r"""The outstanding hours paid upon termination. This field is only applicable for termination payrolls."""


class PutV1CompaniesCompanyIDPayrollsEmployeeCompensationsTypedDict(TypedDict):
    employee_uuid: NotRequired[str]
    r"""The UUID of the employee."""
    version: NotRequired[str]
    r"""The current version of this employee compensation from the prepared payroll. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""
    excluded: NotRequired[bool]
    r"""This employee will be excluded from payroll calculation and will not be paid for the payroll."""
    payment_method: NotRequired[PutV1CompaniesCompanyIDPayrollsPaymentMethod]
    r"""The employee's compensation payment method. Invalid values will be ignored."""
    memo: NotRequired[str]
    r"""Custom text that will be printed as a personal note to the employee on a paystub."""
    fixed_compensations: NotRequired[
        List[PutV1CompaniesCompanyIDPayrollsFixedCompensationsTypedDict]
    ]
    hourly_compensations: NotRequired[
        List[PutV1CompaniesCompanyIDPayrollsHourlyCompensationsTypedDict]
    ]
    paid_time_off: NotRequired[
        List[PutV1CompaniesCompanyIDPayrollsPaidTimeOffTypedDict]
    ]
    r"""An array of all paid time off the employee is eligible for this pay period. Each paid time off object can be the name or the specific policy_uuid."""


class PutV1CompaniesCompanyIDPayrollsEmployeeCompensations(BaseModel):
    employee_uuid: Optional[str] = None
    r"""The UUID of the employee."""

    version: Optional[str] = None
    r"""The current version of this employee compensation from the prepared payroll. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""

    excluded: Optional[bool] = None
    r"""This employee will be excluded from payroll calculation and will not be paid for the payroll."""

    payment_method: Optional[PutV1CompaniesCompanyIDPayrollsPaymentMethod] = None
    r"""The employee's compensation payment method. Invalid values will be ignored."""

    memo: Optional[str] = None
    r"""Custom text that will be printed as a personal note to the employee on a paystub."""

    fixed_compensations: Optional[
        List[PutV1CompaniesCompanyIDPayrollsFixedCompensations]
    ] = None

    hourly_compensations: Optional[
        List[PutV1CompaniesCompanyIDPayrollsHourlyCompensations]
    ] = None

    paid_time_off: Optional[List[PutV1CompaniesCompanyIDPayrollsPaidTimeOff]] = None
    r"""An array of all paid time off the employee is eligible for this pay period. Each paid time off object can be the name or the specific policy_uuid."""


class PutV1CompaniesCompanyIDPayrollsWithholdingPayPeriod(str, Enum):
    r"""The payment schedule tax rate the payroll is based on. Only relevant for off-cycle payrolls."""

    EVERY_WEEK = "Every week"
    EVERY_OTHER_WEEK = "Every other week"
    TWICE_PER_MONTH = "Twice per month"
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    SEMIANNUALLY = "Semiannually"
    ANNUALLY = "Annually"


class PutV1CompaniesCompanyIDPayrollsRequestBodyTypedDict(TypedDict):
    employee_compensations: List[
        PutV1CompaniesCompanyIDPayrollsEmployeeCompensationsTypedDict
    ]
    withholding_pay_period: NotRequired[
        PutV1CompaniesCompanyIDPayrollsWithholdingPayPeriod
    ]
    r"""The payment schedule tax rate the payroll is based on. Only relevant for off-cycle payrolls."""
    skip_regular_deductions: NotRequired[bool]
    r"""Block regular deductions and contributions for this payroll. Only relevant for off-cycle payrolls."""
    fixed_withholding_rate: NotRequired[bool]
    r"""Enable taxes to be withheld at the IRS's required rate of 22% for federal income taxes. State income taxes will be taxed at the state's supplemental tax rate. Otherwise, we'll sum the entirety of the employee's wages and withhold taxes on the entire amount at the rate for regular wages. Only relevant for off-cycle payrolls."""


class PutV1CompaniesCompanyIDPayrollsRequestBody(BaseModel):
    employee_compensations: List[PutV1CompaniesCompanyIDPayrollsEmployeeCompensations]

    withholding_pay_period: Optional[
        PutV1CompaniesCompanyIDPayrollsWithholdingPayPeriod
    ] = None
    r"""The payment schedule tax rate the payroll is based on. Only relevant for off-cycle payrolls."""

    skip_regular_deductions: Optional[bool] = None
    r"""Block regular deductions and contributions for this payroll. Only relevant for off-cycle payrolls."""

    fixed_withholding_rate: Optional[bool] = None
    r"""Enable taxes to be withheld at the IRS's required rate of 22% for federal income taxes. State income taxes will be taxed at the state's supplemental tax rate. Otherwise, we'll sum the entirety of the employee's wages and withhold taxes on the entire amount at the rate for regular wages. Only relevant for off-cycle payrolls."""


class PutV1CompaniesCompanyIDPayrollsRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    payroll_id: str
    r"""The UUID of the payroll"""
    request_body: PutV1CompaniesCompanyIDPayrollsRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1CompaniesCompanyIDPayrollsRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    payroll_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the payroll"""

    request_body: Annotated[
        PutV1CompaniesCompanyIDPayrollsRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
