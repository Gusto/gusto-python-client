"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto_app_integration.types import BaseModel
from gusto_app_integration.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RefreshAccessTokenRequestBodyTypedDict(TypedDict):
    client_id: str
    r"""Your client id"""
    client_secret: str
    r"""Your client secret"""
    refresh_token: str
    r"""The `refresh_token` being exchanged for an access token code"""
    grant_type: str
    r"""this should be the literal string 'refresh_token'"""
    redirect_uri: NotRequired[str]
    r"""The redirect URI you set up via the Developer Portal"""


class RefreshAccessTokenRequestBody(BaseModel):
    client_id: str
    r"""Your client id"""

    client_secret: str
    r"""Your client secret"""

    refresh_token: str
    r"""The `refresh_token` being exchanged for an access token code"""

    grant_type: str
    r"""this should be the literal string 'refresh_token'"""

    redirect_uri: Optional[str] = None
    r"""The redirect URI you set up via the Developer Portal"""


class RefreshAccessTokenRequestTypedDict(TypedDict):
    request_body: RefreshAccessTokenRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class RefreshAccessTokenRequest(BaseModel):
    request_body: Annotated[
        RefreshAccessTokenRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
