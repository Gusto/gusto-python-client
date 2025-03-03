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
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PutV1ContractorDocumentSignFieldsTypedDict(TypedDict):
    key: NotRequired[str]
    r"""Unique identifier of the field"""
    value: NotRequired[str]
    r"""Value for the field"""


class PutV1ContractorDocumentSignFields(BaseModel):
    key: Optional[str] = None
    r"""Unique identifier of the field"""

    value: Optional[str] = None
    r"""Value for the field"""


class PutV1ContractorDocumentSignRequestBodyTypedDict(TypedDict):
    fields: List[PutV1ContractorDocumentSignFieldsTypedDict]
    r"""List of fields and the values they will be set to."""
    agree: bool
    r"""Whether you agree to sign electronically"""
    signed_by_ip_address: str
    r"""The IP address of the signatory who signed the form."""


class PutV1ContractorDocumentSignRequestBody(BaseModel):
    fields: List[PutV1ContractorDocumentSignFields]
    r"""List of fields and the values they will be set to."""

    agree: bool
    r"""Whether you agree to sign electronically"""

    signed_by_ip_address: str
    r"""The IP address of the signatory who signed the form."""


class PutV1ContractorDocumentSignRequestTypedDict(TypedDict):
    document_uuid: str
    r"""The ID or UUID of the document"""
    request_body: PutV1ContractorDocumentSignRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1ContractorDocumentSignRequest(BaseModel):
    document_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID or UUID of the document"""

    request_body: Annotated[
        PutV1ContractorDocumentSignRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
