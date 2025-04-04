"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
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


class PutV1CompanyIndustryRequestBodyTypedDict(TypedDict):
    naics_code: str
    r"""North American Industry Classification System (NAICS) is used to classify businesses with a six digit number based on the primary type of work the business performs"""
    title: NotRequired[str]
    r"""Industry title"""
    sic_codes: NotRequired[List[str]]
    r"""A list of Standard Industrial Classification (SIC) codes, which are four digit number that categorize the industries that companies belong to based on their business activities. If sic_codes is not passed in, we will perform an internal lookup with naics_code."""


class PutV1CompanyIndustryRequestBody(BaseModel):
    naics_code: str
    r"""North American Industry Classification System (NAICS) is used to classify businesses with a six digit number based on the primary type of work the business performs"""

    title: Optional[str] = None
    r"""Industry title"""

    sic_codes: Optional[List[str]] = None
    r"""A list of Standard Industrial Classification (SIC) codes, which are four digit number that categorize the industries that companies belong to based on their business activities. If sic_codes is not passed in, we will perform an internal lookup with naics_code."""


class PutV1CompanyIndustryRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    request_body: PutV1CompanyIndustryRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1CompanyIndustryRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PutV1CompanyIndustryRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
