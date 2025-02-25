"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .entity_error_object import EntityErrorObject, EntityErrorObjectTypedDict
from enum import Enum
from gusto_app_integration.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PayrollProcessingRequestStatus(str, Enum):
    r"""The status of the payroll processing request"""

    CALCULATING = "calculating"
    CALCULATE_SUCCESS = "calculate_success"
    SUBMITTING = "submitting"
    SUBMIT_SUCCESS = "submit_success"
    PROCESSING_FAILED = "processing_failed"


class PayrollProcessingRequestTypedDict(TypedDict):
    status: NotRequired[PayrollProcessingRequestStatus]
    r"""The status of the payroll processing request"""
    errors: NotRequired[List[EntityErrorObjectTypedDict]]
    r"""Errors that occurred during async payroll processing"""


class PayrollProcessingRequest(BaseModel):
    status: Optional[PayrollProcessingRequestStatus] = None
    r"""The status of the payroll processing request"""

    errors: Optional[List[EntityErrorObject]] = None
    r"""Errors that occurred during async payroll processing"""
