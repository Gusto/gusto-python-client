"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .employee_custom_field import EmployeeCustomField, EmployeeCustomFieldTypedDict
from .garnishment import Garnishment, GarnishmentTypedDict
from .job import Job, JobTypedDict
from .paid_time_off import PaidTimeOff, PaidTimeOffTypedDict
from .termination import Termination, TerminationTypedDict
from enum import Enum
from gusto_app_integration.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class OnboardingStatus(str, Enum):
    r"""The current onboarding status of the employee"""

    ONBOARDING_COMPLETED = "onboarding_completed"
    ADMIN_ONBOARDING_INCOMPLETE = "admin_onboarding_incomplete"
    SELF_ONBOARDING_PENDING_INVITE = "self_onboarding_pending_invite"
    SELF_ONBOARDING_INVITED = "self_onboarding_invited"
    SELF_ONBOARDING_INVITED_STARTED = "self_onboarding_invited_started"
    SELF_ONBOARDING_INVITED_OVERDUE = "self_onboarding_invited_overdue"
    SELF_ONBOARDING_COMPLETED_BY_EMPLOYEE = "self_onboarding_completed_by_employee"
    SELF_ONBOARDING_AWAITING_ADMIN_REVIEW = "self_onboarding_awaiting_admin_review"


class OnboardingDocumentsConfigTypedDict(TypedDict):
    r"""Configuration for an employee onboarding documents during onboarding"""

    uuid: NotRequired[Nullable[str]]
    r"""The UUID of the onboarding documents config"""
    i9_document: NotRequired[bool]
    r"""Whether to include Form I-9 for an employee during onboarding"""


class OnboardingDocumentsConfig(BaseModel):
    r"""Configuration for an employee onboarding documents during onboarding"""

    uuid: OptionalNullable[str] = UNSET
    r"""The UUID of the onboarding documents config"""

    i9_document: Optional[bool] = None
    r"""Whether to include Form I-9 for an employee during onboarding"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["uuid", "i9_document"]
        nullable_fields = ["uuid"]
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


class PaymentMethod(str, Enum):
    r"""The employee's payment method"""

    DIRECT_DEPOSIT = "Direct Deposit"
    CHECK = "Check"


class CurrentEmploymentStatus(str, Enum):
    r"""The current employment status of the employee. Full-time employees work 30+ hours per week. Part-time employees are split into two groups: those that work 20-29 hours a week, and those that work under 20 hours a week. Variable employees have hours that vary each week. Seasonal employees are hired for 6 months of the year or less."""

    FULL_TIME = "full_time"
    PART_TIME_UNDER_TWENTY_HOURS = "part_time_under_twenty_hours"
    PART_TIME_TWENTY_PLUS_HOURS = "part_time_twenty_plus_hours"
    VARIABLE = "variable"
    SEASONAL = "seasonal"


class EmployeeTypedDict(TypedDict):
    r"""The representation of an employee in Gusto."""

    uuid: str
    r"""The UUID of the employee in Gusto."""
    first_name: str
    last_name: str
    middle_initial: NotRequired[Nullable[str]]
    email: NotRequired[Nullable[str]]
    r"""The personal email address of the employee. This is provided to support syncing users between our system and yours. You may not use this email address for any other purpose (e.g. marketing)."""
    company_uuid: NotRequired[str]
    r"""The UUID of the company the employee is employed by."""
    manager_uuid: NotRequired[Nullable[str]]
    r"""The UUID of the employee's manager."""
    version: NotRequired[str]
    r"""The current version of the employee. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""
    department: NotRequired[Nullable[str]]
    r"""The employee's department in the company."""
    terminated: NotRequired[bool]
    r"""Whether the employee is terminated."""
    two_percent_shareholder: NotRequired[Nullable[bool]]
    r"""Whether the employee is a two percent shareholder of the company. This field only applies to companies with an S-Corp entity type."""
    onboarded: NotRequired[bool]
    r"""Whether the employee has completed onboarding."""
    onboarding_status: NotRequired[Nullable[OnboardingStatus]]
    r"""The current onboarding status of the employee"""
    onboarding_documents_config: NotRequired[OnboardingDocumentsConfigTypedDict]
    r"""Configuration for an employee onboarding documents during onboarding"""
    jobs: NotRequired[List[JobTypedDict]]
    eligible_paid_time_off: NotRequired[List[PaidTimeOffTypedDict]]
    terminations: NotRequired[List[TerminationTypedDict]]
    garnishments: NotRequired[List[GarnishmentTypedDict]]
    custom_fields: NotRequired[List[EmployeeCustomFieldTypedDict]]
    r"""Custom fields are only included for the employee if the include param has the custom_fields value set"""
    date_of_birth: NotRequired[Nullable[str]]
    has_ssn: NotRequired[bool]
    r"""Indicates whether the employee has an SSN in Gusto."""
    ssn: NotRequired[str]
    r"""Deprecated. This field always returns an empty string."""
    phone: NotRequired[Nullable[str]]
    preferred_first_name: NotRequired[Nullable[str]]
    payment_method: NotRequired[PaymentMethod]
    r"""The employee's payment method"""
    work_email: NotRequired[Nullable[str]]
    r"""The work email address of the employee. This is provided to support syncing users between our system and yours. You may not use this email address for any other purpose (e.g. marketing)."""
    current_employment_status: NotRequired[Nullable[CurrentEmploymentStatus]]
    r"""The current employment status of the employee. Full-time employees work 30+ hours per week. Part-time employees are split into two groups: those that work 20-29 hours a week, and those that work under 20 hours a week. Variable employees have hours that vary each week. Seasonal employees are hired for 6 months of the year or less."""


