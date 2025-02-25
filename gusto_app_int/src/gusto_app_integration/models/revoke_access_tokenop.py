"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto_app_integration.types import BaseModel
from gusto_app_integration.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RevokeAccessTokenRequestBodyTypedDict(TypedDict):
    client_id: str
    r"""Your client id"""
    client_secret: str
    r"""Your client secret"""
    token: str
    r"""The access token that will be revoked."""


class RevokeAccessTokenRequestBody(BaseModel):
    client_id: str
    r"""Your client id"""

    client_secret: str
    r"""Your client secret"""

    token: str
    r"""The access token that will be revoked."""


class RevokeAccessTokenRequestTypedDict(TypedDict):
    request_body: RevokeAccessTokenRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class RevokeAccessTokenRequest(BaseModel):
    request_body: Annotated[
        RevokeAccessTokenRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
