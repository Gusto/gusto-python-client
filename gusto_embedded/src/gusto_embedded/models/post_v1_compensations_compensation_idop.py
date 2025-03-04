"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .flsa_status_type import FlsaStatusType
from .versionheader import VersionHeader
from enum import Enum
from gusto_embedded.types import BaseModel
from gusto_embedded.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PostV1CompensationsCompensationIDPaymentUnit(str, Enum):
    r"""The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'."""

    HOUR = "Hour"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"
    PAYCHECK = "Paycheck"


class PostV1CompensationsCompensationIDMinimumWagesTypedDict(TypedDict):
    r"""The minimum wage record you want to apply to the compensation"""

    uuid: NotRequired[str]
    r"""The UUID of the minimum wage record. Required if adjust_for_minimum_wage set to true"""


class PostV1CompensationsCompensationIDMinimumWages(BaseModel):
    r"""The minimum wage record you want to apply to the compensation"""

    uuid: Optional[str] = None
    r"""The UUID of the minimum wage record. Required if adjust_for_minimum_wage set to true"""


class PostV1CompensationsCompensationIDRequestBodyTypedDict(TypedDict):
    payment_unit: PostV1CompensationsCompensationIDPaymentUnit
    r"""The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'."""
    flsa_status: FlsaStatusType
    r"""The FLSA status for this compensation. Salaried ('Exempt') employees are paid a fixed salary every pay period. Salaried with overtime ('Salaried Nonexempt') employees are paid a fixed salary every pay period, and receive overtime pay when applicable. Hourly ('Nonexempt') employees are paid for the hours they work, and receive overtime pay when applicable. Commissioned employees ('Commission Only Exempt') earn wages based only on commission. Commissioned with overtime ('Commission Only Nonexempt') earn wages based on commission, and receive overtime pay when applicable. Owners ('Owner') are employees that own at least twenty percent of the company."""
    rate: NotRequired[str]
    r"""The dollar amount paid per payment unit."""
    effective_date: NotRequired[str]
    r"""The date when the compensation takes effect."""
    adjust_for_minimum_wage: NotRequired[bool]
    r"""Determines whether the compensation should be adjusted for minimum wage. Only applies to Nonexempt employees."""
    minimum_wages: NotRequired[
        List[PostV1CompensationsCompensationIDMinimumWagesTypedDict]
    ]


class PostV1CompensationsCompensationIDRequestBody(BaseModel):
    payment_unit: PostV1CompensationsCompensationIDPaymentUnit
    r"""The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'."""

    flsa_status: FlsaStatusType
    r"""The FLSA status for this compensation. Salaried ('Exempt') employees are paid a fixed salary every pay period. Salaried with overtime ('Salaried Nonexempt') employees are paid a fixed salary every pay period, and receive overtime pay when applicable. Hourly ('Nonexempt') employees are paid for the hours they work, and receive overtime pay when applicable. Commissioned employees ('Commission Only Exempt') earn wages based only on commission. Commissioned with overtime ('Commission Only Nonexempt') earn wages based on commission, and receive overtime pay when applicable. Owners ('Owner') are employees that own at least twenty percent of the company."""

    rate: Optional[str] = None
    r"""The dollar amount paid per payment unit."""

    effective_date: Optional[str] = None
    r"""The date when the compensation takes effect."""

    adjust_for_minimum_wage: Optional[bool] = None
    r"""Determines whether the compensation should be adjusted for minimum wage. Only applies to Nonexempt employees."""

    minimum_wages: Optional[List[PostV1CompensationsCompensationIDMinimumWages]] = None


class PostV1CompensationsCompensationIDRequestTypedDict(TypedDict):
    job_id: str
    r"""The UUID of the job"""
    request_body: PostV1CompensationsCompensationIDRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1CompensationsCompensationIDRequest(BaseModel):
    job_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the job"""

    request_body: Annotated[
        PostV1CompensationsCompensationIDRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
