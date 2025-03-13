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


class DocumentsTypedDict(TypedDict):
    document_type: str
    r"""The document type"""
    document_title: str
    r"""The document title associated with the document type"""
    issuing_authority: str
    r"""The document's issuing authority"""
    document_number: NotRequired[str]
    r"""The document's document number"""
    expiration_date: NotRequired[str]
    r"""The document's expiration date"""


class Documents(BaseModel):
    document_type: str
    r"""The document type"""

    document_title: str
    r"""The document title associated with the document type"""

    issuing_authority: str
    r"""The document's issuing authority"""

    document_number: Optional[str] = None
    r"""The document's document number"""

    expiration_date: Optional[str] = None
    r"""The document's expiration date"""


class PutV1EmployeesEmployeeIDI9AuthorizationDocumentsRequestBodyTypedDict(TypedDict):
    documents: List[DocumentsTypedDict]
    r"""An array of I-9 verification documents"""


class PutV1EmployeesEmployeeIDI9AuthorizationDocumentsRequestBody(BaseModel):
    documents: List[Documents]
    r"""An array of I-9 verification documents"""


class PutV1EmployeesEmployeeIDI9AuthorizationDocumentsRequestTypedDict(TypedDict):
    employee_id: str
    r"""The UUID of the employee"""
    request_body: PutV1EmployeesEmployeeIDI9AuthorizationDocumentsRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1EmployeesEmployeeIDI9AuthorizationDocumentsRequest(BaseModel):
    employee_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the employee"""

    request_body: Annotated[
        PutV1EmployeesEmployeeIDI9AuthorizationDocumentsRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
