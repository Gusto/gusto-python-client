"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto_app_integration.types import BaseModel
from gusto_app_integration.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PutV1CompaniesRequestBodyTypedDict(TypedDict):
    contractor_only: bool
    r"""Whether the company only supports contractors. Must be updated in order for the company to start supporting W-2 employees. Can only be updated from true to false. Note that updating this value will require additional onboarding steps to be completed in order for the company to support W-2 employees."""


class PutV1CompaniesRequestBody(BaseModel):
    contractor_only: bool
    r"""Whether the company only supports contractors. Must be updated in order for the company to start supporting W-2 employees. Can only be updated from true to false. Note that updating this value will require additional onboarding steps to be completed in order for the company to support W-2 employees."""


class PutV1CompaniesRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    request_body: PutV1CompaniesRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1CompaniesRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PutV1CompaniesRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
