"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pay_schedule_assignment_employee_change import (
    PayScheduleAssignmentEmployeeChange,
    PayScheduleAssignmentEmployeeChangeTypedDict,
)
from enum import Enum
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


class PayScheduleAssignmentPreviewType(str, Enum):
    r"""The pay schedule assignment type."""

    SINGLE = "single"
    HOURLY_SALARIED = "hourly_salaried"
    BY_EMPLOYEE = "by_employee"
    BY_DEPARTMENT = "by_department"


class PayScheduleAssignmentPreviewTypedDict(TypedDict):
    r"""The representation of a pay schedule assignment preview."""

    type: NotRequired[Nullable[PayScheduleAssignmentPreviewType]]
    r"""The pay schedule assignment type."""
    employee_changes: NotRequired[List[PayScheduleAssignmentEmployeeChangeTypedDict]]
    r"""A list of pay schedule changes including pay period and transition pay period."""


class PayScheduleAssignmentPreview(BaseModel):
    r"""The representation of a pay schedule assignment preview."""

    type: OptionalNullable[PayScheduleAssignmentPreviewType] = UNSET
    r"""The pay schedule assignment type."""

    employee_changes: Optional[List[PayScheduleAssignmentEmployeeChange]] = None
    r"""A list of pay schedule changes including pay period and transition pay period."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["type", "employee_changes"]
        nullable_fields = ["type"]
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
