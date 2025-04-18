"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from enum import Enum
from gusto_embedded.types import BaseModel
from gusto_embedded.utils import (
    FieldMetadata,
    HeaderMetadata,
    MultipartFormMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import io
import pydantic
from typing import IO, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class PostV1CompaniesAttachmentDocumentTypedDict(TypedDict):
    file_name: str
    content: Union[bytes, IO[bytes], io.BufferedReader]
    content_type: NotRequired[str]


class PostV1CompaniesAttachmentDocument(BaseModel):
    file_name: Annotated[
        str, pydantic.Field(alias="fileName"), FieldMetadata(multipart=True)
    ]

    content: Annotated[
        Union[bytes, IO[bytes], io.BufferedReader],
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(content=True)),
    ]

    content_type: Annotated[
        Optional[str],
        pydantic.Field(alias="Content-Type"),
        FieldMetadata(multipart=True),
    ] = None


class PostV1CompaniesAttachmentCategory(str, Enum):
    r"""The category of a company attachment."""

    GEP_NOTICE = "gep_notice"
    COMPLIANCE = "compliance"


class PostV1CompaniesAttachmentRequestBodyTypedDict(TypedDict):
    r"""The binary payload of the file and the company attachment category."""

    document: PostV1CompaniesAttachmentDocumentTypedDict
    r"""The binary payload of the file to be uploaded."""
    category: PostV1CompaniesAttachmentCategory
    r"""The category of a company attachment."""


class PostV1CompaniesAttachmentRequestBody(BaseModel):
    r"""The binary payload of the file and the company attachment category."""

    document: Annotated[
        PostV1CompaniesAttachmentDocument,
        FieldMetadata(multipart=MultipartFormMetadata(file=True)),
    ]
    r"""The binary payload of the file to be uploaded."""

    category: Annotated[
        PostV1CompaniesAttachmentCategory, FieldMetadata(multipart=True)
    ]
    r"""The category of a company attachment."""


class PostV1CompaniesAttachmentRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    request_body: PostV1CompaniesAttachmentRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1CompaniesAttachmentRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PostV1CompaniesAttachmentRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="multipart/form-data")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
