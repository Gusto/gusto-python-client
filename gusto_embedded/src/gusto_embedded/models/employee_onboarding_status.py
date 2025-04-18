"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto_embedded.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class EmployeeOnboardingStatusOnboardingStepTypedDict(TypedDict):
    title: NotRequired[str]
    r"""User-friendly description of the onboarding step."""
    id: NotRequired[str]
    r"""String identifier for the onboarding step."""
    required: NotRequired[bool]
    r"""When true, this step is required."""
    completed: NotRequired[bool]
    r"""When true, this step has been completed."""
    requirements: NotRequired[List[str]]
    r"""A list of onboarding steps required to begin this step."""


class EmployeeOnboardingStatusOnboardingStep(BaseModel):
    title: Optional[str] = None
    r"""User-friendly description of the onboarding step."""

    id: Optional[str] = None
    r"""String identifier for the onboarding step."""

    required: Optional[bool] = None
    r"""When true, this step is required."""

    completed: Optional[bool] = None
    r"""When true, this step has been completed."""

    requirements: Optional[List[str]] = None
    r"""A list of onboarding steps required to begin this step."""


class EmployeeOnboardingStatusTypedDict(TypedDict):
    r"""The representation of an employee's onboarding status."""

    uuid: str
    r"""Unique identifier for this employee."""
    onboarding_status: NotRequired[str]
    r"""One of the \"onboarding_status\" enum values."""
    onboarding_steps: NotRequired[List[EmployeeOnboardingStatusOnboardingStepTypedDict]]
    r"""List of steps required to onboard an employee."""


class EmployeeOnboardingStatus(BaseModel):
    r"""The representation of an employee's onboarding status."""

    uuid: str
    r"""Unique identifier for this employee."""

    onboarding_status: Optional[str] = None
    r"""One of the \"onboarding_status\" enum values."""

    onboarding_steps: Optional[List[EmployeeOnboardingStatusOnboardingStep]] = None
    r"""List of steps required to onboard an employee."""
