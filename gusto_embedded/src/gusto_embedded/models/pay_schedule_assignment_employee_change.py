"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pay_schedule_assignment_pay_period import (
    PayScheduleAssignmentPayPeriod,
    PayScheduleAssignmentPayPeriodTypedDict,
)
from .pay_schedule_assignment_transition_pay_period import (
    PayScheduleAssignmentTransitionPayPeriod,
    PayScheduleAssignmentTransitionPayPeriodTypedDict,
)
from gusto_embedded.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PayScheduleAssignmentEmployeeChangeTypedDict(TypedDict):
    employee_uuid: NotRequired[str]
    r"""The UUID of the employee."""
    first_name: NotRequired[str]
    r"""The employee's first name."""
    last_name: NotRequired[str]
    r"""The employee's last name."""
    pay_frequency: NotRequired[str]
    r"""New pay schedule frequency and name."""
    first_pay_period: NotRequired[PayScheduleAssignmentPayPeriodTypedDict]
    r"""Pay schedule assignment first pay period information."""
    transition_pay_period: NotRequired[
        PayScheduleAssignmentTransitionPayPeriodTypedDict
    ]
    r"""Pay schedule assignment transition pay period information."""


class PayScheduleAssignmentEmployeeChange(BaseModel):
    employee_uuid: Optional[str] = None
    r"""The UUID of the employee."""

    first_name: Optional[str] = None
    r"""The employee's first name."""

    last_name: Optional[str] = None
    r"""The employee's last name."""

    pay_frequency: Optional[str] = None
    r"""New pay schedule frequency and name."""

    first_pay_period: Optional[PayScheduleAssignmentPayPeriod] = None
    r"""Pay schedule assignment first pay period information."""

    transition_pay_period: Optional[PayScheduleAssignmentTransitionPayPeriod] = None
    r"""Pay schedule assignment transition pay period information."""
