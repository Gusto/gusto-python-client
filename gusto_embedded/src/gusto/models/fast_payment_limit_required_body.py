"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .payment_speed_param import PaymentSpeedParam
from gusto.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class FastPaymentLimitRequiredBodyTypedDict(TypedDict):
    fast_payment_limit: str
    r"""Fast payment limit. This limit is an aggregate of all fast payrolls amount. This limit is only relevant when payment speed is 1-day or 2-day."""
    payment_speed: NotRequired[PaymentSpeedParam]
    r"""Gusto Embedded supports three payment speeds (1-day, 2-day, and 4-day). For next-day payments, funds are deposited in your team's bank account by the end of the next business day. Most people will see the funds arrive the next afternoon, but payments may arrive as late as the end of the business day."""


class FastPaymentLimitRequiredBody(BaseModel):
    fast_payment_limit: str
    r"""Fast payment limit. This limit is an aggregate of all fast payrolls amount. This limit is only relevant when payment speed is 1-day or 2-day."""

    payment_speed: Optional[PaymentSpeedParam] = None
    r"""Gusto Embedded supports three payment speeds (1-day, 2-day, and 4-day). For next-day payments, funds are deposited in your team's bank account by the end of the next business day. Most people will see the funds arrive the next afternoon, but payments may arrive as late as the end of the business day."""
