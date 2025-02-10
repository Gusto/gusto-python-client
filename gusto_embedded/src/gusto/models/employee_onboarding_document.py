"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class EmployeeOnboardingDocumentTypedDict(TypedDict):
    r"""Configuration for an employee onboarding documents during onboarding"""

    i9_document: NotRequired[str]
    r"""Whether to include Form I-9 for an employee during onboarding"""


class EmployeeOnboardingDocument(BaseModel):
    r"""Configuration for an employee onboarding documents during onboarding"""

    i9_document: Optional[str] = None
    r"""Whether to include Form I-9 for an employee during onboarding"""
