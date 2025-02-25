"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto_app_integration.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PayrollPaymentSpeedChangedTypeTypedDict(TypedDict):
    r"""Only applicable when a payroll is moved to four day processing instead of fast ach."""

    original_check_date: NotRequired[str]
    r"""Original check date when fast ach applies."""
    current_check_date: NotRequired[str]
    r"""Current check date."""
    original_debit_date: NotRequired[str]
    r"""Original debit date when fast ach applies."""
    current_debit_date: NotRequired[str]
    r"""Current debit date."""
    reason: NotRequired[str]
    r"""The reason why the payroll is moved to four day."""


class PayrollPaymentSpeedChangedType(BaseModel):
    r"""Only applicable when a payroll is moved to four day processing instead of fast ach."""

    original_check_date: Optional[str] = None
    r"""Original check date when fast ach applies."""

    current_check_date: Optional[str] = None
    r"""Current check date."""

    original_debit_date: Optional[str] = None
    r"""Original debit date when fast ach applies."""

    current_debit_date: Optional[str] = None
    r"""Current debit date."""

    reason: Optional[str] = None
    r"""The reason why the payroll is moved to four day."""