class Employee(BaseModel):
    r"""The representation of an employee in Gusto."""

    uuid: str
    r"""The UUID of the employee in Gusto."""

    first_name: str

    last_name: str

    middle_initial: OptionalNullable[str] = UNSET

    email: OptionalNullable[str] = UNSET
    r"""The personal email address of the employee. This is provided to support syncing users between our system and yours. You may not use this email address for any other purpose (e.g. marketing)."""

    company_uuid: Optional[str] = None
    r"""The UUID of the company the employee is employed by."""

    manager_uuid: OptionalNullable[str] = UNSET
    r"""The UUID of the employee's manager."""

    version: Optional[str] = None
    r"""The current version of the employee. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""

    department: OptionalNullable[str] = UNSET
    r"""The employee's department in the company."""

    terminated: Optional[bool] = None
    r"""Whether the employee is terminated."""

    two_percent_shareholder: OptionalNullable[bool] = UNSET
    r"""Whether the employee is a two percent shareholder of the company. This field only applies to companies with an S-Corp entity type."""

    onboarded: Optional[bool] = None
    r"""Whether the employee has completed onboarding."""

    onboarding_status: OptionalNullable[OnboardingStatus] = UNSET
    r"""The current onboarding status of the employee"""

    onboarding_documents_config: Optional[OnboardingDocumentsConfig] = None
    r"""Configuration for an employee onboarding documents during onboarding"""

    jobs: Optional[List[Job]] = None

    eligible_paid_time_off: Optional[List[PaidTimeOff]] = None

    terminations: Optional[List[Termination]] = None

    garnishments: Optional[List[Garnishment]] = None

    custom_fields: Optional[List[EmployeeCustomField]] = None
    r"""Custom fields are only included for the employee if the include param has the custom_fields value set"""

    date_of_birth: OptionalNullable[str] = UNSET

    has_ssn: Optional[bool] = None
    r"""Indicates whether the employee has an SSN in Gusto."""

    ssn: Optional[str] = None
    r"""Deprecated. This field always returns an empty string."""

    phone: OptionalNullable[str] = UNSET

    preferred_first_name: OptionalNullable[str] = UNSET

    payment_method: Optional[PaymentMethod] = PaymentMethod.CHECK
    r"""The employee's payment method"""

    work_email: OptionalNullable[str] = UNSET
    r"""The work email address of the employee. This is provided to support syncing users between our system and yours. You may not use this email address for any other purpose (e.g. marketing)."""

    current_employment_status: OptionalNullable[CurrentEmploymentStatus] = UNSET
    r"""The current employment status of the employee. Full-time employees work 30+ hours per week. Part-time employees are split into two groups: those that work 20-29 hours a week, and those that work under 20 hours a week. Variable employees have hours that vary each week. Seasonal employees are hired for 6 months of the year or less."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "middle_initial",
            "email",
            "company_uuid",
            "manager_uuid",
            "version",
            "department",
            "terminated",
            "two_percent_shareholder",
            "onboarded",
            "onboarding_status",
            "onboarding_documents_config",
            "jobs",
            "eligible_paid_time_off",
            "terminations",
            "garnishments",
            "custom_fields",
            "date_of_birth",
            "has_ssn",
            "ssn",
            "phone",
            "preferred_first_name",
            "payment_method",
            "work_email",
            "current_employment_status",
        ]
        nullable_fields = [
            "middle_initial",
            "email",
            "manager_uuid",
            "department",
            "two_percent_shareholder",
            "onboarding_status",
            "date_of_birth",
            "phone",
            "preferred_first_name",
            "work_email",
            "current_employment_status",
        ]
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
