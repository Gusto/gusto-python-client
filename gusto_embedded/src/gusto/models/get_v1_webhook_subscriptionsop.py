"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto.types import BaseModel
from gusto.utils import FieldMetadata, HeaderMetadata, SecurityMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetV1WebhookSubscriptionsSecurityTypedDict(TypedDict):
    system_access_auth: str


class GetV1WebhookSubscriptionsSecurity(BaseModel):
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


class GetV1WebhookSubscriptionsRequestTypedDict(TypedDict):
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class GetV1WebhookSubscriptionsRequest(BaseModel):
    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
