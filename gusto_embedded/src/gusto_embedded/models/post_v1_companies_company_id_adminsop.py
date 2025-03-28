"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
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


class PostV1CompaniesCompanyIDAdminsRequestBodyTypedDict(TypedDict):
    first_name: str
    r"""The first name of the admin."""
    last_name: str
    r"""The last name of the admin."""
    email: str
    r"""The email of the admin for Gusto's system. If the email matches an existing user, this will create an admin account for them."""


class PostV1CompaniesCompanyIDAdminsRequestBody(BaseModel):
    first_name: str
    r"""The first name of the admin."""

    last_name: str
    r"""The last name of the admin."""

    email: str
    r"""The email of the admin for Gusto's system. If the email matches an existing user, this will create an admin account for them."""


class PostV1CompaniesCompanyIDAdminsRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    request_body: PostV1CompaniesCompanyIDAdminsRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1CompaniesCompanyIDAdminsRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PostV1CompaniesCompanyIDAdminsRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
