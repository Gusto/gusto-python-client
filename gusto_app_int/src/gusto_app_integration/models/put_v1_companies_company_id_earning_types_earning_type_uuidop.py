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


class PutV1CompaniesCompanyIDEarningTypesEarningTypeUUIDRequestBodyTypedDict(TypedDict):
    name: NotRequired[str]
    r"""The name of the custom earning type."""


class PutV1CompaniesCompanyIDEarningTypesEarningTypeUUIDRequestBody(BaseModel):
    name: Optional[str] = None
    r"""The name of the custom earning type."""


class PutV1CompaniesCompanyIDEarningTypesEarningTypeUUIDRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    earning_type_uuid: str
    r"""The UUID of the earning type"""
    request_body: PutV1CompaniesCompanyIDEarningTypesEarningTypeUUIDRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1CompaniesCompanyIDEarningTypesEarningTypeUUIDRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    earning_type_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the earning type"""

    request_body: Annotated[
        PutV1CompaniesCompanyIDEarningTypesEarningTypeUUIDRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
