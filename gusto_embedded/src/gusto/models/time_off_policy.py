"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from gusto.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PolicyType(str, Enum):
    r"""Type of the time off policy"""

    VACATION = "vacation"
    SICK = "sick"


class TimeOffPolicyEmployeesTypedDict(TypedDict):
    uuid: NotRequired[str]


class TimeOffPolicyEmployees(BaseModel):
    uuid: Optional[str] = None


class TimeOffPolicyTypedDict(TypedDict):
    r"""Representation of a Time Off Policy"""

    uuid: str
    r"""Unique identifier of a time off policy"""
    company_uuid: str
    r"""Unique identifier for the company owning the time off policy"""
    name: str
    r"""Name of the time off policy"""
    policy_type: PolicyType
    r"""Type of the time off policy"""
    accrual_method: str
    r"""Policy time off accrual method"""
    is_active: bool
    r"""boolean representing if a policy is active or not"""
    employees: List[TimeOffPolicyEmployeesTypedDict]
    r"""List of employee UUIDs under a time off policy"""
    accrual_rate: NotRequired[str]
    r"""The rate at which the time off hours will accrue for an employee on the policy. Represented as a float, e.g. \"40.0\"."""
    accrual_rate_unit: NotRequired[str]
    r"""The number of hours an employee has to work or be paid for to accrue the number of hours set in the accrual rate. Only used for hourly policies (per_hour_paid, per_hour_paid_no_overtime, per_hour_work, per_hour_worked_no_overtime). Represented as a float, e.g. \"40.0\"."""
    paid_out_on_termination: NotRequired[bool]
    r"""Boolean representing if an employee's accrued time off hours will be paid out on termination"""
    accrual_waiting_period_days: NotRequired[int]
    r"""Number of days before an employee on the policy will begin accruing time off hours"""
    carryover_limit_hours: NotRequired[str]
    r"""The max number of hours an employee can carryover from one year to the next"""
    max_accrual_hours_per_year: NotRequired[str]
    r"""The max number of hours an employee can accrue in a year"""
    max_hours: NotRequired[str]
    r"""The max number of hours an employee can accrue"""
    complete: NotRequired[bool]
    r"""boolean representing if a policy has completed configuration"""
    version: NotRequired[str]
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""


class TimeOffPolicy(BaseModel):
    r"""Representation of a Time Off Policy"""

    uuid: str
    r"""Unique identifier of a time off policy"""

    company_uuid: str
    r"""Unique identifier for the company owning the time off policy"""

    name: str
    r"""Name of the time off policy"""

    policy_type: PolicyType
    r"""Type of the time off policy"""

    accrual_method: str
    r"""Policy time off accrual method"""

    is_active: bool
    r"""boolean representing if a policy is active or not"""

    employees: List[TimeOffPolicyEmployees]
    r"""List of employee UUIDs under a time off policy"""

    accrual_rate: Optional[str] = None
    r"""The rate at which the time off hours will accrue for an employee on the policy. Represented as a float, e.g. \"40.0\"."""

    accrual_rate_unit: Optional[str] = None
    r"""The number of hours an employee has to work or be paid for to accrue the number of hours set in the accrual rate. Only used for hourly policies (per_hour_paid, per_hour_paid_no_overtime, per_hour_work, per_hour_worked_no_overtime). Represented as a float, e.g. \"40.0\"."""

    paid_out_on_termination: Optional[bool] = None
    r"""Boolean representing if an employee's accrued time off hours will be paid out on termination"""

    accrual_waiting_period_days: Optional[int] = None
    r"""Number of days before an employee on the policy will begin accruing time off hours"""

    carryover_limit_hours: Optional[str] = None
    r"""The max number of hours an employee can carryover from one year to the next"""

    max_accrual_hours_per_year: Optional[str] = None
    r"""The max number of hours an employee can accrue in a year"""

    max_hours: Optional[str] = None
    r"""The max number of hours an employee can accrue"""

    complete: Optional[bool] = None
    r"""boolean representing if a policy has completed configuration"""

    version: Optional[str] = None
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""
