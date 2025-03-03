"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
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
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetV1EmployeesEmployeeIDJobsQueryParamInclude(str, Enum):
    r"""Available options:
    - all_compensations: Include all effective dated compensations for each job instead of only the current compensation
    """

    ALL_COMPENSATIONS = "all_compensations"


class GetV1EmployeesEmployeeIDJobsRequestTypedDict(TypedDict):
    employee_id: str
    r"""The UUID of the employee"""
    page: NotRequired[int]
    r"""The page that is requested. When unspecified, will load all objects unless endpoint forces pagination."""
    per: NotRequired[int]
    r"""Number of objects per page. For majority of endpoints will default to 25"""
    include: NotRequired[GetV1EmployeesEmployeeIDJobsQueryParamInclude]
    r"""Available options:
    - all_compensations: Include all effective dated compensations for each job instead of only the current compensation
    """
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class GetV1EmployeesEmployeeIDJobsRequest(BaseModel):
    employee_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the employee"""

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

    include: Annotated[
        Optional[GetV1EmployeesEmployeeIDJobsQueryParamInclude],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Available options:
    - all_compensations: Include all effective dated compensations for each job instead of only the current compensation
    """

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
