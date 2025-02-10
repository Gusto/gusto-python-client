"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto.types import BaseModel
from gusto.utils import FieldMetadata, HeaderMetadata, RequestMetadata, SecurityMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PostV1PartnerManagedCompaniesSecurityTypedDict(TypedDict):
    system_access_auth: str


class PostV1PartnerManagedCompaniesSecurity(BaseModel):
    system_access_auth: Annotated[
        str,
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="http",
                sub_type="bearer",
                field_name="Authorization",
            )
        ),
    ]


class UserTypedDict(TypedDict):
    r"""Information for the user who will be the primary payroll administrator for the new company."""

    first_name: str
    r"""The first name of the user who will be the primary payroll admin."""
    last_name: str
    r"""The last name of the user who will be the primary payroll admin."""
    email: str
    r"""The email of the user who will be the primary payroll admin."""
    phone: NotRequired[str]
    r"""The phone number of the user who will be the primary payroll admin."""


class User(BaseModel):
    r"""Information for the user who will be the primary payroll administrator for the new company."""

    first_name: str
    r"""The first name of the user who will be the primary payroll admin."""

    last_name: str
    r"""The last name of the user who will be the primary payroll admin."""

    email: str
    r"""The email of the user who will be the primary payroll admin."""

    phone: Optional[str] = None
    r"""The phone number of the user who will be the primary payroll admin."""


class PostV1PartnerManagedCompaniesCompanyTypedDict(TypedDict):
    name: str
    r"""The legal name of the company."""
    trade_name: NotRequired[str]
    r"""The name of the company."""
    ein: NotRequired[str]
    r"""The employer identification number (EIN) of the company."""
    contractor_only: NotRequired[bool]
    r"""Whether the company only supports contractors. Should be set to true if the company has no W-2 employees. If not passed, will default to false (i.e. the company will support both contractors and employees)."""


class PostV1PartnerManagedCompaniesCompany(BaseModel):
    name: str
    r"""The legal name of the company."""

    trade_name: Optional[str] = None
    r"""The name of the company."""

    ein: Optional[str] = None
    r"""The employer identification number (EIN) of the company."""

    contractor_only: Optional[bool] = None
    r"""Whether the company only supports contractors. Should be set to true if the company has no W-2 employees. If not passed, will default to false (i.e. the company will support both contractors and employees)."""


class PostV1PartnerManagedCompaniesRequestBodyTypedDict(TypedDict):
    user: UserTypedDict
    r"""Information for the user who will be the primary payroll administrator for the new company."""
    company: PostV1PartnerManagedCompaniesCompanyTypedDict


class PostV1PartnerManagedCompaniesRequestBody(BaseModel):
    user: User
    r"""Information for the user who will be the primary payroll administrator for the new company."""

    company: PostV1PartnerManagedCompaniesCompany


class PostV1PartnerManagedCompaniesRequestTypedDict(TypedDict):
    request_body: PostV1PartnerManagedCompaniesRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1PartnerManagedCompaniesRequest(BaseModel):
    request_body: Annotated[
        PostV1PartnerManagedCompaniesRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1PartnerManagedCompaniesResponseBodyTypedDict(TypedDict):
    r"""Object returned when creating a partner managed company"""

    access_token: NotRequired[str]
    r"""Access token that can be used for OAuth access to the account. Access tokens expire 2 hours after they are issued."""
    refresh_token: NotRequired[str]
    r"""Refresh token that can be exchanged for a new access token."""
    company_uuid: NotRequired[str]
    r"""Gusto’s UUID for the company"""
    expires_in: NotRequired[int]
    r"""Time of access_token expiration in seconds"""


class PostV1PartnerManagedCompaniesResponseBody(BaseModel):
    r"""Object returned when creating a partner managed company"""

    access_token: Optional[str] = None
    r"""Access token that can be used for OAuth access to the account. Access tokens expire 2 hours after they are issued."""

    refresh_token: Optional[str] = None
    r"""Refresh token that can be exchanged for a new access token."""

    company_uuid: Optional[str] = None
    r"""Gusto’s UUID for the company"""

    expires_in: Optional[int] = None
    r"""Time of access_token expiration in seconds"""
