"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from enum import Enum
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


class GetV1JobsJobIDQueryParamInclude(str, Enum):
    r"""Available options:
    - all_compensations: Include all effective dated compensations for the job instead of only the current compensation
    """

    ALL_COMPENSATIONS = "all_compensations"


class GetV1JobsJobIDRequestTypedDict(TypedDict):
    job_id: str
    r"""The UUID of the job"""
    include: NotRequired[GetV1JobsJobIDQueryParamInclude]
    r"""Available options:
    - all_compensations: Include all effective dated compensations for the job instead of only the current compensation
    """
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class GetV1JobsJobIDRequest(BaseModel):
    job_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the job"""

    include: Annotated[
        Optional[GetV1JobsJobIDQueryParamInclude],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Available options:
    - all_compensations: Include all effective dated compensations for the job instead of only the current compensation
    """

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
