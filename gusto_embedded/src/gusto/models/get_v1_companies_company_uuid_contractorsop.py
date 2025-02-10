"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto.types import BaseModel
from gusto.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetV1CompaniesCompanyUUIDContractorsRequestTypedDict(TypedDict):
    company_uuid: str
    r"""The UUID of the company"""
    page: NotRequired[float]
    r"""The page that is requested. When unspecified, will load all objects unless endpoint forces pagination."""
    per: NotRequired[float]
    r"""Number of objects per page. For majority of endpoints will default to 25"""
    search_term: NotRequired[str]
    r"""A string to search for in the object's names"""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class GetV1CompaniesCompanyUUIDContractorsRequest(BaseModel):
    company_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    page: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The page that is requested. When unspecified, will load all objects unless endpoint forces pagination."""

    per: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Number of objects per page. For majority of endpoints will default to 25"""

    search_term: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A string to search for in the object's names"""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
