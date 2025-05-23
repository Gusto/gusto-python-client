"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .compensation import Compensation, CompensationTypedDict
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


class JobTypedDict(TypedDict):
    r"""The representation of a job in Gusto."""

    uuid: str
    r"""The UUID of the job."""
    version: NotRequired[str]
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""
    employee_uuid: NotRequired[str]
    r"""The UUID of the employee to which the job belongs."""
    hire_date: NotRequired[str]
    r"""The date when the employee was hired or rehired for the job."""
    title: NotRequired[Nullable[str]]
    r"""The title for the job."""
    primary: NotRequired[bool]
    r"""Whether this is the employee's primary job. The value will be set to true unless an existing job exists for the employee."""
    rate: NotRequired[str]
    r"""The current compensation rate of the job."""
    payment_unit: NotRequired[Nullable[str]]
    r"""The payment unit of the current compensation for the job."""
    current_compensation_uuid: NotRequired[str]
    r"""The UUID of the current compensation of the job."""
    two_percent_shareholder: NotRequired[bool]
    r"""Whether the employee owns at least 2% of the company."""
    state_wc_covered: NotRequired[Nullable[bool]]
    r"""Whether this job is eligible for workers' compensation coverage in the state of Washington (WA)."""
    state_wc_class_code: NotRequired[Nullable[str]]
    r"""The risk class code for workers' compensation in Washington state. Please visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more."""
    compensations: NotRequired[List[CompensationTypedDict]]


class Job(BaseModel):
    r"""The representation of a job in Gusto."""

    uuid: str
    r"""The UUID of the job."""

    version: Optional[str] = None
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""

    employee_uuid: Optional[str] = None
    r"""The UUID of the employee to which the job belongs."""

    hire_date: Optional[str] = None
    r"""The date when the employee was hired or rehired for the job."""

    title: OptionalNullable[str] = None
    r"""The title for the job."""

    primary: Optional[bool] = None
    r"""Whether this is the employee's primary job. The value will be set to true unless an existing job exists for the employee."""

    rate: Optional[str] = None
    r"""The current compensation rate of the job."""

    payment_unit: OptionalNullable[str] = UNSET
    r"""The payment unit of the current compensation for the job."""

    current_compensation_uuid: Optional[str] = None
    r"""The UUID of the current compensation of the job."""

    two_percent_shareholder: Optional[bool] = None
    r"""Whether the employee owns at least 2% of the company."""

    state_wc_covered: OptionalNullable[bool] = UNSET
    r"""Whether this job is eligible for workers' compensation coverage in the state of Washington (WA)."""

    state_wc_class_code: OptionalNullable[str] = UNSET
    r"""The risk class code for workers' compensation in Washington state. Please visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more."""

    compensations: Optional[List[Compensation]] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "version",
            "employee_uuid",
            "hire_date",
            "title",
            "primary",
            "rate",
            "payment_unit",
            "current_compensation_uuid",
            "two_percent_shareholder",
            "state_wc_covered",
            "state_wc_class_code",
            "compensations",
        ]
        nullable_fields = [
            "title",
            "payment_unit",
            "state_wc_covered",
            "state_wc_class_code",
        ]
        null_default_fields = ["title"]

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
