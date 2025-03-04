"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto_embedded.types import BaseModel
from gusto_embedded.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetV1CompaniesCompanyIDPaySchedulesPayScheduleIDRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    pay_schedule_id: str
    r"""The UUID of the pay schedule"""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class GetV1CompaniesCompanyIDPaySchedulesPayScheduleIDRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    pay_schedule_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the pay schedule"""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
