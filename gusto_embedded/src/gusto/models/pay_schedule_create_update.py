"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pay_schedule_frequency_create_update import PayScheduleFrequencyCreateUpdate
from gusto.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PayScheduleCreateUpdateTypedDict(TypedDict):
    r"""The representation of a pay schedule."""

    uuid: str
    r"""The unique identifier of the pay schedule in Gusto."""
    frequency: NotRequired[PayScheduleFrequencyCreateUpdate]
    r"""The frequency that employees on this pay schedule are paid with Gusto."""
    anchor_pay_date: NotRequired[str]
    r"""The first date that employees on this pay schedule are paid with Gusto."""
    anchor_end_of_pay_period: NotRequired[str]
    r"""The last date of the first pay period. This can be the same date as the anchor pay date."""
    day_1: NotRequired[Nullable[int]]
    r"""An integer between 1 and 31 indicating the first day of the month that employees are paid. This field is only relevant for pay schedules with the “Twice per month” and “Monthly” frequencies. It will be null for pay schedules with other frequencies."""
    day_2: NotRequired[Nullable[int]]
    r"""An integer between 1 and 31 indicating the second day of the month that employees are paid. This field is the second pay date for pay schedules with the \"Twice per month\" frequency. For semi-monthly pay schedules, this field should be set to 31. For months shorter than 31 days, we will set the second pay date to the last day of the month. It will be null for pay schedules with other frequencies."""
    name: NotRequired[Nullable[str]]
    r"""This field will be hourly when the pay schedule is for hourly employees, salaried when the pay schedule is for salaried employees, the department name if pay schedule is by department, and null when the pay schedule is for all employees."""
    custom_name: NotRequired[str]
    r"""A custom name for a pay schedule, defaults to the pay frequency description."""
    auto_pilot: NotRequired[bool]
    r"""With Autopilot® enabled, payroll will run automatically one day before your payroll deadlines."""
    active: NotRequired[bool]
    r"""Whether this pay schedule is associated with any employees. A pay schedule is inactive when it's unassigned."""


class PayScheduleCreateUpdate(BaseModel):
    r"""The representation of a pay schedule."""

    uuid: str
    r"""The unique identifier of the pay schedule in Gusto."""

    frequency: Optional[PayScheduleFrequencyCreateUpdate] = None
    r"""The frequency that employees on this pay schedule are paid with Gusto."""

    anchor_pay_date: Optional[str] = None
    r"""The first date that employees on this pay schedule are paid with Gusto."""

    anchor_end_of_pay_period: Optional[str] = None
    r"""The last date of the first pay period. This can be the same date as the anchor pay date."""

    day_1: OptionalNullable[int] = UNSET
    r"""An integer between 1 and 31 indicating the first day of the month that employees are paid. This field is only relevant for pay schedules with the “Twice per month” and “Monthly” frequencies. It will be null for pay schedules with other frequencies."""

    day_2: OptionalNullable[int] = UNSET
    r"""An integer between 1 and 31 indicating the second day of the month that employees are paid. This field is the second pay date for pay schedules with the \"Twice per month\" frequency. For semi-monthly pay schedules, this field should be set to 31. For months shorter than 31 days, we will set the second pay date to the last day of the month. It will be null for pay schedules with other frequencies."""

    name: OptionalNullable[str] = UNSET
    r"""This field will be hourly when the pay schedule is for hourly employees, salaried when the pay schedule is for salaried employees, the department name if pay schedule is by department, and null when the pay schedule is for all employees."""

    custom_name: Optional[str] = None
    r"""A custom name for a pay schedule, defaults to the pay frequency description."""

    auto_pilot: Optional[bool] = None
    r"""With Autopilot® enabled, payroll will run automatically one day before your payroll deadlines."""

    active: Optional[bool] = None
    r"""Whether this pay schedule is associated with any employees. A pay schedule is inactive when it's unassigned."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "frequency",
            "anchor_pay_date",
            "anchor_end_of_pay_period",
            "day_1",
            "day_2",
            "name",
            "custom_name",
            "auto_pilot",
            "active",
        ]
        nullable_fields = ["day_1", "day_2", "name"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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
