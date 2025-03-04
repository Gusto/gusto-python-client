"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto_embedded.types import BaseModel
from gusto_embedded.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PostV1SandboxGenerate1099RequestBodyTypedDict(TypedDict):
    contractor_id: str
    r"""The contractor UUID."""
    year: NotRequired[int]
    r"""Must be equal to or more recent than 2015. If not specified, defaults to the previous year.

    """


class PostV1SandboxGenerate1099RequestBody(BaseModel):
    contractor_id: str
    r"""The contractor UUID."""

    year: Optional[int] = None
    r"""Must be equal to or more recent than 2015. If not specified, defaults to the previous year.

    """


class PostV1SandboxGenerate1099RequestTypedDict(TypedDict):
    request_body: PostV1SandboxGenerate1099RequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1SandboxGenerate1099Request(BaseModel):
    request_body: Annotated[
        PostV1SandboxGenerate1099RequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
