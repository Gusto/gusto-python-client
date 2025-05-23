"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from gusto_app_integration.types import BaseModel
from gusto_app_integration.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetV1LocationsLocationUUIDMinimumWagesHeaderXGustoAPIVersion(str, Enum):
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""

    TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01 = "2024-04-01"


class GetV1LocationsLocationUUIDMinimumWagesRequestTypedDict(TypedDict):
    location_uuid: str
    r"""The UUID of the location"""
    x_gusto_api_version: NotRequired[
        GetV1LocationsLocationUUIDMinimumWagesHeaderXGustoAPIVersion
    ]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
    effective_date: NotRequired[str]


class GetV1LocationsLocationUUIDMinimumWagesRequest(BaseModel):
    location_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the location"""

    x_gusto_api_version: Annotated[
        Optional[GetV1LocationsLocationUUIDMinimumWagesHeaderXGustoAPIVersion],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = GetV1LocationsLocationUUIDMinimumWagesHeaderXGustoAPIVersion.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""

    effective_date: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
