"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
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
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PrintingFormat(str, Enum):
    r"""The type of check stock being printed. Check the \"Types of check stock\" section in this [link](https://support.gusto.com/article/999877761000000/Pay-your-team-by-check) for more info on check types"""

    TOP = "top"
    BOTTOM = "bottom"


class PostV1PayrollsPayrollUUIDGeneratedDocumentsPrintablePayrollChecksRequestBodyTypedDict(
    TypedDict
):
    printing_format: PrintingFormat
    r"""The type of check stock being printed. Check the \"Types of check stock\" section in this [link](https://support.gusto.com/article/999877761000000/Pay-your-team-by-check) for more info on check types"""
    starting_check_number: NotRequired[int]
    r"""The starting check number we will start generating checks from. Use to override the sequence that will be used to generate check numbers."""


class PostV1PayrollsPayrollUUIDGeneratedDocumentsPrintablePayrollChecksRequestBody(
    BaseModel
):
    printing_format: PrintingFormat
    r"""The type of check stock being printed. Check the \"Types of check stock\" section in this [link](https://support.gusto.com/article/999877761000000/Pay-your-team-by-check) for more info on check types"""

    starting_check_number: Optional[int] = None
    r"""The starting check number we will start generating checks from. Use to override the sequence that will be used to generate check numbers."""


class PostV1PayrollsPayrollUUIDGeneratedDocumentsPrintablePayrollChecksRequestTypedDict(
    TypedDict
):
    payroll_uuid: str
    r"""The UUID of the payroll"""
    request_body: PostV1PayrollsPayrollUUIDGeneratedDocumentsPrintablePayrollChecksRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1PayrollsPayrollUUIDGeneratedDocumentsPrintablePayrollChecksRequest(
    BaseModel
):
    payroll_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the payroll"""

    request_body: Annotated[
        PostV1PayrollsPayrollUUIDGeneratedDocumentsPrintablePayrollChecksRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
