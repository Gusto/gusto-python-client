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


class PostV1ContractorsContractorUUIDBankAccountsAccountType(str, Enum):
    CHECKING = "Checking"
    SAVINGS = "Savings"


class PostV1ContractorsContractorUUIDBankAccountsRequestBodyTypedDict(TypedDict):
    name: str
    routing_number: str
    account_number: str
    account_type: PostV1ContractorsContractorUUIDBankAccountsAccountType


class PostV1ContractorsContractorUUIDBankAccountsRequestBody(BaseModel):
    name: str

    routing_number: str

    account_number: str

    account_type: PostV1ContractorsContractorUUIDBankAccountsAccountType


class PostV1ContractorsContractorUUIDBankAccountsRequestTypedDict(TypedDict):
    contractor_uuid: str
    r"""The UUID of the contractor"""
    request_body: PostV1ContractorsContractorUUIDBankAccountsRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1ContractorsContractorUUIDBankAccountsRequest(BaseModel):
    contractor_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the contractor"""

    request_body: Annotated[
        PostV1ContractorsContractorUUIDBankAccountsRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
