"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .entity_type import EntityType
from .status import Status
from .time_sheet_sort_by import TimeSheetSortBy
from .time_sheet_sort_order import TimeSheetSortOrder
from .versionheader import VersionHeader
from gusto_app_integration.types import BaseModel
from gusto_app_integration.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetCompaniesCompanyUUIDTimeTrackingTimeSheetsRequestTypedDict(TypedDict):
    company_uuid: str
    r"""The UUID of the company"""
    entity_uuids: NotRequired[List[str]]
    r"""Entity UUIDs that reported time sheets"""
    entity_type: NotRequired[EntityType]
    r"""Type of entities to filter. One of: \"Employee\", \"Contractor\" """
    status: NotRequired[Status]
    r"""Status of time sheets. One of: \"approved\", \"pending\", \"rejected\" """
    sort_by: NotRequired[TimeSheetSortBy]
    r"""Field to sort by. One of: \"created_at\", \"updated_at\", \"shift_started_at\", \"shift_ended_at\" """
    sort_order: NotRequired[TimeSheetSortOrder]
    r"""Sortinng order. One of: \"asc\", \"desc\" """
    before: NotRequired[str]
    r"""time sheets that were created before ISO 8601 timestamp. Filtering by \"created_at\" """
    after: NotRequired[str]
    r"""time sheets that were created before ISO 8601 timestamp. Filtering by \"created_at\" """
    page: NotRequired[int]
    r"""The page that is requested. When unspecified, will load all objects unless endpoint forces pagination."""
    per: NotRequired[int]
    r"""Number of objects per page. For majority of endpoints will default to 25"""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class GetCompaniesCompanyUUIDTimeTrackingTimeSheetsRequest(BaseModel):
    company_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    entity_uuids: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Entity UUIDs that reported time sheets"""

    entity_type: Annotated[
        Optional[EntityType],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Type of entities to filter. One of: \"Employee\", \"Contractor\" """

    status: Annotated[
        Optional[Status],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Status of time sheets. One of: \"approved\", \"pending\", \"rejected\" """

    sort_by: Annotated[
        Optional[TimeSheetSortBy],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Field to sort by. One of: \"created_at\", \"updated_at\", \"shift_started_at\", \"shift_ended_at\" """

    sort_order: Annotated[
        Optional[TimeSheetSortOrder],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Sortinng order. One of: \"asc\", \"desc\" """

    before: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""time sheets that were created before ISO 8601 timestamp. Filtering by \"created_at\" """

    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""time sheets that were created before ISO 8601 timestamp. Filtering by \"created_at\" """

    page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The page that is requested. When unspecified, will load all objects unless endpoint forces pagination."""

    per: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Number of objects per page. For majority of endpoints will default to 25"""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
