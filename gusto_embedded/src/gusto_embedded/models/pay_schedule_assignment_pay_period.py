"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto_embedded.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PayScheduleAssignmentPayPeriodTypedDict(TypedDict):
    r"""Pay schedule assignment first pay period information."""

    pay_schedule_uuid: NotRequired[str]
    r"""The pay schedule UUID."""
    start_date: NotRequired[str]
    r"""Pay period start date."""
    end_date: NotRequired[str]
    r"""Pay period end date."""
    check_date: NotRequired[str]
    r"""Pay period check date."""


class PayScheduleAssignmentPayPeriod(BaseModel):
    r"""Pay schedule assignment first pay period information."""

    pay_schedule_uuid: Optional[str] = None
    r"""The pay schedule UUID."""

    start_date: Optional[str] = None
    r"""Pay period start date."""

    end_date: Optional[str] = None
    r"""Pay period end date."""

    check_date: Optional[str] = None
    r"""Pay period check date."""
