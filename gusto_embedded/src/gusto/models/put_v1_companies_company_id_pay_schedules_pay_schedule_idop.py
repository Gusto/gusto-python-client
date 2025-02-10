"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from enum import Enum
from gusto.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from gusto.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PutV1CompaniesCompanyIDPaySchedulesPayScheduleIDFrequency(str, Enum):
    r"""The frequency that employees on this pay schedule are paid with Gusto."""

    EVERY_WEEK = "Every week"
    EVERY_OTHER_WEEK = "Every other week"
    TWICE_PER_MONTH = "Twice per month"
    MONTHLY = "Monthly"


class PutV1CompaniesCompanyIDPaySchedulesPayScheduleIDRequestBodyTypedDict(TypedDict):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""
    frequency: NotRequired[PutV1CompaniesCompanyIDPaySchedulesPayScheduleIDFrequency]
    r"""The frequency that employees on this pay schedule are paid with Gusto."""
    anchor_pay_date: NotRequired[str]
    r"""The first date that employees on this pay schedule are paid with Gusto."""
    anchor_end_of_pay_period: NotRequired[str]
    r"""The last date of the first pay period. This can be the same date as the anchor pay date."""
    day_1: NotRequired[Nullable[int]]
    r"""An integer between 1 and 31 indicating the first day of the month that employees are paid. This field is only relevant for pay schedules with the “Twice per month” and “Monthly” frequencies. It will be null for pay schedules with other frequencies."""
    day_2: NotRequired[Nullable[int]]
    r"""An integer between 1 and 31 indicating the second day of the month that employees are paid. This field is the second pay date for pay schedules with the \"Twice per month\" frequency. For semi-monthly pay schedules, set this field to 31. For months shorter than 31 days, we will set the second pay date to the last day of the month. It will be null for pay schedules with other frequencies."""
    custom_name: NotRequired[str]
    r"""A custom pay schedule name."""
    auto_pilot: NotRequired[bool]
    r"""With Autopilot® enabled, payroll will run automatically one day before your payroll deadlines."""


class PutV1CompaniesCompanyIDPaySchedulesPayScheduleIDRequestBody(BaseModel):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""

    frequency: Optional[PutV1CompaniesCompanyIDPaySchedulesPayScheduleIDFrequency] = (
        None
    )
    r"""The frequency that employees on this pay schedule are paid with Gusto."""

    anchor_pay_date: Optional[str] = None
    r"""The first date that employees on this pay schedule are paid with Gusto."""

    anchor_end_of_pay_period: Optional[str] = None
    r"""The last date of the first pay period. This can be the same date as the anchor pay date."""

    day_1: OptionalNullable[int] = UNSET
    r"""An integer between 1 and 31 indicating the first day of the month that employees are paid. This field is only relevant for pay schedules with the “Twice per month” and “Monthly” frequencies. It will be null for pay schedules with other frequencies."""

    day_2: OptionalNullable[int] = UNSET
    r"""An integer between 1 and 31 indicating the second day of the month that employees are paid. This field is the second pay date for pay schedules with the \"Twice per month\" frequency. For semi-monthly pay schedules, set this field to 31. For months shorter than 31 days, we will set the second pay date to the last day of the month. It will be null for pay schedules with other frequencies."""

    custom_name: Optional[str] = None
    r"""A custom pay schedule name."""

    auto_pilot: Optional[bool] = None
    r"""With Autopilot® enabled, payroll will run automatically one day before your payroll deadlines."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "frequency",
            "anchor_pay_date",
            "anchor_end_of_pay_period",
            "day_1",
            "day_2",
            "custom_name",
            "auto_pilot",
        ]
        nullable_fields = ["day_1", "day_2"]
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


class PutV1CompaniesCompanyIDPaySchedulesPayScheduleIDRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    pay_schedule_id: str
    r"""The UUID of the pay schedule"""
    request_body: PutV1CompaniesCompanyIDPaySchedulesPayScheduleIDRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1CompaniesCompanyIDPaySchedulesPayScheduleIDRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    pay_schedule_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the pay schedule"""

    request_body: Annotated[
        PutV1CompaniesCompanyIDPaySchedulesPayScheduleIDRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
