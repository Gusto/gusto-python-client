"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .sort_order import SortOrder
from .versionheader import VersionHeader
from enum import Enum
from gusto_embedded.types import BaseModel
from gusto_embedded.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ProcessingStatuses(str, Enum):
    UNPROCESSED = "unprocessed"
    PROCESSED = "processed"


class PayrollTypes(str, Enum):
    REGULAR = "regular"
    OFF_CYCLE = "off_cycle"
    EXTERNAL = "external"


class GetV1CompaniesCompanyIDPayrollsQueryParamInclude(str, Enum):
    TOTALS = "totals"
    PAYROLL_STATUS_META = "payroll_status_meta"
    RISK_BLOCKERS = "risk_blockers"


class GetV1CompaniesCompanyIDPayrollsRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    processing_statuses: NotRequired[List[ProcessingStatuses]]
    r"""Whether to include processed and/or unprocessed payrolls in the response, defaults to processed, for multiple attributes comma separate the values, i.e. `?processing_statuses=processed,unprocessed`"""
    payroll_types: NotRequired[List[PayrollTypes]]
    r"""Whether to include regular and/or off_cycle payrolls in the response, defaults to regular, for multiple attributes comma separate the values, i.e. `?payroll_types=regular,off_cycle`"""
    include: NotRequired[List[GetV1CompaniesCompanyIDPayrollsQueryParamInclude]]
    r"""Include the requested attribute in the response. The risk_blockers option will include submission_blockers and credit_blockers if applicable. In v2023-04-01 totals are no longer included by default. For multiple attributes comma separate the values, i.e. `?include=totals,payroll_status_meta`"""
    start_date: NotRequired[str]
    r"""Return payrolls whose pay period is after the start date"""
    end_date: NotRequired[str]
    r"""Return payrolls whose pay period is before the end date. If left empty, defaults to today's date."""
    sort_order: NotRequired[SortOrder]
    r"""A string indicating whether to sort resulting events in ascending (asc) or descending (desc) chronological order. Events are sorted by their `timestamp`. Defaults to asc if left empty."""
    page: NotRequired[int]
    r"""The page that is requested. When unspecified, will load all objects unless endpoint forces pagination."""
    per: NotRequired[int]
    r"""Number of objects per page. For majority of endpoints will default to 25"""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class GetV1CompaniesCompanyIDPayrollsRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    processing_statuses: Annotated[
        Optional[List[ProcessingStatuses]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Whether to include processed and/or unprocessed payrolls in the response, defaults to processed, for multiple attributes comma separate the values, i.e. `?processing_statuses=processed,unprocessed`"""

    payroll_types: Annotated[
        Optional[List[PayrollTypes]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Whether to include regular and/or off_cycle payrolls in the response, defaults to regular, for multiple attributes comma separate the values, i.e. `?payroll_types=regular,off_cycle`"""

    include: Annotated[
        Optional[List[GetV1CompaniesCompanyIDPayrollsQueryParamInclude]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Include the requested attribute in the response. The risk_blockers option will include submission_blockers and credit_blockers if applicable. In v2023-04-01 totals are no longer included by default. For multiple attributes comma separate the values, i.e. `?include=totals,payroll_status_meta`"""

    start_date: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Return payrolls whose pay period is after the start date"""

    end_date: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Return payrolls whose pay period is before the end date. If left empty, defaults to today's date."""

    sort_order: Annotated[
        Optional[SortOrder],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A string indicating whether to sort resulting events in ascending (asc) or descending (desc) chronological order. Events are sorted by their `timestamp`. Defaults to asc if left empty."""

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
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
