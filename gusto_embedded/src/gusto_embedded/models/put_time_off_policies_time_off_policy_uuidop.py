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
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccrualMethod(str, Enum):
    r"""Accrual method of the time off policy"""

    UNLIMITED = "unlimited"
    PER_PAY_PERIOD = "per_pay_period"
    PER_CALENDAR_YEAR = "per_calendar_year"
    PER_ANNIVERSARY_YEAR = "per_anniversary_year"
    PER_HOUR_WORKED = "per_hour_worked"
    PER_HOUR_WORKED_NO_OVERTIME = "per_hour_worked_no_overtime"
    PER_HOUR_PAID = "per_hour_paid"
    PER_HOUR_PAID_NO_OVERTIME = "per_hour_paid_no_overtime"


class PutTimeOffPoliciesTimeOffPolicyUUIDRequestBodyTypedDict(TypedDict):
    r"""Can update any attributes of the time off policy except policy_type, is_active, complete & employees"""

    name: NotRequired[str]
    r"""Name of the time off policy"""
    accrual_method: NotRequired[AccrualMethod]
    r"""Accrual method of the time off policy"""
    accrual_rate: NotRequired[str]
    r"""The rate at which the time off hours will accrue for an employee on the policy. Represented as a float, e.g. \"40.0\"."""
    accrual_rate_unit: NotRequired[str]
    r"""The number of hours an employee has to work or be paid for to accrue the number of hours set in the accrual rate. Only used for hourly policies (per_hour_paid, per_hour_paid_no_overtime, per_hour_work, per_hour_worked_no_overtime). Represented as a float, e.g. \"40.0\"."""
    paid_out_on_termination: NotRequired[bool]
    r"""Boolean representing if an employee's accrued time off hours will be paid out on termination"""
    accrual_waiting_period_days: NotRequired[int]
    r"""Number of days before an employee on the policy will begin accruing time off hours. If accrual_method is per_anniversary_year, per_calendar_year, or unlimited, then accrual_waiting_period_days should be 0."""
    carryover_limit_hours: NotRequired[str]
    r"""The max number of hours an employee can carryover from one year to the next. If accrual_method is unlimited, then carryover_limit_hours must be blank."""
    max_accrual_hours_per_year: NotRequired[str]
    r"""The max number of hours an employee can accrue in a year. If accrual_method is unlimited, then max_accrual_hours_per_year must be blank."""
    max_hours: NotRequired[str]
    r"""The max number of hours an employee can accrue. If accrual_method is unlimited, then max_hours must be blank."""


class PutTimeOffPoliciesTimeOffPolicyUUIDRequestBody(BaseModel):
    r"""Can update any attributes of the time off policy except policy_type, is_active, complete & employees"""

    name: Optional[str] = None
    r"""Name of the time off policy"""

    accrual_method: Optional[AccrualMethod] = None
    r"""Accrual method of the time off policy"""

    accrual_rate: Optional[str] = None
    r"""The rate at which the time off hours will accrue for an employee on the policy. Represented as a float, e.g. \"40.0\"."""

    accrual_rate_unit: Optional[str] = None
    r"""The number of hours an employee has to work or be paid for to accrue the number of hours set in the accrual rate. Only used for hourly policies (per_hour_paid, per_hour_paid_no_overtime, per_hour_work, per_hour_worked_no_overtime). Represented as a float, e.g. \"40.0\"."""

    paid_out_on_termination: Optional[bool] = None
    r"""Boolean representing if an employee's accrued time off hours will be paid out on termination"""

    accrual_waiting_period_days: Optional[int] = None
    r"""Number of days before an employee on the policy will begin accruing time off hours. If accrual_method is per_anniversary_year, per_calendar_year, or unlimited, then accrual_waiting_period_days should be 0."""

    carryover_limit_hours: Optional[str] = None
    r"""The max number of hours an employee can carryover from one year to the next. If accrual_method is unlimited, then carryover_limit_hours must be blank."""

    max_accrual_hours_per_year: Optional[str] = None
    r"""The max number of hours an employee can accrue in a year. If accrual_method is unlimited, then max_accrual_hours_per_year must be blank."""

    max_hours: Optional[str] = None
    r"""The max number of hours an employee can accrue. If accrual_method is unlimited, then max_hours must be blank."""


class PutTimeOffPoliciesTimeOffPolicyUUIDRequestTypedDict(TypedDict):
    time_off_policy_uuid: str
    r"""The UUID of the company time off policy"""
    request_body: PutTimeOffPoliciesTimeOffPolicyUUIDRequestBodyTypedDict
    r"""Can update any attributes of the time off policy except policy_type, is_active, complete & employees"""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutTimeOffPoliciesTimeOffPolicyUUIDRequest(BaseModel):
    time_off_policy_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company time off policy"""

    request_body: Annotated[
        PutTimeOffPoliciesTimeOffPolicyUUIDRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""Can update any attributes of the time off policy except policy_type, is_active, complete & employees"""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
