"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from enum import Enum
from gusto_embedded.types import BaseModel
from gusto_embedded.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PostV1CompanyFlowsEntityType(str, Enum):
    r"""the type of target entity applicable to the flow. This field is optional for company flows, please refer to the flow_types table above for more details."""

    COMPANY = "Company"
    EMPLOYEE = "Employee"


class PostV1CompanyFlowsRequestBodyTypedDict(TypedDict):
    flow_type: str
    r"""flow type"""
    entity_uuid: NotRequired[str]
    r"""UUID of the target entity applicable to the flow. This field is optional for company flows, please refer to the flow_types table above for more details."""
    entity_type: NotRequired[PostV1CompanyFlowsEntityType]
    r"""the type of target entity applicable to the flow. This field is optional for company flows, please refer to the flow_types table above for more details."""


class PostV1CompanyFlowsRequestBody(BaseModel):
    flow_type: str
    r"""flow type"""

    entity_uuid: Optional[str] = None
    r"""UUID of the target entity applicable to the flow. This field is optional for company flows, please refer to the flow_types table above for more details."""

    entity_type: Optional[PostV1CompanyFlowsEntityType] = None
    r"""the type of target entity applicable to the flow. This field is optional for company flows, please refer to the flow_types table above for more details."""


class PostV1CompanyFlowsRequestTypedDict(TypedDict):
    company_uuid: str
    r"""The UUID of the company"""
    request_body: PostV1CompanyFlowsRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1CompanyFlowsRequest(BaseModel):
    company_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PostV1CompanyFlowsRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
