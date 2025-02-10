"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .flsa_status_type import FlsaStatusType
from .versionheader import VersionHeader
from enum import Enum
from gusto.types import BaseModel
from gusto.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PutV1CompensationsCompensationIDPaymentUnit(str, Enum):
    r"""The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'."""

    HOUR = "Hour"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"
    PAYCHECK = "Paycheck"


class PutV1CompensationsCompensationIDMinimumWagesTypedDict(TypedDict):
    r"""The minimum wage record you want to apply to the compensation"""

    uuid: NotRequired[str]
    r"""The UUID of the minimum wage record. Required if adjust_for_minimum_wage set to true"""


class PutV1CompensationsCompensationIDMinimumWages(BaseModel):
    r"""The minimum wage record you want to apply to the compensation"""

    uuid: Optional[str] = None
    r"""The UUID of the minimum wage record. Required if adjust_for_minimum_wage set to true"""


class PutV1CompensationsCompensationIDRequestBodyTypedDict(TypedDict):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""
    rate: NotRequired[str]
    r"""The dollar amount paid per payment unit."""
    payment_unit: NotRequired[PutV1CompensationsCompensationIDPaymentUnit]
    r"""The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'."""
    flsa_status: NotRequired[FlsaStatusType]
    r"""The FLSA status for this compensation. Salaried ('Exempt') employees are paid a fixed salary every pay period. Salaried with overtime ('Salaried Nonexempt') employees are paid a fixed salary every pay period, and receive overtime pay when applicable. Hourly ('Nonexempt') employees are paid for the hours they work, and receive overtime pay when applicable. Commissioned employees ('Commission Only Exempt') earn wages based only on commission. Commissioned with overtime ('Commission Only Nonexempt') earn wages based on commission, and receive overtime pay when applicable. Owners ('Owner') are employees that own at least twenty percent of the company."""
    adjust_for_minimum_wage: NotRequired[bool]
    r"""Determines whether the compensation should be adjusted for minimum wage. Only applies to Nonexempt employees."""
    minimum_wages: NotRequired[
        List[PutV1CompensationsCompensationIDMinimumWagesTypedDict]
    ]


class PutV1CompensationsCompensationIDRequestBody(BaseModel):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""

    rate: Optional[str] = None
    r"""The dollar amount paid per payment unit."""

    payment_unit: Optional[PutV1CompensationsCompensationIDPaymentUnit] = None
    r"""The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'."""

    flsa_status: Optional[FlsaStatusType] = None
    r"""The FLSA status for this compensation. Salaried ('Exempt') employees are paid a fixed salary every pay period. Salaried with overtime ('Salaried Nonexempt') employees are paid a fixed salary every pay period, and receive overtime pay when applicable. Hourly ('Nonexempt') employees are paid for the hours they work, and receive overtime pay when applicable. Commissioned employees ('Commission Only Exempt') earn wages based only on commission. Commissioned with overtime ('Commission Only Nonexempt') earn wages based on commission, and receive overtime pay when applicable. Owners ('Owner') are employees that own at least twenty percent of the company."""

    adjust_for_minimum_wage: Optional[bool] = None
    r"""Determines whether the compensation should be adjusted for minimum wage. Only applies to Nonexempt employees."""

    minimum_wages: Optional[List[PutV1CompensationsCompensationIDMinimumWages]] = None


class PutV1CompensationsCompensationIDRequestTypedDict(TypedDict):
    compensation_id: str
    r"""The UUID of the compensation"""
    request_body: PutV1CompensationsCompensationIDRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1CompensationsCompensationIDRequest(BaseModel):
    compensation_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the compensation"""

    request_body: Annotated[
        PutV1CompensationsCompensationIDRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
