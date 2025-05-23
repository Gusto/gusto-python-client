"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto_embedded.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PayrollReversalTypedDict(TypedDict):
    r"""Example response"""

    reversed_payroll_uuid: NotRequired[str]
    r"""The UUID for the payroll run being reversed."""
    reversal_payroll_uuid: NotRequired[str]
    r"""The UUID of the payroll where the reversal was applied."""
    reason: NotRequired[str]
    r"""A reason provided by the admin who created the reversal."""
    approved_at: NotRequired[Nullable[str]]
    r"""Timestamp of when the reversal was approved."""
    category: NotRequired[str]
    r"""Category chosen by the admin who requested the reversal."""
    reversed_employee_uuids: NotRequired[List[str]]
    r"""Array of affected employee UUIDs."""


class PayrollReversal(BaseModel):
    r"""Example response"""

    reversed_payroll_uuid: Optional[str] = None
    r"""The UUID for the payroll run being reversed."""

    reversal_payroll_uuid: Optional[str] = None
    r"""The UUID of the payroll where the reversal was applied."""

    reason: Optional[str] = None
    r"""A reason provided by the admin who created the reversal."""

    approved_at: OptionalNullable[str] = UNSET
    r"""Timestamp of when the reversal was approved."""

    category: Optional[str] = None
    r"""Category chosen by the admin who requested the reversal."""

    reversed_employee_uuids: Optional[List[str]] = None
    r"""Array of affected employee UUIDs."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "reversed_payroll_uuid",
            "reversal_payroll_uuid",
            "reason",
            "approved_at",
            "category",
            "reversed_employee_uuids",
        ]
        nullable_fields = ["approved_at"]
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
