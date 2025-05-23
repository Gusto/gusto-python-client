"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from gusto_app_integration.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PaymentPeriod(str, Enum):
    r"""How often the agency collects the withholding amount. e.g. $500 monthly -> `Monthly`."""

    EVERY_WEEK = "Every week"
    EVERY_OTHER_WEEK = "Every other week"
    TWICE_PER_MONTH = "Twice per month"
    MONTHLY = "Monthly"


class GarnishmentChildSupportTypedDict(TypedDict):
    r"""Additional child support order details"""

    state: NotRequired[str]
    r"""The two letter state abbreviation for the state issuing the child support order. Agency data is available in the `GET /v1/garnishments/child_support` API."""
    payment_period: NotRequired[PaymentPeriod]
    r"""How often the agency collects the withholding amount. e.g. $500 monthly -> `Monthly`."""
    fips_code: NotRequired[str]
    r"""The FIPS code associated with the state or county agency issuing the child support order. Agency data is available in the `GET /v1/garnishments/child_support` API."""
    case_number: NotRequired[Nullable[str]]
    r"""Child Support Enforcement Case Number associated with this child support obligation - required for most states. Agency specific requirements are available in the `GET /v1/garnishments/child_support` API."""
    order_number: NotRequired[Nullable[str]]
    r"""Order Identifier or Order ID associated with this child support obligation - required for some states. Agency specific requirements are available in the `GET /v1/garnishments/child_support` API."""
    remittance_number: NotRequired[Nullable[str]]
    r"""Child Support Enforcement Remittance ID associated with this child support obligation - required for some states. Agency specific requirements are available in the `GET /v1/garnishments/child_support` API."""


class GarnishmentChildSupport(BaseModel):
    r"""Additional child support order details"""

    state: Optional[str] = None
    r"""The two letter state abbreviation for the state issuing the child support order. Agency data is available in the `GET /v1/garnishments/child_support` API."""

    payment_period: Optional[PaymentPeriod] = None
    r"""How often the agency collects the withholding amount. e.g. $500 monthly -> `Monthly`."""

    fips_code: Optional[str] = None
    r"""The FIPS code associated with the state or county agency issuing the child support order. Agency data is available in the `GET /v1/garnishments/child_support` API."""

    case_number: OptionalNullable[str] = UNSET
    r"""Child Support Enforcement Case Number associated with this child support obligation - required for most states. Agency specific requirements are available in the `GET /v1/garnishments/child_support` API."""

    order_number: OptionalNullable[str] = UNSET
    r"""Order Identifier or Order ID associated with this child support obligation - required for some states. Agency specific requirements are available in the `GET /v1/garnishments/child_support` API."""

    remittance_number: OptionalNullable[str] = UNSET
    r"""Child Support Enforcement Remittance ID associated with this child support obligation - required for some states. Agency specific requirements are available in the `GET /v1/garnishments/child_support` API."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "state",
            "payment_period",
            "fips_code",
            "case_number",
            "order_number",
            "remittance_number",
        ]
        nullable_fields = ["case_number", "order_number", "remittance_number"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
