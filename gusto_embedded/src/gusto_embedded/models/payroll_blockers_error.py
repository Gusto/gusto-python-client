"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto_embedded import utils
from gusto_embedded.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PayrollBlockersErrorMetadataTypedDict(TypedDict):
    key: NotRequired[str]
    r"""A categorization of the payroll blocker, e.g. \"geocode_error\" """


class PayrollBlockersErrorMetadata(BaseModel):
    key: Optional[str] = None
    r"""A categorization of the payroll blocker, e.g. \"geocode_error\" """


class ErrorsTypedDict(TypedDict):
    error_key: NotRequired[str]
    r"""The string \"base\" """
    category: NotRequired[str]
    r"""The string \"payroll_blocker\" """
    message: NotRequired[str]
    r"""Human readable description of the payroll blocker"""
    metadata: NotRequired[PayrollBlockersErrorMetadataTypedDict]


class Errors(BaseModel):
    error_key: Optional[str] = None
    r"""The string \"base\" """

    category: Optional[str] = None
    r"""The string \"payroll_blocker\" """

    message: Optional[str] = None
    r"""Human readable description of the payroll blocker"""

    metadata: Optional[PayrollBlockersErrorMetadata] = None


class PayrollBlockersErrorData(BaseModel):
    errors: Optional[List[Errors]] = None


class PayrollBlockersError(Exception):
    r"""Payroll Blockers Error

    For detailed information, see the [Payroll Blockers guide](https://docs.gusto.com/embedded-payroll/docs/payroll-blockers)
    """

    data: PayrollBlockersErrorData

    def __init__(self, data: PayrollBlockersErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, PayrollBlockersErrorData)
